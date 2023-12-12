from main_processing_class import DataProcessingMainClass
from base_class import DataProcessingBaseClass
import luigi
import os


class SetUpOutputDirs(DataProcessingBaseClass):

    def output(self):
        
        output_dirs = [
            luigi.LocalTarget(os.path.join(self.base_output_directory, 'coding_test_results/', dir)) for dir in [
            'filtered_bed_files',
            'intersected_bed_files',
            'number_of_breaks_per_sample',
            'summary_results'
            ]
        ]

        return output_dirs


    def run(self):

        for output_dir in self.output():
            if not os.path.isdir(output_dir.path):
                os.makedirs(output_dir.path)