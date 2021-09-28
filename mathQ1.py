import math


qInput = []
qInput.append(input("Digite la q1 [number,pot]:"))
qInput.append(input("Digite la q2 [number,pot]:"))

d = math.pow(float(input("Digite la distancia en m:")),2) 

print(d)

potTotal = 9
qFormTotal = 9

for number in qInput:
    resultTemp = str(number).split(",")
    potTotal += float(resultTemp[1])
    qFormTotal *= abs(float(resultTemp[0]))
    print(qFormTotal)

qFormTotal = qFormTotal / d

print(qFormTotal,"x10",potTotal,"N")






