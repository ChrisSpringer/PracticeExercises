# Christopher Springer
# 11/24/2026
# Class exercise

import pandas as pd
import numpy as np

series_1 = pd.Series([10,20,30,20,np.nan])

print(f'Series list:\n{series_1}')

total = np.sum(series_1)
mean = np.mean(series_1)
max = np.max(series_1)
min = np.min(series_1)
print(f'Sum: {total}')
print(f'Mean: {mean:.2f}')
print(f'Max: {max}')
print(f'Min: {min}\n')


print(f'First three values:\n{series_1.head(3)}\n')
print(f'Checking for empty values:\n{series_1.isnull()}\n')
print(f'Empty values filled:\n{series_1.fillna(0)}\n')
print(f'Sorted values:\n{series_1.sort_values()}\n')
print(f'Count of values:\n{series_1.value_counts()}\n')