def function(x, y, z):
    numerator = y**3

    denominator = z + z**2 + (z + y**2)

    a = x + (numerator / denominator)
    print("Результат функції: ", a)

x = 4
y = -0.8
z = -5
function(x, y, z)