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

from electrical_model import elec_Model
from clgload_model import clg_Model
from costs_calcs import Enery_Costs_Calcs



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
        "Hour of 5AM to 6AM Averaged Electrical Demand"
    )

    ####kW#######6Am
    Six_AM_kW = create_AV(
        oid=1, name="6:00AM_Forecasted_kW", pv=0, pv_writable=False
    )
    Six_AM_kW.units = EngineeringUnits("kilowatts")
    Six_AM_kW.description = CharacterString(
        "Hour of 6AM to 7AM Averaged Electrical Demand"
    )


    ####kW#######7Am
    Seven_AM_kW = create_AV(
        oid=2, name="7:00AM_Forecasted_kW", pv=0, pv_writable=False
    )
    Seven_AM_kW.units = EngineeringUnits("kilowatts")
    Seven_AM_kW.description = CharacterString(
        "Hour of 7AM to 8AM Averaged Electrical Demand"
    )


    ####kW#######8Am
    Eight_AM_kW = create_AV(
        oid=3, name="8:00AM_Forecasted_kW", pv=0, pv_writable=False
    )
    Eight_AM_kW.units = EngineeringUnits("kilowatts")
    Eight_AM_kW.description = CharacterString(
        "Hour of 8AM to 9AM Averaged Electrical Demand"
    )

    ####kW#######9Am
    Nine_AM_kW = create_AV(
        oid=4, name="9:00AM_Forecasted_kW", pv=0, pv_writable=False
    )
    Nine_AM_kW.units = EngineeringUnits("kilowatts")
    Nine_AM_kW.description = CharacterString(
        "Hour of 9AM to 10AM Averaged Electrical Demand"
    )


    ####kW#######10Am
    Ten_AM_kW = create_AV(
        oid=5, name="10:00AM_Forecasted_kW", pv=0, pv_writable=False
    )
    Ten_AM_kW.units = EngineeringUnits("kilowatts")
    Ten_AM_kW.description = CharacterString(
        "Hour of 10AM to 11AM Averaged Electrical Demand"
    )

    ####kW#######11Am
    Eleven_AM_kW = create_AV(
        oid=6, name="11:00AM_Forecasted_kW", pv=0, pv_writable=False
    )
    Eleven_AM_kW.units = EngineeringUnits("kilowatts")
    Eleven_AM_kW.description = CharacterString(
        "Hour of 11AM to 12PM Averaged Electrical Demand"
    )

    ####kW#######12Pm
    Twelve_PM_kW = create_AV(
        oid=7, name="12:00PM_Forecasted_kW", pv=0, pv_writable=False
    )
    Twelve_PM_kW.units = EngineeringUnits("kilowatts")
    Twelve_PM_kW.description = CharacterString(
        "Hour of 12PM to 1PM Averaged Electrical Demand"
    )

    ####kW#######1Pm
    One_PM_kW = create_AV(
        oid=8, name="1:00PM_Forecasted_kW", pv=0, pv_writable=False
    )
    One_PM_kW.units = EngineeringUnits("kilowatts")
    One_PM_kW.description = CharacterString(
        "Hour of 1PM to 2PM Averaged Electrical Demand"
    )

    ####kW#######2Pm
    Two_PM_kW = create_AV(
        oid=9, name="2:00PM_Forecasted_kW", pv=0, pv_writable=False
    )
    Two_PM_kW.units = EngineeringUnits("kilowatts")
    Two_PM_kW.description = CharacterString(
        "Hour of 2PM to 3PM Averaged Electrical Demand"
    )

    ####kW#######3Pm
    Three_PM_kW = create_AV(
        oid=10, name="3:00PM_Forecasted_kW", pv=0, pv_writable=False
    )
    Three_PM_kW.units = EngineeringUnits("kilowatts")
    Three_PM_kW.description = CharacterString(
        "Hour of 3PM to 4PM Averaged Electrical Demand"
    )

    ####kW#######4Pm
    Four_PM_kW = create_AV(
        oid=11, name="4:00PM_Forecasted_kW", pv=0, pv_writable=False
    )
    Four_PM_kW.units = EngineeringUnits("kilowatts")
    Four_PM_kW.description = CharacterString(
        "Hour of 4PM to 5PM Averaged Electrical Demand"
    )

    ####kW#######5Pm
    Five_PM_kW = create_AV(
        oid=12, name="5:00PM_Forecasted_kW", pv=0, pv_writable=False
    )
    Five_PM_kW.units = EngineeringUnits("kilowatts")
    Five_PM_kW.description = CharacterString(
        "Hour of 5PM to 6PM Averaged Electrical Demand"
    )

    ####kW#######6Pm
    Six_PM_kW = create_AV(
        oid=13, name="6:00PM_Forecasted_kW", pv=0, pv_writable=False
    )
    Six_PM_kW.units = EngineeringUnits("kilowatts")
    Six_PM_kW.description = CharacterString(
        "Hour of 6PM to 7PAM Averaged Electrical Demand"
    )

    ####kW#######7Pm
    Seven_PM_kW = create_AV(
        oid=14, name="7:00PM_Forecasted_kW", pv=0, pv_writable=False
    )
    Seven_PM_kW.units = EngineeringUnits("kilowatts")
    Seven_PM_kW.description = CharacterString(
        "Hour of 7PM to 8PM Averaged Electrical Demand"
    )

    ####kW#######8Pm
    Eight_PM_kW = create_AV(
        oid=15, name="8:00PM_Forecasted_kW", pv=0, pv_writable=False
    )
    Eight_PM_kW.units = EngineeringUnits("kilowatts")
    Eight_PM_kW.description = CharacterString(
        "Hour of 8PM to 9PM Averaged Electrical Demand"
    )


    ####kW#######dickeyFullerElec
    electric_modelpval = create_AV(
        oid=17, name="Electrical_Forecast_Model_P_Val", pv=0, pv_writable=False
    )
    electric_modelpval.description = CharacterString(
        "Dickey-Fuller Test P-value for the statistics forecast ARIMA model"
    )

        ####kW#######minutes
    electrainmins = create_AV(
        oid=18, name="Elec_Model_Train_Time", pv=0, pv_writable=False
    )
    electrainmins.units = EngineeringUnits("minutes")
    electrainmins.description = CharacterString(
        "Elapsed time training electrical prediction model in minutes"
    )


    '''
    CLG points next
    '''

    ####kW#######5Am
    Five_AM_BTU_Hr = create_AV(
        oid=19, name="5:00AM_Forecasted_BTU_Hr", pv=0, pv_writable=False
    )
    Five_AM_BTU_Hr.units = EngineeringUnits("btusPerHour")
    Five_AM_BTU_Hr.description = CharacterString(
        "Hour of 5AM to 6AM Averaged Demand Cooling Load"
    )

    ####kW#######6Am
    Six_AM_BTU_Hr = create_AV(
        oid=20, name="6:00AM_Forecasted_BTU_Hr", pv=0, pv_writable=False
    )
    Six_AM_BTU_Hr.units = EngineeringUnits("btusPerHour")
    Six_AM_BTU_Hr.description = CharacterString(
        "Hour of 6AM to 7AM Averaged Demand Cooling Load"
    )


    ####kW#######7Am
    Seven_AM_BTU_Hr = create_AV(
        oid=21, name="7:00AM_Forecasted_BTU_Hr", pv=0, pv_writable=False
    )
    Seven_AM_BTU_Hr.units = EngineeringUnits("btusPerHour")
    Seven_AM_BTU_Hr.description = CharacterString(
        "Hour of 7AM to 8AM Averaged Demand Cooling Load"
    )


    ####kW#######8Am
    Eight_AM_BTU_Hr = create_AV(
        oid=22, name="8:00AM_Forecasted_BTU_Hr", pv=0, pv_writable=False
    )
    Eight_AM_BTU_Hr.units = EngineeringUnits("btusPerHour")
    Eight_AM_BTU_Hr.description = CharacterString(
        "Hour of 8AM to 9AM Averaged Demand Cooling Load"
    )

    ####kW#######9Am
    Nine_AM_BTU_Hr = create_AV(
        oid=23, name="9:00AM_Forecasted_BTU_Hr", pv=0, pv_writable=False
    )
    Nine_AM_BTU_Hr.units = EngineeringUnits("btusPerHour")
    Nine_AM_BTU_Hr.description = CharacterString(
        "Hour of 9AM to 10AM Averaged Demand Cooling Load"
    )


    ####kW#######10Am
    Ten_AM_BTU_Hr = create_AV(
        oid=24, name="10:00AM_Forecasted_BTU_Hr", pv=0, pv_writable=False
    )
    Ten_AM_BTU_Hr.units = EngineeringUnits("btusPerHour")
    Ten_AM_BTU_Hr.description = CharacterString(
        "Hour of 10AM to 11AM Averaged Demand Cooling Load"
    )

    ####kW#######11Am
    Eleven_AM_BTU_Hr = create_AV(
        oid=25, name="11:00AM_Forecasted_BTU_Hr", pv=0, pv_writable=False
    )
    Eleven_AM_BTU_Hr.units = EngineeringUnits("btusPerHour")
    Eleven_AM_BTU_Hr.description = CharacterString(
        "Hour of 11AM to 12PM Averaged Demand Cooling Load"
    )

    ####kW#######12Pm
    Twelve_PM_BTU_Hr = create_AV(
        oid=26, name="12:00PM_Forecasted_BTU_Hr", pv=0, pv_writable=False
    )
    Twelve_PM_BTU_Hr.units = EngineeringUnits("btusPerHour")
    Twelve_PM_BTU_Hr.description = CharacterString(
        "Hour of 12PM to 1PM Averaged Demand Cooling Load"
    )

    ####kW#######1Pm
    One_PM_BTU_Hr = create_AV(
        oid=27, name="1:00PM_Forecasted_BTU_Hr", pv=0, pv_writable=False
    )
    One_PM_BTU_Hr.units = EngineeringUnits("btusPerHour")
    One_PM_BTU_Hr.description = CharacterString(
        "Hour of 1PM to 2PM Averaged Demand Cooling Load"
    )

    ####kW#######2Pm
    Two_PM_BTU_Hr = create_AV(
        oid=28, name="2:00PM_Forecasted_BTU_Hr", pv=0, pv_writable=False
    )
    Two_PM_BTU_Hr.units = EngineeringUnits("btusPerHour")
    Two_PM_BTU_Hr.description = CharacterString(
        "Hour of 2PM to 3PM Averaged Demand Cooling Load"
    )

    ####kW#######3Pm
    Three_PM_BTU_Hr = create_AV(
        oid=29, name="3:00PM_Forecasted_BTU_Hr", pv=0, pv_writable=False
    )
    Three_PM_BTU_Hr.units = EngineeringUnits("btusPerHour")
    Three_PM_BTU_Hr.description = CharacterString(
        "Hour of 3PM to 4PM Averaged Demand Cooling Load"
    )

    ####kW#######4Pm
    Four_PM_BTU_Hr = create_AV(
        oid=30, name="4:00PM_Forecasted_BTU_Hr", pv=0, pv_writable=False
    )
    Four_PM_BTU_Hr.units = EngineeringUnits("btusPerHour")
    Four_PM_BTU_Hr.description = CharacterString(
        "Hour of 4PM to 5PM Averaged Demand Cooling Load"
    )

    ####kW#######5Pm
    Five_PM_BTU_Hr = create_AV(
        oid=31, name="5:00PM_Forecasted_BTU_Hr", pv=0, pv_writable=False
    )
    Five_PM_BTU_Hr.units = EngineeringUnits("btusPerHour")
    Five_PM_BTU_Hr.description = CharacterString(
        "Hour of 5PM to 6PM Averaged Demand Cooling Load"
    )

    ####kW#######6Pm
    Six_PM_BTU_Hr = create_AV(
        oid=32, name="6:00PM_Forecasted_BTU_Hr", pv=0, pv_writable=False
    )
    Six_PM_BTU_Hr.units = EngineeringUnits("btusPerHour")
    Six_PM_BTU_Hr.description = CharacterString(
        "Hour of 6PM to 7PM Averaged Demand Cooling Load"
    )

    ####kW#######7Pm
    Seven_PM_BTU_Hr = create_AV(
        oid=33, name="7:00PM_Forecasted_BTU_Hr", pv=0, pv_writable=False
    )
    Seven_PM_BTU_Hr.units = EngineeringUnits("btusPerHour")
    Seven_PM_BTU_Hr.description = CharacterString(
        "Hour of 7PM to 8PM Averaged Demand Cooling Load"
    )

    ####kW#######8Pm
    Eight_PM_BTU_Hr = create_AV(
        oid=34, name="8:00PM_Forecasted_BTU_Hr", pv=0, pv_writable=False
    )
    Eight_PM_BTU_Hr.units = EngineeringUnits("btusPerHour")
    Eight_PM_BTU_Hr.description = CharacterString(
        "Hour of 8PM to 9PM Averaged Demand Cooling Load"
    )


    ####kW#######dickeyFullerElec
    clg_modelpval = create_AV(
        oid=35, name="Clg_Forecast_Model_P_Val", pv=0, pv_writable=False
    )
    clg_modelpval.description = CharacterString(
        "Dickey-Fuller Test P-value for the statistics forecast ARIMA model"
    )

        ####kW#######minutes
    clgtrainmins = create_AV(
        oid=36, name="Clg_Model_Train_Time", pv=0, pv_writable=False
    )
    clgtrainmins.units = EngineeringUnits("minutes")
    clgtrainmins.description = CharacterString(
        "Elapsed time training cooling prediction model in minutes"
    )

    '''
    COST$ points next
    '''
    ####kW#######5Am
    Five_AM_costs = create_AV(
        oid=37, name="5:00AM_Estimated_Costs", pv=0, pv_writable=False
    )
    Five_AM_costs.units = EngineeringUnits("currency1")
    Five_AM_costs.description = CharacterString(
        "Hour of 5AM to 6AM Estimated Energy Costs"
    )

    ####kW#######6Am
    Six_AM_costs = create_AV(
        oid=38, name="6:00AM_Estimated_Costs", pv=0, pv_writable=False
    )
    Six_AM_costs.units = EngineeringUnits("currency1")
    Six_AM_costs.description = CharacterString(
        "Hour of 6AM to 7AM Estimated Energy Costs"
    )


    ####kW#######7Am
    Seven_AM_costs = create_AV(
        oid=39, name="7:00AM_Estimated_Costs", pv=0, pv_writable=False
    )
    Seven_AM_costs.units = EngineeringUnits("currency1")
    Seven_AM_costs.description = CharacterString(
        "Hour of 7AM to 8AM Estimated Energy Costs"
    )


    ####kW#######8Am
    Eight_AM_costs = create_AV(
        oid=40, name="8:00AM_Estimated_Costs", pv=0, pv_writable=False
    )
    Eight_AM_costs.units = EngineeringUnits("currency1")
    Eight_AM_costs.description = CharacterString(
        "Hour of 8AM to 9AM Estimated Energy Costs"
    )

    ####kW#######9Am
    Nine_AM_costs = create_AV(
        oid=41, name="9:00AM_Estimated_Costs", pv=0, pv_writable=False
    )
    Nine_AM_costs.units = EngineeringUnits("currency1")
    Nine_AM_costs.description = CharacterString(
        "Hour of 9AM to 10AM Estimated Energy Costs"
    )


    ####kW#######10Am
    Ten_AM_costs = create_AV(
        oid=42, name="10:00AM_Estimated_Costs", pv=0, pv_writable=False
    )
    Ten_AM_costs.units = EngineeringUnits("currency1")
    Ten_AM_costs.description = CharacterString(
        "Hour of 10AM to 11AM Estimated Energy Costs"
    )

    ####kW#######11Am
    Eleven_AM_costs = create_AV(
        oid=43, name="11:00AM_Estimated_Costs", pv=0, pv_writable=False
    )
    Eleven_AM_costs.units = EngineeringUnits("currency1")
    Eleven_AM_costs.description = CharacterString(
        "Hour of 11AM to 12PM Estimated Energy Costs"
    )

    ####kW#######12Pm
    Twelve_PM_costs = create_AV(
        oid=44, name="12:00PM_Estimated_Costs", pv=0, pv_writable=False
    )
    Twelve_PM_costs.units = EngineeringUnits("currency1")
    Twelve_PM_costs.description = CharacterString(
        "Hour of 12PM to 1PM Estimated Energy Costs"
    )

    ####kW#######1Pm
    One_PM_costs = create_AV(
        oid=45, name="1:00PM_Estimated_Costs", pv=0, pv_writable=False
    )
    One_PM_costs.units = EngineeringUnits("currency1")
    One_PM_costs.description = CharacterString(
        "Hour of 1PM to 2PM Estimated Energy Costs"
    )

    ####kW#######2Pm
    Two_PM_costs = create_AV(
        oid=46, name="2:00PM_Estimated_Costs", pv=0, pv_writable=False
    )
    Two_PM_costs.units = EngineeringUnits("currency1")
    Two_PM_costs.description = CharacterString(
        "Hour of 2PM to 3PM Estimated Energy Costs"
    )

    ####kW#######3Pm
    Three_PM_costs = create_AV(
        oid=47, name="3:00PM_Estimated_Costs", pv=0, pv_writable=False
    )
    Three_PM_costs.units = EngineeringUnits("currency1")
    Three_PM_costs.description = CharacterString(
        "Hour of 3PM to 4PM Estimated Energy Costs"
    )

    ####kW#######4Pm
    Four_PM_costs = create_AV(
        oid=48, name="4:00PM_Estimated_Costs", pv=0, pv_writable=False
    )
    Four_PM_costs.units = EngineeringUnits("currency1")
    Four_PM_costs.description = CharacterString(
        "Hour of 4PM to 5PM Estimated Energy Costs"
    )

    ####kW#######5Pm
    Five_PM_costs = create_AV(
        oid=49, name="5:00PM_Estimated_Costs", pv=0, pv_writable=False
    )
    Five_PM_costs.units = EngineeringUnits("currency1")
    Five_PM_costs.description = CharacterString(
        "Hour of 5PM to 6PM Estimated Energy Costs"
    )

    ####kW#######6Pm
    Six_PM_costs = create_AV(
        oid=50, name="6:00PM_Estimated_Costs", pv=0, pv_writable=False
    )
    Six_PM_costs.units = EngineeringUnits("currency1")
    Six_PM_costs.description = CharacterString(
        "Hour of 6PM to 7PM Estimated Energy Costs"
    )

    ####kW#######7Pm
    Seven_PM_costs = create_AV(
        oid=51, name="7:00PM_Estimated_Costs", pv=0, pv_writable=False
    )
    Seven_PM_costs.units = EngineeringUnits("currency1")
    Seven_PM_costs.description = CharacterString(
        "Hour of 7PM to 8PM Estimated Energy Costs"
    )

    ####kW#######8Pm
    Eight_PM_costs = create_AV(
        oid=52, name="8:00PM_Estimated_Costs", pv=0, pv_writable=False
    )
    Eight_PM_costs.units = EngineeringUnits("currency1")
    Eight_PM_costs.description = CharacterString(
        "Hour of 8PM to 9PM Estimated Energy Costs"
    )


    '''
    Costs arent modeled, just calculated based on utility rates
    '''

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
    new_device.this_application.add_object(electric_modelpval)
    new_device.this_application.add_object(electrainmins)

    new_device.this_application.add_object(Five_AM_BTU_Hr)
    new_device.this_application.add_object(Six_AM_BTU_Hr)
    new_device.this_application.add_object(Seven_AM_BTU_Hr)
    new_device.this_application.add_object(Eight_AM_BTU_Hr)
    new_device.this_application.add_object(Nine_AM_BTU_Hr)
    new_device.this_application.add_object(Ten_AM_BTU_Hr)
    new_device.this_application.add_object(Eleven_AM_BTU_Hr)
    new_device.this_application.add_object(Twelve_PM_BTU_Hr)
    new_device.this_application.add_object(One_PM_BTU_Hr)
    new_device.this_application.add_object(Two_PM_BTU_Hr)
    new_device.this_application.add_object(Three_PM_BTU_Hr)
    new_device.this_application.add_object(Four_PM_BTU_Hr)
    new_device.this_application.add_object(Five_PM_BTU_Hr)
    new_device.this_application.add_object(Six_PM_BTU_Hr)
    new_device.this_application.add_object(Seven_PM_BTU_Hr)
    new_device.this_application.add_object(Eight_PM_BTU_Hr)
    new_device.this_application.add_object(clg_modelpval)
    new_device.this_application.add_object(clgtrainmins)

    new_device.this_application.add_object(Five_AM_costs)
    new_device.this_application.add_object(Six_AM_costs)
    new_device.this_application.add_object(Seven_AM_costs)
    new_device.this_application.add_object(Eight_AM_costs)
    new_device.this_application.add_object(Nine_AM_costs)
    new_device.this_application.add_object(Ten_AM_costs)
    new_device.this_application.add_object(Eleven_AM_costs)
    new_device.this_application.add_object(Twelve_PM_costs)
    new_device.this_application.add_object(One_PM_costs)
    new_device.this_application.add_object(Two_PM_costs)
    new_device.this_application.add_object(Three_PM_costs)
    new_device.this_application.add_object(Four_PM_costs)
    new_device.this_application.add_object(Five_PM_costs)
    new_device.this_application.add_object(Six_PM_costs)
    new_device.this_application.add_object(Seven_PM_costs)
    new_device.this_application.add_object(Eight_PM_costs)


    return new_device



