from normalise_break_counts import NormaliseBreakCounts
from base_class import DataProcessingBaseClass
import luigi
import glob

class BatchProcessing(DataProcessingBaseClass, luigi.WrapperTask):

    BED_FILE_EXTENSION = luigi.Parameter()

    def pass_main_class_parameters(self, sample) -> dict:
        """
        Pass luigi parameters across tasks

        This allows passing the sample name across luigi tasks
        """
        return {
            "sample": sample,
            "input_directory": self.input_directory,
            "base_output_directory": self.base_output_directory,
            "asisi_sites": self.asisi_sites,
            "min_read_quality": self.min_read_quality
            #"normalisation_number": self.normalisation_number
            }
    
    

    def requires(self):
        # loop over each bed file in the input directory
        for bedfile in glob.glob(self.input_directory + self.BED_FILE_EXTENSION):
            # process the sample
            yield NormaliseBreakCounts(**self.pass_main_class_parameters(sample=bedfile))