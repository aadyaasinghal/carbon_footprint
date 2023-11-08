import pandas as pd
import numpy as np
#loading the csv file
df1 = pd.read_csv("user_data.csv", index_col = "time stamp")

# equations from https://www.epa.gov/energy/greenhouse-gases-equivalencies-calculator-calculations-and-references

p = df1["water use"].to_numpy()
totalCarbon = np.sum(p)/244956
print (totalCarbon)
def waterCalc(df):
    # line turns the data frame column into a numpy array
    p = df["water use"].to_numpy()
    # adds up all of water usage nums and divides by 244956 (water calc equation)
    totalCarbon = np.sum(p)/244956
    # units of calc are metric tons
    return totalCarbon

def gasolineCalc(df):
    # line turns the data frame column into a numpy array
    p = df["gas usage"].to_numpy()
    # adds up all of gas usage nums and multiplies by 0.008887 (gas calc equation)
    totalCarbon = np.sum(p) * 0.008887
    # units of calc are metric tons
    return totalCarbon

x = gasolineCalc(df1)
print (x)

def milesDrivenCalc(df):
    # line turns the data frame column into a numpy array
    p = df["driving distance"].to_numpy()
    # adds up all of gas usage nums and multiplies by 0.000390 (miles driven calc equation)
    totalCarbon = np.sum(p) * 0.000390
    # units of calc are metric tons
    return totalCarbon

x = milesDrivenCalc(df1)
print (x)

def trashCalc(df):
    # line turns the data frame column into a numpy array
    p = df["trash production"].to_numpy()
    # adds up all of trash production nums and multiplies by 0.0231 (trash production calc equation)
    totalCarbon = np.sum(p) * 0.0231
    # units of calc are metric tons
    return totalCarbon

x = trashCalc(df1)
print (x)

def planeCalc(df):
    # line turns the data frame column into a numpy array
    # data stored in csv files is number of hours user spent on plane
    p = df["plane travel"].to_numpy()
    # adds up all of hours spent on plane and multiplies by 90 and then multiplies by 0.001 (plane travel calc equation)
    totalCarbon = np.sum(p) * 90 * 0.001
    # units of calc are metric tons
    return totalCarbon

x = planeCalc(df1)
print (x)

