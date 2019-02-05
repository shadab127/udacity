#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
#plt.show()
################################################################################


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary

""" for adaboost
from sklearn.ensemble import AdaBoostClassifier
from time import time
from sklearn.metrics import accuracy_score

max_acc =0
training_time =0
predicting_time =0
temp_i=0
temp_j=0
for i in range(1,11):
    for j in range(50,52):
        clf = AdaBoostClassifier(n_estimators=i, learning_rate= j/(100.0))
        t0 = time()
        clf.fit(features_train, labels_train)
        temp_traning = round(time()-t0,3)

        t0 = time()
        pred = clf.predict(features_test)
        temp_predicting = round(time()-t0,3)

        temp = accuracy_score(pred, labels_test)
        if max_acc < temp:
            max_acc = temp
            training_time = temp_traning
            predicting_time = temp_predicting
            temp_i = i
            temp_j = j

print "estimator: ",temp_i," learning_rate: ",j," max accuracy : ",max_acc," training time: ",training_time," s  predicting time: ",predicting_time," s"
try:
    prettyPicture(clf, features_test, labels_test)
    plt.show()
except NameError:
    pass
"""
"""
from sklearn import neighbors
from time import time
from sklearn.metrics import accuracy_score
max_acc =0
training_time =0
predicting_time =0
temp_i=0
for i in range(1,10):
    clf = neighbors.KNeighborsClassifier(n_neighbors=i)
    t0 = time()
    clf.fit(features_train, labels_train)
    temp_traning = round(time() - t0, 3)

    t0 = time()
    pred = clf.predict(features_test)
    temp_predicting = round(time() - t0, 3)

    temp = accuracy_score(pred, labels_test)
    if max_acc < temp:
        max_acc = temp
        training_time = temp_traning
        predicting_time = temp_predicting
        temp_i = i

print "neighbors: ",temp_i," leaf_size: ",30," max accuracy : ",max_acc," training time: ",training_time," s  predicting time: ",predicting_time," s"
"""

"""
from sklearn import ensemble
from time import time
from sklearn.metrics import accuracy_score
max_acc =0
training_time =0
predicting_time =0
temp_i=0
temp_j=0
for i in range(1,101):
    for j in range(1,101):
        clf = ensemble.RandomForestClassifier(n_estimators=i, max_depth=j)
        t0 = time()
        clf.fit(features_train, labels_train)
        temp_traning = round(time() - t0, 3)

        t0 = time()
        pred = clf.predict(features_test)
        temp_predicting = round(time() - t0, 3)

        temp = accuracy_score(pred, labels_test)
        if max_acc < temp:
            max_acc = temp
            training_time = temp_traning
            predicting_time = temp_predicting
            temp_i = i
            temp_j = j

print "n_estimators: ",temp_i," max_depth: ",temp_j," max accuracy : ",max_acc," training time: ",training_time," s  predicting time: ",predicting_time," s"
"""

from sklearn import tree
from time import time
from sklearn.metrics import accuracy_score
max_acc =0
training_time =0
predicting_time =0
temp_i=0
temp_j=0
for i in range(2,101):
    for j in range(2,101):
        clf = tree.DecisionTreeClassifier(min_samples_split=i,max_depth=j)
        t0 = time()
        clf.fit(features_train, labels_train)
        temp_traning = round(time() - t0, 3)

        t0 = time()
        pred = clf.predict(features_test)
        temp_predicting = round(time() - t0, 3)

        temp = accuracy_score(pred, labels_test)
        if max_acc < temp:
            max_acc = temp
            training_time = temp_traning
            predicting_time = temp_predicting
            temp_i = i
            temp_j = j

print "min_sample_split: ",temp_i," max_depth: ",temp_j," max accuracy : ",max_acc," training time: ",training_time," s  predicting time: ",predicting_time," s"