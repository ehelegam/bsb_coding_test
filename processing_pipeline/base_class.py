import luigi
import logging
import datetime
import subprocess


class DataProcessingBaseClass(luigi.Task):
    """
    The data processing base class
    """
    input_directory = luigi.Parameter()
    output_directory = luigi.Parameter()
    #asisi_sites = luigi.Parameter()
    min_read_quality = luigi.IntParameter()
    #normalization_number = luigi.IntParameter()
        
    
    
    def pass_base_class_parameters(self) -> dict:
        """
        Pass luigi parameters across tasks
        """
        return {
            "input_directory": self.input_directory,
            "output_directory": self.output_directory,
            #"asisi_sites": self.asisi_sites,
            "min_read_quality": self.min_read_quality,
            #"normalization_number": self.normalization_number
            }