import math
from task1 import input_positive_float

a = input_positive_float("Введіть додатнє число a ")
b = input_positive_float("Введіть додатнє число b ")
    
result = math.sqrt(a * b)
print("Середнє геометричне чисел a і b ", result)
