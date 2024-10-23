import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 

df = pd.read_csv("/Users/aadyaasinghal/Downloads/carbon footprint/website/templates/fake_data.csv")
#pull columns from dataframe
    dates = df["dates"]
    water_use = df["water use"]

    #plot data
    plt.plot(dates, water_use, ".-", color ="#3c9c7d")
    plt.grid(True)
    plt.xlabel("month")
    plt.ylabel("carbon output (metric tons)")
    plt.show()

    plt.savefig("data.png")