a=int(input("enter"))
x,y,z=1,1,1
while(a>y):
    x,y,z=y,x+y,z+1
if(abs(x-a)>abs(a-y)):
    z,x=z+1,y
print("{} is the nearest fibonacci {}th in the fibonacci list".format(x,z) )
