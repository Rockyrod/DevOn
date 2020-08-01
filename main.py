# Import necessary libraries
from dbconnect import PostgreSQL_Connection
import pandas as pd 
import numpy as np
import time

# 1.Extract the data from given url in csv format and also add a column Processed_time which is nothing but time at the point of scrapping the data

url = "http://www.tennet.org/english/operational_management/export_data.aspx?exporttype=bidpriceladder&format=csv&datefrom=2020-01-01&dateto=2020-01-02&submit=1"
df = pd.read_csv(url)
df.insert(16, 'Processed_time', time.strftime('%d-%m-%Y %H:%M:%S'))
print(df)

# 2.Perform pivot using pandas on same dataframe:
# where : 'PTE' as columns 
#         'Date' as index 
#         'total_plus' as value
# Use aggregate function if necessary while performing above operation.

pivoted_data = pd.pivot_table(df, index=['Date'],columns=['PTE'],values=['total_plus'], aggfunc=np.max)
print(pivoted_data)

# 3.Store data into sql database, create a database (test) and table name (test table).
# TO-DO
print("Connect Postgres Database")
dbconnect = PostgreSQL_Connection("Postgres","Test","test123","127.0.0.1")

#Store the data into tables
print("STORE api data into test table database test")
df.to_sql('test',PostgreSQL_Connection,if_exists='fail')

#4.Once stored, please perform CRUD operations on the data in database using python/java code.
# TO-DO

print('Please perform CRUD Operations on data')

# create table
create_table = execute_sql("""CREATE TABLE Table_Name
                              (ID    INT PRIMARY KEY     NOT NULL,
                               NAME  TEXT    NOT NULL,
                               ADRESS""")
                  

print ('Table created successfully')

# insert data into table
inserted_table = execute_sql(
                  """ INSERT INTO Table_Name (column1,column2,column3,column4) \
                    VALUES (value1,value2,value3,value4)");
                  
                    INSERT INTO Table_Name (column1,column2,column3,column4) \
                    VALUES (value1,value2,value3,value4)");

                    INSERT INTO Table_Name (column1,column2,column3,column4) \
                    VALUES (value1,value2,value3,value4)"""); 

# select table data
select_table_data = execute_sql(" SELECT * FROM Table_Name ")

# update table
updated_table = execute_sql("UPDATE Table_Name set column = value where colum_name(PK) = 1")