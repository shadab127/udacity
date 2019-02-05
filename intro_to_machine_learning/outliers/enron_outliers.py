#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
data_dict.pop('TOTAL')
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)
max_ex = 0
ans = []
min_ex = 99999999
ans_min = []
for x in data_dict:
    if data_dict[x]["salary"] == "NaN":
        continue
    if data_dict[x]["salary"] > max_ex:
        ans = data_dict[x]
        max_ex = data_dict[x]["salary"]
    if data_dict[x]["salary"] < min_ex:
        ans_min = data_dict[x]
        min_ex = data_dict[x]["salary"]

print ans," \n",ans_min
max =0
tempsal = tempbonus = 0
### your code below
for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )
    if(max<salary):
        max = salary
        tempbonus = bonus

print max," ",tempbonus
for temp in data_dict:
    if data_dict[temp]['salary'] == 'NaN':
        continue
    if data_dict[temp]['salary'] >= 1000000 and data_dict[temp]['bonus'] >= 5000000:
        print temp
        print data_dict[temp]
matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()


