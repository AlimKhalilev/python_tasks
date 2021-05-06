import random
from math import sqrt

def BozoSort(values, asc=True):
    if isinstance(values[0], list):
        temp = []
        for i in values:
            for j in i:
                temp.append(j)
        values = temp

    index1 = random.randint(0, len(values)-1)
    index2 = random.randint(0, len(values)-1)
    while index1 == index2:
        index2 = random.randint(0, len(values)-1)

    values[index1], values[index2] = values[index2], values[index1]

    for i in range(0, len(values)):
        if i >= len(values) - 1:
            return values
        elif asc:
            if values[i] > values[i+1]:
                return BozoSort(values, asc)
        else:
            if values[i] < values[i+1]:
                return BozoSort(values, asc)


def user_input():
    try:
        n = int(input('Введите количество чисел n: '))

        if 4 <= n <= 100:
            numbers = list(map(int, input(f'Введите {n} чисел: ').split(' ')))
            if len(numbers) != n:
                print('Неверное количество чисел')
                raise ValueError

            print(*BozoSort(numbers), sep=' ')
            print(*BozoSort(numbers, False), sep=' ')

            size = int(sqrt(n))
            array = []
            for i in range(0, size):
                array.append(numbers[i*size:(i*size)+size])

            print(*BozoSort(array), sep=' ')
            print(*BozoSort(array, False), sep=' ')

            print(*BozoSort(numbers[0:3]), sep=' ')
            print(*BozoSort(numbers[0:3], False), sep=' ')

        else:
            print('Неверное количество чисел')
            raise ValueError

    except ValueError or TypeError:
        user_input()

user_input()