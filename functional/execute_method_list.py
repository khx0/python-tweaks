#!/usr/bin/python
# -*- coding: utf-8 -*-
##########################################################################################
# author: Nikolas Schnellbaecher
# contact: khx0@posteo.net
# date: 2020-02-22
# file: execute_function_list.py
# tested with python 3.7.2
##########################################################################################

class BaseClass():

    def __init__(self):

        self.fList = []
        self.fList.append(self.print_01)
        self.fList.append(self.print_02)
        self.fList.append(self.print_03)

    def print_01(self):
    	
        print("=== 01 ===")

    def print_02(self):

        print("=== 02 ===")

    def print_03(self):

        print("=== 03 ===")

    def execute_F_stack(self):
        
        for Func in self.fList:

            Func()

if __name__ == '__main__':

    class_01 = BaseClass()

    class_01.execute_F_stack()
