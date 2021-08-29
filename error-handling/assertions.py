#!/usr/bin/python
# -*- coding: utf-8 -*-
##########################################################################################
# author: Nikolas Schnellbaecher
# contact: khx0@posteo.net
# date: 2020-08-29
# file: assertions.py
##########################################################################################

import numpy as np

if __name__ == '__main__':

    x = 1.45

    # assertion for float type
    assert isinstance(x, float), "Float assertion failed."

    # check for mutiple float types at the same time
    # In particular the usage of np.floating is very helpful to cover multiple cases simultaneously.
    assert isinstance(x, (np.floating, float)), "Float assertion failed."

    # positivity assertion
    assert x > 0.0, "Positivity assertion failed."
