n = input("Введите кол-во чисел: ")
inp = input("Введите " + n + " чисел через пробел: ").split(' ')
numbers = []

for strNum in inp:
    num = int(strNum)
    index = len(numbers)
    for i in range(len(numbers)):
        if numbers[i] < num:
            index = i
            break
    numbers.insert(index, num)
    if len(numbers) > 5:
        numbers = numbers[1:6]
    
    for number in numbers:
        print(number, end=' ')
    print()