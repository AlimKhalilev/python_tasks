def powerOfTwo(n):
    count = 0
    d = 1
    while d <= n:
        count += 1
        d = d * 2
    return count

def getNumber01(num):
    while type:
        getNumber = input('Введите число ' + num + ': ')
        try:
            getTempNumber = int(getNumber)
        except ValueError:
            print('"' + getNumber + '"' + ' - не является числом')
        else:
            break
    return float(getNumber)

a = getNumber01("a")
print(powerOfTwo(a))