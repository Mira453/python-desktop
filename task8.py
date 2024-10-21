def numbers(A, B):
    if not all(isinstance(i, int) for i in [A, B]):
        raise ValueError("Помилка! Координати повинні бути цілими числами.")
    elif B < A:
        raise ValueError("А повинно бути менше за В")
    
    N = 0
    for i in range(A, B + 1):
        print(i)
        N += 1

    print("Кількість чисел", N)
    
try:
    A = 5
    B = 23
    numbers(A, B)   
except ValueError as e:
    print(e) 