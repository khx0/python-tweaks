#!/usr/bin/python
# -*- coding: utf-8 -*-
##########################################################################################
# author: Nikolas Schnellbaecher
# contact: khx0@posteo.net
# date: 2020-03-26
# file: np_len_size_shape_dims.py
# tested with python 3.7.6
##########################################################################################

import numpy as np

if __name__ == '__main__':

    print("running np.__version__ =", np.__version__)

    # illustration of numpy's ndim shape and size methods

    X = np.array([[1.0, 2.0, 3.0],
                  [4.0, 5.0, 6.0]])
    print("X =", X)
    print("ndim =", np.ndim(X))
    print("len =", len(X))
    print("np.shape =", X.shape)
    print("np.size =", np.size(X))

    X = np.array([1.0, 2.0, 3.0])
    print("X =", X)
    print("ndim =", np.ndim(X))
    print("len =", len(X))
    print("np.shape =", X.shape)
    print("np.size =", np.size(X))
    
    X = np.array([[1.0], 
                  [2.0],
                  [3.0]])
    print("X =", X)
    print("ndim =", np.ndim(X))
    print("len =", len(X))
    print("np.shape =", X.shape)
    print("np.size =", np.size(X))


