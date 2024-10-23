from flask import Blueprint, render_template, request, flash, redirect, url_for, sessions
import pandas as pd
from werkzeug.security import generate_password_hash, check_password_hash
import matplotlib.pyplot as plt
import datetime as dt
from tables import *

def add_row(df1, df2):
    y = pd.concat([df1, df2])
    return y

def graph(column, lower_limit, higer_limit):
    plt.switch_backend('Agg')
    user_data = pd.read_csv("user_data.csv")
    single_col= user_data[column]
    #begin plot, search on google hex code for more colors
    plt.plot(single_col, ".--", markersize = 15, color="green")
    #add upper and lower limits to y-axis
    
    plt.ylabel("CO2 Produced [metric tons]")
    plt.title(column)
    plt.ylim(lower_limit, higer_limit)
    #save graph to image folder
    plt.savefig("website/static/styles/images/" + column + ".png", dpi = 200)


# tells flask to add a authorization pg
views = Blueprint("views", __name__)

@views.route("/home" , methods = ["GET","POST"])
def home():
    print ("Hello")
    return render_template("home.html")

@views.route("/stats" , methods = ["GET","POST"])
def stats():
    df = pd.read_csv("user_data.csv")
    weekly_graph(df)
    piechart(df)
    now,percentages, differences = compare(df)
    water_usage='{0:.3f}'.format(now[0])
    water_pie = water_usage
    gas_usage = '{0:.2f}'.format(now[1])
    gas_pie = gas_usage
    miles_driven = '{0:.2f}'.format(now[2])
    miles_pie = miles_driven
    airplane_hours = '{0:.2f}'.format(now[3])
    airplane_pie = airplane_hours
    trash_production = '{0:.2f}'.format(now[4])
    trash_pie = trash_production
    water_increase = '{0:.2f}'.format(percentages[0])
    gas_increase = '{0:.2f}'.format(percentages[1])
    miles_increase = '{0:.2f}'.format(percentages[2])
    airplane_increase = '{0:.2f}'.format(percentages[3])
    trash_increase = '{0:.2f}'.format(percentages[4])
    water_change = '{0:.3f}'.format(differences[0])
    gas_change = '{0:.2f}'.format(differences[1])
    miles_change = '{0:.2f}'.format(differences[2])
    airplane_change = '{0:.2f}'.format(differences[3])
    trash_change = '{0:.2f}'.format(differences[4])
    bignumber = now[0] + now[1] + now[2] + now[3] + now[4]
    bignumber = '{0:.2f}'.format(bignumber)
    return render_template("stats.html",
                        water_usage = water_usage,
                        gas_usage = gas_usage,
                        miles_driven = miles_driven,
                        airplane_hours = airplane_hours,
                        trash_production = trash_production,
                        water_increase = water_increase,
                        gas_increase = gas_increase,
                        miles_increase = miles_increase,
                        airplane_increase = airplane_increase,
                        trash_increase = trash_increase,
                        water_change = water_change,
                        gas_change = gas_change,
                        miles_change = miles_change,
                        airplane_change = airplane_change,
                        trash_change = trash_change,
                        water_pie = water_usage,
                        gas_pie = gas_usage,
                        miles_pie = miles_driven,
                        airplane_pie = airplane_hours,
                        trash_pie = trash_production,
                        bignumber = bignumber,
                        )


@views.route("/take-action" , methods = ["GET","POST"])
def take_action():
    return render_template("takeaction.html")

@views.route("/about" , methods = ["GET","POST"])
def about():
    return render_template("about.html")

@views.route("/sign_up" , methods = ["GET","POST"])
def sign_up():
    return render_template("sign_up.html")


@views.route("/calculator", methods = ["GET","POST"])
def calculator():
    if request.method == "POST": 
        water = request.form.get("water-use")
        gasoline = request.form.get("gas-use")
        miles_driven = request.form.get("miles-driven")
        trash = request.form.get("trash-production")
        plane = request.form.get("airplane-hours")
        date = str(dt.datetime.now())
        print(f"Received data - Water: {water}, Gasoline: {gasoline}, Miles Driven: {miles_driven}, Trash: {trash}, Plane: {plane}")

        data = {
        "dates": [date],
        "water use": [float(water)],
        "gas usage": [float(gasoline)],
        "miles driven": [float(miles_driven)], 
        "trash production": [float(trash)],
        "plane travel": [float(plane)],                                                    
        }

        df2 = pd.DataFrame(data)
        df1 = pd.read_csv("user_data.csv", index_col = "dates")
        df2.set_index("dates", inplace = True)
        df = add_row(df1, df2)
        df.to_csv("user_data.csv", mode='w',header=True)
        
        return render_template("stats.html")

    return render_template("calculator.html")
