a, operation, b = input("Введите через пробел: Число 1, Операцию (+, -, *, /), Число 2: ").split()
if operation == "+":
    print("Ответ: {0}".format(float(a) + float(b)))
elif operation == "-" :
    print("Ответ: {0}".format(float(a) - float(b)))
elif operation == "*" :
    print("Ответ: {0}".format(float(a) * float(b)))
elif operation == "/" :
    print("Ответ: {0}".format(float(a) / float(b)))
else:
    print("Неверная операция")