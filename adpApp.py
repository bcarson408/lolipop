from flask import Flask,render_template,url_for,redirect,request
from wtforms import Form, BooleanField, StringField, validators
# from forms import CocktailForm,CocktailForm1,IngredientForm
import json
import os.path as path
# import pdb
from json.decoder import JSONDecodeError
import pandas as pd
from scrapers import fantasypros_data, fantasypros

app = Flask(__name__)
app.config['SECRET_KEY'] = "😀😀@#$%^&*"

# player_stats_dict={}
#




@app.route("/")
def home():
    # return render_template('home.html',old_data=old_data['cocktails'])
    return render_template("base.html")

@app.route("/adp")
def adp():
    data = fantasypros()

    headers = [*data[0]][0:9]
    return render_template('/adp.html',data=fantasypros(), headers = headers )

@app.route("/stat_year/<player>", methods=['GET'])
def stat_year(player):
    data = fantasypros()
    for x in data:
        if x['Player'] == player:
            stat_data = x
            years = [*x][10:]
            # content = { x:y for x,y in stat_data }
            return render_template('/stat_year.html', stats = stat_data ,columns = [*stat_data[years[0]]] ,data1 = x[years[0]] ,  data2 = x[years[1]],data3 = x[years[2]])



@app.route("/rb")
def rb():
    context={}
    return render_template('/rb.html',df=rb_df.values.tolist(),headers=headers)

@app.route("/qb")
def qb():
    context={}
    return render_template('/qb.html',df="player_stats_dict",headers="")


@app.route("/wr")
def wr():
    context={}
    return render_template('/wr.html',df=wr_df.values.tolist(),headers=headers)


@app.route("/by_team")
def by_team():
    # (['Player', 'ESPN', 'RTSports', 'Fantrax', 'FFC']
    groupby = df.groupby(['Team', 'POS','Bye']).first()
    keys_byteam = groupby.to_dict()['Player'].keys()
    values_byteam = groupby.to_dict()['Player'].values()
    return render_template('/by_team.html',
                            k=keys_byteam,
                            headers=df.columns.tolist(),
                            values=values_byteam
                            )

if __name__ == "__main__":
    app.run(debug=True)
