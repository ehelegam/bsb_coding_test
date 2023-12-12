#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 14:52:35 2023

@author: ehelegam
"""

from main_processing_class import DataProcessingMainClass
from setup_output_dirs import SetUpOutputDirs
from utils import *
import pandas as pd
import luigi
import time
import glob
import os


class FilterBedFile(DataProcessingMainClass):
    """
    A luigi task to filter bed files
    """

    def requires(self):
        return SetUpOutputDirs(**self.pass_base_class_parameters())


    def output(self):
        filtered_bed_files = os.path.join(
            self.base_output_directory,
            'coding_test_results/'
            'filtered_bed_files',
            # combine basename and replace to declare the output file name
            os.path.basename(self.sample).replace('.breakends', '_filtered')
        )

        return luigi.LocalTarget(filtered_bed_files)



    def run(self):
        # read the bed file
        # a decorators will filter the bed file
        filter_bed_file_content = read_and_filter_bed_file_content(self.sample)

        # save the filtered bed file
        filter_bed_file_content.to_csv(self.output().path, sep = '\t', header=False, index=False)