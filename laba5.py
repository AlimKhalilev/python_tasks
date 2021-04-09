def getNumber01(num):
    while type:
        getNumber = input('Введите число ' + num + ': ')
        try:
            getTempNumber = float(getNumber)
        except ValueError:
            print('"' + getNumber + '"' + ' - не является числом')
        else:
            break
    return float(getNumber)


x0 = getNumber01("x0") #  float(input("Число x0: "))
v0 = getNumber01("v0") #
t = getNumber01("t")
a = g = 9.81

answer = x0 + v0*t - 1/2*a*t*t  #a*t*t / 2
print(answer)