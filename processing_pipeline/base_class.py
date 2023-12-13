import luigi
import logging
import datetime
import subprocess


class DataProcessingBaseClass(luigi.Task):
    """
    The data processing base class
    """
    input_directory = luigi.Parameter()
    base_output_directory = luigi.Parameter()
    asisi_sites = luigi.Parameter()
    min_read_quality = luigi.IntParameter()
    #normalisation_number = luigi.IntParameter()
        
    
    
    def pass_base_class_parameters(self) -> dict:
        """
        Pass luigi parameters across tasks
        """
        return {
            "input_directory": self.input_directory,
            "base_output_directory": self.base_output_directory,
            "asisi_sites": self.asisi_sites,
            "min_read_quality": self.min_read_quality
            #"normalisation_number": self.normalisation_number
            }