"""



"""

import numpy as np
import pandas as pd
import csv
import matplotlib as mpt

raw_data = open("dataset_trees_from_R.csv", 'rt')
trees_reader = csv.reader(raw_data, delimiter=',')
trees_dataset = list(trees_reader)

print(trees_dataset)
print(type(trees_dataset))

# load dataset in CSV via pandas
data = pd.read_csv("dataset_trees_from_R.csv")
print(data)

print(data.info)



def how_to_multiply_column_in_df_by_number ():
    df = pd.DataFrame(np.ones((5,6)),columns=['one','two','three',
                                       'four','five','six'])
    df.one *=5
    df.two = df.two*5
    df.three = df.three.multiply(5)
    df['four'] = df['four']*5
    df.loc[:, 'five'] *=5
    df.iloc[:, 5] = df.iloc[:, 5]*5
    return 0



df = pd.DataFrame(np.ones((5,6)),columns=['one','two','three',
                                       'four','five','six'])
df.one *=5
df.two = df.two*5
df.three = df.three.multiply(5)
df['four'] = df['four']*5
df.loc[:, 'five'] *=5
df.iloc[:, 5] = df.iloc[:, 5]*5

















