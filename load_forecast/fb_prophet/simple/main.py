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

from model import Model


def start_device():
    print("Starting BACnet device")
    new_device = BAC0.lite()
    new_device._log.info('Device ID : {}'.format(new_device.Boid))
    time.sleep(10)

    default_pv = CharacterString("empty")


    ####kW#######5Am
    Five_AM_kW = create_AV(
        oid=0, name="5:00AM_Forecasted_kW", pv=0, pv_writable=False
    )
    Five_AM_kW.units = EngineeringUnits("kilowatts")
    Five_AM_kW.description = CharacterString(
        "5AM Electrical Demand"
    )

    ####kW#######6Am
    Six_AM_kW = create_AV(
        oid=1, name="6:00AM_Forecasted_kW", pv=0, pv_writable=False
    )
    Six_AM_kW.units = EngineeringUnits("kilowatts")
    Six_AM_kW.description = CharacterString(
        "6AM Electrical Demand"
    )


    ####kW#######7Am
    Seven_AM_kW = create_AV(
        oid=2, name="7:00AM_Forecasted_kW", pv=0, pv_writable=False
    )
    Seven_AM_kW.units = EngineeringUnits("kilowatts")
    Seven_AM_kW.description = CharacterString(
        "7AM Electrical Demand"
    )


    ####kW#######8Am
    Eight_AM_kW = create_AV(
        oid=3, name="8:00AM_Forecasted_kW", pv=0, pv_writable=False
    )
    Eight_AM_kW.units = EngineeringUnits("kilowatts")
    Eight_AM_kW.description = CharacterString(
        "8AM Electrical Demand"
    )

    ####kW#######9Am
    Nine_AM_kW = create_AV(
        oid=4, name="9:00AM_Forecasted_kW", pv=0, pv_writable=False
    )
    Nine_AM_kW.units = EngineeringUnits("kilowatts")
    Nine_AM_kW.description = CharacterString(
        "9AM Electrical Demand"
    )


    ####kW#######10Am
    Ten_AM_kW = create_AV(
        oid=5, name="10:00AM_Forecasted_kW", pv=0, pv_writable=False
    )
    Ten_AM_kW.units = EngineeringUnits("kilowatts")
    Ten_AM_kW.description = CharacterString(
        "10AM Electrical Demand"
    )

    ####kW#######11Am
    Eleven_AM_kW = create_AV(
        oid=6, name="11:00AM_Forecasted_kW", pv=0, pv_writable=False
    )
    Eleven_AM_kW.units = EngineeringUnits("kilowatts")
    Eleven_AM_kW.description = CharacterString(
        "11AM Electrical Demand"
    )

    ####kW#######12Pm
    Twelve_PM_kW = create_AV(
        oid=7, name="12:00PM_Forecasted_kW", pv=0, pv_writable=False
    )
    Twelve_PM_kW.units = EngineeringUnits("kilowatts")
    Twelve_PM_kW.description = CharacterString(
        "12PM Electrical Demand"
    )

    ####kW#######1Pm
    One_PM_kW = create_AV(
        oid=8, name="1:00PM_Forecasted_kW", pv=0, pv_writable=False
    )
    One_PM_kW.units = EngineeringUnits("kilowatts")
    One_PM_kW.description = CharacterString(
        "1PM Electrical Demand"
    )

    ####kW#######2Pm
    Two_PM_kW = create_AV(
        oid=9, name="2:00PM_Forecasted_kW", pv=0, pv_writable=False
    )
    Two_PM_kW.units = EngineeringUnits("kilowatts")
    Two_PM_kW.description = CharacterString(
        "2PM Electrical Demand"
    )

    ####kW#######3Pm
    Three_PM_kW = create_AV(
        oid=10, name="3:00PM_Forecasted_kW", pv=0, pv_writable=False
    )
    Three_PM_kW.units = EngineeringUnits("kilowatts")
    Three_PM_kW.description = CharacterString(
        "3PM Electrical Demand"
    )

    ####kW#######4Pm
    Four_PM_kW = create_AV(
        oid=11, name="4:00PM_Forecasted_kW", pv=0, pv_writable=False
    )
    Four_PM_kW.units = EngineeringUnits("kilowatts")
    Four_PM_kW.description = CharacterString(
        "4PM Electrical Demand"
    )

    ####kW#######5Pm
    Five_PM_kW = create_AV(
        oid=12, name="5:00PM_Forecasted_kW", pv=0, pv_writable=False
    )
    Five_PM_kW.units = EngineeringUnits("kilowatts")
    Five_PM_kW.description = CharacterString(
        "5PM Electrical Demand"
    )

    ####kW#######6Pm
    Six_PM_kW = create_AV(
        oid=13, name="6:00PM_Forecasted_kW", pv=0, pv_writable=False
    )
    Six_PM_kW.units = EngineeringUnits("kilowatts")
    Six_PM_kW.description = CharacterString(
        "6PM Electrical Demand"
    )

    ####kW#######7Pm
    Seven_PM_kW = create_AV(
        oid=14, name="7:00PM_Forecasted_kW", pv=0, pv_writable=False
    )
    Seven_PM_kW.units = EngineeringUnits("kilowatts")
    Seven_PM_kW.description = CharacterString(
        "7PM Electrical Demand"
    )

    ####kW#######8Pm
    Eight_PM_kW = create_AV(
        oid=15, name="8:00PM_Forecasted_kW", pv=0, pv_writable=False
    )
    Eight_PM_kW.units = EngineeringUnits("kilowatts")
    Eight_PM_kW.description = CharacterString(
        "8PM Electrical Demand"
    )


    ####kW#######rmse
    rootmse = create_AV(
        oid=16, name="Model_RMSE", pv=0, pv_writable=False
    )
    rootmse.units = EngineeringUnits("kilowatts")
    rootmse.description = CharacterString(
        "Model Root Mean Squared Error"
    )

    ####kW#######mean
    modelmean = create_AV(
        oid=17, name="Model_MEAN", pv=0, pv_writable=False
    )
    modelmean.units = EngineeringUnits("kilowatts")
    modelmean.description = CharacterString(
        "Model Mean Value to Compare with RSME"
    )

    ####kW#######mean
    trainmins = create_AV(
        oid=18, name="Model_Train_Time", pv=0, pv_writable=False
    )
    trainmins.units = EngineeringUnits("minutes")
    trainmins.description = CharacterString(
        "Elapsed time training prediction model in minutes"
    )


    new_device.this_application.add_object(Five_AM_kW)
    new_device.this_application.add_object(Six_AM_kW)
    new_device.this_application.add_object(Seven_AM_kW)
    new_device.this_application.add_object(Eight_AM_kW)
    new_device.this_application.add_object(Nine_AM_kW)
    new_device.this_application.add_object(Ten_AM_kW)
    new_device.this_application.add_object(Eleven_AM_kW)
    new_device.this_application.add_object(Twelve_PM_kW)
    new_device.this_application.add_object(One_PM_kW)
    new_device.this_application.add_object(Two_PM_kW)
    new_device.this_application.add_object(Three_PM_kW)
    new_device.this_application.add_object(Four_PM_kW)
    new_device.this_application.add_object(Five_PM_kW)
    new_device.this_application.add_object(Six_PM_kW)
    new_device.this_application.add_object(Seven_PM_kW)
    new_device.this_application.add_object(Eight_PM_kW)
    new_device.this_application.add_object(rootmse)
    new_device.this_application.add_object(modelmean)
    new_device.this_application.add_object(trainmins)

    return new_device



