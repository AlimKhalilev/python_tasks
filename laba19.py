import itertools

def getNumber01():
    while type:
        getNumber = input('Введите длину строки: ')
        try:
            getTempNumber = int(getNumber)
        except ValueError:
            print('"' + getNumber + '"' + ' - не является числом')
        else:
            break
    return int(getNumber)

myList = []
myLen = getNumber01()
myStr = input("Введите кол-во символов: ")

def intersectionStr(str):
    for i in range(len(str)):
        for j in range(len(myStr)):
            if myStr[j] not in str:
                return False
    return True

for i in itertools.product(myStr, repeat=myLen):
    myList.append("".join(i))

for i in myList:
    if intersectionStr(i):
        print(i, end=" ")
