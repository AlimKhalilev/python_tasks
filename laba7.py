import math

def getNumber01(num):
    while type:
        getNumber = input('Введите число ' + num + ': ')
        try:
            getTempNumber = int(getNumber)
        except ValueError:
            print('"' + getNumber + '"' + ' - не является числом')
        else:
            break
    return int(getNumber)

s_type = getNumber01("Способ ввода (1 - по сторонам, 2 - по координатам)")
if s_type == 1:
    a = getNumber01("Сторона а")
    b = getNumber01("Сторона b")
    c = getNumber01("Сторона c")

    p = (a + b + c) / 2
    ans = math.sqrt(p * (p-a) * (p-b) * (p-c))
    print('Площадь равна: {0}'.format(ans))
elif s_type == 2:
    x1, y1 = input("Введите через пробел координаты x1, y1: ").split()
    x2, y2 = input("Введите через пробел координаты x2, y2: ").split()
    x3, y3 = input("Введите через пробел координаты x3, y3: ").split()

    ans = abs((int(x2)-int(x1))*(int(y3)-int(y1))-(int(x3)-int(x1))*(int(y2)-int(y1)))/2
    print('Площадь равна: {0}'.format(ans))
else:
    print("Неверный способ ввода")
