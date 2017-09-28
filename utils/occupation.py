import csv
import random

def dictionary():
    dic = {}
    with open('data/occupations.csv') as csvfile:
        rows = csv.reader(csvfile, delimiter = "\n")
        for row in rows:
            tempRow = row[0].rsplit(',',2)
            if(tempRow[1] != "Percentage"):
                dic[tempRow[0]] = (float(tempRow[1]), tempRow[2])
    return dic

def occupationGenerator():
    dic = dictionary()
    randomNum = random.uniform(0, dic["Total"][0])
    
    for key in dic:
        if(key != "Total"):
            randomNum -= dic[key][0]
            if(randomNum < 0):
                return key
