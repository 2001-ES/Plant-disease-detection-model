import numpy as np
import pandas as pd
import cv2
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

def classify():
    # Reading CSV files and preparing training and test datasets
    dataf = pd.read_csv("Datasetinfectedhealthy.csv")
    
    # Extract features and labels from the dataset
    X = dataf.drop(['imgid', 'fold num'], axis=1)
    y = X['label']
    X = X.drop('label', axis=1)
    
    print("\nTraining dataset:-\n")
    print(X)
    
    # Reading the latest unlabeled log data
    log = pd.read_csv("datasetlog/Datasetunlabelledlog.csv")
    log = log.tail(1)
    X_ul = log.drop(['imgid', 'fold num'], axis=1)
    
    print("\nTest dataset:-\n")
    print(X_ul)
    
    print("\n*To terminate press (q)*")
    
    # Variable to store sum of predictions
    Sum = 0
    
    # Train-test splitting and model training using GaussianNB
    for n in range(4):
        x_train, Xi_test, y_train, yi_test = train_test_split(X, y, test_size=0.52, random_state=60)
        if cv2.waitKey(1) == ord('q' or 'Q'): 
            break
        classifier = GaussianNB()
        classifier.fit(x_train, y_train)
        pred = classifier.predict(X_ul)
        Sum += pred
        print(pred)

    # Averaging predictions over the 4 iterations
    final_prediction = int(Sum / 4)
    print("\nPrediction: %d" % final_prediction)

    if final_prediction < 2:
        print("The leaf is sufficiently healthy!")
    else:
        print("The leaf is infected!")
    
    print("\nKeypress on any image window to terminate")
    cv2.waitKey(0)
