#!/usr/bin/python
# -*- coding: utf-8 -*-
##########################################################################################
# author: Nikolas Schnellbaecher
# contact: khx0@posteo.net
# date: 2020-10-04
# file: datetime_comparator.py
# tested with python 3.7.6 and pytest 6.6.1
##########################################################################################

'''
pytest invocation:
To run this script as a pytest, run
$pytest -s <MY_PYTHON_SCRIPT.py>
or via
$python -m pytest -s <MY_PYTHON_SCRIPT.py>
where python is your current python interpreter.
'''

# When working with database entries, it is often necessary to compare timestamps.
# By loading timestamps as raw text, they often exists as pure string objects.
# Using the datetime module one can conveniently parse timestamp strings into
# datetime objects, which have access to comparator operators.

import os
import datetime

BASEDIR = os.path.dirname(os.path.abspath(__file__))

##########################################################################################
# User settings:
# To parse a timestamp string to a datetime object (or the other way around),
# one can specify a timestamp signature as exemplary shown below.
TIMESTAMP_SIGNATURE = '%Y-%m-%d %H:%M:%S.%f'
##########################################################################################

def test_datetime_comparator():

    timeString_1 = '2018-09-17 22:04:57.707'
    print(type(timeString_1))

    time_1 = datetime.datetime.strptime(timeString_1, TIMESTAMP_SIGNATURE)
    print(type(time_1))

    assert isinstance(time_1, datetime.datetime), "Error: Type assertion failed."

    # datetime objects can now be compared using the standard <, <=, >, >= comparator
    # operators
    # self reflectiveness
    assert time_1 == time_1
    assert time_1 <= time_1
    assert time_1 >= time_1
    print("time_1 == time_1", time_1 == time_1)
    print("time_1 <= time_1", time_1 <= time_1)
    print("time_1 >= time_1", time_1 >= time_1)

    timeString_2 = '2018-09-17 23:12:27.107'

    time_2 = datetime.datetime.strptime(timeString_2, TIMESTAMP_SIGNATURE)

    assert time_1 < time_2
    assert time_1 <= time_2
    assert not(time_1 > time_2)
    assert not(time_1 >= time_2)
    assert not(time_1 == time_2)
    print("time_1 < time_2", time_1 < time_2)
    print("time_1 <= time_2", time_1 <= time_2)
    print("time_1 > time_2", time_1 > time_2)
    print("time_1 >= time_2", time_1 >= time_2)
    print("time_1 == time_2", time_1 == time_2)

if __name__ == '__main__':

    test_datetime_comparator()
