import sqlite3
import pandas as pd 
import numpy as np
import time
from sqlalchemy import create_engine

# 1.Extract the data from given url in csv format and also add a column Processed_time which is nothing but time at the point of scrapping the data

url = "http://www.tennet.org/english/operational_management/export_data.aspx?exporttype=bidpriceladder&format=csv&datefrom=2020-01-01&dateto=2020-01-02&submit=1"
df = pd.read_csv(url)
data = df.insert(16, 'Processed_time', time.strftime('%d-%m-%Y %H:%M:%S'))
# print(df)

# create Test database and test table
engine = create_engine('sqlite:///new_test.db', echo=True)
sqlite_connection = engine.connect()
# table_name = "New_Table"
# df.to_sql(table_name, sqlite_connection, if_exists='fail')
# result1 = pd.read_sql_query("SELECT * from New_Table",engine)
total_plus = pd.read_sql_query("SELECT total_plus from New_Table ",engine)
print(total_plus)

