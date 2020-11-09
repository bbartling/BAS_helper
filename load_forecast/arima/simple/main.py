#!/usr/bin/env python
import pandas as pd
from sqlalchemy import create_engine
import BAC0, time, requests
from BAC0.core.utils.notes import note_and_log

from bacpypes.basetypes import EngineeringUnits, DateTime
from bacpypes.primitivedata import CharacterString, Date, Time, Real

from BAC0.core.devices.create_objects import (
    create_AV,
    create_MV,
    create_BV,
    create_AI,
    create_BI,
    create_AO,
    create_BO,
    create_CharStrValue,
    create_DateTimeValue,
)

from BAC0.tasks.RecurringTask import RecurringTask

import time, numpy
from sqlalchemy import create_engine
from datetime import datetime, timedelta
from threading import Timer
import sqlite3


from clgload_model import clg_Model
from costs_calcs import Enery_Costs_Calcs



def start_device():
    print("Starting BACnet device")
    new_device = BAC0.lite()
    new_device._log.info('Device ID : {}'.format(new_device.Boid))
    time.sleep(10)

    default_pv = CharacterString("empty")



    '''
    CLG points next
    '''



    ####kW#######dickeyFullerElec
    clg_modelpval = create_AV(
        oid=1, name="Clg_Forecast_Model_P_Val", pv=0, pv_writable=False
    )
    clg_modelpval.description = CharacterString(
        "Dickey-Fuller Test P-value for the statistics forecast ARIMA model"
    )

        ####kW#######minutes
    clgtrainmins = create_AV(
        oid=2, name="Clg_Model_Train_Time", pv=0, pv_writable=False
    )
    clgtrainmins.units = EngineeringUnits("minutes")
    clgtrainmins.description = CharacterString(
        "Elapsed time training cooling prediction model in minutes"
    )



    '''
    Costs arent modeled, just calculated based on utility rates
    '''


    new_device.this_application.add_object(clg_modelpval)
    new_device.this_application.add_object(clgtrainmins)

    return new_device



class App:
    dev = start_device()
    clgload_model = clg_Model()
    costs_calculations = Enery_Costs_Calcs()


app = App()


def clg_update_model():

    app.clgload_model.update()


    clg_modelpval= app.dev.this_application.get_object_id(("analogValue", 1))
    clgtrainmins= app.dev.this_application.get_object_id(("analogValue", 2))

    clg_modelpval.presentValue = app.clgload_model.dickfulr_pval
    clgtrainmins.presentValue = app.clgload_model.train_minutes

    #costs_calculations()

def cost_updates():

    app.costs_calculations.update()



def get_clg_data():
    '''
    perform read request on on cooling system
    '''

    allStuff = {}
    stamp = time.time()

    try:
        allStuff['Date'] = stamp

        app.dev._log.info("Attempting to perform BACnet read request")
        T1 = app.dev.read('12345:2 analogInput 2 presentValue')
        app.dev._log.info("Bacnet read request of the T1 sensor is {}".format(T1))

        T2 = app.dev.read('12345:2 analogInput 3 presentValue')
        app.dev._log.info("Bacnet read request of the T2 sensor is {}".format(T2))

        #500 is for water
        delta = abs(T1-T2)
        #GPM = 100
        #load = 500 * delta * GPM

        #sensible heat added to air
        CFM = 1300
        load = 1.08 * delta * CFM
        allStuff['load'] = load

        allStuff['Date'] = datetime.fromtimestamp(allStuff['Date'])
        master_data = pd.DataFrame(allStuff,index=[0])
        master_data = master_data.set_index('Date')


        engine = create_engine('sqlite:///save_data.db')
        sqlite_connection = engine.connect()
        sqlite_table = "clg_data"
        master_data.to_sql(sqlite_table, sqlite_connection, if_exists='append')
        sqlite_connection.close()
        app.dev._log.info("Data saved to Sqlite")
        app.dev._log.info("Load Calc in BTU/Hr == {}".format(round(load)))


    except:

        app.dev._log.warning("Error performing BACnet Read Request & db save!")
        time.sleep(300)


'''
#this main function is just for testing purposes
def main():

    task_device_two = RecurringTask(get_clg_data, delay=60)
    task_device_two.start()
    task_device_three = RecurringTask(clg_update_model, delay=120)
    task_device_three.start()


    while True:
        pass

'''

#This main function is for deployment
#Also to note get_elecmeter_data function also calls other functions
def main():
    task_device_one = RecurringTask(get_clg_data, delay=60)
    task_device_one.start()


    x=datetime.today()
    y = x.replace(day=x.day, hour=0, minute=0, second=0, microsecond=0) + timedelta(days=1)
    delta_t=y-x
    secs=delta_t.total_seconds()
    t = Timer(secs, clg_update_model)
    t.start()
    while True:
        pass


if __name__ == "__main__":
    main()
