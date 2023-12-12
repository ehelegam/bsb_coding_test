from main_processing_class import DataProcessingMainClass
from filter_bed_files import FilterBedFile
from utils import read_bed_file_content
import pandas as pd
import subprocess
import luigi
import time
import glob
import os


class IntersectBedFiles(DataProcessingMainClass):
    """
    A luigi task to intersect bed files
    """


    def requires(self):
        return FilterBedFile(**self.pass_main_class_parameters(sample=self.sample))


    def output(self):
        return luigi.LocalTarget(
            os.path.join(self.base_output_directory, 'coding_test_results/', 'intersected_bed_files/', 
            os.path.basename(self.sample).replace('.breakends', '_intersected'))
        )

    def run(self):

        # command line to run bedtools intersect
        intersection_command = [
            'bedtools',
            'intersect',
            '-a', self.input().path,
            '-b', self.asisi_sites
        ]

        # create the local target
        with open(self.output().path, 'w') as intersect_output:
            subprocess.call(intersection_command, stdout=intersect_output)