class App:
    dev = start_device()
    electric_model = elec_Model()
    clgload_model = clg_Model()
    costs_calculations = Enery_Costs_Calcs()


app = App()


def electric_update_model():

    app.electric_model.update()

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
    electric_modelpval= app.dev.this_application.get_object_id(("analogValue", 17))
    electrainmins= app.dev.this_application.get_object_id(("analogValue", 18))


    Five_AM_kW.presentValue = app.electric_model.kW_5AM
    Six_AM_kW.presentValue = app.electric_model.kW_6AM
    Seven_AM_kW.presentValue = app.electric_model.kW_7AM
    Eight_AM_kW.presentValue = app.electric_model.kW_8AM
    Nine_AM_kW.presentValue = app.electric_model.kW_9AM
    Ten_AM_kW.presentValue = app.electric_model.kW_10AM
    Eleven_AM_kW.presentValue = app.electric_model.kW_11AM
    Twelve_PM_kW.presentValue = app.electric_model.kW_12PM
    One_PM_kW.presentValue = app.electric_model.kW_1PM
    Two_PM_kW.presentValue = app.electric_model.kW_2PM
    Three_PM_kW.presentValue = app.electric_model.kW_3PM
    Four_PM_kW.presentValue = app.electric_model.kW_4PM
    Five_PM_kW.presentValue = app.electric_model.kW_5PM
    Six_PM_kW.presentValue = app.electric_model.kW_6PM
    Seven_PM_kW.presentValue = app.electric_model.kW_7PM
    Eight_PM_kW.presentValue = app.electric_model.kW_8PM
    electric_modelpval.presentValue = app.electric_model.dickfulr_pval
    electrainmins.presentValue = app.electric_model.train_minutes

    clg_update_model()
    cost_updates()


