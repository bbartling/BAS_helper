#!/usr/bin/env python

import BAC0, time, requests
from datetime import datetime, timedelta
from threading import Timer
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

from meteo_parser import OpenWeatherOne



def start_device():
    print("Starting BACnet device")
    new_device = BAC0.lite()
    new_device._log.info('Device ID : {}'.format(new_device.Boid))
    time.sleep(10)

    default_pv = CharacterString("empty")

    ####humidity#######
    Current_humidity = create_AV(
        oid=0, name="Midnight_Humidity", pv=0, pv_writable=False
    )
    Current_humidity.units = EngineeringUnits("percent")
    Current_humidity.description = CharacterString(
        "Midnight Humidity in Percent Relative Humidity"
    )

    ####temp#######
    Current_temp = create_AV(oid=1, name="Midnight_Temp", pv=0, pv_writable=False)
    Current_tempunits = EngineeringUnits("degreesFahrenheit")
    Current_description = CharacterString("5AM Temperature in degF")

    ####dewpoint#######
    Current_dewpoint = create_AV(
        oid=2, name="Midnight_Dewpoint", pv=0, pv_writable=False
    )
    Current_dewpoint.units = EngineeringUnits("degreesFahrenheit")
    Current_dewpoint.description = CharacterString(
        "Midnight Outdoor Dewpoint"
    )

    ####clouds#######
    Current_clouds = create_AV(
        oid=3, name="Midnight_Cloud_Cover", pv=0, pv_writable=False
    )
    Current_clouds.units = EngineeringUnits("percent")
    Current_clouds.description = CharacterString(
        "Midnight Cloud Cover In Percent"
    )

    ####description#######
    Current_description = create_CharStrValue(
        oid=4, name="Midnight_Weather_Description", pv=default_pv
    )
    Current_description.description = CharacterString(
        "Midnight Weather Description"
    )

    ####humidity#######
    Five_AM_humidity = create_AV(
        oid=5, name="5:00AM_Humidity", pv=0, pv_writable=False
    )
    Five_AM_humidity.units = EngineeringUnits("percent")
    Five_AM_humidity.description = CharacterString(
        "5AM Humidity in Percent Relative Humidity"
    )

    ####temp#######
    Five_AM_temp = create_AV(oid=6, name="5:00AM_Temp", pv=0, pv_writable=False)
    Five_AM_temp.units = EngineeringUnits("degreesFahrenheit")
    Five_AM_temp.description = CharacterString("5AM Temperature in degF")

    ####dewpoint#######
    Five_AM_dewpoint = create_AV(
        oid=7, name="5:00AM_Dewpoint", pv=0, pv_writable=False
    )
    Five_AM_dewpoint.units = EngineeringUnits("degreesFahrenheit")
    Five_AM_dewpoint.description = CharacterString(
        "5AM Outdoor Dewpoint"
    )

    ####clouds#######
    Five_AM_clouds = create_AV(
        oid=8, name="5:00AM_Cloud_Cover", pv=0, pv_writable=False
    )
    Five_AM_clouds.units = EngineeringUnits("percent")
    Five_AM_clouds.description = CharacterString(
        "5AM Cloud Cover In Percent"
    )

    ####description#######
    Five_AM_description = create_CharStrValue(
        oid=9, name="5:00AM_Weather_Description", pv=default_pv
    )
    Five_AM_description.description = CharacterString(
        "5AM Weather Description 5AM"
    )

    ####humidity#######3HR
    Eight_AM_humidity = create_AV(
        oid=10, name="8:00AM_Humidity", pv=0, pv_writable=False
    )
    Eight_AM_humidity.units = EngineeringUnits("percent")
    Eight_AM_humidity.description = CharacterString(
        "8:00AM Humidity in Percent Relative Humidity"
    )

    ####temp#######3HR
    Eight_AM_temp = create_AV(oid=11, name="8:00AM_Temp", pv=0, pv_writable=False)
    Eight_AM_temp.units = EngineeringUnits("degreesFahrenheit")
    Eight_AM_temp.description = CharacterString("8:00AM Temp in degF")

    ####dewpoint#######3HR
    Eight_AM_dewpoint = create_AV(
        oid=12, name="8:00AM_Dewpoint", pv=0, pv_writable=False
    )
    Eight_AM_dewpoint.units = EngineeringUnits("degreesFahrenheit")
    Eight_AM_dewpoint.description = CharacterString(
        "8:00AM Outdoor Dewpoint"
    )

    ####clouds#######3HR
    Eight_AM_clouds = create_AV(
        oid=13, name="8:00AM_Cloud_Cover", pv=0, pv_writable=False
    )
    Eight_AM_clouds.units = EngineeringUnits("percent")
    Eight_AM_clouds.description = CharacterString(
        "8:00AM Cloud Cover In Percent"
    )

    ####description#######3HR
    Eight_AM_description = create_CharStrValue(
        oid=14, name="8:00AM_Weather_Description", pv=default_pv
    )
    Eight_AM_description.description = CharacterString(
        "8:00AM Weather Description"
    )

    ####humidity#######6HR
    Eleven_AM_humidity = create_AV(
        oid=15, name="11:00AM_Humidity", pv=0, pv_writable=False
    )
    Eleven_AM_humidity.units = EngineeringUnits("percent")
    Eleven_AM_humidity.description = CharacterString(
        "11:00AM Humidity in Percent Relative Humidity"
    )

    ####temp#######6HR
    Eleven_AM_temp = create_AV(oid=16, name="11:00AM_Temp", pv=0, pv_writable=False)
    Eleven_AM_temp.units = EngineeringUnits("degreesFahrenheit")
    Eleven_AM_temp.description = CharacterString("11:00AM Temp in degF")

    ####dewpoint#######6HR
    Eleven_AM_dewpoint = create_AV(
        oid=17, name="11:00AM_Dewpoint", pv=0, pv_writable=False
    )
    Eleven_AM_dewpoint.units = EngineeringUnits("degreesFahrenheit")
    Eleven_AM_dewpoint.description = CharacterString(
        "11:00AM Outdoor Dewpoint"
    )

    ####clouds#######6HR
    Eleven_AM_clouds = create_AV(
        oid=18, name="11:00AM_Cloud_Cover", pv=0, pv_writable=False
    )
    Eleven_AM_clouds.units = EngineeringUnits("percent")
    Eleven_AM_clouds.description = CharacterString(
        "11:00AM Cloud Cover In Percent"
    )

    ####description#######6HR
    Eleven_AM_description = create_CharStrValue(
        oid=19, name="11:00AM_Weather_Description", pv=default_pv
    )
    Eleven_AM_description.description = CharacterString(
        "11:00AM Weather Description"
    )

    ####humidity#######9HR
    Two_PM_humidity = create_AV(
        oid=20, name="2:00PM_Humidity", pv=0, pv_writable=False
    )
    Two_PM_humidity.units = EngineeringUnits("percent")
    Two_PM_humidity.description = CharacterString(
        "2:00PM Humidity in Percent Relative Humidity"
    )

    ####temp#######9HR
    Two_PM_temp = create_AV(oid=21, name="2:00PM_Temp", pv=0, pv_writable=False)
    Two_PM_temp.units = EngineeringUnits("degreesFahrenheit")
    Two_PM_temp.description = CharacterString("2:00PM Temp in degF")

    ####dewpoint#######9HR
    Two_PM_dewpoint = create_AV(
        oid=22, name="2:00PM_Dewpoint", pv=0, pv_writable=False
    )
    Two_PM_dewpoint.units = EngineeringUnits("degreesFahrenheit")
    Two_PM_dewpoint.description = CharacterString(
        "2:00PM Outdoor Dewpoint"
    )

    ####clouds#######9HR
    Two_PM_clouds = create_AV(
        oid=23, name="2:00PM_Cloud_Cover", pv=0, pv_writable=False
    )
    Two_PM_clouds.units = EngineeringUnits("percent")
    Two_PM_clouds.description = CharacterString(
        "2:00PM Cloud Cover In Percent"
    )

    ####description#######9HR
    Two_PM_description = create_CharStrValue(
        oid=24, name="2:00PM_Weather_Description", pv=default_pv
    )
    Two_PM_description.description = CharacterString(
        "2:00PM Weather Description"
    )

    ####humidity#######12HR
    Five_PM_humidity = create_AV(
        oid=25, name="5:00PM_Humidity", pv=0, pv_writable=False
    )
    Five_PM_humidity.units = EngineeringUnits("percent")
    Five_PM_humidity.description = CharacterString(
        "5:00PM Humidity in Percent Relative Humidity"
    )

    ####temp#######12HR
    Five_PM_temp = create_AV(oid=26, name="5:00PM_Temp", pv=0, pv_writable=False)
    Five_PM_temp.units = EngineeringUnits("degreesFahrenheit")
    Five_PM_temp.description = CharacterString("5:00PM Temp in degF")

    ####dewpoint#######12HR
    Five_PM_dewpoint = create_AV(
        oid=27, name="5:00PM_Dewpoint", pv=0, pv_writable=False
    )
    Five_PM_dewpoint.units = EngineeringUnits("degreesFahrenheit")
    Five_PM_dewpoint.description = CharacterString(
        "5:00PM Outdoor Dewpoint"
    )

    ####clouds#######12HR
    Five_PM_clouds = create_AV(
        oid=28, name="5:00PM_Cloud_Cover", pv=0, pv_writable=False
    )
    Five_PM_clouds.units = EngineeringUnits("percent")
    Five_PM_clouds.description = CharacterString(
        "5:00PM Cloud Cover In Percent"
    )

    ####description#######12HR
    Five_PM_description = create_CharStrValue(
        oid=29, name="5:00PM_Weather_Description", pv=default_pv
    )
    Five_PM_description.description = CharacterString(
        "5:00PM Weather Description"
    )

    ####humidity#######15HR
    Eight_PM_humidity = create_AV(
        oid=30, name="8:00PM_Humidity", pv=0, pv_writable=False
    )
    Eight_PM_humidity.units = EngineeringUnits("percent")
    Eight_PM_humidity.description = CharacterString(
        "8:00PM Humidity in Percent Relative Humidity"
    )

    ####temp#######15HR
    Eight_PM_temp = create_AV(oid=31, name="8:00PM_Temp", pv=0, pv_writable=False)
    Eight_PM_temp.units = EngineeringUnits("degreesFahrenheit")
    Eight_PM_temp.description = CharacterString("8:00PM Temp in degF")

    ####dewpoint#######15HR
    Eight_PM_dewpoint = create_AV(
        oid=32, name="8:00PM_Dewpoint", pv=0, pv_writable=False
    )
    Eight_PM_dewpoint.units = EngineeringUnits("degreesFahrenheit")
    Eight_PM_dewpoint.description = CharacterString(
        "8:00PM Outdoor Dewpoint"
    )

    ####clouds#######15HR
    Eight_PM_clouds = create_AV(
        oid=33, name="8:00PM_Cloud_Cover", pv=0, pv_writable=False
    )
    Eight_PM_clouds.units = EngineeringUnits("percent")
    Eight_PM_clouds.description = CharacterString(
        "8:00PM Cloud Cover In Percent"
    )

    ####description#######15HR
    Eight_PM_description = create_CharStrValue(
        oid=34, name="8:00PM_Weather_Description", pv=default_pv
    )
    Eight_PM_description.description = CharacterString(
        "8:00PM Weather Description"
    )

    ####GPS#######
    latitude = create_AV(oid=35, name="Latitude_GPS_Setting", pv=0, pv_writable=False)
    latitude.description = CharacterString("GPS Latitude for Weather Data Request")

    ####GPS#######
    longitude = create_AV(oid=36, name="Longitude_GPS_Setting", pv=0, pv_writable=False)
    longitude.description = CharacterString("GPS Longitude for Weather Data Request")

    new_device.this_application.add_object(Current_humidity)
    new_device.this_application.add_object(Current_temp)
    new_device.this_application.add_object(Current_dewpoint)
    new_device.this_application.add_object(Current_clouds)
    new_device.this_application.add_object(Current_description)

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
    weather = OpenWeatherOne(units="imperial")


