from filter_bed_files import FilterBedFile
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
            "output_directory": self.output_directory,
            #"asisi_sites": self.asisi_sites,
            "min_read_quality": self.min_read_quality,
            #"normalization_number": self.normalization_number
            }
    
    

    def requires(self):
        for bedfile in glob.glob(self.input_directory + self.BED_FILE_EXTENSION.replace('"', '')):
            yield FilterBedFile(**self.pass_main_class_parameters(sample=bedfile))