def clg_update_model():

    app.clgload_model.update()

    Five_AM_BTU_Hr= app.dev.this_application.get_object_id(("analogValue", 19))
    Six_AM_BTU_Hr= app.dev.this_application.get_object_id(("analogValue", 20))
    Seven_AM_BTU_Hr= app.dev.this_application.get_object_id(("analogValue", 21))
    Eight_AM_BTU_Hr= app.dev.this_application.get_object_id(("analogValue", 21))
    Nine_AM_BTU_Hr= app.dev.this_application.get_object_id(("analogValue", 23))
    Ten_AM_BTU_Hr= app.dev.this_application.get_object_id(("analogValue", 24))
    Eleven_AM_BTU_Hr= app.dev.this_application.get_object_id(("analogValue", 25))
    Twelve_PM_BTU_Hr= app.dev.this_application.get_object_id(("analogValue", 26))
    One_PM_BTU_Hr= app.dev.this_application.get_object_id(("analogValue", 27))
    Two_PM_BTU_Hr= app.dev.this_application.get_object_id(("analogValue", 28))
    Three_PM_BTU_Hr= app.dev.this_application.get_object_id(("analogValue", 29))
    Four_PM_BTU_Hr= app.dev.this_application.get_object_id(("analogValue", 30))
    Five_PM_BTU_Hr= app.dev.this_application.get_object_id(("analogValue", 31))
    Six_PM_BTU_Hr= app.dev.this_application.get_object_id(("analogValue", 32))
    Seven_PM_BTU_Hr= app.dev.this_application.get_object_id(("analogValue", 33))
    Eight_PM_BTU_Hr= app.dev.this_application.get_object_id(("analogValue", 34))
    clg_modelpval= app.dev.this_application.get_object_id(("analogValue", 35))
    clgtrainmins= app.dev.this_application.get_object_id(("analogValue", 36))


    Five_AM_BTU_Hr.presentValue = app.clgload_model.btuhr_5AM
    Six_AM_BTU_Hr.presentValue = app.clgload_model.btuhr_6AM
    Seven_AM_BTU_Hr.presentValue = app.clgload_model.btuhr_7AM
    Seven_AM_BTU_Hr.presentValue = app.clgload_model.btuhr_8AM
    Nine_AM_BTU_Hr.presentValue = app.clgload_model.btuhr_9AM
    Ten_AM_BTU_Hr.presentValue = app.clgload_model.btuhr_10AM
    Eleven_AM_BTU_Hr.presentValue = app.clgload_model.btuhr_11AM
    Twelve_PM_BTU_Hr.presentValue = app.clgload_model.btuhr_12PM
    One_PM_BTU_Hr.presentValue = app.clgload_model.btuhr_1PM
    Two_PM_BTU_Hr.presentValue = app.clgload_model.btuhr_2PM
    Three_PM_BTU_Hr.presentValue = app.clgload_model.btuhr_3PM
    Four_PM_BTU_Hr.presentValue = app.clgload_model.btuhr_4PM
    Five_PM_BTU_Hr.presentValue = app.clgload_model.btuhr_5PM
    Six_PM_BTU_Hr.presentValue = app.clgload_model.btuhr_6PM
    Seven_PM_BTU_Hr.presentValue = app.clgload_model.btuhr_7PM
    Eight_PM_BTU_Hr.presentValue = app.clgload_model.btuhr_8PM
    clg_modelpval.presentValue = app.clgload_model.dickfulr_pval
    clgtrainmins.presentValue = app.clgload_model.train_minutes

