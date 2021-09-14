from flask import Flask,render_template,url_for,redirect,request
import json
import os.path as path
from json.decoder import JSONDecodeError


app = Flask(__name__)
app.config['SECRET_KEY'] = "😀😀@#$%^&*"


with open("../cocktails.json",'r') as read_file:
    try:
        old_data = json.load(read_file)
    except JSONDecodeError:
        print("failed")
        old_data =  {'cocktails':[]}


def open_json():
    with open("../cocktails.json",'r') as read_file:
        try:
            old_data = json.load(read_file)
        except JSONDecodeError:
            print("failed")
            old_data =  {'cocktails':[]}
    return old_data


@app.route("/")
def home():
    # return render_template('home.html',old_data=old_data['cocktails'])
    return render_template("base.html")

def write_json(formdata):
    with open("../cocktails.json",'w') as read_file:
        try:
            json.dump(formdata,read_file,indent = 2)
        except JSONDecodeError:
            pass

@app.route("/cocktail",methods=['GET', 'POST'])
def cocktail():
    form = CocktailForm(request.form)
    if request.method =="POST":
        old_data = open_json()
        form.data['submit']=""
        old_data['cocktails'].append(form.data)
        # write_json(old_data['cocktails'])
        return render_template('results.html',form=form,form_data=form.data,od=old_data)
    else:
        return render_template('form.html',form=form)

@app.route("/cocktail1",methods=['GET', 'POST'])
def cocktail1():
    form = CocktailForm1(request.form)
    f1 = IngredientForm()
    if request.method =="POST":
        old_data = open_json()
        form.data['submit']=""
        old_data.append(form.data)
        write_json(old_data)
        return render_template('results1.html',form=form,form_data=form.data,od=old_data)
    else:
        return render_template('form1.html',form=form)


@app.route("/cocktail_listing")
def cocktail_listing():
    with open("../cocktails.json",'r') as read_file:
        try:
            old_data = json.load(read_file)
        except JSONDecodeError:
            print("failed")
            old_data =  {'cocktails':[]}
    return render_template('/cocktail-listing.html',data=old_data)


# @app.route("/input", methods=["POST","GET"])
# def input():
#     if request.method == "POST":
#         drink = request.form.to_dict()
#         return redirect(url_for("new_drink",d=drink['Cocktail-Name']    ))
#     else:
#         return render_template("input.html")

# @app.route("/<d>",methods=["POST","GET"])
# def new_drink(d):
#         return f"<h1>{d.cocktail.data}</h1>"



@app.route("/<cocktail>",methods=["POST","GET"])
def about(cocktail):
    # return render_template('/cocktail.html',data=cocktail)
    with open("../cocktails.json",'r') as read_file:
        try:
            old_data = json.load(read_file)
        except JSONDecodeError:
            print("failed")
            old_data =  {'cocktails':[]}
    for drink in old_data:
        if drink["name"] == cocktail:
            return render_template('/cocktail.html',data=drink)


@app.route("/delete/<cocktail>", methods=["POST","GET"])
def delete(cocktail):
    open_data = open_json()
    num_of_cocktails = len(open_data)
    count = 0
    for drink in old_data:
        if drink['name'] == cocktail:
            del old_data[count]
            count+=1
            write_json(old_data)
            return render_template('/cocktail-listing.html',data=old_data,cocktail=drink,count=count)
    return render_template('/test.html',data=old_data[count]['name'],number=drink['name'])

@app.route("/update/<cocktail>", methods=["POST","GET"])
def update(cocktail):
    open_data = open_json()
    form = CocktailForm(request.form)
    num_of_cocktails = len(old_data['cocktails'])
    count = 0
    for drink in old_data['cocktails']:
        if drink["name"] == cocktail:
            old_data['cocktails'][count]
            count+=1
            # write_json(old_data)
            return render_template('form.html',form=old_data['cocktails'][0])





if __name__ == "__main__":
    app.run(debug=True)
