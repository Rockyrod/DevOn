## Problem statement:

1. Get data from API end point in CSV format, and store the same in a file:
	-- while storing in CSV file, please add a column processed_time, which is current time at the point of scraping the data.
	end point: 
	http://www.tennet.org/english/operational_management/export_data.aspx?exporttype=bidpriceladder&format=csv&datefrom=2020-01-01&dateto=2020-01-02&submit=1
 
 
2. Perform pivot using pandas on same dataframe:
	--where : 'PTE' as columns 
			  'Date' as index 
			  'total_plus' as value
    -- Use aggregate function if necessary while performing above operation.		

3. Store data into sql database, create a database (test) and table name (test table).
4. Once stored, please perform CRUD operations on the data in database using python/java code.

## Solution:

Step1 : Run main.py file
Note:pivoted_data.csv has been stored as reference for final ouptut