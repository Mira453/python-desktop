import math

def number(N):
    if not isinstance(N, int):
       print("Помилка! Число повинно бути цілим.")
    elif N > 1:
        for i in range(2, int(math.sqrt(N)) + 1):
            if N % i == 0:
                print(f"{N} не є простим числом.")
                return
        print(f"{N} є простим числом.")
    else:
        print("Число менше за 1")
        
N = 56
number(N)
