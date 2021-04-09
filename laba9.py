def getCleanMin(hh, mm):
    return (int(hh) * 60) + int(mm)

hh1, mm1 = input("Введите первое время в формате hh:mm ").split(":")
hh2, mm2 = input("Введите второе время в формате hh:mm ").split(":")

if int(hh1) < 0 or int(hh1) > 23 or int(mm1) < 0 or int(mm1) > 59:
    print("Неверно введено первое время")
elif int(hh2) < 0 or int(hh2) > 23 or int(mm2) < 0 or int(mm2) > 59:
    print("Неверно введено второе время")
else:
    if getCleanMin(hh2, mm2) - getCleanMin(hh1, mm1) > 15:
        print("Встреча не состоится")
    else:
        print("Встреча состоится")