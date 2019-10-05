import csv

xList = []
yList = []
file = open(r"C:\Users\user\Desktop\Fire.txt")
reader = csv.reader(file)
for row in reader:
    xList.append(float(row[0]))
    yList.append(float(row[1]))
file.close()



xMin = xMax = xList[0]
yMin = yMax = yList[0]
tSum = 0

def method_name():
    return xMin

for val in xList:
    if val < xMin:
        xMin = val
        tSum += val
print(" x Minimuma:" + str(+xMin))

def method_name():
    return xMax

for val in xList:
 if val > xMax:
     xMax = val
     tSum += val
print(" x Maximuma:" + str(+xMax))

def method_name():
    return yMin

for val in yList:
    if val < yMin:
        yMin = val
        tSum += val
print(" y Minimuma:" + str(+yMin))

def method_name():
    return yMax

for val in yList:
    if val > yMax:
        yMax = val
        tSum += val
print(" y Maximuma:" + str(+yMax))

def method_name():
    return kerület

seged = (xMin + yMin)
kerület = 2 * seged
print ("Kerület:" + str(kerület))

def method_name():
    return terület

terület = (yMax* xMax)
print ("Terület:" + str(terület))


  