from collections import Counter
import csv

with open('heightWeight.csv', newline='') as f:
    reader = csv.reader(f)
    meanList = list(reader)

meanList.pop(0)

heightList = []

for i in range(len(meanList)):
    num = meanList[i][1]
    heightList.append(float(num))

findlength = len(heightList)
total = 0

for i in heightList:
    total = total + i

mean = total/findlength

print("Mean is " + str(mean))