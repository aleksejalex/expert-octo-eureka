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

















