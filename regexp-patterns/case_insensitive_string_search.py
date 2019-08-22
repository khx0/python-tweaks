#!/usr/bin/python
# -*- coding: utf-8 -*-
##########################################################################################
# author: Nikolas Schnellbaecher
# contact: khx0@posteo.net
# date: 2019-08-23
# file: wrap_multiparameter_functions.py
# tested with python 2.7.15
# tested with python 3.7.2
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
    	print('{} contains {}.'.format(full_string, sub_string))

    if re.search(sub_string, full_string, re.I):
    	print('{} contains {} using the re.I option.'.format(full_string, sub_string))

    # test 2
    full_string = 'path_to_data_set_TYPE_c_3.dat'
    sub_string = 'type_c'

    if re.search(sub_string, full_string):
    	print('{} contains {}.'.format(full_string, sub_string))

    if re.search(sub_string, full_string, re.I):
    	print('{} contains {} using the re.I option.'.format(full_string, sub_string))
