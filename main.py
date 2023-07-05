print("Запуск Програми\n\n")

print("1-Гривні")
print("2-Долари")
print("3-Євро\n")

Money_Type = int(input("Введіть номер валюти: "))
print(" ")

if Money_Type == 1:
    Money = int(input("Введіть суму: "))
    print(" ")
    print("Гривні", Money)
    print("Долари", round(Money/36.9, 2))
    print("євро", round(Money/40.27, 2))
elif Money_Type == 2:
    Money = int(input("Введіть суму: "))
    print(" ")
    print("Гривні", round(Money*36.9, 2))
    print("Долари", Money)
    print("євро", round(Money/1.09, 2))
elif Money_Type == 3:
    Money = int(input("Введіть суму: "))
    print(" ")
    print("Гривні", round(Money*40.27, 2))
    print("Долари", round(Money*1.09, 2))
    print("євро", Money)
else:
    print("Іншого варіанту вибору немає.")