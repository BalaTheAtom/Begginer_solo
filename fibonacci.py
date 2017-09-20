class fib():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def fibs(self):
        while(True):
            yield(self.b)
            self.a,self.b=self.b,self.a+self.b
fibInst=fib(0,1)
a=int(input("enter : "))
for i in fibInst.fibs():
    if i > 610:break
    print(i,end=',')

