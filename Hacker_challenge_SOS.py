class sos:
    def __init__(self,inp):
        self.inp=inp.upper()
    def compare(self):
        sting=self.inp
        expect=len(self.inp)//3
        cstring="SOS"*expect
        k=0
        for i in range(len(sting)):
            if(sting[i]!=cstring[i]):
                k+=1
        return (k)
sobject=sos(input("Enter the SOS comparison string"))
print(sobject.compare())