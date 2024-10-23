import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import datetime as dt
font = {"fontname": "DM Sans"}


def get_dates(df):
    dfcolumn = df["dates"]
    return dfcolumn

def get_week(date1):
    date1_object= dt.datetime.strptime(date1,"%Y-%m-%d %H:%M:%S.%f")
    return date1_object.isocalendar().week

def get_weeknum(column):
    weeknums = []
    for datestring in column:
        weeknum= get_week(datestring)
        weeknums.append(weeknum)
    return weeknums

def get_uniqueweeks(column):
    '''
    >>> column = [1,1,1,2,3,3]
    >>> get_uniqueweeks(column)
    array([1,2,3])
    '''
    return np.unique(column)

def waterCalc(df):
    # line turns the data frame column into a numpy array
    p = df["water use"].to_numpy()
    # adds up all of water usage nums and divides by 244956 (water calc equation)
    totalCarbon = np.sum(p)/244956
    # units of calc are metric tons
    return totalCarbon

def get_weeklycarbon(df,fcn):
    dates = get_dates(df)
    weeknums = get_weeknum(dates)
    uniqueweeks = get_uniqueweeks(weeknums)
    carbonnum = []
    for week in uniqueweeks:
        df_slice = df[week == weeknums]
        totalCarbon = fcn(df_slice)
        carbonnum.append(totalCarbon)
    return uniqueweeks, np.array(carbonnum)

def gasolineCalc(df):
    p = df["gas usage"].to_numpy()
    totalCarbon = np.sum(p) * 0.008887
    return totalCarbon

def milesDrivenCalc(df):
    p = df["miles driven"].to_numpy()
    totalCarbon = np.sum(p) * 0.000390
    return totalCarbon

def trashCalc(df):
    p = df["trash production"].to_numpy()
    totalCarbon = np.sum(p) * 0.0231
    return totalCarbon

def planeCalc(df):
    p = df["plane travel"].to_numpy()
    totalCarbon = np.sum(p) * 90 * 0.001
    return totalCarbon

def totalCalc(df):
    uniqueweeks, weeklyCarbonTrash = get_weeklycarbon(df, trashCalc)
    uniqueweeks, weeklyCarbonPlane = get_weeklycarbon(df, planeCalc)
    uniqueweeks, weeklyCarbonMiles = get_weeklycarbon(df, milesDrivenCalc)
    uniqueweeks, weeklyCarbonGas = get_weeklycarbon(df, gasolineCalc)
    uniqueweeks, weeklyCarbonWater = get_weeklycarbon(df, waterCalc)
    return uniqueweeks, weeklyCarbonTrash+weeklyCarbonPlane+weeklyCarbonMiles+weeklyCarbonGas+weeklyCarbonWater

