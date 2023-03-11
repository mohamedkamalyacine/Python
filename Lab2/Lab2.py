# ================= Q1 ================= #
"""
import math
radius = 5
circleArea = math.pi * math.pow(radius, 2)
print(circleArea)
"""

# ================= Q2 ================= #
"""
import my_module
message = "Hello, World"
print(my_module.reverseString(message))
"""

# ================= Q3 ================= #
"""
from random import randint
print(randint(1,11))
"""

# ================= Q4 ================= #
"""
from datetime import datetime as dt
print(dt.now())
"""

# ================= Q5 ================= #
"""
currentFile = open("Lab2\example.txt", "r")
totalLinesNum = len(currentFile.readlines())
print("The total number of lines: ", totalLinesNum)
currentFile.close()
"""

# ================= Q6 ================= #
"""
import my_module
currentFile = open("Lab2\example.txt", "r")
fileContent = currentFile.read()
print(my_module.reverseString(fileContent))
currentFile.close()
"""

# ================= Q7 ================= #
"""
currentFile = "Lab2\example.txt"

with open(currentFile, 'r') as file:
   fileContent= file.readlines()
   print([i.rstrip('\n') for i in fileContent])

file.close()
"""

# ================= Q8 ================= #
"""
currentFile = open("Lab2\example.txt", "r")
fileContent = currentFile.read()

newFile = open("newExample.txt", "a")
newFile.write(fileContent)

newFile = open("newExample.txt", "r")
newFileContent = newFile.read()
print(newFileContent)

currentFile.close()
newFile.close()
"""

# ================= Q9 ================= #
"""
currentFile = "Lab2\example.txt"

with open(currentFile, 'r') as file:
    fileWords = file.read().split()

longestWordLength = len(max(fileWords, key=len))
result = [textword for textword in fileWords if len(textword) == longestWordLength]

print(result)
file.close()
"""

# ================= Q10 ================= #
"""
numList = [1, 2, 3, 4, 5, 6, 7 ,8 ,9 ,10, 11, 12, 13, 14, 15]

def getSumEven(data):
    sum = 0
    length = len(numList)
    for i in range(length):
        if data[i] % 2 == 0:
            print(f"{data[i]} ")
            sum += data[i]
    return sum

#sum = getSumEven(numList)
print(f"The Sum of even numbers = {getSumEven(numList)}")
"""

# ================= Q11 ================= #
"""
players = ["Messi", "C.Ronaldo", "M.Salah", "Pedri",
           "Pirlo", "Ronaldinho", "Buffon", "Iniesta"]

def getWordsHaveA(data):
    returnedList = []
    for word in players:
        if "a" in word:
            returnedList.append(word)
    return returnedList


print(f"Wods that contain A --> {getWordsHaveA(players)}")
"""
# ================= Q12 ================= #
"""
myDict = {"_id": 1, "name": "Mohamed", "age": 25}

def swapDictKeyValue(dict = {}):
    print(f"Function recieved ", dict)
    returnedDict = {}
    for key, value in dict.items():
        returnedDict[value] = key
    return returnedDict

print(f"After Swapping: {swapDictKeyValue(myDict)}")
"""

# ================= Q13 ================= #
"""
numbers = [10, 15, 60, -5, 100]

def getMaxMinNums(numList):
    if isinstance(numList, list):
        print(f"Function recieved --> {numList}")
        #y = max(numList)
        #print(y)
        maxMinNums = [max(numList), min(numList)]
        return maxMinNums
    else:
        print("false")

recievedList = getMaxMinNums(numbers)
print(f"MAximum number = {recievedList[0]}")
print(f"Minimum Number = {recievedList[1]}")
"""

# ================= Q14 ================= #
"""
import math

numbers = [10, 15, 60, -5, 100]

def powerTwo(numList):
    if isinstance(numList, list):
        poweredList = []
        print(f"Function recieved --> {numList}")
        for i in numList:
            poweredList.append(math.pow(i, 2))
        
        return poweredList
    else:
        print("false")
        return -1

result = powerTwo(numbers)
print(f"Result --> {result}")
"""
# ================= Q15 ================= #
"""
def mixLists(*args):
    returnedList = []
    for element in args:
        returnedList += element
    
    return returnedList

names = ["Mohamed", "Mostafa", "Ibrahim", "Mai"]
numbs = [100, 200, 300, 400, 500]

print(f'Result --> {mixLists(names, numbs)}')
"""

# ================= Q15 ================= #

txt = "Hello, "

def welcomeMessage(data, **kwargs):
    for v in kwargs.values():
        data += v
    return data

print(f'{welcomeMessage(txt, name = "mohamed ", age = "25")}')