class App:
    dev = start_device()
    model = Model()

app = App()


def update_model():

    app.model.update()
    Five_AM_kW= app.dev.this_application.get_object_id(("analogValue", 0))
    Six_AM_kW= app.dev.this_application.get_object_id(("analogValue", 1))
    Seven_AM_kW= app.dev.this_application.get_object_id(("analogValue", 2))
    Eight_AM_kW= app.dev.this_application.get_object_id(("analogValue", 3))
    Nine_AM_kW= app.dev.this_application.get_object_id(("analogValue", 4))
    Ten_AM_kW= app.dev.this_application.get_object_id(("analogValue", 5))
    Eleven_AM_kW= app.dev.this_application.get_object_id(("analogValue", 6))
    Twelve_PM_kW= app.dev.this_application.get_object_id(("analogValue", 7))
    One_PM_kW= app.dev.this_application.get_object_id(("analogValue", 8))
    Two_PM_kW= app.dev.this_application.get_object_id(("analogValue", 9))
    Three_PM_kW= app.dev.this_application.get_object_id(("analogValue", 10))
    Four_PM_kW= app.dev.this_application.get_object_id(("analogValue", 11))
    Five_PM_kW= app.dev.this_application.get_object_id(("analogValue", 12))
    Six_PM_kW= app.dev.this_application.get_object_id(("analogValue", 13))
    Seven_PM_kW= app.dev.this_application.get_object_id(("analogValue", 14))
    Eight_PM_kW= app.dev.this_application.get_object_id(("analogValue", 15))
    rootmse= app.dev.this_application.get_object_id(("analogValue", 16))
    modelmean= app.dev.this_application.get_object_id(("analogValue", 17))
    trainmins= app.dev.this_application.get_object_id(("analogValue", 18))

    new_Five_AM_kW = app.model.kW_5AM
    new_Six_AM_kW = app.model.kW_6AM
    new_Seven_AM_kW = app.model.kW_7AM
    new_Eight_AM_kW = app.model.kW_8AM
    new_Nine_AM_kW = app.model.kW_9AM
    new_Ten_AM_kW = app.model.kW_10AM
    new_Eleven_AM_kW = app.model.kW_11AM
    new_Twelve_PM_kW = app.model.kW_12PM
    new_One_PM_kW = app.model.kW_1PM
    new_Two_PM_kW = app.model.kW_2PM
    new_Three_PM_kW = app.model.kW_3PM
    new_Four_PM_kW = app.model.kW_4PM
    new_Five_PM_kW = app.model.kW_5PM
    new_Six_PM_kW = app.model.kW_6PM
    new_Seven_PM_kW = app.model.kW_7PM
    new_Eight_PM_kW = app.model.kW_8PM
    new_rootmse = app.model.model_rsme
    new_modelmean = app.model.model_mean
    new_trainmins = app.model.train_minutes

    app.dev._log.info("Setting {}, type {}, to {}".format(Five_AM_kW, type(Five_AM_kW), new_Five_AM_kW))
    Five_AM_kW.presentValue = new_Five_AM_kW

    app.dev._log.info("Setting {}, type {}, to {}".format(Six_AM_kW, type(Six_AM_kW), new_Six_AM_kW))
    Six_AM_kW.presentValue = new_Five_AM_kW

    app.dev._log.info("Setting {}, type {}, to {}".format(Seven_AM_kW, type(Seven_AM_kW), new_Seven_AM_kW))
    Seven_AM_kW.presentValue = new_Five_AM_kW

    app.dev._log.info("Setting {}, type {}, to {}".format(Eight_AM_kW, type(Eight_AM_kW), new_Eight_AM_kW))
    Eight_AM_kW.presentValue = new_Eight_AM_kW

    app.dev._log.info("Setting {}, type {}, to {}".format(Nine_AM_kW, type(Nine_AM_kW), new_Nine_AM_kW))
    Nine_AM_kW.presentValue = new_Five_AM_kW

    app.dev._log.info("Setting {}, type {}, to {}".format(Ten_AM_kW, type(Ten_AM_kW), new_Ten_AM_kW))
    Ten_AM_kW.presentValue = new_Five_AM_kW

    app.dev._log.info("Setting {}, type {}, to {}".format(Eleven_AM_kW, type(Eleven_AM_kW), new_Eleven_AM_kW))
    Eleven_AM_kW.presentValue = new_Eleven_AM_kW

    app.dev._log.info("Setting {}, type {}, to {}".format(Twelve_PM_kW, type(Twelve_PM_kW), new_Twelve_PM_kW))
    Twelve_PM_kW.presentValue = new_Two_PM_kW

    app.dev._log.info("Setting {}, type {}, to {}".format(One_PM_kW, type(One_PM_kW), new_One_PM_kW))
    One_PM_kW.presentValue = new_Two_PM_kW

    app.dev._log.info("Setting {}, type {}, to {}".format(Two_PM_kW, type(Two_PM_kW), new_Two_PM_kW))
    Two_PM_kW.presentValue = new_Two_PM_kW

    app.dev._log.info("Setting {}, type {}, to {}".format(Three_PM_kW, type(Three_PM_kW), new_Three_PM_kW))
    Three_PM_kW.presentValue = new_Two_PM_kW

    app.dev._log.info("Setting {}, type {}, to {}".format(Four_PM_kW, type(Four_PM_kW), new_Four_PM_kW))
    Four_PM_kW.presentValue = new_Two_PM_kW

    app.dev._log.info("Setting {}, type {}, to {}".format(Five_PM_kW, type(Five_PM_kW), new_Five_PM_kW))
    Five_PM_kW.presentValue = new_Five_PM_kW

    app.dev._log.info("Setting {}, type {}, to {}".format(Six_PM_kW, type(Six_PM_kW), new_Six_PM_kW))
    Six_PM_kW.presentValue = new_Five_PM_kW

    app.dev._log.info("Setting {}, type {}, to {}".format(Seven_PM_kW, type(Seven_PM_kW), new_Seven_PM_kW))
    Seven_PM_kW.presentValue = new_Five_PM_kW

    app.dev._log.info("Setting {}, type {}, to {}".format(Eight_PM_kW, type(Eight_PM_kW), new_Eight_PM_kW))
    Eight_PM_kW.presentValue = new_Eight_PM_kW

    app.dev._log.info("Setting {}, type {}, to {}".format(rootmse, type(rootmse), new_rootmse))
    rootmse.presentValue = new_rootmse

    app.dev._log.info("Setting {}, type {}, to {}".format(modelmean, type(modelmean), new_modelmean))
    modelmean.presentValue = new_modelmean

    app.dev._log.info("Setting {}, type {}, to {}".format(trainmins, type(trainmins), new_trainmins))
    trainmins.presentValue = new_trainmins



