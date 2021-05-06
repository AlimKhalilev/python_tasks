def print_factorization(n: int):
    maxprime = 0
    primes = {}
    num = n
    while num > 1:
        for i in range(2, num + 1):
            if num % i == 0:
                num = int(num / i)
                if i > maxprime:
                    maxprime = i
                if i not in primes:
                    primes[i] = 0
                primes[i] += 1
                break
    for p in primes:
        if primes[p] > 1:
            print(p,'^',primes[p],sep='',end='')
        else:
            print(p,end='')
        if p < maxprime:
            print('*',end='')
    print()
print_factorization(int(input("Введите число: ")))