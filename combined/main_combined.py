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
from meteo_parser import OpenWeatherOne



def start_device():
    print("Starting BACnet device")
    new_device = BAC0.lite()
    new_device._log.info('Device ID : {}'.format(new_device.Boid))
    time.sleep(10)

    default_pv = CharacterString("empty")

    ####humidity#######
    Five_AM_humidity = create_AV(
        oid=0, name="5:00AM_Humidity", pv=0, pv_writable=False
    )
    Five_AM_humidity.units = EngineeringUnits("percent")
    Five_AM_humidity.description = CharacterString(
        "5AM Humidity in Percent Relative Humidity"
    )

    ####temp#######
    Five_AM_temp = create_AV(oid=1, name="5:00AM_Temp", pv=0, pv_writable=False)
    Five_AM_temp.units = EngineeringUnits("degreesFahrenheit")
    Five_AM_temp.description = CharacterString("5AM Temperature in degF")

    ####dewpoint#######
    Five_AM_dewpoint = create_AV(
        oid=2, name="5:00AM_Dewpoint", pv=0, pv_writable=False
    )
    Five_AM_dewpoint.units = EngineeringUnits("degreesFahrenheit")
    Five_AM_dewpoint.description = CharacterString(
        "5AM Outdoor Dewpoint"
    )

    ####clouds#######
    Five_AM_clouds = create_AV(
        oid=3, name="5:00AM_Cloud_Cover", pv=0, pv_writable=False
    )
    Five_AM_clouds.units = EngineeringUnits("percent")
    Five_AM_clouds.description = CharacterString(
        "5AM Cloud Cover In Percent"
    )

    ####description#######
    Five_AM_description = create_CharStrValue(
        oid=4, name="5:00AM_Weather_Description", pv=default_pv
    )
    Five_AM_description.description = CharacterString(
        "5AM Weather Description 5AM"
    )

    ####humidity#######3HR
    Eight_AM_humidity = create_AV(
        oid=5, name="8:00AM_Humidity", pv=0, pv_writable=False
    )
    Eight_AM_humidity.units = EngineeringUnits("percent")
    Eight_AM_humidity.description = CharacterString(
        "8:00AM Humidity in Percent Relative Humidity"
    )

    ####temp#######3HR
    Eight_AM_temp = create_AV(oid=6, name="8:00AM_Temp", pv=0, pv_writable=False)
    Eight_AM_temp.units = EngineeringUnits("degreesFahrenheit")
    Eight_AM_temp.description = CharacterString("8:00AM Temp in degF")

    ####dewpoint#######3HR
    Eight_AM_dewpoint = create_AV(
        oid=7, name="8:00AM_Dewpoint", pv=0, pv_writable=False
    )
    Eight_AM_dewpoint.units = EngineeringUnits("degreesFahrenheit")
    Eight_AM_dewpoint.description = CharacterString(
        "8:00AM Outdoor Dewpoint"
    )

    ####clouds#######3HR
    Eight_AM_clouds = create_AV(
        oid=8, name="8:00AM_Cloud_Cover", pv=0, pv_writable=False
    )
    Eight_AM_clouds.units = EngineeringUnits("percent")
    Eight_AM_clouds.description = CharacterString(
        "8:00AM Cloud Cover In Percent"
    )

    ####description#######3HR
    Eight_AM_description = create_CharStrValue(
        oid=9, name="8:00AM_Weather_Description", pv=default_pv
    )
    Eight_AM_description.description = CharacterString(
        "8:00AM Weather Description"
    )

    ####humidity#######6HR
    Eleven_AM_humidity = create_AV(
        oid=10, name="11:00AM_Humidity", pv=0, pv_writable=False
    )
    Eleven_AM_humidity.units = EngineeringUnits("percent")
    Eleven_AM_humidity.description = CharacterString(
        "11:00AM Humidity in Percent Relative Humidity"
    )

    ####temp#######6HR
    Eleven_AM_temp = create_AV(oid=11, name="11:00AM_Temp", pv=0, pv_writable=False)
    Eleven_AM_temp.units = EngineeringUnits("degreesFahrenheit")
    Eleven_AM_temp.description = CharacterString("11:00AM Temp in degF")

    ####dewpoint#######6HR
    Eleven_AM_dewpoint = create_AV(
        oid=12, name="11:00AM_Dewpoint", pv=0, pv_writable=False
    )
    Eleven_AM_dewpoint.units = EngineeringUnits("degreesFahrenheit")
    Eleven_AM_dewpoint.description = CharacterString(
        "11:00AM Outdoor Dewpoint"
    )

    ####clouds#######6HR
    Eleven_AM_clouds = create_AV(
        oid=13, name="11:00AM_Cloud_Cover", pv=0, pv_writable=False
    )
    Eleven_AM_clouds.units = EngineeringUnits("percent")
    Eleven_AM_clouds.description = CharacterString(
        "11:00AM Cloud Cover In Percent"
    )

    ####description#######6HR
    Eleven_AM_description = create_CharStrValue(
        oid=14, name="11:00AM_Weather_Description", pv=default_pv
    )
    Eleven_AM_description.description = CharacterString(
        "11:00AM Weather Description"
    )

    ####humidity#######9HR
    Two_PM_humidity = create_AV(
        oid=15, name="2:00PM_Humidity", pv=0, pv_writable=False
    )
    Two_PM_humidity.units = EngineeringUnits("percent")
    Two_PM_humidity.description = CharacterString(
        "2:00PM Humidity in Percent Relative Humidity"
    )

    ####temp#######9HR
    Two_PM_temp = create_AV(oid=16, name="2:00PM_Temp", pv=0, pv_writable=False)
    Two_PM_temp.units = EngineeringUnits("degreesFahrenheit")
    Two_PM_temp.description = CharacterString("2:00PM Temp in degF")

    ####dewpoint#######9HR
    Two_PM_dewpoint = create_AV(
        oid=17, name="2:00PM_Dewpoint", pv=0, pv_writable=False
    )
    Two_PM_dewpoint.units = EngineeringUnits("degreesFahrenheit")
    Two_PM_dewpoint.description = CharacterString(
        "2:00PM Outdoor Dewpoint"
    )

    ####clouds#######9HR
    Two_PM_clouds = create_AV(
        oid=18, name="2:00PM_Cloud_Cover", pv=0, pv_writable=False
    )
    Two_PM_clouds.units = EngineeringUnits("percent")
    Two_PM_clouds.description = CharacterString(
        "2:00PM Cloud Cover In Percent"
    )

    ####description#######9HR
    Two_PM_description = create_CharStrValue(
        oid=19, name="2:00PM_Weather_Description", pv=default_pv
    )
    Two_PM_description.description = CharacterString(
        "2:00PM Weather Description"
    )

    ####humidity#######12HR
    Five_PM_humidity = create_AV(
        oid=20, name="5:00PM_Humidity", pv=0, pv_writable=False
    )
    Five_PM_humidity.units = EngineeringUnits("percent")
    Five_PM_humidity.description = CharacterString(
        "5:00PM Humidity in Percent Relative Humidity"
    )

    ####temp#######12HR
    Five_PM_temp = create_AV(oid=21, name="5:00PM_Temp", pv=0, pv_writable=False)
    Five_PM_temp.units = EngineeringUnits("degreesFahrenheit")
    Five_PM_temp.description = CharacterString("5:00PM Temp in degF")

    ####dewpoint#######12HR
    Five_PM_dewpoint = create_AV(
        oid=22, name="5:00PM_Dewpoint", pv=0, pv_writable=False
    )
    Five_PM_dewpoint.units = EngineeringUnits("degreesFahrenheit")
    Five_PM_dewpoint.description = CharacterString(
        "5:00PM Outdoor Dewpoint"
    )

    ####clouds#######12HR
    Five_PM_clouds = create_AV(
        oid=23, name="5:00PM_Cloud_Cover", pv=0, pv_writable=False
    )
    Five_PM_clouds.units = EngineeringUnits("percent")
    Five_PM_clouds.description = CharacterString(
        "5:00PM Cloud Cover In Percent"
    )

    ####description#######12HR
    Five_PM_description = create_CharStrValue(
        oid=24, name="5:00PM_Weather_Description", pv=default_pv
    )
    Five_PM_description.description = CharacterString(
        "5:00PM Weather Description"
    )

    ####humidity#######15HR
    Eight_PM_humidity = create_AV(
        oid=25, name="8:00PM_Humidity", pv=0, pv_writable=False
    )
    Eight_PM_humidity.units = EngineeringUnits("percent")
    Eight_PM_humidity.description = CharacterString(
        "8:00PM Humidity in Percent Relative Humidity"
    )

    ####temp#######15HR
    Eight_PM_temp = create_AV(oid=26, name="8:00PM_Temp", pv=0, pv_writable=False)
    Eight_PM_temp.units = EngineeringUnits("degreesFahrenheit")
    Eight_PM_temp.description = CharacterString("8:00PM Temp in degF")

    ####dewpoint#######15HR
    Eight_PM_dewpoint = create_AV(
        oid=27, name="8:00PM_Dewpoint", pv=0, pv_writable=False
    )
    Eight_PM_dewpoint.units = EngineeringUnits("degreesFahrenheit")
    Eight_PM_dewpoint.description = CharacterString(
        "8:00PM Outdoor Dewpoint"
    )

    ####clouds#######15HR
    Eight_PM_clouds = create_AV(
        oid=28, name="8:00PM_Cloud_Cover", pv=0, pv_writable=False
    )
    Eight_PM_clouds.units = EngineeringUnits("percent")
    Eight_PM_clouds.description = CharacterString(
        "8:00PM Cloud Cover In Percent"
    )

    ####description#######15HR
    Eight_PM_description = create_CharStrValue(
        oid=29, name="8:00PM_Weather_Description", pv=default_pv
    )
    Eight_PM_description.description = CharacterString(
        "8:00PM Weather Description"
    )

    ####GPS#######
    latitude = create_AV(oid=30, name="Latitude_GPS_Setting", pv=0, pv_writable=False)
    latitude.description = CharacterString("GPS Latitude for Weather Data Request")

    ####GPS#######
    longitude = create_AV(oid=31, name="Longitude_GPS_Setting", pv=0, pv_writable=False)
    longitude.description = CharacterString("GPS Longitude for Weather Data Request")

    ####kW#######
    Five_AM_kW = create_AV(
        oid=32, name="5:00AM_Forecasted_kW", pv=0, pv_writable=False
    )
    Five_AM_kW.units = EngineeringUnits("kilowatts")
    Five_AM_kW.description = CharacterString(
        "5AM Electrical Demand"
    )


    ####kW#######3HR
    Eight_AM_kW = create_AV(
        oid=33, name="8:00AM_Forecasted_kW", pv=0, pv_writable=False
    )
    Eight_AM_kW.units = EngineeringUnits("kilowatts")
    Eight_AM_kW.description = CharacterString(
        "8AM Electrical Demand"
    )


    ####kW#######6HR
    Eleven_AM_kW = create_AV(
        oid=34, name="11:00AM_Forecasted_kW", pv=0, pv_writable=False
    )
    Eleven_AM_kW.units = EngineeringUnits("kilowatts")
    Eleven_AM_kW.description = CharacterString(
        "11AM Electrical Demand"
    )


    ####kW#######9HR
    Two_PM_kW = create_AV(
        oid=35, name="2:00PM_Forecasted_kW", pv=0, pv_writable=False
    )
    Two_PM_kW.units = EngineeringUnits("kilowatts")
    Two_PM_kW.description = CharacterString(
        "2PM Electrical Demand"
    )


    ####kW#######12HR
    Five_PM_kW = create_AV(
        oid=36, name="5:00PM_Forecasted_kW", pv=0, pv_writable=False
    )
    Five_PM_kW.units = EngineeringUnits("kilowatts")
    Five_PM_kW.description = CharacterString(
        "5PM Electrical Demand"
    )


    ####kW#######15HR
    Eight_PM_kW = create_AV(
        oid=37, name="8:00PM_Forecasted_kW", pv=0, pv_writable=False
    )
    Eight_PM_kW.units = EngineeringUnits("kilowatts")
    Eight_PM_kW.description = CharacterString(
        "8PM Electrical Demand"
    )


    new_device.this_application.add_object(Five_AM_kW)
    new_device.this_application.add_object(Eight_AM_kW)
    new_device.this_application.add_object(Eleven_AM_kW)
    new_device.this_application.add_object(Two_PM_kW)
    new_device.this_application.add_object(Five_PM_kW)
    new_device.this_application.add_object(Eight_PM_kW)

    new_device.this_application.add_object(Five_AM_humidity)
    new_device.this_application.add_object(Five_AM_temp)
    new_device.this_application.add_object(Five_AM_dewpoint)
    new_device.this_application.add_object(Five_AM_clouds)
    new_device.this_application.add_object(Five_AM_description)

    new_device.this_application.add_object(Eight_AM_humidity)
    new_device.this_application.add_object(Eight_AM_temp)
    new_device.this_application.add_object(Eight_AM_dewpoint)
    new_device.this_application.add_object(Eight_AM_clouds)
    new_device.this_application.add_object(Eight_AM_description)

    new_device.this_application.add_object(Eleven_AM_humidity)
    new_device.this_application.add_object(Eleven_AM_temp)
    new_device.this_application.add_object(Eleven_AM_dewpoint)
    new_device.this_application.add_object(Eleven_AM_clouds)
    new_device.this_application.add_object(Eleven_AM_description)

    new_device.this_application.add_object(Two_PM_humidity)
    new_device.this_application.add_object(Two_PM_temp)
    new_device.this_application.add_object(Two_PM_dewpoint)
    new_device.this_application.add_object(Two_PM_clouds)
    new_device.this_application.add_object(Two_PM_description)

    new_device.this_application.add_object(Five_PM_humidity)
    new_device.this_application.add_object(Five_PM_temp)
    new_device.this_application.add_object(Five_PM_dewpoint)
    new_device.this_application.add_object(Five_PM_clouds)
    new_device.this_application.add_object(Five_PM_description)

    new_device.this_application.add_object(Eight_PM_humidity)
    new_device.this_application.add_object(Eight_PM_temp)
    new_device.this_application.add_object(Eight_PM_dewpoint)
    new_device.this_application.add_object(Eight_PM_clouds)
    new_device.this_application.add_object(Eight_PM_description)

    new_device.this_application.add_object(latitude)
    new_device.this_application.add_object(longitude)


    return new_device



