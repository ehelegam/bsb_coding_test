from filter_bed_files import FilterBedFile
from intersect_bed_files import IntersectBedFiles
from base_class import DataProcessingBaseClass
import luigi
import glob

class CompletePipeline(DataProcessingBaseClass, luigi.WrapperTask):

    BED_FILE_EXTENSION = luigi.Parameter()

    def pass_main_class_parameters(self, sample) -> dict:
        """
        Pass luigi parameters across tasks
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
        for bedfile in glob.glob(self.input_directory + self.BED_FILE_EXTENSION):
            yield IntersectBedFiles(**self.pass_main_class_parameters(sample=bedfile))