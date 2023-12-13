from main_processing_class import DataProcessingMainClass
from batch_processing import BatchProcessing
from utils import read_bed_file_content
import pandas as pd
import subprocess
import luigi
import time
import glob
import os


class CombineBreakCounts(DataProcessingMainClass):
    """
    A luigi task to combine the counts datasets
    """


    def requires(self):
        return BatchProcessing(**self.pass_base_class_parameters())

    
    def output(self):
        return luigi.LocalTarget(
            os.path.join(
                os.path.join(self.base_output_directory, 'coding_test_results/', 
                'summary_results/', 'break_counts_combined.csv')
            )
        )

    def run(self):

        # create the combined data frame
        # use list comprehension to create a list of pd.DataFrame
        combined_break_counts = [pd.read_csv(sample_result) for sample_result in glob.glob(
            os.path.join(
                self.base_output_directory,
                'coding_test_results/',
                'normalised_break_counts/',
                '*'
            )
        )]

        # combine the counts and save a CSV
        pd.concat(combined_break_counts).to_csv(self.output().path, index=False)