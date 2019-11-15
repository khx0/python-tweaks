#!/usr/bin/python
# -*- coding: utf-8 -*-
##########################################################################################
# author: Nikolas Schnellbaecher
# contact: khx0@posteo.net
# date: 2019-11-15
# file: execute_function_list.py
# tested with python 3.7.2
##########################################################################################

def print_01():
    print("=== 01 ===")

def print_02():
    print("=== 02 ===")

def print_03():
    print("=== 03 ===")

if __name__ == '__main__':

    fList = []

    fList.append(print_01)
    fList.append(print_02)
    fList.append(print_03)

    print(fList)

    for f in fList:
        f()

    fList.__delitem__(1)

    print(fList)

    for f in fList:
        f()
