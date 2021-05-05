def bmi(weight, height):
    return weight / ((height/100)**2)

def print_bmi(bmi):
    category = ["Underweight", "Normal weight", "Overweight", "Obesity"]
    print(bmi)
    if bmi < 18.5:
        print(category[0])
    elif ((18.5 <= bmi) and (bmi < 25)):
        print(category[1])
    elif ((25.0 <= bmi) and (bmi < 30)):
        print(category[2])
    elif (30.0 <= bmi):
        print(category[3])

weight, height = [int(x) for x in input("Введите через пробел Вес и Рост: ").split()]
print_bmi(bmi(weight, height))

