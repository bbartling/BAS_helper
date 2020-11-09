#!/usr/bin/env python

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

import time
from meteo_parser import OpenWeather


def start_device():
    print("Starting BACnet device")
    new_device = BAC0.lite()
    new_device._log.info('Device ID : {}'.format(new_device.Boid))
    time.sleep(10)

    default_pv = CharacterString("empty")

    current_humidity = create_AV(
        oid=0, name="Current_Humidity", pv=0, pv_writable=False
    )
    current_humidity.units = EngineeringUnits("percent")
    current_humidity.description = CharacterString(
        "Current Humidity in percent relative humidity"
    )

    current_temp = create_AV(oid=1, name="Current_Temp", pv=0, pv_writable=False)
    current_temp.units = EngineeringUnits("degreesFahrenheit")
    current_temp.description = CharacterString("Current Temperature in degF")

    current_windspd = create_AV(
        oid=2, name="Current_Wind_Speed", pv=0, pv_writable=False
    )
    current_windspd.units = EngineeringUnits("milesPerHour")
    current_windspd.description = CharacterString(
        "Current Wind Speed"
    )

    current_winddir = create_CharStrValue(
        oid=3, name="Current_Wind_Dir", pv=default_pv , pv_writable=False
    )
    current_winddir.description = CharacterString(
        "Wind Direction String"
    )

    current_pressure = create_AV(
        oid=4, name="Current_Pressure", pv=0, pv_writable=False
    )
    current_pressure.units = EngineeringUnits("hectopascals")
    current_pressure.description = CharacterString(
        "Current Barometric Pressure"
    )

    current_cloudcov = create_AV(
        oid=5, name="Current_Cloud_Cover", pv=0, pv_writable=False
    )
    current_cloudcov.units = EngineeringUnits("percent")
    current_cloudcov.description = CharacterString(
        "Current Cloud Cover in Percent"
    )

    last_update = create_DateTimeValue(
        oid=1, name="Last_Update"
    )
    last_update.description = CharacterString(
        "Last update timestamp"
    )

    current_location = create_CharStrValue(
        oid=8, name="Weather_Station_City", pv=default_pv
    )
    current_location.description = CharacterString(
        "Location of Weather Station"
    )

    current_description = create_CharStrValue(
        oid=9, name="Current_Weather_Description", pv=default_pv
    )
    current_description.description = CharacterString(
        "Weather Station Description String"
    )

    current_dewpoint = create_AV(
        oid=10, name="Current_Dewpoint", pv=0, pv_writable=False
    )
    current_dewpoint.units = EngineeringUnits("degreesFahrenheit")
    current_dewpoint.description = CharacterString(
        "Current Outdoor Dewpoint"
    )



    new_device.this_application.add_object(current_humidity)
    new_device.this_application.add_object(current_temp)
    new_device.this_application.add_object(current_windspd)
    new_device.this_application.add_object(current_winddir)
    new_device.this_application.add_object(current_pressure)
    new_device.this_application.add_object(current_cloudcov)
    new_device.this_application.add_object(last_update)
    new_device.this_application.add_object(current_location)
    new_device.this_application.add_object(current_description)
    new_device.this_application.add_object(current_dewpoint)

    return new_device



class App:
    dev = start_device()
    weather = OpenWeather(city="duluth", units="imperial")


app = App()


def update():
    app.weather.update()
    current_humid = app.dev.this_application.get_object_name("Current_Humidity")
    current_temp = app.dev.this_application.get_object_name("Current_Temp")
    current_winddir = app.dev.this_application.get_object_name("Current_Wind_Dir")
    current_windspd = app.dev.this_application.get_object_name("Current_Wind_Speed")
    current_pressure = app.dev.this_application.get_object_name("Current_Pressure")
    current_cloudcov = app.dev.this_application.get_object_name("Current_Cloud_Cover")

    last_update = app.dev.this_application.get_object_name("Last_Update")
    current_location = app.dev.this_application.get_object_name("Weather_Station_City")
    current_description = app.dev.this_application.get_object_name("Current_Weather_Description")
    current_dewpoint = app.dev.this_application.get_object_name("Current_Dewpoint")




    new_temp = app.weather.temp
    new_hum = app.weather.hum
    new_winddir = app.weather.winddir
    new_windspd = app.weather.windspd
    new_pressure = app.weather.press
    new_cloudcov = app.weather.cloudcov
    new_update_date = app.weather.update
    new_update_time = app.weather.update
    new_location = app.weather.city
    new_description = app.weather.descrip
    new_dewpoint = app.weather.dewpoint



    last_update.presentValue.date = Date(
    app.weather.timestamp.date().isoformat()
    )
    last_update.presentValue.time = Time(
    app.weather.timestamp.time().isoformat()
    )


    app.dev._log.info("Setting Temp to {}".format(new_temp))
    current_temp.presentValue = new_temp

    app.dev._log.info("Setting Humidity to {}".format(new_hum))
    current_humid.presentValue = new_hum

    app.dev._log.info("Setting Wind Dir to {}".format(new_winddir))
    current_winddir.presentValue = new_winddir

    app.dev._log.info("Setting Wind Spd to {}".format(new_windspd))
    current_windspd.presentValue = new_windspd

    app.dev._log.info("Setting B Press to {}".format(new_pressure))
    current_pressure.presentValue = new_pressure

    app.dev._log.info("Setting Cloud Cov to {}".format(new_cloudcov))
    current_cloudcov.presentValue = new_cloudcov

    app.dev._log.info("Setting Location to {}".format(new_location))
    current_location.presentValue = new_location

    app.dev._log.info("Setting Description to {}".format(new_description))
    current_description.presentValue = new_description

    app.dev._log.info("Setting Dewpoint to {}".format(new_dewpoint))
    current_dewpoint.presentValue = new_dewpoint




def main():
    task_device = RecurringTask(update, delay=900)
    task_device.start()
    while True:
        pass


if __name__ == "__main__":
    main()
