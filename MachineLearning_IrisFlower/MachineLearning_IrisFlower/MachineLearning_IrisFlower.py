#import csv
import pandas as pd

file = open("C:\\Users\\Andreas\\Documents\\GitHub\\MachineLearning_IrisFlower\\MachineLearning_IrisFlower\\Data\\iris.csv")

type(file)
csvreader = pd.read_csv(file)

#header = []
#header = next(csvreader)
#print(header)

#rows = []
#for row in csvreader:
#        rows.append(row)
#for i in range(0,len(rows)):
#    print(str(rows[i]) + '\n')
    
print("\nData Type:")
print(type(file))
print(csvreader.head(3))

file.close()