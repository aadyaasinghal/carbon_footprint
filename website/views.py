from flask import Blueprint, render_template, request, flash, redirect, url_for, sessions
import pandas as pd
from werkzeug.security import generate_password_hash, check_password_hash
import matplotlib.pyplot as plt

def add_row(df1, df2):
    y = pd.concat([df1, df2])
    return y

def graph(column, lower_limit, higer_limit):
    plt.ioff()
    user_data = pd.read_csv("user_data.csv")
    single_col= user_data[column]
    #begin plot, search on google hex code for more colors
    plt.plot(single_col, ".--", markersize = 15, color="green")
    #add upper and lower limits to y-axis
    
    plt.ylabel("CO2 Produced [metric tons]")
    plt.title(column)
    plt.ylim(lower_limit, higer_limit)
    #save graph to image folder
    plt.savefig("website/static/images/" + column + ".png", dpi = 200)


# tells flask to add a authorization pg
views = Blueprint("views", __name__)

@views.route("/home" , methods = ["GET","POST"])
def home():
    return render_template("home.html")

@views.route("/stats" , methods = ["GET","POST"])
def stats():
    df = pd.read_csv("user_data.csv", index_col = "miles driven")
    row = df[-1]
    total = sum(row)
    print ("TEST", total)
    return render_template("stats.html", total=total)

@views.route("/take-action" , methods = ["GET","POST"])
def take_action():
    return render_template("take action.html")


@views.route("/calculator", methods = ["GET","POST"])
def calculator():
    if request.method == "POST": 
        water = request.form.get("water")
        gasoline = request.form.get("gasoline")
        miles_driven = request.form.get("miles driven")
        trash = request.form.get("trash")
        plane = request.form.get("plane")
        
        data = {
        "miles driven": [miles_driven], 
        "water use": [water],
        "plane travel": [plane],
        "trash production": [trash],
        "gas usage": [gasoline], 
        }

        df2 = pd.DataFrame(data)
        df1 = pd.read_csv("user_data.csv", index_col = "water use")
        df2.set_index("water use", inplace = True)
        df = add_row(df1, df2)
        df.to_csv("user_data.csv")

        graph("water use", 0, 750 )
        graph("gas usage", 0, 30)
        graph("miles driven", 0, 300)
        graph("trash production", 0, 5)
        graph("plane travel", 0, 40)

    return render_template("calculator.html")