class App:
    dev = start_device()
    model = Model()
    weather = OpenWeatherOne(units="imperial")


app = App()


def update_model():

    app.model.update()
    Five_AM_kW= app.dev.this_application.get_object_id(("analogValue", 32))
    Eight_AM_kW= app.dev.this_application.get_object_id(("analogValue", 33))
    Eleven_AM_kW= app.dev.this_application.get_object_id(("analogValue", 34))
    Two_PM_kW= app.dev.this_application.get_object_id(("analogValue", 35))
    Five_PM_kW= app.dev.this_application.get_object_id(("analogValue", 36))
    Eight_PM_kW= app.dev.this_application.get_object_id(("analogValue", 37))


    new_Five_AM_kW = app.model.kW_5AM
    new_Eight_AM_kW = app.model.kW_8AM
    new_Eleven_AM_kW = app.model.kW_11AM
    new_Two_PM_kW = app.model.kW_2PM
    new_Five_PM_kW = app.model.kW_5PM
    new_Eight_PM_kW = app.model.kW_8PM


    app.dev._log.info("Setting {}, type {}, to {}".format(Five_AM_kW, type(Five_AM_kW), new_Five_AM_kW))
    Five_AM_kW.presentValue = new_Five_AM_kW

    app.dev._log.info("Setting {}, type {}, to {}".format(Eight_AM_kW, type(Eight_AM_kW), new_Eight_AM_kW))
    Eight_AM_kW.presentValue = new_Eight_AM_kW

    app.dev._log.info("Setting {}, type {}, to {}".format(Eleven_AM_kW, type(Eleven_AM_kW), new_Eleven_AM_kW))
    Eleven_AM_kW.presentValue = new_Eleven_AM_kW

    app.dev._log.info("Setting {}, type {}, to {}".format(Two_PM_kW, type(Two_PM_kW), new_Two_PM_kW))
    Two_PM_kW.presentValue = new_Two_PM_kW

    app.dev._log.info("Setting {}, type {}, to {}".format(Five_PM_kW, type(Five_PM_kW), new_Five_PM_kW))
    Five_PM_kW.presentValue = new_Five_PM_kW

    app.dev._log.info("Setting {}, type {}, to {}".format(Eight_PM_kW, type(Eight_PM_kW), new_Eight_PM_kW))
    Eight_PM_kW.presentValue = new_Eight_PM_kW



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




