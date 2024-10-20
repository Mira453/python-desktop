a = input("Введіть ціле число: ")

while True:  
    try:
        a = int(a)  
        break  
    except ValueError:
        a = input("Помилка! Спробуйте ще раз: ")  
if a % 2 == 0:
    print("Число парне")
else:
    print("Число непарвне")