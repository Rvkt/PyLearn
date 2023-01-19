square = []
square_even = []

for i in range(10):
    square.append(i * i)
    if i % 2 == 0:
        square_even.append(i * i)

print(square)
print(square_even)

square = [i * i for i in range(10)]
square_even = [i * i for i in range(10) if i % 2 == 0]
print(square)
print(*square)
