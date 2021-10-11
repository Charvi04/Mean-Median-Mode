import csv
from collections import Counter

with open("SOCR-HeightWeight.csv",newline='') as file:
    fileData = csv.reader(file)
    listdata = list(fileData)
listdata.pop(0)

newData = []
for i in range(len(listdata)):
    num1 = listdata[i][1]
    newData.append(float(num1))

total = 0

for i in newData:
    total += i

mean = total/len(newData)
print("Mean of Data : ",mean)

newData.sort()
n = len(newData)

if(n%2 == 0):
    m1 = float(newData[n//2])
    m2 = float(newData[n//2-1])
    median = (m1 + m2)/2
else:
    median = newData[n//2]

print("Median of Data : ",median)

data = Counter(newData)
dataRange = {"50-60":0,"60-70":0,"70-80":0}

for h,o in data.items():
    if (50 < float(h) < 60):
        dataRange["50-60"] += o
    elif(60 < float(h) < 70):
        dataRange["60-70"] += o
    elif(70 < float(h) < 80):
        dataRange["70-80"] += o

mr,mo = 0,0

for r,o in dataRange.items():
    if(o > mo):
        mr,mo = [int(r.split("-")[0]),int(r.split("-")[1])],o

mode = float((mr[0]+mr[1])/2)

print("Mode of Data : ",mode)
