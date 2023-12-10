#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 14:52:35 2023

@author: ehelegam
"""

from main_processing_class import DataProcessingMainClass
import glob
import os


class FilterBedFile(DataProcessingMainClass):
    """
    A luigi task to filter bed files
    """
        
    
    def run(self):
        
        for bed_file in glob.glob(self.input_directory):
            print(bed_file)