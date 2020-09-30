#!/usr/bin/python
# -*- coding: utf-8 -*-
##########################################################################################
# author: Nikolas Schnellbaecher
# contact: khx0@posteo.net
# date: 2020-09-30
# file: os_environ_demo.py
# tested with python 3.7.6
##########################################################################################

import os

if __name__ == '__main__':

    keys = os.environ.keys()
    
    for i, key in enumerate(keys):
    
        print(i, key)
        
    print(os.environ['PWD'])

    ######################################################################################
    # If your work environment makes it necessary to use an HTTP proxy server, you can set
    # the corresponding environment variable by using the snippet below:
    # os.environ['HTTP_PROXY'] = 'http://myproxy.server.com'
    ######################################################################################
