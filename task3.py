def correctness_coordinates(x1, x2, y1, y2):
    if not all(isinstance(i, (int, float)) for i in [x1, x2, y1, y2]):
        raise ValueError("Помилка! Координати повинні бути числами.")
    
    if x1 == x2 or y1 == y2:
        raise ValueError("Помилка! Координати не повмнні бути обнакові.")
    
    width = abs(x2 - x1)
    height = abs(y2 - y1)
    
    s = width * height
    p = 2 * (width + height)
    
    return s, p

try:
    x1 = 2
    x2 = 4
    y1 = -5
    y2 = 8
    
    s, p = correctness_coordinates(x1, x2, y1, y2)
    
    print("Площа: ", s)
    print("Периметр: ", p)
except ValueError as e:
    print(e)
    