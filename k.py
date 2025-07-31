import pandas as pd

series_1 = pd.Series([10,20,30,40,50])
series_2 = pd.Series([40,50,60,70,80])
print("\n not common series_a and series_b\n")
lm=series_1[~series_1.isin(series_2)]
ml=series_2[~series_2.isin(series_1)]
print(lm)
print(ml)
print("\nddk\n")
kk=lm.union(ml)
print(kk)

