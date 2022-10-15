import pandas as pd
import numpy as np
from scipy import sparse

#https://www.w3resource.com/machine-learning/scikit-learn/iris/index.php

def FileReader():
    return pd.read_csv("C:\\Users\\Andreas\\Documents\\GitHub\\MachineLearning_IrisFlower\\MachineLearning_IrisFlower\\Data\\iris.csv")


iris = FileReader() 

def IrisHead():
    print(iris.head(3))


def IrisShape():
    print(iris.shape)

def IrisKey():
    print(iris.keys)

def IrisInfo():
    print(iris.info())

def IrisQuantile():
    print(iris.quantile(q=0.5, axis=0, numeric_only=True, interpolation='linear'))

def IrisStandarddeviation():
    print(iris.std())

def IrisMean():
    print(iris.mean())

def IrisDescribe():
    print(iris.describe())

IrisDescribe()

#IrisMean()


#IrisStandarddeviation()

#IrisQuantile()

#irishead()

#iris.quantile(
#    q=0.5,                      # The percentile to calculate
#    axis=0,                     # The axis to calculate the percentile on
#    numeric_only=True,          # To calculate only for numeric columns
#    interpolation='linear'      # The type of interpolation to use when the quantile is between 2 values
#)


#IrisShape()
#IrisKey()
#IrisInfo()

#arr = np.eye(4)
#print("Array...\n", arr)

#sparse_matrix = sparse.csr_matrix(arr)
#print(sparse_matrix)

