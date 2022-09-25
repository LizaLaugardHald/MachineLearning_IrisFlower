#import csv
import pandas as pd

file = open("C:\\Users\\Andreas\\Documents\\GitHub\\MachineLearning_IrisFlower\\MachineLearning_IrisFlower\\Data\\iris.csv")

type(file)
csvreader = pd.read_csv(file)
    
print("\nData Type:")
print(type(file))
print(csvreader.head(3))

file.close()

print(csvreader.shape)
print(csvreader.keys)
