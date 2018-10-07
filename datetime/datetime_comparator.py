#!/usr/bin/python
# -*- coding: utf-8 -*-
##########################################################################################
# author: Nikolas Schnellbaecher
# contact: khx0@posteo.net
# date: 2018-10-07
# file: datetime_comparator.py
# tested with python 2.7.15
# tested with python 3.7.0
##########################################################################################

import datetime
import os

def ensure_dir(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)

BASEDIR = os.path.dirname(os.path.abspath(__file__))
DATADIR = os.path.join(BASEDIR, 'data')

if __name__ == '__main__':

    # User settings    
    TIMESTAMP_SIGNATURE = '%Y-%m-%d %H:%M:%S.%f'
    
    ######################################################################################
    
    timeString_1 = '2018-09-17 22:04:57.707'
    print(type(timeString_1))
    
    timeObject_1 = datetime.datetime.strptime(timeString_1, TIMESTAMP_SIGNATURE)
    

             
#             startTimeString = tabB_filtered.iloc[j][STARTTIME_COLNAME]
#             endTimeString = tabB_filtered.iloc[j][ENDTIME_COLNAME]
#         
#             st = datetime.datetime.strptime(startTimeString, TIMESTAMP_SIGNATURE)
#             et = datetime.datetime.strptime(endTimeString, TIMESTAMP_SIGNATURE)
#         
#             if (st <= qt and qt <= et):

            

    