a = input("Введіть ціле число a ")
b = input("Введіть ціле число b ")
c = input("Введіть ціле число c ")

while True:  
    try:
        a = int(a)
        b = int(b)
        c = int(c)  
        break  
    except ValueError:
        print("Помилка! Спробуйте ще раз: ")
        a = input("Введіть ціле число a ")
        b = input("Введіть ціле число b ")
        c = input("Введіть ціле число c ")
        
if a<b<c:
    print("Висловлювання a<b<c правдиве.")
else:
    print("Висловлювання a<b<c неправдиве")
    
if a > 0 or b > 0 or c > 0:
    print("Одне з цих чисел додатне")
else:
    print("Немає додатніх чисел")
    
if (a > 0) + (b > 0) + (c > 0) == 1:
    print("Рівно одне з цих чисел додатне")
else:
    print("Не рівно одне з цих чисел додатне")