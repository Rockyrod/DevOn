# functions to connect to PostgreSQL and execute SQLs
import time
import pandas as pd
import psycopg2

class PostgreSQL_Connection:
    def __init__(self,user_name,database_name,postgres_pwd,postgres_host):
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

# get the list of all tables present in the database

    def get_all_tables(self):
        self.cursor.execute(""" SELECT table_name FROM information_schema.tables """)

        tables = [table for table in self.cursor.fetchall()]
        return tables

# get the details of records of the table as dataframe

    def get_all_df(self,table_name):
        if self.connection:
            sql_stmt = 'select * from ' + table_name
            df = pd.read_sql(sql_stmt, con = self.connection)
            return df
        else:
            print("No connection found in PostgreSQL -- try again with correct credential")
            return ""

# Executes a single SQL command

    def execute_SQL(self, inputSQL):
        if self.is_connection:
            start = time.time()
            results = self.cursor.execute(inputSQL)
            self.connection.commit()
            end = time.time()
            print("--- Duration = {} secs ---".format(round((end - start), 1)))
            return results

        else:
            print("No connection to PostgreSQL - check user credentials.")
            return ""


PostgreSQL_Connection('postgres','Test','test123','localhost')


