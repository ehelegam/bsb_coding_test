from main_processing_class import DataProcessingMainClass
from setup_output_dirs import SetUpOutputDirs
from utils import read_bed_file_content
import pandas as pd
import subprocess
import luigi
import time
import glob
import os


class CountsUnfilteredBreak(DataProcessingMainClass):
    """
    A luigi task to count breaks per sample
    """


    def requires(self):
        return SetUpOutputDirs(**self.pass_base_class_parameters())

    
    def output(self):
        return luigi.LocalTarget(
            os.path.join(
                os.path.join(self.base_output_directory, 'coding_test_results/', 'counts_unfiltered_break/',
                os.path.basename(self.sample).replace('.breakends', '_unfiltered-break.csv'))
            )
        )

    def run(self):
        # read the intersected bed file
        # pd.DataFrame
        intersection_bed_file = read_bed_file_content(self.sample)

        # create pandas data frame object
        # num_breaks = nrow ( intersection_bed_file )
        # columns: sample_name & num_breaks
        counts_per_sample = pd.DataFrame(
            {
                "sample_name": [os.path.basename(self.sample).replace('.breakends.bed', '')],
                "num_unfiltered_breaks": [len(intersection_bed_file.index)]
            }
        )
        
        counts_per_sample.to_csv(self.output().path, index=False)
