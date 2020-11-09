#!/usr/bin/env python
from BAC0.core.utils.notes import note_and_log
import requests, json, time, numpy
from sqlalchemy import create_engine
from datetime import datetime, timedelta
import sqlite3
import pandas as pd
import numpy as np
from numpy import savetxt
import datetime

# Load specific forecasting tools
from statsmodels.tsa.arima_model import ARMA,ARMAResults,ARIMA,ARIMAResults
from statsmodels.graphics.tsaplots import plot_acf,plot_pacf # for determining (p,q) orders
from pmdarima import auto_arima # for determining ARIMA orders
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import adfuller
import pmdarima as pm
from pmdarima.model_selection import train_test_split

@note_and_log
class elec_Model:

    backup_data = [[-5.0, -5.0, -5.0, -5.0, -5.0, -5.0, -5.0, -5.0,
    -5.0, -5.0, -5.0, -5.0, -5.0, -5.0, -5.0, -5.0,
    -5.0, -5.0, -5.0, -5.0, -5.0, -5.0, -5.0, -5.0]]

    def __init__(self):
        self.data = None



    def update(self):

        def clean_dataset(df):
            assert isinstance(df, pd.DataFrame), "df needs to be a pd.DataFrame"
            df.dropna(inplace=True)
            indices_to_keep = ~df.isin([np.nan, np.inf, -np.inf]).any(1)
            return df[indices_to_keep].astype(np.float64)

        def adf_test(series,title=''):
            """
            Pass in a time series and an optional title, returns an ADF report
            """
            starting = (f'Augmented Dickey-Fuller Test: {title}')
            self._log.info(starting)
            result = adfuller(series.dropna(),autolag='AIC') # .dropna() handles differenced data

            labels = ['ADF test statistic','p-value','# lags used','# observations']
            out = pd.Series(result[0:4],index=labels)

            for key,val in result[4].items():
                out[f'critical value ({key})']=val

            info = out.to_string()
            model_info = f"model info: {info}"
            self._log.info(model_info)      # .to_string() removes the line "dtype: float64"

            if result[1] <= 0.05:
                one = f"Strong evidence against the null hypothesis"
                self._log.info(one)
                two = f"Reject the null hypothesis"
                self._log.info(two)
                three = f"Data has no unit root and is stationary"
                self._log.info(three)
            else:
                four = f"Weak evidence against the null hypothesis"
                self._log.info(four)
                five = f"Fail to reject the null hypothesis"
                self._log.info(five)
                six = f"Data has a unit root and is non-stationary"
                self._log.info(six)

            pval_obj = result[1]
            return pval_obj

        '''
        # create a differenced series
        def difference(dataset, interval=1):
        	diff = list()
        	for i in range(interval, len(dataset)):
        		value = dataset[i] - dataset[i - interval]
        		diff.append(value)
        	return diff

        # invert differenced forecast
        def inverse_difference(last_ob, value):
        	return value + last_ob

        # define a dataset with a linear trend
        data = [i+1 for i in range(20)]
        print(data)
        # difference the dataset
        diff = difference(data)
        print(diff)
        # invert the difference
        inverted = [inverse_difference(data[i], diff[i]) for i in range(len(diff))]
        print(inverted)
        '''

        self._log.info("Attempting to get data from db")
        hourly_avg_elec = pd.DataFrame()

        try:
            con = sqlite3.connect('./save_data.db')
            df = pd.read_sql("SELECT * from elec_data", con, index_col='Date', parse_dates=True)

            if len(df) > 1000:

                self._log.info("Attempting to clean dataset")
                df = clean_dataset(df)

                df.reset_index()
                df.index = pd.to_datetime(df.index)
                hourly_avg_elec['kW'] = df['kW'].resample('H').mean()
                hourly_avg_elec['kW'].fillna(value=hourly_avg_elec['kW'].mean(), inplace=True)

                len_split = int(len(hourly_avg_elec)*.1)
                test = hourly_avg_elec.iloc[:len_split]
                train = hourly_avg_elec.iloc[len_split:]

                self._log.info("Attempting electrical load forecast")
                start = datetime.datetime.now()



                if hourly_avg_elec.index.freq == None:
                    hourly_avg_elec = hourly_avg_elec.asfreq('h')
                    self._log.info("df.index freq reset to hourly")

                else:
                    self._log.info("df.index freq LOOKS GOOD")


                result = seasonal_decompose(hourly_avg_elec['kW'], model='add')  # model='mul' also works


                #periods is hours in a day so predict 1 days data
                periods = 24
                #Dicky Fuller statistic test
                pval_obj = adf_test(hourly_avg_elec['kW'])


                p_info = (f'Dickey-Fuller Test P-val: {pval_obj}')
                self._log.info(p_info)

                model = pm.auto_arima(train, seasonal=False)

                forecast = model.predict(periods)
                savetxt('kwh_projection.csv', forecast, delimiter=',')

                self.arr = forecast
                self.pval = pval_obj

                end = datetime.datetime.now()
                diff = (end - start)

                diff_seconds = int(diff.total_seconds())
                minute_seconds, seconds = divmod(diff_seconds, 60)
                hours, minutes = divmod(minute_seconds, 60)
                hms = f"FINISHED! {hours}h {minutes}m {seconds}s"
                self._log.info(hms)

                self.minutes = minutes

                return self.arr,self.minutes,self.pval

            else:
                self._log.warning("Not enough db data")
                self._log.warning("Using backup data for electric meter!")

                self.arr = numpy.asarray(self.backup_data).reshape(-1)
                self.pval = -5.0
                self.minutes = -5.0

                return self.arr,self.minutes,self.pval


        except Exception as error:
            self._log.error("Error accessing db & forecast attempt {}".format(error))
            self._log.warning("Using backup data for electric meter!")

            self.arr = numpy.asarray(self.backup_data).reshape(-1)
            self.pval = -5.0
            self.minutes = -5.0

            return self.arr,self.minutes,self.pval




    @property
    def kW_5AM(self):
        return self.arr[5]

    @property
    def kW_6AM(self):
        return self.arr[6]

    @property
    def kW_7AM(self):
        return self.arr[7]

    @property
    def kW_8AM(self):
        return self.arr[8]

    @property
    def kW_9AM(self):
        return self.arr[9]

    @property
    def kW_10AM(self):
        return self.arr[10]

    @property
    def kW_11AM(self):
        return self.arr[11]

    @property
    def kW_12PM(self):
        return self.arr[12]

    @property
    def kW_1PM(self):
        return self.arr[13]

    @property
    def kW_2PM(self):
        return self.arr[14]

    @property
    def kW_3PM(self):
        return self.arr[15]

    @property
    def kW_4PM(self):
        return self.arr[16]

    @property
    def kW_5PM(self):
        return self.arr[17]

    @property
    def kW_6PM(self):
        return self.arr[18]

    @property
    def kW_7PM(self):
        return self.arr[19]

    @property
    def kW_8PM(self):
        return self.arr[20]

    @property
    def train_minutes(self):
        return self.minutes

    @property
    def dickfulr_pval(self):
        return self.pval
