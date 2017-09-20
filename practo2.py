print("guess letter program ")
count = 0
word = []
correctword = "EVAPORATE"
clue = list("_"*(len(correctword)))
length = 0
while(True):
letter = input("guess letter ").upper()
count = count + 1
if ( letter in word):
print("it is already guessed ")
elif (letter in correctword):
print("you guessed correctly")
length = length + 1
word.append(letter)
for i in range(len(correctword)):
if(correctword[i] == letter):
clue[i] = letter
print("".join(clue))

else:
print("incorrect guessed ")
if(length == len(set(correctword))):
print("successfully guessed")
print("total count is ", count)
break