import pandas as pd

data = pd.read_csv(r'C:\pythoncode\Giant.csv')
df = pd.DataFrame(data, columns=['CEO','Established'])
print(df)
