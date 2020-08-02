# functions to connect to PostgreSQL and execute SQLs
import time
import pandas as pd
import psycopg2

class PostgreSQL_Connection:
    def __init__(self,user_name,database_name,postgres_pwd,postgres_host,port ="5432"):
        self.user      = user_name
        self.database  = database_name
        self.password  = postgres_pwd
        self.host      = postgres_host

        try:
            self.connection = psycopg2.connect(
                host     = self.host,
                database = self.database,
                user     = self.user,
                password = self.password
            )
            self.is_connection = True
            self.cursor = self.connection.cursor()
        except:
            self.is_connection = False
        
# get the details of records of the table as dataframe

    def get_records(self,table_name):
        if self.connection:
            sql_stmt = 'select * from ' + table_name
            records = pd.read_sql(sql_stmt, con = self.connection)
            return records
        else:
            print("No connection found in PostgreSQL -- try again with correct credential")
            return ""

# Executes a single SQL command

    inputSQL = """ SELECT * From Table_Namec """

    def execute_SQL(self, inputSQL):
        if self.is_connection:
            results = self.cursor.execute(inputSQL)
            self.connection.commit()
            return results
        else:
            print("No connection to PostgreSQL - check user credentials.")
            return ""




