
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from statistics import mean

def Threshold(array):
    balanceAr=[]
    newAr=array
    for eachRow in array:
        array.setflags(write=1)
        for eachPix in eachRow:
             avg=mean(eachPix[:3])
             balanceAr.append(avg)
    balance=mean(balanceAr)
    for eachRow in newAr:
        for eachPix in eachRow:
            if mean(eachPix[:3]) > balance:
                eachPix[0] = 255
                eachPix[1] = 255
                eachPix[2] = 255
                eachPix[3] = 255
            else:
                eachPix[0] = 0
                eachPix[1] = 0
                eachPix[2] = 0
                eachPix[3] = 255
    return newAr


image1=Image.open("images//numbers//0.1.png","r")
ias1=np.asarray(image1)
image2=Image.open("images//numbers//y0.4.png","r")
ias2=np.asarray(image2)
image3=Image.open("images//numbers//y0.5.png","r")
ias3=np.asarray(image3)
image4=Image.open("images//sentdex.png","r")
ias4=np.asarray(image4)


ias1 = Threshold(ias1)
ias2 = Threshold(ias2)
ias3 = Threshold(ias3)
ias4 = Threshold(ias4)

fig=plt.figure()
ax1=plt.subplot2grid((8,6),(0,0),rowspan=4,colspan=3)
ax2=plt.subplot2grid((8,6),(4,0),rowspan=4,colspan=3)
ax3=plt.subplot2grid((8,6),(0,3),rowspan=4,colspan=3)
ax4=plt.subplot2grid((8,6),(4,3),rowspan=4,colspan=3)

ax1.imshow(ias1)
ax2.imshow(ias2)
ax3.imshow(ias3)
ax4.imshow(ias4)

plt.show()



# plt.imshow(ias)
# plt.show()
# uniq=np.unique(ias,axis=0)


