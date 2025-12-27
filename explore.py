import pandas as pd
df = pd.read_csv('trx-10k.csv')


df_clean = df.copy()
df_clean['status'] = df_clean['status'].str.lower()
df_clean['status'] = df_clean['status'].replace('failed', 'fail')
df_clean['status'] = df_clean['status'].replace('succeed', 'success')

df_clean['card_type'] = df_clean['card_type'].str.lower()

df_clean['card_type'] = df_clean['card_type'].replace({
'mastcard': 'mastercard',
'master-card': 'mastercard',
'master card':'mastercard'})

df_clean['card_type'] = df_clean['card_type'].replace('vsa', 'visa')

df_clean['city'] = df_clean['city'].str.lower()
df_clean['city'] = df_clean['city'].str.strip()
df_clean['city'] = df_clean['city'].replace({
'thr': 'tehran',
'tehr@n': 'tehran',
'thran': 'tehran'
})


print(df_clean['status'].unique())
print(df_clean['card_type'].unique())
print(df_clean['city'].unique())
print(df_clean.info())
