def square(x):
    return x * x


def apply_twice(func, value):
    return func(value)

print(apply_twice(square, 3))   # square(square(3)) = 81
print("mamasein migad")