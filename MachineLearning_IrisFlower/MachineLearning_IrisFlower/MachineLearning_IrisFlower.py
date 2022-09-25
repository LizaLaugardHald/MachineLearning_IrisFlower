import csv

file = open("C:\\Users\\Andreas\\Documents\\GitHub\\MachineLearning_IrisFlower\\MachineLearning_IrisFlower\\Data\\iris.csv")

type(file)
csvreader = csv.reader(file)

header = []
header = next(csvreader)
print(header)

rows = []
for row in csvreader:
        rows.append(row)
for i in range(0,len(rows)):
    print(str(rows[i]) + '\n')
    

#print(rows + '\n')

file.close()

