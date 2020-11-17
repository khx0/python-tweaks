#!/usr/bin/python
# -*- coding: utf-8 -*-
##########################################################################################
# author: Nikolas Schnellbaecher
# contact: khx0@posteo.net
# date: 2020-11-17
# file: concatenate_base_dict.py
# tested with python 3.7.6
##########################################################################################

if __name__ == '__main__':

    base_dict = {'a': 1,
                 'b': 2,
                 'c': 3}

    derived_dict_01 = {'d': 4, **base_dict}

    derived_dict_02 = {'e': 5, **base_dict}

    #######################################################################
    # This is an elegant way to pass a common base dict to two new derived
    # dicts, without having to duplicate common dict entries.
    #######################################################################

    print('---------------------------------')
    for key, value in derived_dict_01.items():
        print(key, value)

    print('---------------------------------')
    for key, value in derived_dict_02.items():
        print(key, value)
