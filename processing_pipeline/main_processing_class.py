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
    sample = luigi.Parameter(default='undefined')


    def pass_main_class_parameters(self, sample) -> dict:
        """
        Pass luigi parameters across tasks
        """
        return {
            "sample": sample,
            "input_directory": self.input_directory,
            "base_output_directory": self.base_output_directory,
            "asisi_sites": self.asisi_sites,
            "min_read_quality": self.min_read_quality,
            #"normalization_number": self.normalization_number
            }