#import csv
import pandas as pd

def filereader():
    return pd.read_csv("C:\\Users\\Andreas\\Documents\\GitHub\\MachineLearning_IrisFlower\\MachineLearning_IrisFlower\\Data\\iris.csv")


iris = filereader() 

def irishead():
    print(iris.head(3))


def irisshape():
    print(iris.shape)

def iriskey():
    print(iris.keys)

def irisinfo():
    print(iris.info())


irishead()
irisshape()
iriskey()
irisinfo()



