import pandas as pd

df = pd.read_csv("newlol1.csv")
df.drop_duplicates(subset =['URL'],keep = "first")
df.to_csv("newlol2.csv",index = False)