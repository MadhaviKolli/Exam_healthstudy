#Structure the code
#Move parts of your code from part 1 into functions and modules.
#Create at least one class (e.g. HealthAnalyzer) that can perform some part of the analysis (e.g. calculate statistics or plot graphs).
#import sys, os

#sys.path.append(os.path.abspath(".."))
#import src.hea_stu as hs
#import src.io_utils as io  

import pandas as pd


def summary_statistics(df):

    columns = [
        'age',
        'height',
        'weight',
        'systolic_bp',
        'cholesterol'
    ]

    return df[columns].agg(
        ['mean', 'median', 'min', 'max']
    )



