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
    #min_mapping_quality = luigi.IntParameter()
    #normalization_number = luigi.IntParameter()
        
    
    
    def pass_class_parameters(self) -> dict:
        """
        Pass luigi parameters across tasks
        """
        return {
            "input_directory": self.input_directory,
            "asisi_sites": self.asisi_sites,
            "min_mapping_quality": self.min_mapping_quality,
            "normalization_number": self.normalization_number
            }
    
    