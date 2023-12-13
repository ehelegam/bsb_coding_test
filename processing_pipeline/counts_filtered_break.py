from main_processing_class import DataProcessingMainClass
from intersect_bed_files import IntersectBedFiles
from utils import read_bed_file_content
import pandas as pd
import subprocess
import luigi
import time
import glob
import os


class CountsFilteredBreak(DataProcessingMainClass):
    """
    A luigi task to count breaks per sample
    """


    def requires(self):
        return IntersectBedFiles(**self.pass_main_class_parameters(sample=self.sample))

    
    def output(self):
        return luigi.LocalTarget(
            os.path.join(
                os.path.join(self.base_output_directory, 'coding_test_results/', 'counts_filtered_break/',
                os.path.basename(self.sample).replace('.breakends', '_filtered-breaks.csv'))
            )
        )

    def run(self):
        # read the intersected bed file
        # pd.DataFrame
        intersection_bed_file = read_bed_file_content(self.input().path)

        # create pandas data frame object
        # num_breaks = nrow ( intersection_bed_file )
        # columns: sample_name & num_breaks
        counts_per_sample = pd.DataFrame(
            {
                "sample_name": [os.path.basename(self.sample).replace('.breakends.bed', '')],
                "num_breaks": [len(intersection_bed_file.index)]
            }
        )
        
        counts_per_sample.to_csv(self.output().path, index=False)
