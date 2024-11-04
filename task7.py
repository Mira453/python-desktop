
def check_queen_move(x1, y1, x2, y2):
    if not all(isinstance(i, int) for i in [x1, y1, x2, y2]):
        raise ValueError("Помилка! Координати повинні бути цілими числами.")
    elif not (1 <= x1 <= 8 and 1 <= y1 <= 8 and 1 <= x2 <= 8 and 1 <= y2 <= 8):
       raise ValueError("Помилка! Число повино бути в діапазоні від 1 до 8")
    
    if x1 == x2 and y1 == y2:
        return False
    
    if x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
        return True
    
    
try:
    x1 = 4
    x2 = 4
    y1 = 5
    y2 = 7
    
    if check_queen_move(x1, y1, x2, y2):
        print(f"Ферзь за один хід може перейти з поля ({x1}, {y1}) на поле ({x2}, {y2})")
    else:
        print(f"Ферзь не може зробити хід з ({x1}, {y1}) на ({x2}, {y2})")
except ValueError as e:
    print(e)   