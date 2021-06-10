#!/usr/bin/python
# -*- coding: utf-8 -*-
##########################################################################################
# author: Nikolas Schnellbaecher
# contact: khx0@posteo.net
# date: 2021-06-10
# file: test_dataclass
##########################################################################################

from dataclasses import dataclass

# Dataclasses are available since Python version 3.7.

def job(run_config):

    print("RunConfig.name =", run_config.name, "called from within run function")

    # DO WORK HERE

    return None

@dataclass
class RunConfig:
    """Class for keeping track of a run configuration."""
    name: str = 'run_01'
    iterations: int = 100
    seed: int = 0

# the created RunConfig dataclass is now available in this script as a globally
# instantiated class
print(RunConfig)

# access dataclass members directly
print("RunConfig.name =", RunConfig.name, "called from global scope")

# pass RunConfig class to a job runner function
job(RunConfig)
