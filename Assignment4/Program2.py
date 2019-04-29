import csv
from Program1 import *

with open("Hweights.txt") as f:
    reader=csv.reader(f)
    h=list(reader)

HiddenW=[]

for i in range(len(h)):
    s=h[i][0].split()
    for j in range(len(s)):
        s[j]=float(s[j])
    HiddenW.append(s)



with open("Oweights.txt") as g:
    readerr=csv.reader(g)
    o=list(readerr)

OutputW=[]


for i in range(len(o)):
    s=o[i][0].split()
    for j in range(len(s)):
        s[j]=float(s[j])
    OutputW.append(s)
HiddenWeights=HiddenW
OutputWeights=OutputW

for i in range(len(inputs)):
    f=feedForward(inputs[i])
    O=f[0]
    Segma=outputLayerError(O,outputs[i])
    mse=MSE(Segma)
    print('MSE: ',mse)




