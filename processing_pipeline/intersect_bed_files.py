from main_processing_class import DataProcessingMainClass
from utils import read_bed_file_content
import pandas as pd
import luigi
import time
import glob
import os


class InterceptBedFiles(DataProcessingMainClass):
    """
    A luigi task to intersect bed files
    """

    def output(self):
        

