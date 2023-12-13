import subprocess
import argparse
import datetime
import sys
import os


### Script version
version = '0.0.1'


arguments_parser = argparse.ArgumentParser(description="""
        Data Processing Pipeline

        Run the data processing pipeline to identify breaks in sequencing data

        Draft by: Elves H Duarte
        E-mail: ehelegam@gmail.com
        GitHub: Coding Test - Advanced (https://github.com/ehelegam/bsb_coding_test)""")
arguments_parser.add_argument('--path-to-data-pipeline', help='Absolute path to the data processing pipeline', required=False,
                              dest='path_to_pipeline', action='store', default=sys.path[0])
arguments_parser.add_argument('--input-directory', help='Absolute path to the directory containing the input BED file.', required=False,
                              dest='input_directory', action='store', default=f'{sys.path[0]}/coding-test-advanced/data/breaks/')
arguments_parser.add_argument('--min-read-quality', help='The minimun acceptable read quality.', required=False,
                              dest='min_read_quality', action='store', default=30)
arguments_parser.add_argument('--asisi-sites', help='Absolute path to the target AsiSI sites.', required=False,
                              dest='asisi_sites', action='store', default=f'{sys.path[0]}/coding-test-advanced/data/chr21_AsiSI_sites.t2t.bed')
arguments_parser.add_argument('--base-output-directory ', help='Absolute path to the output base directory (i.e., where you want the output files). Defaults to the current working directory', required=False, dest='base_output_directory', action='store', default=f'{os.getcwd()}')
arguments_parser.add_argument('--version', action='version', version=f'v{version}')


### parse the command-line arguments
arguments = arguments_parser.parse_args()


def main():
    """
    LuK - Luigi pipeline for Kronos Bio
    """

    # the run command line

    sub_command = f"""PYTHONPATH={arguments.path_to_pipeline}/processing_pipeline/ \
        luigi --module plot_combined_data PlotCombinedData \
            --input-directory {arguments.input_directory} \
                --min-read-quality {arguments.min_read_quality} \
                    --asisi-sites {arguments.asisi_sites} \
                        --base-output-directory {arguments.base_output_directory} \
                             --local-scheduler"""


    ### check SF and ddPCR reports exist
    if  not all([
        os.path.isdir(arguments.input_directory),
        os.path.isfile(arguments.asisi_sites)
        ]):
            raise FileNotFoundError('Check if the path to the input directory and/or the AsiSI sites is correct')

    if not isinstance(arguments.min_read_quality, int):
        raise TypeError('The minimun read quality must be an integer.')

    # submit
    subprocess.call(sub_command, shell=True)


if __name__ == "__main__":
    main()

