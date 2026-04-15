# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 23:01:43 2026

@author: ovouz
"""

import pandas as pd
import numpy as num

data = pd.read_csv('marscrater_pds.csv', low_memory= False);

print(len(data))
print(len(data.columns))

c1 = data["CRATER_ID"].value_counts(sort=False)
print(c1)

c2 = data["CRATER_NAME"].value_counts(sort=False)