even_squares = []
for i in range(10):
    if i % 2 == 0:
        even_squares.append(i ** 2)
print(even_squares)

even_squares = [i ** 2 for i in range(10) if i % 2 == 0]
print(even_squares)