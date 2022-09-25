import pandas as pd
import numpy as np
from scipy import sparse

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


#irishead()
#irisshape()
#iriskey()
#irisinfo()

arr = np.eye(4)
print("Array...\n", arr)

sparse_matrix = sparse.csr_matrix(arr)
print(sparse_matrix)

