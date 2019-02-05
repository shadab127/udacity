#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
countSal =0
countEmail=0
for x in enron_data:
    if enron_data[x]['salary'] == 'NaN' :
        countSal +=1
    if enron_data[x]['email_address'] == 'NaN':
        countEmail +=1
        print enron_data[x]
print len(enron_data)-countSal," ",len(enron_data)-countEmail

lines = [line.rstrip('\n') for line in open("../final_project/poi_names.txt", "r")]
for line in lines:
    print line

print len(lines)
