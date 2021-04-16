import re

def getNumber01():
    while type:
        getNumber = input('Введите кол-во номеров: ')
        try:
            getTempNumber = int(getNumber)
        except ValueError:
            print('"' + getNumber + '"' + ' - не является числом')
        else:
            break
    return float(getNumber)

isFound = False
a = getNumber01()
tickets = input("Введите {0} номеров билетов через пробел: ".format("a")).split()

for ticket in tickets:
    match = re.search(r'a.{3}55661', ticket)
    if match:
        print(match.group())
        isFound = True

if not isFound:
    print(-1)