red = [1, 3, 5, 7, 9, 12, 14, 16, 18,  19, 21, 23, 25, 27, 30, 32, 34, 36]
black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]

redStr = [str(i) for i in red]
blackStr = [str(i) for i in black]

countRed = 0
countBlack = 0

myDict = {}
tableNumbers = []
uniqueNumbers = []

for i in range(0,37):
    tableNumbers.append(str(i))

def getNumber01():
    while type:
        getNumber = input('')
        try:
            getTempNumber = int(getNumber)
        except ValueError:
            print('"' + getNumber + '"' + ' - не является числом')
        else:
            break
    return int(getNumber)

def putToDict(num):
    if myDict.get(num) == None:
        myDict[num] = 1
    else:
        myDict[num] += 1

def getMaxKeyFromDict():
    sortKeyArr = sorted(myDict, key=myDict.get)
    return " ".join(sortKeyArr)

def getCleanTable():
    sortKeyArr = sorted(myDict, key=myDict.get)
    sortKeyArrInt = [int(i) for i in sortKeyArr]
    tableNumbersInt = [int(i) for i in tableNumbers]
    newList = list(set(tableNumbersInt) - set(sortKeyArrInt))
    newListStr = [str(i) for i in newList]
    return " ".join(newListStr)

game = True

while game:
    a = getNumber01()
    putToDict(str(a)) # пополнить словарь значениями

    if str(a) in blackStr:
        countBlack += 1
    elif str(a) in redStr:
        countRed += 1

    print(getMaxKeyFromDict())
    print(getCleanTable())
    print(str(countRed) + " " + str(countBlack))

    if a == -1:
        game = False
