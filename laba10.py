s, l1, r1, l2, r2 = [int(x) for x in input("Введите число и два диапазона чисел через пробел: ").split()]
mySum = l1 + r2

if (mySum == s):
    print(str(l1) + " " + str(r2))
elif (s > mySum):
    if ((mySum - s) + l1 >= l1) and ((mySum - s) + l1 <= r1):
        print(str(mySum) + " " + str(r2))
    else:
        print(-1)
elif (s < mySum):
    if (r2 - (mySum - s) >= l2) and (r2 - (mySum - s) <= r2):
        print(str(l1) + " " + str(mySum))
    else:
        print(-1)
 