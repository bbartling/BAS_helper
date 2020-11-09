#!/usr/bin/env python
from BAC0.core.utils.notes import note_and_log
import requests, json, time, numpy
from sqlalchemy import create_engine
from datetime import datetime, timedelta
import sqlite3
import pandas as pd
import numpy as np

from fbprophet import Prophet

@note_and_log
class Model:

    def __init__(self):
        self.data = None



    def update(self):

        hourly_avg = pd.DataFrame()

        def clean_dataset(df):
            assert isinstance(df, pd.DataFrame), "df needs to be a pd.DataFrame"
            df.dropna(inplace=True)
            indices_to_keep = ~df.isin([np.nan, np.inf, -np.inf]).any(1)
            return df[indices_to_keep].astype(np.float64)


        self._log.info("Attempting to get data from db")

        try:
            con = sqlite3.connect('./save_data.db')
            df = pd.read_sql("SELECT * from all_data", con, index_col='Date', parse_dates=True)

            if len(df) > 1000:

                self._log.info("Attempting to clean dataset")
                df = clean_dataset(df)

                df.reset_index()
                df.index = pd.to_datetime(df.index)
                hourly_avg['kW'] = df['kW'].resample('H').mean()
                hourly_avg['kW'].fillna(value=hourly_avg['kW'].mean(), inplace=True)

                hourly_avg['stamp'] = hourly_avg.index
                prof_df = hourly_avg[['stamp','kW']]
                prof_df.columns = ['ds','y']
                prof_df['ds'] = pd.to_datetime(prof_df['ds'])


                self._log.info("Attempting electrical load forecast")

                m = Prophet()
                m.fit(prof_df)

                periods = 16
                future = m.make_future_dataframe(periods=periods,freq = 'H')
                forecast = m.predict(future)

                forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(periods)

                data = [[forecast.yhat.tail(periods)]]
                self.arr = numpy.asarray(data).reshape(-1)
                return self.arr

            else:
                self._log.warning("Not enough db data")
                self._log.warning("Using backup data for electric meter!")

                backup_data = [[-5.0, -5.0, -5.0, -5.0, -5.0, -5.0, -5.0, -5.0,
                -5.0, -5.0, -5.0, -5.0, -5.0, -5.0, -5.0, -5.0]]
                backup_data_arr = numpy.asarray(backup_data).reshape(-1)
                self.arr = backup_data_arr
                return self.arr


        except Exception as error:
            self._log.error("Error accessing db & forecast attempt {}".format(error))
            self._log.warning("Using backup data for electric meter!")


            backup_data = [[-5.0, -5.0, -5.0, -5.0, -5.0, -5.0, -5.0, -5.0,
            -5.0, -5.0, -5.0, -5.0, -5.0, -5.0, -5.0, -5.0]]
            backup_data_arr = numpy.asarray(backup_data).reshape(-1)
            self.arr = backup_data_arr
            return self.arr



    @property
    def kW_5AM(self):
        return self.arr[0]

    @property
    def kW_8AM(self):
        return self.arr[3]

    @property
    def kW_11AM(self):
        return self.arr[6]

    @property
    def kW_2PM(self):
        return self.arr[9]

    @property
    def kW_5PM(self):
        return self.arr[12]

    @property
    def kW_8PM(self):
        return self.arr[15]