def cost_updates():

    app.costs_calculations.update()
    Five_AM_costs= app.dev.this_application.get_object_id(("analogValue", 37))
    Six_AM_costs= app.dev.this_application.get_object_id(("analogValue", 38))
    Seven_AM_costs= app.dev.this_application.get_object_id(("analogValue", 39))
    Eight_AM_costs= app.dev.this_application.get_object_id(("analogValue", 40))
    Nine_AM_costs= app.dev.this_application.get_object_id(("analogValue", 41))
    Ten_AM_costs= app.dev.this_application.get_object_id(("analogValue", 42))
    Eleven_AM_costs= app.dev.this_application.get_object_id(("analogValue", 43))
    Twelve_PM_costs= app.dev.this_application.get_object_id(("analogValue", 44))
    One_PM_costs= app.dev.this_application.get_object_id(("analogValue", 45))
    Two_PM_costs= app.dev.this_application.get_object_id(("analogValue", 46))
    Three_PM_costs= app.dev.this_application.get_object_id(("analogValue", 47))
    Four_PM_costs= app.dev.this_application.get_object_id(("analogValue", 48))
    Five_PM_costs= app.dev.this_application.get_object_id(("analogValue", 49))
    Six_PM_costs= app.dev.this_application.get_object_id(("analogValue", 50))
    Seven_PM_costs= app.dev.this_application.get_object_id(("analogValue", 51))
    Eight_PM_costs= app.dev.this_application.get_object_id(("analogValue", 52))

    Five_AM_costs.presentValue = app.costs_calculations.costs_5AM
    Six_AM_costs.presentValue = app.costs_calculations.costs_6AM
    Seven_AM_costs.presentValue = app.costs_calculations.costs_7AM
    Seven_AM_costs.presentValue = app.costs_calculations.costs_8AM
    Nine_AM_costs.presentValue = app.costs_calculations.costs_9AM
    Ten_AM_costs.presentValue = app.costs_calculations.costs_10AM
    Eleven_AM_costs.presentValue = app.costs_calculations.costs_11AM
    Twelve_PM_costs.presentValue = app.costs_calculations.costs_12PM
    One_PM_costs.presentValue = app.costs_calculations.costs_1PM
    Two_PM_costs.presentValue = app.costs_calculations.costs_2PM
    Three_PM_costs.presentValue = app.costs_calculations.costs_3PM
    Four_PM_costs.presentValue = app.costs_calculations.costs_4PM
    Five_PM_costs.presentValue = app.costs_calculations.costs_5PM
    Six_PM_costs.presentValue = app.costs_calculations.costs_6PM
    Seven_PM_costs.presentValue = app.costs_calculations.costs_7PM
    Eight_PM_costs.presentValue = app.costs_calculations.costs_8PM

    #app.dev._log.info("Setting {}, type {}, to {}".format(Five_AM_kW, type(Five_AM_kW), new_Five_AM_kW))



