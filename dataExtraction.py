# Import appropriate modules first
import numpy as np
import pandas as pd
import sqlite3

# CREATE A STRING THAT PRODUCES THE SQL SYNTAX NEEDED TO CREATE THE TABLE
# SIMILAR TO WHAT I DID EARLIER
"""
query = 
CREATE TABLE wine(
    fixed acidity 
 volatile acidity 
3 - citric acid 
4 - residual sugar 
5 - chlorides 
6 - free sulfur dioxide 
7 - total sulfur dioxide 
8 - density 
9 - pH 
10 - sulphates 
11 - alcohol 
Output variable (based on sensory data): 
12 - quality (score between 0 and 10)
wine_class



# HERE WE TELL THE CONNECTION TO EXECUTE THE QUERY WHICH IS CREATING OUR TABLE
# con.execute(query) 
# NOW WE COMMIT THE QUERY
con.commit()

# LET'S INSERT SOME INFORMATION INTO OUR TABLE
# IMPORTANT TO NOTE THAT THE FORMAT THIS IS IN IS tuple WITHIN A LIST
#data = [(69, 'Carl', 'Marx', '420 W. Praiseit Street', '11/9/2007'),

#(27, 'Paco', 'Jerte', '777 N. Pardall Way', '9/10/2009')]

# NEXT WE USE A SQL STATEMENT TO INSERT THE 'data' LIST INTO OUR 'customers' TABLE
stmt = "INSERT INTO wine wine.db"

# HERE WE EXECUTE THE STATEMENT TO INSERT THE DATA INTO OUR TABLE
con.executemany(stmt, data)
# WE COMMIT AGAIN
con.commit()
"""

# HERE WE'RE CONNECTING TO THE IN-MEMORY DATABASE
# WE'RE CALLING THIS CONNECTION 'con'
con = sqlite3.connect('wine.db')

# NEXT WE DO A QUERY TO SEE ALL THE DATA IN OUR TABLE
cursor = con.execute('SELECT * FROM mainTable')

rows = cursor.fetchall()

# NEXT WE CONVERT THE RETRIEVED QUERY INTO A DATAFRAME USING PANDAS
winePD = pd.DataFrame(rows, columns = list(zip(*cursor.description))[0])

print("It worked! :)")

# Now subset data by red and white wine
red = con.execute("SELECT * FROM mainTable where wine_class = 'red'")
red_rows = red.fetchall()

white = con.execute("SELECT * FROM mainTable where wine_class = 'white'")
white_rows = white.fetchall()

redPD = pd.DataFrame(red_rows, columns = list(zip(*red.description))[0])

whitePD = pd.DataFrame(white_rows, columns = list(zip(*white.description))[0])

#redNP = np.array(redPD)
#whiteNP = np.array(whitePD)

num_errors = 0
for item in winePD:
	num_errors += len(winePD[(winePD[item] == -999) | (winePD[item] == -1000)])
print("We have total of: ", str(num_errors), "overall number of errors")

redPD = redPD.replace([-999, -1000], np.nan)
#redPD[redPD < 0.0] = np.nan
redPD.fillna(redPD.mean())
print(redPD)

whitePD = whitePD.replace([-999, -1000], np.nan)
#whitePD[whitePD < 0.0] = np.nan
whitePD.fillna(whitePD.mean())

"""
for column in redPD:
	replace_values(redPD)


def replace_values(data, column):
	data[column].replace(-999, np.mean(column), inplace = True)
	data[column].replace(-1000, np.mean(column), inplace = True)
"""

# FIN :)