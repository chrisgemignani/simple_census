import csv


"""
TODO: use DictReader

csvfile = csv.DictReader(open("../data/CENSUS_STATEAGESEX.csv"))

and .split(",")
"""

data = {}

def get_age_range(num): 
    if num <= 10:
        return 10
    else if num <= 20:
        return 20
    else if num <= 30:
        return 30
    else if num <= 40:
        return 40
    else if num <= 50:
        return 50
    else if num <= 60:
        return 60
    else if num <= 70:
        return 70
    else return 80

with open("../data/CENSUS_STATEAGESEX.csv", 'rb') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',') 
    for row in csvreader:

        age = get_age_range(row[2])

        if row[0] in data:
            data[row0][str(age)] += 

        else:
            data[row[0]] = {
                "10": {"male": 0, "female": 0},
                "20": {"male": 0, "female": 0},
                "30": {"male": 0, "female": 0},
                "40": {"male": 0, "female": 0},
                "50": {"male": 0, "female": 0},
                "60": {"male": 0, "female": 0},
                "70": {"male": 0, "female": 0},
                "80": {"male": 0, "female": 0},
            }
