import random

answers = ["Загаданное число больше", "Загаданное число меньше", "Поздравляю! Вы угадали"]

def game(userNum, randNum):
    if (userNum < randNum):
        answer = 0
    elif (userNum > randNum):
        answer = 1
    else:
        answer = 2
    print(answers[answer])
    return answer

def getNumber01(count):
    while type:
        getNumber = input('Попытка № {0}. Введите загаданное число: '.format(count+1))
        try:
            getTempNumber = int(getNumber)
        except ValueError:
            print('"' + getNumber + '"' + ' - не является числом')
        else:
            break
    return float(getNumber)

process = True
while process:

    i = 0
    cnt = 5
    randNum = random.randint(0, 50)

    while cnt > i:
        a = getNumber01(i)
        res = game(a, randNum)
        i += 1
        if res == 2:
            break
        elif i == cnt and res != 2:
            print("Вы проиграли! Было задано число: {0}".format(randNum))

    again = input("Хотите начать сначала? (1 - ДА ): ")
    if again != "1":
        process = False

