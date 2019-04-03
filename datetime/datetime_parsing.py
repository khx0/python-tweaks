#!/usr/bin/python
# -*- coding: utf-8 -*-
##########################################################################################
# author: Nikolas Schnellbaecher
# contact: khx0@posteo.net
# date: 2019-04-03
# file: datetime_comparator.py
# tested with python 2.7.15
# tested with python 3.7.2
##########################################################################################

# When working with database entries, it is often necessary to compare timestamps.
# By loading timestamps as raw text, they often exists as pure string objects.
# Using the datetime module one can conveniently parse timestamp strings into
# datetime objects, which have access to comparator operators.

import os
import datetime

BASEDIR = os.path.dirname(os.path.abspath(__file__))

if __name__ == '__main__':

    ######################################################################################
    # User settings:
    # To parse a timestamp string to a datetime object (or the other way around),
    # one can specify a timestamp signature as exemplary shown below.
    TIMESTAMP_SIGNATURE = '%Y-%m-%d_%H:%M:%S'
    ######################################################################################
    
    # create a datetime object with the current time
    now = datetime.datetime.now()
    print("now =", now)
    print("type(now) =", type(now))

    # convert the datetime object to a string using the "strftime" function
    timestamp_str = now.strftime(TIMESTAMP_SIGNATURE)
    print("type(timestamp_str) =", type(timestamp_str))
    print("timestampstr =", timestamp_str)

    # conversely convert a datetime string back to a datetime object using the
    # "strptime" function of the datetime module
    datetime_object = datetime.datetime.strptime(timestamp_str, TIMESTAMP_SIGNATURE)
    print("type(datetime_object) =", type(datetime_object))
    print("datetime_object =", datetime_object)

    
    # ToDo: add pytest module for the datetime examples





