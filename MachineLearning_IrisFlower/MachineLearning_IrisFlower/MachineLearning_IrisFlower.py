import csv

file = open("C:\\Users\\Andreas\\Documents\\GitHub\\MachineLearning_IrisFlower\\MachineLearning_IrisFlower\\Data\\iris.csv")

type(file)
csvreader = csv.reader(file)

header = []
header = next(csvreader)
print(header)