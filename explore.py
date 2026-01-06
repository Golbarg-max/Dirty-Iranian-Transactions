import pandas as pd
import mysql.connector

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

df_clean = df_clean.drop('id', axis=1)
df_clean['transaction_id'] = range(1, len(df_clean) + 1)
df_clean = df_clean.where(pd.notna(df_clean), None)

cnx  = mysql.connector.connect(
    user='root', 
    password = 'pass245word', 
    host = 'localhost',
    database = 'transactions_db')
cursor = cnx.cursor()
cursor.execute("TRUNCATE TABLE transactions;")
sql_query = """INSERT INTO transactions (transaction_id, status, time, card_type, city, amount) 
            VALUES (%s, %s, %s, %s, %s, %s);"""
for index, row in df_clean.iterrows():
    cursor.execute(sql_query, (row['transaction_id'], row['status'], row['time'], row['card_type'], row['city'], row['amount']))
cnx.commit()

df = pd.read_sql("SELECT * FROM transactions", cnx)
df.to_csv('transactions_clean.csv', index=False)

cursor.close()