def get_elecmeter_data():
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
        sqlite_table = "elec_data"
        master_data.to_sql(sqlite_table, sqlite_connection, if_exists='append')
        sqlite_connection.close()
        app.dev._log.info("Data saved to Sqlite")


    except:
        app.dev._log.warning("No data being saved to db!")


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
        GPM = 100
        load = 500 * delta * GPM

        allStuff['load'] = load


    except:
        app.dev._log.error("Error performing BACnet Read Request! {}".format(error))

        allStuff['Date'] = numpy.nan
        allStuff['load'] = numpy.nan



    try:

        '''
        attempt to save data to Sqlite
        '''

        allStuff['Date'] = datetime.fromtimestamp(allStuff['Date'])
        master_data = pd.DataFrame(allStuff,index=[0])
        master_data = master_data.set_index('Date')


        engine = create_engine('sqlite:///save_data.db')
        sqlite_connection = engine.connect()
        sqlite_table = "clg_data"
        master_data.to_sql(sqlite_table, sqlite_connection, if_exists='append')
        sqlite_connection.close()
        app.dev._log.info("Data saved to Sqlite")


    except:
        app.dev._log.warning("No data being saved to db!")



'''
#this main function is just for testing purposes
def main():
    task_device_one = RecurringTask(get_elecmeter_data, delay=60)
    task_device_one.start()
    task_device_two = RecurringTask(get_clg_data, delay=60)
    task_device_two.start()
    task_device_three = RecurringTask(electric_update_model, delay=120)
    task_device_three.start()


    while True:
        pass

'''

#This main function is for deployment
#Also to note get_elecmeter_data function also calls other functions
def main():
    task_device_one = RecurringTask(get_elecmeter_data, delay=60)
    task_device_one.start()
    task_device_two = RecurringTask(get_clg_data, delay=60)
    task_device_two.start()

    x=datetime.today()
    y = x.replace(day=x.day, hour=0, minute=0, second=0, microsecond=0) + timedelta(days=1)
    delta_t=y-x
    secs=delta_t.total_seconds()
    t = Timer(secs, electric_update_model)
    t.start()
    while True:
        pass


if __name__ == "__main__":
    main()
