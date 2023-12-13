from main_processing_class import DataProcessingMainClass
from combine_break_counts import CombineBreakCounts
from utils import read_bed_file_content
from utils import barplot
import pandas as pd
import subprocess
import luigi
import time
import glob
import os


class PlotCombinedData(DataProcessingMainClass):
    """
    A luigi task to combine the counts datasets
    """


    def requires(self):
        return CombineBreakCounts(**self.pass_base_class_parameters())

    
    def output(self):
        pass


    def run(self):
        # read the combined counts data
        combined_break_counts = pd.read_csv(self.input().path).sort_values(['num_breaks']).reset_index(drop=True)

        # plot the number of breaks
        barplot(dataset = combined_break_counts, ycol = 'num_breaks', ylabel = 'Number of breaks', 
        base_dir = self.base_output_directory, output = 'number_of_breaks_per_sample.png')

        # plot the number of breaks (normalised/1,000)
        barplot(dataset = combined_break_counts, ycol = 'nomalised_counts_per_thousand', ylabel = 'Number of breaks (/1,000)', 
        base_dir = self.base_output_directory, output = 'number_of_breaks_per_sample_norm_per_thousand.png')

        # plot the number of breaks (normalised/unfiltered counts)
        barplot(dataset = combined_break_counts, ycol = 'nomalised_counts_per_unfiltered', ylabel = 'Number of breaks (/unfiltered counts)', 
        base_dir = self.base_output_directory, output = 'number_of_breaks_per_samplenorm_per_unfiltered_reads.png')


        