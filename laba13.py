def isPrime(n):
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return d * d > n and "Простое" or "Составное"

def getNumber01(num):
    while type:
        getNumber = input('Введите число для проверки на простоту ' + num + ': ')
        try:
            getTempNumber = int(getNumber)
        except ValueError:
            print('"' + getNumber + '"' + ' - не является числом')
        else:
            break
    return float(getNumber)

a = getNumber01("a")
print(isPrime(a))
