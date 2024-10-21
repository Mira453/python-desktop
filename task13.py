
def is_valid_name(name, surname):
    if not name.isalpha() or not surname.isalpha():
        print("Ім'я та прізвище повинно містити тільки літери")
        return False
    return True

def is_valid_phone(phone):
    if not phone.isdigit():
        print("Номер телефону повинен містити тільки цифри")
        return False
    return True

def forma1():
    while True:
        name = input("Введіть ім'я: ")
        surname = input("Введіть прізвище: ")
        phone = input("Введіть номер телефону: ")
        if is_valid_name(name, surname) == True and is_valid_phone(phone) == True:
        
            if not name or not surname or not phone:
                print("Не залишайте жодні поля порожніми")
            else:
                print("Спасибі")
                break
        else:
            print("Спробуйте ще раз.")
        
forma1()