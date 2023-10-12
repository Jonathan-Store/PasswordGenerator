import random
import string
characterSet = []
for i in string.ascii_letters:
    characterSet.append(i)

for i in range(0,10):
    characterSet.append(str(i))



passwordArray = []
for i in range(1, random.randint(8,12)):
    passwordArray.append(characterSet[random.randint(1,len(characterSet))])

password = ""
for i in range(len(passwordArray)):
    password = password+passwordArray[i]

print(password)
