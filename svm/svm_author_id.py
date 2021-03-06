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

#features_train = features_train[:len(features_train)/100]
#labels_train = labels_train[:len(labels_train)/100]

from sklearn.svm import SVC
#clf = SVC(kernel="rbf")

def run_test(clf):
  t0 = time()
  clf.fit(features_train, labels_train)
  print "training time:", round(time()-t0, 3), "s"
  t0 = time()
  accuracy = clf.score(features_test, labels_test)
  print "predicting time:", round(time()-t0, 3), "s"
  print "accuracy:", accuracy
  print "=========================================="

#print "Training with c=10.0"
#run_test(SVC(C=10.0, kernel="rbf"))

#print "Training with c=100.0"
#run_test(SVC(C=100.0, kernel="rbf"))

#print "Training with c=1000.0"
#run_test(SVC(C=1000.0, kernel="rbf"))

print "Training with c=10000.0"
run_test(SVC(C=10000.0, kernel="rbf"))

#########################################################


