#!/usr/bin/python
# -*- coding: utf-8 -*-
##########################################################################################
# author: Nikolas Schnellbaecher
# contact: khx0@posteo.net
# date: 2020-10-04
# file: floor_divide_fail.py
# tested with python 3.7.6
##########################################################################################

if __name__ == '__main__':

    '''
    Make sure that you are aware of the fact that -7 // 2 = -4 in python,
    while 7 // 2 = 3.
    Also make sure to have the correct operator precedence in mind and note
    the difference in the two snippets below.
    '''

    n_value = 7

    # gives 3
    print(n_value // 2)

    # gives -4
    print(-n_value // 2)

    # gives -3
    print(-(n_value // 2))

    print("version 1 --> the minus sign takes precedence over the floor division:")
    for i in range(-n_value // 2, 4, 1):
        print(i)

    print("version 2 --> the floor division takes precedence over the minus sign:")
    for i in range(-(n_value // 2), 4, 1):
        print(i)
