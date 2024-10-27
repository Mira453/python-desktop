
def is_valid_name(name):
    if not name.isalpha() :
        print("Ім'я повинно містити тільки літери")
        return False
    return True

def is_valid_surname(surname):
    if not surname.isalpha():
        print("Прізвище повинно містити тільки літери")
        return False
    return True

def is_valid_phone(phone):
    if not phone.isdigit():
        print("Номер телефону повинен містити тільки цифри")
        return False
    return True

def variant1():
    while True:
        name = input("Введіть ім'я: ")
        surname = input("Введіть прізвище: ")
        phone = input("Введіть номер телефону: ")
        
        if not name or not surname or not phone:
                print("Не залишайте жодні поля порожніми")
        elif is_valid_name(name) == True and is_valid_phone(phone) == True and is_valid_surname(surname) == True:
            print("Спасибі")
            break
      
def variant2():
    while True:
        name = input("Введіть ім'я: ")
        surname = input("Введіть прізвище: ")
        phone = input("Введіть номер телефону: ")
        
        if not name and not surname and not phone:
            print("Не залишайте всі поля порожніми")
        elif phone and not is_valid_phone(phone):
            continue
        elif name and not is_valid_name(name):
            continue
        elif surname and not is_valid_surname(surname):
            continue
        else:
            print("Спасибі")
            break
        
def variant3():
    while True:
        name = input("Введіть ім'я: ")
        surname = input("Введіть прізвище: ")
        phone = input("Введіть номер телефону: ")
        
        if not name or not surname:
            print("Не залишайте поля з ім'ям і прізвиськом порожніми")
        elif phone and not is_valid_phone(phone):
            continue
        elif is_valid_name(name) == True and is_valid_surname(surname) == True:
            print("Спасибі")
            break
         
        
variant2()
