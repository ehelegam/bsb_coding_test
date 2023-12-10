#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 14:52:35 2023

@author: ehelegam
"""

from main_processing_class import DataProcessingMainClass
from utils import read_bed_file_content
import pandas as pd
import luigi
import time
import glob
import os


class FilterBedFile(DataProcessingMainClass):
    """
    A luigi task to filter bed files
    """

    def run(self):


        filter_bed_file_content = read_bed_file_content(self.sample)
        time.sleep(30)
        filter_bed_file_content.to_csv(self.output().path, sep = '\t')
            

    def output(self):
        
        filtered_bed_files = os.path.join(
            self.output_directory,
                'filtered_bed_files',
                os.path.basename(self.sample).replace('.bed', '_filtered.bed')
        )
        return luigi.LocalTarget(filtered_bed_files)