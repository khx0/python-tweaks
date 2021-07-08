#!/usr/bin/python
# -*- coding: utf-8 -*-
##########################################################################################
# author: Nikolas Schnellbaecher
# contact: khx0@posteo.net
# date: 2021-07-08
# file: datetime_str_conversion.py
# tested with python 3.7.6 and pytest 6.2.4
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
from datetime import datetime

BASEDIR = os.path.dirname(os.path.abspath(__file__))

def datetime_str_conversion(input_str, in_signature, out_signature):
    output_str = datetime.strptime(input_str, in_signature).strftime(out_signature)
    return output_str

'''
%m month
%d day
%Y Year

%-m month with leading zero removed, i.e. 06 --> 6
'''

def test_datetime_str_conversion():

    input_str = r'6/11/2007'

    output_str = datetime_str_conversion(input_str, "%m/%d/%Y", "(%-m, %d, %Y)")
    print("input =", input_str)
    print("output =", output_str)

    output_str_reference = r'(6, 11, 2007)'
    assert output_str == output_str_reference

    print("All test passed successfully.")

if __name__ == '__main__':

    test_datetime_str_conversion()
