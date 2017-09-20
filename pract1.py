
st="APPLE"
def findOccurences(s, ch):
    return [i for i, letter in enumerate(s) if letter == ch]
d=len(st)
times=0
l=[]
b=[0 for x in range(d)]
while(True):
    letter_entered=input("Please enter a char : ").upper()
    times=times+1
    a=list(findOccurences(st,letter_entered))
    for i in range(d):
        if(i in a and not i in l):
            b[i]=st[i]
            l.append(i)
        elif(i not in l):
            b[i]='_'
    if (st == "".join(b)):
        print("you WON !! and the word is {}".format(st))
        print("number of trials: {}".format(times))
        length=len(set(st))
        yourLucK=int((length/times)*100)
        print("your Luck percentage : {}%".format(yourLucK))
        break
    else:
        for i in range(d):
            print(b[i],end='')




