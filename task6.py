def field_coordinates(x, y):
    if not all(isinstance(i, int) for i in [x, y]):
        raise ValueError("Помилка! Координати повинні бути цілими числами.")
    elif not (1 <= x <= 8) or not (1 <= y <= 8):
       raise ValueError("Помилка! Число повино бути в діапазоні від 1 до 8")
    
    
    if y % 2 != 0 and x % 2 != 0 or x == y:
        print(f"Поле з координатами x = {x}  y = {y} чорне")
    elif x % 2 == 0:
        print(f"Поле з координатами x = {x} y = {y} біле")     
            
try:
    x = 4
    y = 7
    
    field_coordinates(x, y)
except ValueError as e:
    print(e)