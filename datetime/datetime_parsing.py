#!/usr/bin/python
# -*- coding: utf-8 -*-
##########################################################################################
# author: Nikolas Schnellbaecher
# contact: khx0@posteo.net
# date: 2020-03-27
# file: datetime_comparator.py
# tested with python 3.7.2 and pytest 5.4.1
##########################################################################################

'''
pytest invocation:
To run this script as a pytest, run
$pytest -s <MY_PYTHON_SCRIPT.py>
or via
$python -m pytest -s <MY_PYTHON_SCRIPT.py>
where python is your current python interpreter.
'''

import os
import datetime

BASEDIR = os.path.dirname(os.path.abspath(__file__))

##########################################################################################
# User settings:
# To parse a timestamp string to a datetime object (or the other way around),
# one can specify a timestamp signature as exemplary shown below.
TIMESTAMP_SIGNATURE = '%Y-%m-%d_%H:%M:%S'
##########################################################################################

def test_datetime_parsing():

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
    now_recovered = datetime.datetime.strptime(timestamp_str, TIMESTAMP_SIGNATURE)
    print("type(now_recovered) =", type(now_recovered))
    print("now_recovered =", now_recovered)

    # illustrate equality between the original datetime object and the datetime object
    # which was recovered by string parsing using strptime
    assert now.year == now_recovered.year
    assert now.month == now_recovered.month
    assert now.day == now_recovered.day
    assert now.hour == now_recovered.hour
    assert now.minute == now_recovered.minute
    assert now.second == now_recovered.second

    print("All test passed successfully.")

if __name__ == '__main__':

    test_datetime_parsing()
