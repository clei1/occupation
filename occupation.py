'''
Connie Lei & Lisa Eng
SoftDev pd8
Work #03--Files Occupy Space
2017-09-14
'''

# allows us to import and read a file
import csv
import random

def occupationGenerator():
    # creation of our dictionary
    dic = {}

    with open('occupations.csv') as csvfile:
        rows = csv.reader(csvfile, delimiter = "\n")
   
        for row in rows:
            tempRow = row[0].rsplit(',',1)
            if(tempRow[1] != "Percentage"):
                dic[tempRow[0]] = float(tempRow[1])

    randomNum = random.uniform(0, dic["Total"])
    
    for key in dic:
        if(key != "Total"):
            randomNum -= dic[key]
            if(randomNum < 0):
                return key

print(occupationGenerator())



