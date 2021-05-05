def getNumber01(text):
    while type:
        getNumber = input(text)
        try:
            getTempNumber = int(getNumber)
        except ValueError:
            print('"' + getNumber + '"' + ' - не является числом')
        else:
            break
    return int(getNumber)

def sortByPriceAndLitres(alcohol):
    return alcohol.get('price') / alcohol.get('litres')

alcoholList = []
money = getNumber01('Введите кол-во денег: ')
drinkCount = getNumber01('Введите кол-во доступного алкоголя: ')

alcoholName = ""
alcoholBotles = 0
alcoholLitres = 0

while drinkCount:
    drinkCount -= 1
    name, price, litres = input("Введите [Название алкоголя, стоимость, кол-во] через пробел: ").split()
    alcoholList.append({"name": name, "price": int(price), "litres": int(litres)})
    #print(alcoholList)

alcoholList.sort(key=sortByPriceAndLitres) # сортируем по коэф. цены и литров (сначала самые дешевые)

if (money >= alcoholList[0]["price"]):
    alcoholName = alcoholList[0]["name"] # 1 элемент массива это тот алкоголь, который нам нужен
    alcoholPrice = alcoholList[0]["price"]
    while ((money - alcoholPrice) > 0):
        money -= alcoholPrice
        alcoholLitres += alcoholList[0]["litres"]
        alcoholBotles += 1
    print(alcoholName + " " + str(alcoholBotles))
    print(alcoholLitres)
    print(money)
else:
    print(-1)
