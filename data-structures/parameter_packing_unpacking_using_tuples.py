#!/usr/bin/python
# -*- coding: utf-8 -*-
##########################################################################################
# author: Nikolas Schnellbaecher
# contact: khx0@posteo.net
# date: 2020-02-22
# file: parameter_packing_unpacking_using_tuples.py
# tested with python 3.7.2
##########################################################################################

import os
import datetime

today = datetime.datetime.now().strftime("%Y-%m-%d")

BASEDIR = os.path.dirname(os.path.abspath(__file__))
RAWDIR = os.path.join(BASEDIR, 'raw')
OUTDIR = os.path.join(BASEDIR, 'out')

def workerThread(params):
	'''
	Prototypical parameter unpacking using pythons tuple data structure.
	This is a convenient way to call run functions for parameter sweeps.
	'''
	p1, p2, p3 = params

	print("p1 from inside workerThread =", p1)
	print("p2 from inside worderThread =", p2)
	print("p3 from inside workerThread =", p3)

	##############
	# DO WORK HERE
	##############

	return None

if __name__ == '__main__':

    # assign some dummy parameters p1, p2, p3 and store them in a tuple
	p1 = 0.5

	p2 = 9.8

	p3 = 1.0e-3

	params = p1, p2, p3

	print(params)
	print(type(params))

	workerThread(params)
