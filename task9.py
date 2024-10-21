def reverse_number(N):
    reversed_number = 0
    
    if not isinstance(N, int):
        raise ValueError("Помилка! Число повинно бути цілим.")
    
    while N > 0:
        last_digit = N % 10
        reversed_number = reversed_number * 10 + last_digit
        N = N // 10 
    return reversed_number

try:
    N = 78909
    print("Перевернуте число: ", reverse_number(N))
except ValueError as e:
    print(e)