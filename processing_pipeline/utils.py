"""

"""
import pandas as pd



def filter_bed_decorator(decorated_function, min_read_quality=30):
    def decorator_wrapper(*args, **kwargs):
        bedfile = decorated_function(*args, **kwargs)
        return bedfile[bedfile['read_quality'].values >= min_read_quality]
    return decorator_wrapper





def read_bed_file_content(path_to_bed_file: str) -> pd.DataFrame:
    """
    Read content of a bed
    
    The function is passed to a decorator to filter the bed file by read quality
    """
    return pd.read_csv(path_to_bed_file, sep='\t', header=None, names=['chr1', 'start', 'end', 'read_name', 'read_quality', 'read_orientation'])


read_and_filter_bed_file_content = filter_bed_decorator(read_bed_file_content)