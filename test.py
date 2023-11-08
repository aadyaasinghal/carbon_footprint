import pandas
import os
from datetime import datetime as dt
# dict. has a key and value seperated by a comma- for this dict. we made the key a string, and value an empty list
data = {
        "miles driven": [], 
        "water use": [],
         "plane travel": [],
           "trash production": [],
           "gas usage": [], 
           }
# creates a new csv file if the user data does not alr exist
if not os.path.exists("user_data.csv"):
    df = pandas.DataFrame(data)
    df.set_index("miles driven", inplace = True)
    df.to_csv("user_data.csv")
# loads the user_data.csv file
df1 = pandas.read_csv("user_data.csv", index_col = "miles driven")
# function adds a new row to the existing data the two inputs are df1 and df2 output is y
def add_row(df1, df2):
    y = pandas.concat([df1, df2])
    return y
# make a new row 1
data = {
        "miles driven": [5], 
        "water use": [10],
         "plane travel": [15],
        "trash production": [20],
        "gas usage": [25], 
           }


df2 = pandas.DataFrame(data)
# adding to the existing data frame "df1" and "df2" is a new row
x = add_row(df1, df2)
x.set_index("miles driven", inplace = True)
x.to_csv("user_data.csv")

# make a new row #2
df1 = pandas.read_csv("user_data.csv", index_col = "miles driven")
data = {
        "miles driven": [20], 
        "water use": [25],
         "plane travel": [30],
           "trash production": [35],
           "gas usage": [40], 
           }


df2 = pandas.DataFrame(data)
# adding to the existing data frame "df1" and "df2" is a new row
x = add_row(df1, df2)

# adding to the existing data frame "df1" and "df2" is a new row
x.set_index("miles driven", inplace = True)
x.to_csv("user_data.csv")