app = App()


def update_weather():

    app.weather.update()

    Current_humidity = app.dev.this_application.get_object_id(("analogValue", 0))
    Current_temp = app.dev.this_application.get_object_id(("analogValue", 1))
    Current_dewpoint = app.dev.this_application.get_object_id(("analogValue", 2))
    Current_clouds = app.dev.this_application.get_object_id(("analogValue", 3))
    Current_description = app.dev.this_application.get_object_name("Midnight_Weather_Description")

    Five_AM_humid = app.dev.this_application.get_object_id(("analogValue", 5))
    Five_AM_temp = app.dev.this_application.get_object_id(("analogValue", 6))
    Five_AM_dewpoint = app.dev.this_application.get_object_id(("analogValue", 7))
    Five_AM_clouds = app.dev.this_application.get_object_id(("analogValue", 8))
    Five_AM_description = app.dev.this_application.get_object_name("5:00AM_Weather_Description")

    Eight_AM_humid = app.dev.this_application.get_object_id(("analogValue", 10))
    Eight_AM_temp = app.dev.this_application.get_object_id(("analogValue", 11))
    Eight_AM_dewpoint = app.dev.this_application.get_object_id(("analogValue", 12))
    Eight_AM_clouds = app.dev.this_application.get_object_id(("analogValue", 13))
    Eight_AM_description = app.dev.this_application.get_object_name("8:00AM_Weather_Description")

    Eleven_AM_humid = app.dev.this_application.get_object_id(("analogValue", 15))
    Eleven_AM_temp = app.dev.this_application.get_object_id(("analogValue", 16))
    Eleven_AM_dewpoint = app.dev.this_application.get_object_id(("analogValue", 17))
    Eleven_AM_clouds = app.dev.this_application.get_object_id(("analogValue", 18))
    Eleven_AM_description = app.dev.this_application.get_object_name("11:00AM_Weather_Description")

    Two_PM_humid = app.dev.this_application.get_object_id(("analogValue", 20))
    Two_PM_temp = app.dev.this_application.get_object_id(("analogValue", 21))
    Two_PM_dewpoint = app.dev.this_application.get_object_id(("analogValue", 22))
    Two_PM_clouds = app.dev.this_application.get_object_id(("analogValue", 23))
    Two_PM_description = app.dev.this_application.get_object_name("2:00PM_Weather_Description")

    Five_PM_humid = app.dev.this_application.get_object_id(("analogValue", 25))
    Five_PM_temp = app.dev.this_application.get_object_id(("analogValue", 26))
    Five_PM_dewpoint = app.dev.this_application.get_object_id(("analogValue", 27))
    Five_PM_clouds = app.dev.this_application.get_object_id(("analogValue", 28))
    Five_PM_description = app.dev.this_application.get_object_name("5:00PM_Weather_Description")

    Eight_PM_humid = app.dev.this_application.get_object_id(("analogValue", 30))
    Eight_PM_temp = app.dev.this_application.get_object_id(("analogValue", 31))
    Eight_PM_dewpoint = app.dev.this_application.get_object_id(("analogValue", 32))
    Eight_PM_clouds = app.dev.this_application.get_object_id(("analogValue", 33))
    Eight_PM_description = app.dev.this_application.get_object_name("8:00PM_Weather_Description")

    latitude = app.dev.this_application.get_object_id(("analogValue", 35))
    longitude = app.dev.this_application.get_object_id(("analogValue", 36))

    new_temp = app.weather.temp
    new_hum = app.weather.hum
    new_dewpoint = app.weather.dewpoint
    new_clouds = app.weather.clouds
    new_desciption = app.weather.desciption

    new_Five_AM_temp = app.weather.temp_5AM
    new_Five_AM_hum = app.weather.hum_5AM
    new_Five_AM_dewpoint = app.weather.dewpoint_5AM
    new_Five_AM_clouds = app.weather.clouds_5AM
    new_Five_AM_desciption = app.weather.desciption_5AM

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


    app.dev._log.info("Setting {}, type {}, to {}".format(Current_temp, type(Current_temp), new_temp))
    Current_temp.presentValue = new_temp

    app.dev._log.info("Setting {}, type {}, to {}".format(Current_humidity, type(Current_humidity), new_hum))
    Current_humidity.presentValue = new_hum

    app.dev._log.info("Setting {}, type {}, to {}".format(Current_dewpoint, type(Current_dewpoint), new_dewpoint))
    Current_dewpoint.presentValue = new_dewpoint

    app.dev._log.info("Setting {}, type {}, to {}".format(Current_clouds, type(Current_clouds), new_clouds))
    Current_clouds.presentValue = new_clouds

    app.dev._log.info("Setting {}, type {}, to {}".format(Current_description, type(Current_description), new_desciption))
    Current_description.presentValue = new_desciption

    app.dev._log.info("Setting {}, type {}, to {}".format(Five_AM_temp, type(Five_AM_temp), new_Five_AM_temp))
    Five_AM_temp.presentValue = new_Five_AM_temp

    app.dev._log.info("Setting {}, type {}, to {}".format(Five_AM_humid, type(Five_AM_humid), new_Five_AM_hum))
    Five_AM_humid.presentValue = new_Five_AM_hum

    app.dev._log.info("Setting {}, type {}, to {}".format(Five_AM_dewpoint, type(Five_AM_dewpoint), new_Five_AM_dewpoint))
    Five_AM_dewpoint.presentValue = new_Five_AM_dewpoint

    app.dev._log.info("Setting {}, type {}, to {}".format(Five_AM_clouds, type(Five_AM_clouds), new_Five_AM_clouds))
    Five_AM_clouds.presentValue = new_Five_AM_clouds

    app.dev._log.info("Setting {}, type {}, to {}".format(Five_AM_description, type(Five_AM_description), new_Five_AM_desciption))
    Five_AM_description.presentValue = new_Five_AM_desciption

    app.dev._log.info("Setting {}, type {}, to {}".format(Eight_AM_temp, type(Eight_AM_temp), new_Eight_AM_temp))
    Eight_AM_temp.presentValue = new_Eight_AM_temp

    app.dev._log.info("Setting {}, type {}, to {}".format(Eight_AM_humid, type(Eight_AM_humid), new_Eight_AM_hum))
    Eight_AM_humid.presentValue = new_Eight_AM_hum

    app.dev._log.info("Setting {}, type {}, to {}".format(Eight_AM_dewpoint, type(Eight_AM_dewpoint), new_Eight_AM_dewpoint))
    Eight_AM_dewpoint.presentValue = new_Eight_AM_dewpoint

    app.dev._log.info("Setting {}, type {}, to {}".format(Eight_AM_clouds, type(Eight_AM_clouds), new_Eight_AM_clouds))
    Eight_AM_clouds.presentValue = new_Eight_AM_clouds

    app.dev._log.info("Setting {}, type {}, to {}".format(Eight_AM_description, type(Eight_AM_description), new_Eight_AM_desciption))
    Eight_AM_description.presentValue = new_Eight_AM_desciption

    app.dev._log.info("Setting {}, type {}, to {}".format(Eleven_AM_temp, type(Eleven_AM_temp), new_Eleven_AM_temp))
    Eleven_AM_temp.presentValue = new_Eleven_AM_temp

    app.dev._log.info("Setting {}, type {}, to {}".format(Eleven_AM_humid, type(Eleven_AM_humid), new_Eleven_AM_hum))
    Eleven_AM_humid.presentValue = new_Eleven_AM_hum

    app.dev._log.info("Setting {}, type {}, to {}".format(Eleven_AM_dewpoint, type(Eleven_AM_dewpoint), new_Eleven_AM_dewpoint))
    Eleven_AM_dewpoint.presentValue = new_Eleven_AM_dewpoint

    app.dev._log.info("Setting {}, type {}, to {}".format(Eleven_AM_clouds, type(Eleven_AM_clouds), new_Eleven_AM_clouds))
    Eleven_AM_clouds.presentValue = new_Eleven_AM_clouds

    app.dev._log.info("Setting {}, type {}, to {}".format(Eleven_AM_description, type(Eleven_AM_description), new_Eleven_AM_desciption))
    Eleven_AM_description.presentValue = new_Eleven_AM_desciption

    app.dev._log.info("Setting {}, type {}, to {}".format(Two_PM_temp, type(Two_PM_temp), new_Two_PM_temp))
    Two_PM_temp.presentValue = new_Two_PM_temp

    app.dev._log.info("Setting {}, type {}, to {}".format(Two_PM_humid, type(Two_PM_humid), new_Two_PM_hum))
    Two_PM_humid.presentValue = new_Two_PM_hum

    app.dev._log.info("Setting {}, type {}, to {}".format(Two_PM_dewpoint, type(Two_PM_dewpoint), new_Two_PM_dewpoint))
    Two_PM_dewpoint.presentValue = new_Two_PM_dewpoint

    app.dev._log.info("Setting {}, type {}, to {}".format(Two_PM_clouds, type(Two_PM_clouds), new_Two_PM_clouds))
    Two_PM_clouds.presentValue = new_Two_PM_clouds

    app.dev._log.info("Setting {}, type {}, to {}".format(Two_PM_description, type(Two_PM_description), new_Two_PM_desciption))
    Two_PM_description.presentValue = new_Two_PM_desciption

    app.dev._log.info("Setting {}, type {}, to {}".format(Five_PM_temp, type(Five_PM_temp), new_Five_PM_temp))
    Five_PM_temp.presentValue = new_Five_PM_temp

    app.dev._log.info("Setting {}, type {}, to {}".format(Five_PM_humid, type(Five_PM_humid), new_Five_PM_hum))
    Five_PM_humid.presentValue = new_Five_PM_hum

    app.dev._log.info("Setting {}, type {}, to {}".format(Five_PM_dewpoint, type(Five_PM_dewpoint), new_Five_PM_dewpoint))
    Five_PM_dewpoint.presentValue = new_Five_PM_dewpoint

    app.dev._log.info("Setting {}, type {}, to {}".format(Five_PM_clouds, type(Five_PM_clouds), new_Five_PM_clouds))
    Five_PM_clouds.presentValue = new_Five_PM_clouds

    app.dev._log.info("Setting {}, type {}, to {}".format(Five_PM_description, type(Five_PM_description), new_Five_PM_desciption))
    Five_PM_description.presentValue = new_Five_PM_desciption

    app.dev._log.info("Setting {}, type {}, to {}".format(Eight_PM_temp, type(Eight_PM_temp), new_Eight_PM_temp))
    Eight_PM_temp.presentValue = new_Eight_PM_temp

    app.dev._log.info("Setting {}, type {}, to {}".format(Eight_PM_humid, type(Eight_PM_humid), new_Eight_PM_hum))
    Eight_PM_humid.presentValue = new_Eight_PM_hum

    app.dev._log.info("Setting {}, type {}, to {}".format(Eight_PM_dewpoint, type(Eight_PM_dewpoint), new_Eight_PM_dewpoint))
    Eight_PM_dewpoint.presentValue = new_Eight_PM_dewpoint

    app.dev._log.info("Setting {}, type {}, to {}".format(Eight_PM_clouds, type(Eight_PM_clouds), new_Eight_PM_clouds))
    Eight_PM_clouds.presentValue = new_Eight_PM_clouds

    app.dev._log.info("Setting {}, type {}, to {}".format(Eight_PM_description, type(Eight_PM_description), new_Eight_PM_desciption))
    Eight_PM_description.presentValue = new_Eight_PM_desciption

    app.dev._log.info("Setting {}, type {}, to {}".format(latitude, type(latitude), new_latitude))
    latitude.presentValue = new_latitude

    app.dev._log.info("Setting {}, type {}, to {}".format(longitude, type(longitude), new_longitude))
    longitude.presentValue = new_longitude


'''
def main():
    task_device = RecurringTask(update_weather, delay=300)
    task_device.start()
    while True:
        pass

'''

def main():
    x=datetime.today()
    y = x.replace(day=x.day, hour=0, minute=1, second=0, microsecond=0) + timedelta(days=1)
    delta_t=y-x

    secs=delta_t.total_seconds()
    t = Timer(secs, update_weather)
    t.start()
    while True:
        pass




if __name__ == "__main__":
    main()
