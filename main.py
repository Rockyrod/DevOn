# Import necessary libraries
from dbconnect import PostgreSQL_Connection
import pandas as pd 
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

pivoted_data = pd.pivot_table(data=df,index=['Date']) # TO-DO change the code as per requirement aggfunc={'Age':np.mean,'Survived':np.sum})
print(pivoted_data)

# 3.Store data into sql database, create a database (test) and table name (test table).
# TO-DO

#4.Once stored, please perform CRUD operations on the data in database using python/java code.
# TO-DO




