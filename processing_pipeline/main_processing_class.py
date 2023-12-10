#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 14:46:50 2023

@author: ehelegam
"""

from base_class import DataProcessingBaseClass
import luigi

class DataProcessingMainClass(DataProcessingBaseClass):
    """
    The data processing base class
    """
    sample = luigi.Parameter()