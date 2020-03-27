#!/usr/bin/python
# -*- coding: utf-8 -*-
##########################################################################################
# author: Nikolas Schnellbaecher
# contact: khx0@posteo.net
# date: 2020-03-27
# file: wrap_multiparameter_functions.py
# tested with python 3.7.6
##########################################################################################

'''
Specifying the re.I option in the re.search() function
uses case insensitive string matching.
'''

import re

if __name__ == '__main__':

    # test 1
    full_string = 'path_to_data_set_type_c_3.dat'

    sub_string = 'TYPE_C'

    if re.search(sub_string, full_string):
    	print(f'{full_string} contains {sub_string}.')

    if re.search(sub_string, full_string, re.I):
    	print(f'{full_string} contains {sub_string} using the re.I option.')

    # test 2
    full_string = 'path_to_data_set_TYPE_c_3.dat'
    sub_string = 'type_c'

    if re.search(sub_string, full_string):
    	print(f'{full_string} contains {sub_string}.')

    if re.search(sub_string, full_string, re.I):
    	print(f'{full_string} contains {sub_string} using the re.I option.')
