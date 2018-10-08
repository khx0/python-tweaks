#!/usr/bin/python
# -*- coding: utf-8 -*-
##########################################################################################
# author: Nikolas Schnellbaecher
# contact: khx0@posteo.net
# date: 2018-09-13
# file: wrap_multiparameter_functions.py
# tested with python 2.7.15
# tested with python 3.7.0
##########################################################################################

'''
    Using pythons lambda construct one can easily wrap 
    multiparameter functions up, once all parameters
    are fixed. In this way on can create function handles
    which can easily be called or passed to other modules
    or functions. This is in particular useful
    to generate smooth interfaces and communicate with
    different APIs consistently.
    I commonly encounter the case where I want to wrap multiparameter
    functions and make them a callable object, which takes only
    one independent variable, as illustrated below.
'''

import numpy as np

# this toy function has the independent variable x
# and two model parameters
def linear_model(x, m, b):
    return m * x + b

if __name__ == '__main__':

    # set model parameters
    m = 2.0
    b = -1.0

    fcall = lambda x: linear_model(x, m, b)

    y_explicit = linear_model(1.0, m, b)
    
    y_wrapped = fcall(1.0)
    
    print("y(explicit) =", y_explicit)
    print("y(wrapped) =", y_wrapped)

    assert np.isclose(y_explicit, y_wrapped), "Error: Test assertion failed."
