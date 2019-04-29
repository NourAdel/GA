# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
class Fuzzyset:
    def __init__(self,na,typ, s):
        self.type=typ
        self.numbers=s
        self.setname=na
       

class variable:
    def __init__(self,na,l,n,v):
        self.sets=l
        self.numofsets=n
        self.value=v
        self.name=na


class point:
     def __init__(self,x,y):
         self.x=x
         self.y=y
         
def normalize (n=float, b=bool):
    if b==True:
        p=point(n,1)
    else:
        p=point(n,0)
    return (p)
	
def intersection (p1=point, p2=point,p3=point,p4=point):
    D=(p1.x-p2.x)*(p3.y-p4.y)-(p1.y-p2.y)*(p3.x-p4.x)
    if (D==0):
        return(False)
    pre=(p1.x*p2.y)-(p1.y*p2.x)
    post=(p3.x*p4.y)-(p3.y*p4.x)
    Y=(pre*(p3.y-p4.y)-(p1.y-p2.y)*post)/D
    return (Y)
    
def TriangleFuzzification(ss=Fuzzyset,val=float):
    points=[]
    f=False
    mid=ss.numbers[1]
    for i in range(3):
        p=normalize(ss.numbers[i],f)
        points.append(p)
        f= not f
    Val=normalize(val,False)
    Val1=normalize(val,True)
    if(val<=mid):
        membership=intersection(points[0],points[1],Val,Val1)
    else:
        membership=intersection(points[1],points[2],Val,Val1)    
    print("M of","(", val,")" ,ss.setname," = ", membership)
    return (membership)
        


     
     
         


