from collections import Counter
import csv

with open('heightWeight.csv', newline='') as f:
    reader = csv.reader(f)
    medianList = list(reader)

medianList.pop(0)

heightList = []

for i in range(len(medianList)):
    num = medianList[i][1]
    heightList.append(float(num))

heightList.sort()

listLength = len(heightList)

if listLength%2 == 0:
    median1 = float(heightList[listLength//2])
    median2 = float(heightList[listLength//2 + 1])
    median = (median1 + median2)//2
else:
    median = float(heightList[listLength//2])

print("Median is "+ str(median))