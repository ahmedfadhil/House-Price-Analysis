import pandas as pd

df = pd.read_csv('ZILLOW-Z77006_ZRIMFRR.csv')
print(df.head())

df.set_index('Date', inplace=True)

df.to_csv('new.csv')
df = pd.read_csv('new.csv')
print(df.head())

df = pd.read_csv('new.csv', index_col=0)
print(df.head())

df.columns = ['Austin_HPI']
print(df.head())

df.to_csv('final.csv', header=False)
print(df.head())

df = pd.read_csv('final.csv', names=['Data', 'Austin'],index_col=0)
print(df.head())

df.to_html('example.html')




