from main_processing_class import DataProcessingMainClass
from counts_filtered_break import CountsFilteredBreak
from counts_unfiltered_break import CountsUnfilteredBreak
from utils import *
import pandas as pd
import subprocess
import luigi
import time
import glob
import os


class NormaliseBreakCounts(DataProcessingMainClass):
    """
    A luigi task to count breaks per sample
    """


    def requires(self):
        return {
            "filtered": CountsFilteredBreak(**self.pass_main_class_parameters(sample=self.sample)),
            "unfiltered": CountsUnfilteredBreak(**self.pass_main_class_parameters(sample=self.sample))
        }

    
    def output(self):
        return luigi.LocalTarget(
            os.path.join(
                os.path.join(self.base_output_directory, 'coding_test_results/', 'normalised_break_counts/',
                os.path.basename(self.sample).replace('.breakends', '_normalised-counts.csv'))
            )
        )

    @time_luigi_run
    def run(self):
        
        # filtered and unfiltered counts
        filtered_counts, unfiltered_counts = pd.read_csv(self.input()['filtered'].path), pd.read_csv(self.input()['unfiltered'].path)

        # merge and normalise the number of breaks
        merged_counts = pd.merge(filtered_counts, unfiltered_counts, on='sample_name')

        # normalise counts
        merged_counts['nomalised_counts_per_unfiltered'] = merged_counts['num_breaks'] /(merged_counts['num_unfiltered_breaks'] / 1000)
        merged_counts['nomalised_counts_per_thousand'] = merged_counts['num_breaks'] / 1000

        merged_counts.to_csv(self.output().path)