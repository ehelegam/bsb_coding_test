from filter_bed_files import FilterBedFile
from intersect_bed_files import IntersectBedFiles
from sample_total_breaks import SampleTotalBreaks
from base_class import DataProcessingBaseClass
import luigi
import glob

class CompletePipeline(DataProcessingBaseClass, luigi.WrapperTask):

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
            "min_read_quality": self.min_read_quality,
            #"normalization_number": self.normalization_number
            }
    
    

    def requires(self):
        # loop over each bed file in the input directory
        for bedfile in glob.glob(self.input_directory + self.BED_FILE_EXTENSION):
            # process the sample
            yield SampleTotalBreaks(**self.pass_main_class_parameters(sample=bedfile))