def piechart(df):
    plt.clf()
    uniqueweeks, waterCarbon = get_weeklycarbon(df, waterCalc)
    uniqueweeks, gasolineCarbon = get_weeklycarbon(df, gasolineCalc)
    uniqueweeks, milesDrivenCarbon = get_weeklycarbon(df, milesDrivenCalc)
    uniqueweeks, planeCarbon = get_weeklycarbon(df, planeCalc)
    uniqueweeks, trashCarbon = get_weeklycarbon(df, trashCalc)
    waterCarbon = waterCarbon[-1]
    gasolineCarbon = gasolineCarbon[-1]
    milesDrivenCarbon = milesDrivenCarbon[-1]
    planeCarbon = planeCarbon[-1]
    trashCarbon = trashCarbon[-1] 
    graph = np.array([waterCarbon, gasolineCarbon, milesDrivenCarbon, planeCarbon, trashCarbon])
    #percent = graph/np.sum(graph)
    colors = ["#c1d1ff", "#ffa3b8", "#a4d496", "#ffbd59", "#d8ceff"]
    plt.pie(graph, colors=colors, autopct='%1.1f%%', pctdistance=0.85)
    plt.title("Weekly Breakdown")
    centre_circle = plt.Circle((0, 0), 0.40, fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
    plt.savefig("website/static/piechart.png")
    return graph
#piechart(df)
#graph = piechart(df)

def compare(df):
    uniqueweeks, waterCarbon = get_weeklycarbon(df, waterCalc)
    watercarbonNOW = waterCarbon[-1]
    watercarbonLW = waterCarbon[-2]
    WATERpercentUP =  100*((watercarbonNOW - watercarbonLW)/watercarbonNOW)
    WATERdifference = watercarbonNOW - watercarbonLW
    
    uniqueweeks, gasolineCarbon = get_weeklycarbon(df, gasolineCalc)
    gasolinecarbonNOW = gasolineCarbon[-1]
    gasolinecarbonLW = gasolineCarbon[-2]
    GASOLINEpercentUP =  100*((gasolinecarbonNOW - gasolinecarbonLW)/gasolinecarbonNOW)
    GASOLINEdifference = gasolinecarbonNOW - gasolinecarbonLW

    uniqueweeks, milesDrivenCarbon = get_weeklycarbon(df, milesDrivenCalc)
    milesDrivencarbonNOW = milesDrivenCarbon[-1]
    milesDrivenLW = milesDrivenCarbon[-2]
    milesDrivenpercentUP =  100*((milesDrivencarbonNOW - milesDrivenLW)/milesDrivencarbonNOW)
    milesDrivenDifference = milesDrivencarbonNOW - milesDrivenLW

    uniqueweeks, planeCarbon = get_weeklycarbon(df, planeCalc)
    planecarbonNOW = planeCarbon[-1]
    planecaronLW = planeCarbon[-2]
    planecarbonUP =  100*((planecarbonNOW - planecaronLW)/planecarbonNOW)
    planecarbonDifference = planecarbonNOW - planecaronLW

    uniqueweeks, trashCarbon = get_weeklycarbon(df, trashCalc)
    trashcarbonNOW = trashCarbon[-1]
    trashcarbonLW = trashCarbon[-2]
    trashcarbonUP =  100*((trashcarbonNOW - trashcarbonLW)/trashcarbonNOW)
    trashcarbonDifference = trashcarbonNOW - trashcarbonLW

    now = [watercarbonNOW, gasolinecarbonNOW, milesDrivencarbonNOW, planecarbonNOW, trashcarbonNOW]
    percentages = [WATERpercentUP,GASOLINEpercentUP,milesDrivenpercentUP,planecarbonUP,trashcarbonUP]
    differences = [WATERdifference, GASOLINEdifference, milesDrivenDifference, planecarbonDifference, trashcarbonDifference]
    return now, percentages, differences

#def weekly_graph(df):
    #uniqueweeks, weeklyCarbon = get_weeklycarbon(df, waterCalc)
    #plt.plot(uniqueweeks, weeklyCarbon,  "--", color = "#4777ff")
    #uniqueweeks, weeklyCarbon = get_weeklycarbon(df, gasolineCalc)
    #plt.plot(uniqueweeks, weeklyCarbon,  "--", color = "#ff688b")
    #uniqueweeks, weeklyCarbon = get_weeklycarbon(df, milesDrivenCalc)
    #plt.plot(uniqueweeks, weeklyCarbon,  "--", color = "#6eb858")
    #uniqueweeks, weeklyCarbon = get_weeklycarbon(df, planeCalc)
    #plt.plot(uniqueweeks, weeklyCarbon,  "--", color = "#faa11a")
    #uniqueweeks, weeklyCarbon = get_weeklycarbon(df, trashCalc)
    #plt.plot(uniqueweeks, weeklyCarbon,  "--", color = "#a292df")
    #uniqueweeks, weeklyCarbon = totalCalc(df)
    #plt.plot(uniqueweeks, weeklyCarbon,  "-", color = "#ffe142")
    #plt.title("Weekly Comparison")
    #plt.grid(True)
    #plt.xlabel("Week Number")
    #plt.ylabel("Carbon Produced (metric tons)")
    #plt.legend(loc='upper left')
    #plt.savefig("website/static/weeklycarbon.png")
    #print("HELLO WORLD")

def weekly_graph(df):
    # Plot carbon produced from water usage
    uniqueweeks, weeklyCarbon = get_weeklycarbon(df, waterCalc)
    plt.plot(uniqueweeks, weeklyCarbon, "--", color="#4777ff", label="Water Usage (metric tons CO2)")
    
    # Plot carbon produced from gasoline usage
    uniqueweeks, weeklyCarbon = get_weeklycarbon(df, gasolineCalc)
    plt.plot(uniqueweeks, weeklyCarbon, "--", color="#ff688b", label="Gasoline Usage (metric tons CO2)")
    
    # Plot carbon produced from miles driven
    uniqueweeks, weeklyCarbon = get_weeklycarbon(df, milesDrivenCalc)
    plt.plot(uniqueweeks, weeklyCarbon, "--", color="#6eb858", label="Miles Driven (metric tons CO2)")
    
    # Plot carbon produced from air travel
    uniqueweeks, weeklyCarbon = get_weeklycarbon(df, planeCalc)
    plt.plot(uniqueweeks, weeklyCarbon, "--", color="#faa11a", label="Air Travel (metric tons CO2)")
    
    # Plot carbon produced from trash production
    uniqueweeks, weeklyCarbon = get_weeklycarbon(df, trashCalc)
    plt.plot(uniqueweeks, weeklyCarbon, "--", color="#a292df", label="Trash Production (metric tons CO2)")
    
    # Plot total carbon produced
    uniqueweeks, weeklyCarbon = totalCalc(df)
    plt.plot(uniqueweeks, weeklyCarbon, "-", color="#ffe142", label="Total Carbon Produced (metric tons CO2)")
    
    # Set title and labels
    plt.title("Weekly Comparison of Carbon Footprint")
    plt.grid(True)
    plt.xlabel("Week Number")
    plt.ylabel("Carbon Produced (metric tons CO2)")
    
    # Add the legend to the plot
    plt.legend(loc='upper left')

    # Save the plot as an image
    plt.savefig("website/static/weeklycarbon.png")
    print("HELLO WORLD")