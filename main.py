import math

def input_positive_float(numeric):
    while True:
        user_number = input(numeric)
        try: 
            value = float(user_number)
            if value > 0:
                return value
            else:
                print("Помилка! Число повинно бути додатним")
        except ValueError:
            print("Помилка! Введіть число.") 



def task(number):
    while True:
        number_function = input("Оберіть номер фінкції від 1 до 16 ", number)
        try:
            value = float(number_function)
            if value >= 0 and value < 17:
                return value
            else:
                print("Оберіть коректне число ")
        except ValueError:
            print("Помилка! Введіть число.")

if task() == 1:
    a = input_positive_float("Введіть сторону a ")     
    b = input_positive_float("Введіть сторону b ")
    s = a * b 
    p = 2 * (a + b)

    print("Площа прямокутника ", s)
    print("Периметр прямокутника ", p)
elif task() == 2:
    a = input_positive_float("Введіть додатнє число a ")
    b = input_positive_float("Введіть додатнє число b ")
    
    result = math.sqrt(a * b)
    print("Середнє геометричне чисел a і b ", result)