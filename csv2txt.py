# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 15:55:30 2022

@author: prakhar.newatia
"""

import pandas as pd
import os
dir1 = 'D:\\'
arr = os.listdir(dir1)
csv_files = []
for x in arr:
    if '.csv' in x or '.xlsx' in x:
        csv_files.append(x)
for x in csv_files:
    if x[0] == '~':
        continue
    if '.xlsx' in x:
        df = pd.read_excel(os.path.join(dir1, x))
        df.to_csv(os.path.join(dir1, x.replace(
            'xlsx', 'txt')), sep="|", index=False)
    else:
        df = pd.read_csv(os.path.join(dir1, x))
        df.to_csv(os.path.join(dir1, x.replace(
            'csv', 'txt')), sep="|", index=False)
