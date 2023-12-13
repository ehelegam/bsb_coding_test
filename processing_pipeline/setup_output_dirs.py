from main_processing_class import DataProcessingMainClass
from base_class import DataProcessingBaseClass
import luigi
import os


class SetUpOutputDirs(DataProcessingBaseClass):

    def output(self):
        
        # use list comprehension to create luigi local targets
        output_dirs = [
            luigi.LocalTarget(os.path.join(self.base_output_directory, 'coding_test_results/', dir)) for dir in [
            'filtered_bed_files',
            'intersected_bed_files',
            'counts_filtered_break',
            'counts_unfiltered_break',
            'normalised_break_counts',
            'summary_results'
            ]
        ]

        return output_dirs


    def run(self):

        # loop over the list containing local targets
        # create the directory if it not already created
        for output_dir in self.output():
            if not os.path.isdir(output_dir.path):
                os.makedirs(output_dir.path)