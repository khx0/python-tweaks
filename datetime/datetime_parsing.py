#!/usr/bin/python
# -*- coding: utf-8 -*-
##########################################################################################
# author: Nikolas Schnellbaecher
# contact: khx0@posteo.net
# date: 2019-04-02
# file: datetime_comparator.py
# tested with python 2.7.15
# tested with python 3.7.2
##########################################################################################

# When working with database entries, it is often necessary to compare timestamps.
# By loading timestamps as raw text, they often exists as pure string objects.
# Using the datetime module one can conveniently parse timestamp strings into
# datetime objects, which have access to comparator operators.

import datetime
import os

BASEDIR = os.path.dirname(os.path.abspath(__file__))

if __name__ == '__main__':

    ######################################################################################
    # User settings:
    # To parse a timestampe string to a datetime object, you must specify the timestamp
    # signature as exemplary shown below.
    TIMESTAMP_SIGNATURE = '%Y-%m-%d_%H:%M:%S'
    ######################################################################################
    
    now = datetime.datetime.now()
    print("now =", now)
    print("type(now) =", type(now))

    timestamp_str = now.strftime(TIMESTAMP_SIGNATURE)
    print("type(timestamp_str) =", type(timestamp_str))
    print("timestampstr =", timestamp_str)

    datetime_object = datetime.datetime.strptime(timestamp_str, TIMESTAMP_SIGNATURE)
    print("type(datetime_object) =", type(datetime_object))
    print("datetime_object =", datetime_object)




    # ToDo: add pytest module for the datetime examples

    '''
    timeString_1 = '2018-09-17 22:04:57.707'
    print(type(timeString_1))
    
    time_1 = datetime.datetime.strptime(timeString_1, TIMESTAMP_SIGNATURE)
    print(type(time_1))
    
    # datetime objects can now be compared using the standard <, <=, >, >= comparator
    # operators
    
    # self reflectiveness
    print("time_1 == time_1", time_1 == time_1)
    print("time_1 <= time_1", time_1 <= time_1)
    print("time_1 >= time_1", time_1 >= time_1)
    
    timeString_2 = '2018-09-17 23:12:27.107'
    
    time_2 = datetime.datetime.strptime(timeString_2, TIMESTAMP_SIGNATURE)
    
    print("time_1 < time_2", time_1 < time_2)
    print("time_1 <= time_2", time_1 <= time_2)
    print("time_1 > time_2", time_1 > time_2)
    print("time_1 >= time_2", time_1 >= time_2)
    print("time_1 == time_2", time_1 == time_2)
    '''
