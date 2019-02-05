#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###

#########################################################
from sklearn import svm
from sklearn.metrics import accuracy_score
clf = svm.SVC(C=10000,kernel='rbf')
features_train = features_train[:len(features_train)/1]
labels_train = labels_train[:len(labels_train)/1]
t0=time()
clf.fit(features_train,labels_train)
print "traning time ",time()-t0, " s"
t0=time()
pred = clf.predict(features_test)
print "predicting time ",time()-t0," s"

count = 0
sara = 0
for p in pred:
    if p == 1:
        count +=1
    else:
        sara +=1
print "prediction 10,26,50 ",pred[10]," ",pred[26]," and ",pred[50]
print "chris count: ",count," sara count: ",sara

print accuracy_score(pred,labels_test)

