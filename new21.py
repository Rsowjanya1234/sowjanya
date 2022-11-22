import pandas as pd

data = pd.read_csv("nba.csv",index_col = "name")
first=data.loc[["age","college","salary"]]
print(first)
