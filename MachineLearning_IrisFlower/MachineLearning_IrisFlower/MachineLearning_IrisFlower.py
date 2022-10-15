import pandas as pd
import numpy as np
from scipy import sparse

#https://www.w3resource.com/machine-learning/scikit-learn/iris/index.php
#Jeg kom til Step 1 i "Visualization - Iris flower data set [16 exercises with solution]"

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

def ObservationsSpecies():
    setosa = 0
    versicolor = 0
    virginica = 0
    for x, row in iris.iterrows():
        if row['Species'] == "Iris-setosa":
            setosa = setosa +1
        elif row["Species"] == "Iris-versicolor":
            versicolor = versicolor +1
        elif row["Species"] == "Iris-virginica":
            virginica = virginica +1
        else: 
            print("An erros has occured!")
    print("Observations of each species:")
    print("Amount of setosa = " + str(setosa)) 
    print("Amount of versicolor = " + str(versicolor)) 
    print("Amount of virginica = " + str(virginica))

def NewDataframe():
    print("Original Data:")
    print(iris.head())
    new_irisdata = iris.drop('Id',axis=1)
    print("After removing id column:")
    print(new_irisdata.head()) 

def AccessCells():
    print("Original Data:")
    print(iris.head())
    new_irisdata = iris.drop('Id',axis=1)
    print("After removing id column:")
    print(new_irisdata.head()) 
    x = iris.iloc[:, [1, 2, 3, 4]].values
    print(x) 

AccessCells()

#NewDataframe()


#ObservationsSpecies()         

#IrisDescribe()



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

