#!/usr/bin/env python
from BAC0.core.utils.notes import note_and_log
import time, numpy
from datetime import datetime, timedelta
import pandas as pd
import numpy as np
import datetime



@note_and_log
class Enery_Costs_Calcs:

    backup_data = [[-5.0, -5.0, -5.0, -5.0, -5.0, -5.0, -5.0, -5.0,
    -5.0, -5.0, -5.0, -5.0, -5.0, -5.0, -5.0, -5.0,
    -5.0, -5.0, -5.0, -5.0, -5.0, -5.0, -5.0, -5.0]]

    def __init__(self):
        self.data = None


    def update(self):

        self._log.info("Attempting to get data from csv for cost calcs")

        combine = pd.DataFrame()
        combine2 = pd.DataFrame()

        try:

            clg_projection_df = pd.read_csv('./clg_load_projection.csv')
            projection_df = pd.read_csv('./kwh_projection.csv')
            costs_df = pd.read_csv('./TOU_rates_kwh_summer.csv', index_col='hour')

            clg_projection_df.reset_index(drop=True, inplace=True)
            projection_df.reset_index(drop=True, inplace=True)
            costs_df.reset_index(drop=True, inplace=True)

            combine = pd.concat([costs_df, projection_df], axis=1)
            combine = pd.DataFrame(combine)
            combine['costs_est'] = combine['dollar'] * combine['projected_kwh']

            combine2 = pd.concat([combine, clg_projection_df], axis=1)
            combine2 = pd.DataFrame(combine2)

            combine2.to_csv('combine2.csv')

            clg_projection_df = combine2['projected_load'].rank()
            combine2_rank_dollar = combine2['costs_est'].rank()
            combine2_rank_kwh = combine2['projected_kwh'].rank()

            clg_projection_df.to_csv('combine_rank_clgload.csv')
            combine2_rank_dollar.to_csv('combine_rank_dollar.csv')
            combine2_rank_kwh.to_csv('combine_rank_kwh.csv')

            self.arr = numpy.asarray(combine['costs_est']).reshape(-1)
            return self.arr


        except Exception as error:
            self._log.error("Error with cost calcs {}".format(error))
            self._log.warning("Using backup data for cost projections!")


            self.arr = numpy.asarray(self.backup_data).reshape(-1)

            return self.arr




    @property
    def costs_5AM(self):
        return self.arr[5]

    @property
    def costs_6AM(self):
        return self.arr[6]

    @property
    def costs_7AM(self):
        return self.arr[7]

    @property
    def costs_8AM(self):
        return self.arr[8]

    @property
    def costs_9AM(self):
        return self.arr[9]

    @property
    def costs_10AM(self):
        return self.arr[10]

    @property
    def costs_11AM(self):
        return self.arr[11]

    @property
    def costs_12PM(self):
        return self.arr[12]

    @property
    def costs_1PM(self):
        return self.arr[13]

    @property
    def costs_2PM(self):
        return self.arr[14]

    @property
    def costs_3PM(self):
        return self.arr[15]

    @property
    def costs_4PM(self):
        return self.arr[16]

    @property
    def costs_5PM(self):
        return self.arr[17]

    @property
    def costs_6PM(self):
        return self.arr[18]

    @property
    def costs_7PM(self):
        return self.arr[19]

    @property
    def costs_8PM(self):
        return self.arr[20]