def get_meter_data():
    '''
    perform read request on electricity meter
    '''

    allStuff = {}
    stamp = time.time()

    try:
        allStuff['Date'] = stamp

        app.dev._log.info("Attempting to perform BACnet read request")
        kW = app.dev.read('12345:2 analogInput 2 presentValue')
        app.dev._log.info("Bacnet read request of the electric meter is {}".format(kW))

        allStuff['kW'] = kW


    except:
        app.dev._log.error("Error performing BACnet Read Request! {}".format(error))

        allStuff['Date'] = numpy.nan
        allStuff['kW'] = numpy.nan



    try:

        '''
        attempt to save data to Sqlite
        '''

        allStuff['Date'] = datetime.fromtimestamp(allStuff['Date'])
        master_data = pd.DataFrame(allStuff,index=[0])
        master_data = master_data.set_index('Date')


        engine = create_engine('sqlite:///save_data.db')
        sqlite_connection = engine.connect()
        sqlite_table = "all_data"
        master_data.to_sql(sqlite_table, sqlite_connection, if_exists='append')
        sqlite_connection.close()
        app.dev._log.info("Data saved to Sqlite")


    except:
        app.dev._log.warning("No data being saved to db!")


'''

def main():
    task_device_one = RecurringTask(get_meter_data, delay=60)
    task_device_one.start()
    task_device_two = RecurringTask(update_model, delay=1200)
    task_device_two.start()

    while True:
        pass


'''

def main():
    task_device_one = RecurringTask(get_meter_data, delay=60)
    task_device_one.start()

    x=datetime.today()
    y = x.replace(day=x.day, hour=4, minute=30, second=0, microsecond=0) + timedelta(days=1)
    delta_t=y-x
    secs=delta_t.total_seconds()
    t = Timer(secs, update_model)
    t.start()
    while True:
        pass


if __name__ == "__main__":
    main()
