from flask import Flask, render_template
import csv
import random

my_app = Flask(__name__)

@my_app.route('/')
def root():
    return "Hi everybody!"

def dictionary():
    dic = {}
    with open('occupations.csv') as csvfile:
        rows = csv.reader(csvfile, delimiter = "\n")
        for row in rows:
            tempRow = row[0].rsplit(',',1)
            if(tempRow[1] != "Percentage"):
                dic[tempRow[0]] = float(tempRow[1])
    return dic

def occupationGenerator():
    dic = dictionary()
    randomNum = random.uniform(0, dic["Total"])
    
    for key in dic:
        if(key != "Total"):
            randomNum -= dic[key]
            if(randomNum < 0):
                return key

@my_app.route('/occupations')
def occupations():
    return render_template('template.html', title="Occupations Generator", descriptive_heading="Occupations Generator", collection = dictionary(), l = len(dictionary()), occupation = occupationGenerator())

if __name__ == '__main__':
    my_app.debug = True;
    my_app.run()
