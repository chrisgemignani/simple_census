import csv
from pymongo import Connection

connection = Connection()
db = connection["census"]
collection = db.collection

if collection.count() == 0:

    year1 = "2000"
    year2 = "2008"
    d = { year1: {}, year2: {} }


    def get_age_range(num):
        if num <= 10:
            return "10"
        elif num <= 20:
            return "20"
        elif num <= 30:
            return "30"
        elif num <= 40:
            return "40"
        elif num <= 50:
            return "50"
        elif num <= 60:
            return "60"
        elif num <= 70:
            return "70"
        else:
            return "80"

    with open("data/census.csv", 'rb') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',') 

        #skip the column headers
        csvreader.next()

        for row in csvreader:

            state = row[0]
            sex = row[1]
            age = get_age_range(int(row[2]))
            pop1 = int(row[3])
            pop2 = int(row[4])

            if state not in d[year1]:
                d[year1][state] = {
                    "10": {"M": 0, "F": 0},
                    "20": {"M": 0, "F": 0},
                    "30": {"M": 0, "F": 0},
                    "40": {"M": 0, "F": 0},
                    "50": {"M": 0, "F": 0},
                    "60": {"M": 0, "F": 0},
                    "70": {"M": 0, "F": 0},
                    "80": {"M": 0, "F": 0},
                }
                d[year2][state] = {
                    "10": {"M": 0, "F": 0},
                    "20": {"M": 0, "F": 0},
                    "30": {"M": 0, "F": 0},
                    "40": {"M": 0, "F": 0},
                    "50": {"M": 0, "F": 0},
                    "60": {"M": 0, "F": 0},
                    "70": {"M": 0, "F": 0},
                    "80": {"M": 0, "F": 0},
                }

            d[year1][state][age][sex] += pop1
            d[year2][state][age][sex] += pop2

    collection.insert(d)

"""
data format to be returned:
    {
        "2000": {
            "alabama": {
              "10": {
                "M": 0
                "F": 0
              },
              ...
              "80": {
                ...
              }
            },
            ...
            "tennessee": {
              ...
            }
            ...
        },
        "2008": {
            ...
        }
    }

"""
