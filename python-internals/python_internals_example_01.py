#!/usr/bin/python
# -*- coding: utf-8 -*-
##########################################################################################
# author: Nikolas Schnellbaecher
# contact: khx0@posteo.net
# date: 2020-02-23
# file: python_internals_example_01.py
# tested with python 3.7.2
##########################################################################################

import numpy as np

if __name__ == '__main__':

    print("__name__ =", __name__)
    print("__file__ =", __file__)
    print("__doc__ =", __doc__)
    print("__package__ =", __package__)

    print("//////////////////////////////////////")

    print("globals() =", globals())

	print("//////////////////////////////////////")

	print(np.__version__)
	print(np)
