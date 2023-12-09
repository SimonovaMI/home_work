import pandas as pd

df = pd.read_csv(r'C:\Users\PC\Desktop\Рита Python\PythonProject\data\orderdata_sample.csv', index_col='OrderID')

df['Total'] = df['Quantity'] * df['Price'] + df['Freight']
df.to_csv(r'C:\Users\PC\Desktop\Рита Python\PythonProject\data\orderdata_sample_with_total.csv')

print(df[['Quantity', 'Price', 'Freight', 'Total']].head())

