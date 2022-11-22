import pandas as pd
df = pd.read_csv('online-retail.csv')
df.head()
print(df)
df['Lineprice']=df['quantity'] * ['unitprice']
df.head()
#print(df)

df_customers = df.groupby('customerid').agg(
    order = ('Invoiceno','nunique'),
    skus = ('stockcode','nunique'),
    quantity = ('quantity','sum'),
    revenue = ('lineprice','sum'),
 ).reset_index()
 
df_customers.head()
print(df_customers)
 