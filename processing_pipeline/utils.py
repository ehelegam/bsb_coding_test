"""
Utility scripts
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import datetime
import os


# decorator to time the run command of luigi tasks
def time_luigi_run(func):
    def wrapper(*arg, **kw):
        print('--------------------------------------------------')
        print()
        print(f'run() started at {datetime.datetime.now()}')
        res = func(*arg, **kw)
        print(f'run() ended at {datetime.datetime.now()}')
        print()
        print('--------------------------------------------------')
        return res, func.__name__    
    return wrapper


# decorator to filter bed files
def filter_bed_decorator(decorated_function, min_read_quality):
    def decorator_wrapper(*args, **kwargs):
        bedfile = decorated_function(*args, **kwargs)
        return bedfile[bedfile['read_quality'].values >= min_read_quality]
    return decorator_wrapper


def read_bed_file_content(path_to_bed_file: str) -> pd.DataFrame:
    """
    Read content of a bed
    
    The function can be passed to a decorator to filter the bed file by read quality
    """
    return pd.read_csv(path_to_bed_file, sep='\t', header=None, names=['chr1', 'start', 'end', 'read_name', 'read_quality', 'read_orientation'])


def barplot(dataset: pd.DataFrame, ycol: str, ylabel: str, base_dir, output: str) -> str:
    """
    Generate a barplot
    """
    plt.figure()
    plot = sns.barplot(data= dataset, x = 'sample_name', y = ycol)
    plt.xticks(rotation=50)
    plt.tight_layout()
    plot.set(xlabel = 'Sample Name', ylabel = ylabel)
    plt.savefig(
        os.path.join(
            base_dir,
            'coding_test_results/'
            'summary_results/',
            output
        )
    )

# TODO: fix
read_and_filter_bed_file_content = filter_bed_decorator(read_bed_file_content, 30)