def update_weather():

    app.weather.update()

    Five_AM_humid = app.dev.this_application.get_object_name("5:00AM_Humidity")
    Five_AM_temp = app.dev.this_application.get_object_name("5:00AM_Temp")
    Five_AM_dewpoint = app.dev.this_application.get_object_name("5:00AM_Dewpoint")
    Five_AM_clouds = app.dev.this_application.get_object_name("5:00AM_Cloud_Cover")
    Five_AM_description = app.dev.this_application.get_object_name("5:00AM_Weather_Description")

    Eight_AM_humid = app.dev.this_application.get_object_name("8:00AM_Humidity")
    Eight_AM_temp = app.dev.this_application.get_object_name("8:00AM_Temp")
    Eight_AM_dewpoint = app.dev.this_application.get_object_name("8:00AM_Dewpoint")
    Eight_AM_clouds = app.dev.this_application.get_object_name("8:00AM_Cloud_Cover")
    Eight_AM_description = app.dev.this_application.get_object_name("8:00AM_Weather_Description")

    Eleven_AM_humid = app.dev.this_application.get_object_name("11:00AM_Humidity")
    Eleven_AM_temp = app.dev.this_application.get_object_name("11:00AM_Temp")
    Eleven_AM_dewpoint = app.dev.this_application.get_object_name("11:00AM_Dewpoint")
    Eleven_AM_clouds = app.dev.this_application.get_object_name("11:00AM_Cloud_Cover")
    Eleven_AM_description = app.dev.this_application.get_object_name("11:00AM_Weather_Description")

    Two_PM_humid = app.dev.this_application.get_object_name("2:00PM_Humidity")
    Two_PM_temp = app.dev.this_application.get_object_name("2:00PM_Temp")
    Two_PM_dewpoint = app.dev.this_application.get_object_name("2:00PM_Dewpoint")
    Two_PM_clouds = app.dev.this_application.get_object_name("2:00PM_Cloud_Cover")
    Two_PM_description = app.dev.this_application.get_object_name("2:00PM_Weather_Description")

    Five_PM_humid = app.dev.this_application.get_object_name("5:00PM_Humidity")
    Five_PM_temp = app.dev.this_application.get_object_name("5:00PM_Temp")
    Five_PM_dewpoint = app.dev.this_application.get_object_name("5:00PM_Dewpoint")
    Five_PM_clouds = app.dev.this_application.get_object_name("5:00PM_Cloud_Cover")
    Five_PM_description = app.dev.this_application.get_object_name("5:00PM_Weather_Description")

    Eight_PM_humid = app.dev.this_application.get_object_name("8:00PM_Humidity")
    Eight_PM_temp = app.dev.this_application.get_object_name("8:00PM_Temp")
    Eight_PM_dewpoint = app.dev.this_application.get_object_name("8:00PM_Dewpoint")
    Eight_PM_clouds = app.dev.this_application.get_object_name("8:00PM_Cloud_Cover")
    Eight_PM_description = app.dev.this_application.get_object_name("8:00PM_Weather_Description")

    latitude = app.dev.this_application.get_object_name("Latitude_GPS_Setting")
    longitude = app.dev.this_application.get_object_name("Longitude_GPS_Setting")

    new_temp = app.weather.temp
    new_hum = app.weather.hum
    new_dewpoint = app.weather.dewpoint
    new_clouds = app.weather.clouds
    new_desciption = app.weather.desciption

    new_Eight_AM_temp = app.weather.temp_8AM
    new_Eight_AM_hum = app.weather.hum_8AM
    new_Eight_AM_dewpoint = app.weather.dewpoint_8AM
    new_Eight_AM_clouds = app.weather.clouds_8AM
    new_Eight_AM_desciption = app.weather.desciption_8AM

    new_Eleven_AM_temp = app.weather.temp_11AM
    new_Eleven_AM_hum = app.weather.hum_11AM
    new_Eleven_AM_dewpoint = app.weather.dewpoint_11AM
    new_Eleven_AM_clouds = app.weather.clouds_11AM
    new_Eleven_AM_desciption = app.weather.desciption_11AM

    new_Two_PM_temp = app.weather.temp_2PM
    new_Two_PM_hum = app.weather.hum_2PM
    new_Two_PM_dewpoint = app.weather.dewpoint_2PM
    new_Two_PM_clouds = app.weather.clouds_2PM
    new_Two_PM_desciption = app.weather.desciption_2PM

    new_Five_PM_temp = app.weather.temp_5PM
    new_Five_PM_hum = app.weather.hum_5PM
    new_Five_PM_dewpoint = app.weather.dewpoint_5PM
    new_Five_PM_clouds = app.weather.clouds_5PM
    new_Five_PM_desciption = app.weather.desciption_5PM

    new_Eight_PM_temp = app.weather.temp_8PM
    new_Eight_PM_hum = app.weather.hum_8PM
    new_Eight_PM_dewpoint = app.weather.dewpoint_8PM
    new_Eight_PM_clouds = app.weather.clouds_8PM
    new_Eight_PM_desciption = app.weather.desciption_8PM

    new_latitude = app.weather.lati
    new_longitude = app.weather.long


    app.dev._log.info("Setting 5AM Temp to {}".format(new_temp))
    Five_AM_temp.presentValue = new_temp

    app.dev._log.info("Setting 5AM Humidity to {}".format(new_hum))
    Five_AM_humid.presentValue = new_hum

    app.dev._log.info("Setting 5AM Dewpoint to {}".format(new_dewpoint))
    Five_AM_dewpoint.presentValue = new_dewpoint

    app.dev._log.info("Setting 5AM Clouds to {}".format(new_clouds))
    Five_AM_clouds.presentValue = new_clouds

    app.dev._log.info("Setting 5AM Description to {}".format(new_desciption))
    Five_AM_description.presentValue = new_desciption

    app.dev._log.info("Setting 8AM Temp to {}".format(new_Eight_AM_temp))
    Eight_AM_temp.presentValue = new_Eight_AM_temp

    app.dev._log.info("Setting 8AM Humidity to {}".format(new_Eight_AM_hum))
    Eight_AM_humid.presentValue = new_Eight_AM_hum

    app.dev._log.info("Setting 8AM Dewpoint to {}".format(new_Eight_AM_dewpoint))
    Eight_AM_dewpoint.presentValue = new_Eight_AM_dewpoint

    app.dev._log.info("Setting 8AM Clouds to {}".format(new_Eight_AM_clouds))
    Eight_AM_clouds.presentValue = new_Eight_AM_clouds

    app.dev._log.info("Setting 8AM Description to {}".format(new_Eight_AM_desciption))
    Eight_AM_description.presentValue = new_Eight_AM_desciption

    app.dev._log.info("Setting 11AM Temp to {}".format(new_Eleven_AM_temp))
    Eleven_AM_temp.presentValue = new_Eleven_AM_temp

    app.dev._log.info("Setting 11AM Humidity to {}".format(new_Eleven_AM_hum))
    Eleven_AM_humid.presentValue = new_Eleven_AM_hum

    app.dev._log.info("Setting 11AM Dewpoint to {}".format(new_Eleven_AM_dewpoint))
    Eleven_AM_dewpoint.presentValue = new_Eleven_AM_dewpoint

    app.dev._log.info("Setting 11AM Clouds to {}".format(new_Eleven_AM_clouds))
    Eleven_AM_clouds.presentValue = new_Eleven_AM_clouds

    app.dev._log.info("Setting 11AM Description to {}".format(new_Eleven_AM_desciption))
    Eleven_AM_description.presentValue = new_Eleven_AM_desciption

    app.dev._log.info("Setting 2PM Temp to {}".format(new_Two_PM_temp))
    Two_PM_temp.presentValue = new_Two_PM_temp

    app.dev._log.info("Setting 2PM Humidity to {}".format(new_Two_PM_hum))
    Two_PM_humid.presentValue = new_Two_PM_hum

    app.dev._log.info("Setting 2PM Dewpoint to {}".format(new_Two_PM_dewpoint))
    Two_PM_dewpoint.presentValue = new_Two_PM_dewpoint

    app.dev._log.info("Setting 2PM Clouds to {}".format(new_Two_PM_clouds))
    Two_PM_clouds.presentValue = new_Two_PM_clouds

    app.dev._log.info("Setting 2PM Description to {}".format(new_Two_PM_desciption))
    Two_PM_description.presentValue = new_Two_PM_desciption

    app.dev._log.info("Setting 5PM Temp to {}".format(new_Five_PM_temp))
    Five_PM_temp.presentValue = new_Five_PM_temp

    app.dev._log.info("Setting 5PM Humidity to {}".format(new_Five_PM_hum))
    Five_PM_humid.presentValue = new_Five_PM_hum

    app.dev._log.info("Setting 5PM Dewpoint to {}".format(new_Five_PM_dewpoint))
    Five_PM_dewpoint.presentValue = new_Five_PM_dewpoint

    app.dev._log.info("Setting 5PM Clouds to {}".format(new_Five_PM_clouds))
    Five_PM_clouds.presentValue = new_Five_PM_clouds

    app.dev._log.info("Setting 5PM Description to {}".format(new_Five_PM_desciption))
    Five_PM_description.presentValue = new_Five_PM_desciption

    app.dev._log.info("Setting 8PM Temp to {}".format(new_Eight_PM_temp))
    Eight_PM_temp.presentValue = new_Eight_PM_temp

    app.dev._log.info("Setting 8PM Humidity to {}".format(new_Eight_PM_hum))
    Eight_PM_humid.presentValue = new_Eight_PM_hum

    app.dev._log.info("Setting 8PM Dewpoint to {}".format(new_Eight_PM_dewpoint))
    Eight_PM_dewpoint.presentValue = new_Eight_PM_dewpoint

    app.dev._log.info("Setting 8PM Clouds to {}".format(new_Eight_PM_clouds))
    Eight_PM_clouds.presentValue = new_Eight_PM_clouds

    app.dev._log.info("Setting 8PM Description to {}".format(new_Eight_PM_desciption))
    Eight_PM_description.presentValue = new_Eight_PM_desciption

    app.dev._log.info("GPS longitude is set @ {}".format(new_longitude))
    longitude.presentValue = new_longitude

    app.dev._log.info("GPS latitude is set @ {}".format(new_latitude))
    latitude.presentValue = new_latitude



'''
def main():
    task_device_one = RecurringTask(get_meter_data, delay=30)
    task_device_one.start()
    task_device_two = RecurringTask(update_model, delay=1200)
    task_device_two.start()

    while True:
        pass

'''


def main():

    '''
    BACnet read requests
    '''
    task_device_one = RecurringTask(get_meter_data, delay=60)
    task_device_one.start()

    '''
    Next update electric load forcast
    '''

    x_1 = datetime.today()
    y_1 = x.replace(day=x_1.day, hour=4, minute=45, second=0, microsecond=0) + timedelta(days=1)
    delta_t_1 = y_1 - x_1
    secs_1 = delta_t_1.total_seconds()
    t_1 = Timer(secs_1, update_model)
    t_1.start()

    '''
    Next update weather data forecast
    '''

    x_2 = datetime.today()
    y_2 = x.replace(day=x_2.day, hour=5, minute=15, second=0, microsecond=0) + timedelta(days=1)
    delta_t_2 = y_2 - x_2
    secs_2 = delta_t_2.total_seconds()
    t_2 = Timer(secs_2, update_weather)
    t_2.start()


    while True:
        pass


if __name__ == "__main__":
    main()
