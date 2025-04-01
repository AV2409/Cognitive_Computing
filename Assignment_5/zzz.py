import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

m=np.random.randint(15,40,5)
tu=np.random.randint(15,40,5)
w=np.random.randint(15,40,5)
th=np.random.randint(15,40,5)
f=np.random.randint(15,40,5)
prev=np.random.randint(15,40,5)
cities=['Mumbai','Kolkata','Bengluru','Hyderabad','Chennai']

data={'Cities':cities,
      'Monday':m,
      'Tuesday':tu,
      'Wednesday':w,
      'Thursday':th,
      'Friday':f,
      'Previous_avg':prev}

df=pd.DataFrame(data)
print(df)
df["Avg"] = df.iloc[:, 1:].mean(axis=1)
print(df)

maxx=df.iloc[:, 1:].max(axis=1)
print(maxx)