
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


a = input_positive_float("Введіть сторону a ")     
b = input_positive_float("Введіть сторону b ")
s = a * b 
p = 2 * (a + b)

print("Площа прямокутника ", s)
print("Периметр прямокутника ", p)
