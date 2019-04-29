import csv
import copy
import math
import random
import pickle

with open("train.txt") as f:
    reader=csv.reader(f)
    train=list(reader)

inputs=[]
outputs=[]

Nodes=train[0][0].split()
DataSetLen=int(train[1][0].split()[0])


m=int(Nodes[0])
l=int(Nodes[1])
n=int(Nodes[2])

numofNodes = []
numofNodes.append(m)
numofNodes.append(l)
numofNodes.append(n)

max=-1.0
for i in range(DataSetLen):

    tem=train[i+2][0].split()
    inp=tem[:m]
    oup=tem[m:]
    for i in range(len(inp)):
        if (float(inp[i])>float(max)):
            max=inp[i]
    for i in range(len(oup)):
        if (float(oup[i])>float(max)):
            max=oup[i]
    inputs.append(inp)
    outputs.append(oup)
    i+=1

#Normalization
for i in range(len(inputs)):
    for j in range(len(inputs[i])):
        tem=float(inputs[i][j])
        tem2=tem/float(max)
        inputs[i][j]=tem2
    for j in range(len(outputs[i])):
        tem=float(outputs[i][j])
        tem2=tem/float(max)
        outputs[i][j]=tem2

def generateRandom(numOfNodes):
    Hweights = []
    for i in range (numofNodes[0]):
        Node=[]
        for j in range (numofNodes[1]):
            x=random.uniform(-5,5)
            Node.append(x)
        Hweights.append(Node)
    return Hweights

HiddenWeights=generateRandom(numofNodes)

def generateRandomo(numOfNodes):
    Oweights = []
    for i in range (numofNodes[1]):
        Node=[]
        for j in range (numofNodes[2]):
            x=random.uniform(-5,5)
            Node.append(x)
        Oweights.append(Node)
    return Oweights

OutputWeights=generateRandomo(numofNodes)

def calcNet(inputVector, Nodesweights,num):
    net = []
    count = 0
    for i in range(num):
        temp = 0
        for j in range(len(inputVector)):
            temp += float(inputVector[j])*Nodesweights[j][count]
        if (count+1 < num):
            count += 1
        net.append(temp)
    return net

def activationFun(net):
    I = []
    for i in range (len(net)):
        try:
            I.append(1 / (1 + math.exp(-net[i])))
        except OverflowError:
            I.append(float('inf'))
    return I
def feedForward(inputVector):
    net = calcNet(inputVector, HiddenWeights,l)
    H = activationFun(net)
    net = calcNet(H, OutputWeights,n)
    O = activationFun(net)
    return O,H

def outputLayerError(O,actualoutputlist):
    Segma=[]
    for i in range(len(O)):
        tem=actualoutputlist[i]-O[i]
        Segma.append(tem)
    return Segma

def Snode (Segma,O):
    SN=[]
    for i in range(len(Segma)):
        tem=O[i]*(1-O[i])*Segma[i]
        SN.append(tem)
    return SN

def UpdateOutputWeights(Sn,I):
    k=0
    j=0
    while(k<numofNodes[2]):
        while(j<numofNodes[1]):
            tem= OutputWeights[j][k]+(0.3*Sn[k]*I[j])
            OutputWeights[j][k]=tem
            j+=1
        k+=1

def SHnode (segma,I,outputWeights,l):
    SHN=[]
    for j in range (l):
        s=0
        for k in range(len(segma)):
            s+=segma[k]*outputWeights[j][k]
        tem=I[j]*(1-I[j])*s
        SHN.append(tem)
    return SHN

def UpdateHiddenWeights(SHN,inputvector,l):
    for i in range(len(inputvector)):
        for j in range(l):
            tem=HiddenWeights[i][j]+(0.3*SHN[j]*inputvector[i])
            HiddenWeights[i][j]=tem


def MSE (segma):
    s=0
    for i in range(len(segma)):
        sum=pow(segma[i],2)
        s+=sum
    return (s/2)

for i in range (500):
    for Iteration in range(DataSetLen):
        F=feedForward(inputs[Iteration])
        I=F[1]
        O=F[0]
        s=outputLayerError(O,outputs[Iteration])
        snode=Snode(outputs[Iteration],s)
        UpdateOutputWeights(snode,I)
        shn=SHnode(s,I,OutputWeights,numofNodes[1])
        UpdateHiddenWeights(shn,inputs[Iteration],numofNodes[1])
        mse=MSE(s)
        if mse <= 0.002:
            print("MSE: ",float(mse))
            break
    if mse <= 0.002:
        break
    if i==499:
        print("MSE: ",float(mse))




with open("Hweights.txt",'w') as f:
    for l in range(len(HiddenWeights)):
        for j in range(len(HiddenWeights[l])):
            f.write(str(HiddenWeights[l][j]))
            f.write(" ")

        f.write('\n')
with open("Oweights.txt",'w') as f:
   for l in range(len(OutputWeights)):
        for j in range(len(OutputWeights[l])):
            f.write(str(OutputWeights[l][j]))
            f.write(" ")

        f.write('\n')















