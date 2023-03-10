# ================= Q1 ================= #
"""
def reverseString(txt):
    # print("The recieved string is", txt)
    return txt[::-1]
text = reverseString("kamal")
print(text)
"""

# ================= Q2 ================= #

print("Enter first number")
firstNum = input()
print("Enter second number")
secondNum = input()

def calculator(x,y):
    print(f'sum = {x+y}')
    print(f'sub = {x-y}')
    print(f'Multiplication = {x*y}')
    print(f'Division = {x/y}')
    print(f'Quotient = {x%y}')

calculator(int(firstNum), int(secondNum))


# ================= Q3 ================= #
"""
x = [10, 15, 60, -5, 100]

def getMaxNum(numList):
    if isinstance(numList, list):
        print("Ok")
        print(numList)
        y = max(numList)
        #print(y)
        return y
    else:
        print("false")

maximumNum = getMaxNum(x)
print("the maximum number is ", maximumNum)
"""

# ================= Q4 ================= #
"""
def askUserAge(age):
    if age >= 18:
        print("You are old enough to vote")
    else:
        print("You are too young to vote")

askUserAge(10)
"""

# ================= Q5 ================= #
"""
myList = ["Mohamed", "Abdelrahman", "ali", "Hany"]
def getLongestStr(strList):
    return max(strList, key=len)

longestStr = getLongestStr(myList)
print(longestStr)
"""

# ================= Q6 ================= #
"""
print("Enter a number")
num = input()
num = int(num)

if num > 0:
    print("positive number")
elif num < 0:
    print("negative number")
elif num == 0:
    print("zero")
"""

# ================= Q7 ================= #
"""
vowels = 'aeiou'

#global countVowels
countVowels = 0
txt = "Kamal"

def getVowelsNum(string):
    length = len(string)
    global countVowels
    
    for i in range(length):
        if string[i] in vowels:
            countVowels += 1
        
    return countVowels

x = getVowelsNum(txt)

print("number of vowels are ", x)
"""
# ================= Q8 ================= #
"""
print("enter a sentence")
sentence = input()
print(sentence.upper())
"""

# ================= Q9 ================= #
"""
numList = [1, 2, 3, 4, 5, 6, 7 ,8 ,9 ,10, 11, 12, 13, 14, 15]

def getEven(data):
    returnList = []
    length = len(numList)
    for i in range(length):
        if data[i] % 2 == 0:
            returnList.append(data[i])
            # print(data[i])
    return returnList

newList = getEven(numList)
print(newList)
"""

# ================= Q10 ================= #
"""
stringList = ["Ahmed", "Mina", "Yousef", "Ibrahem", "Mohamed", "Hesham"]
stringList.sort()
print(stringList)
"""