import time
from collections import Counter
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from statistics import mean

def Whatnumisthis(filepath):
    matchedAr=[]
    loadExamps=open('images//numArEx.txt','r').read()
    loadExamps=loadExamps.split('\n')
    i=Image.open(filepath)
    iar=np.asarray(i)
    iarl=iar.tolist()
    inquest=str(iarl)
    for eachExample in loadExamps:
        if len(eachExample)>2:
            splitEx=eachExample.split("::")
            currntNum=splitEx[0]
            curntAr=splitEx[1]
            eachPixEx = curntAr.split('],')
            eachPixInQ = inquest.split('],')
            x = 0

            while(x<len(eachPixEx)):
                if(eachPixEx[x]==eachPixInQ[x]):
                    try:
                        matchedAr.append(int(currntNum))
                    except:
                        matchedAr.append((currntNum))

                x+=1


    return Counter(matchedAr)
path='images//1.png'
a=Whatnumisthis(path)
print(a)
print("the number you have in the image is :" +str(max(a,key=a.get)))
a=input("is it correct")
if(a=='n' or a=='N'):
    print("what is the correct value")
    crct=input()
    numberArrayExamples = open('C:\\Users\\balaswamy\\PycharmProjects\\pythonLearnings\\MachineLearning\\images\\numArEx.txt', 'a')
    ei = Image.open(path)
    eiar = np.array(ei)
    eiarl = str(eiar.tolist())
    lineToWrite = str(crct) + '::' + eiarl + '\n'
    numberArrayExamples.write(lineToWrite)
    numberArrayExamples.close()
else:
    print("your Welcome")
