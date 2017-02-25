# Import appropriate modules first
import numpy as np
import pandas as pd
import sqlite3

# CREATE A STRING THAT PRODUCES THE SQL SYNTAX NEEDED TO CREATE THE TABLE
# SIMILAR TO WHAT I DID EARLIER
query = """
CREATE TABLE customers(
    customer_id VARCHAR(36),
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    address VARCHAR(200), 
    date_enrolled DATETIME
    );"""

# HERE WE'RE CONNECTING TO THE IN-MEMORY DATABASE
# WE'RE CALLING THIS CONNECTION 'con'
con = sqlite3.connect(':memory:')
# HERE WE TELL THE CONNECTION TO EXECUTE THE QUERY WHICH IS CREATING OUR TABLE
con.execute(query) 
# NOW WE COMMIT THE QUERY
con.commit()

# LET'S INSERT SOME INFORMATION INTO OUR TABLE
# IMPORTANT TO NOTE THAT THE FORMAT THIS IS IN IS tuple WITHIN A LIST
data = [(69, 'Carl', 'Marx', '420 W. Praiseit Street', '11/9/2007'),
(27, 'Paco', 'Jerte', '777 N. Pardall Way', '9/10/2009')]

# NEXT WE USE A SQL STATEMENT TO INSERT THE 'data' LIST INTO OUR 'customers' TABLE
stmt = "INSERT INTO customers VALUES(?,?,?,?,?)"

# HERE WE EXECUTE THE STATEMENT TO INSERT THE DATA INTO OUR TABLE
con.executemany(stmt, data)
# WE COMMIT AGAIN
con.commit()

# NEXT WE DO A QUERY TO SEE ALL THE DATA IN OUR TABLE
cursor = con.execute('SELECT * FROM customers')


rows = cursor.fetchall()

# NEXT WE CONVERT THE RETRIEVED QUERY INTO A DATAFRAME USING PANDAS
customersPD = pd.DataFrame(rows, columns = list(zip(*cursor.description))[0])

print("It worked! :)")
# FIN :)