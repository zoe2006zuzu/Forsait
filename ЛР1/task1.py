numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
x = numbers.index(None)
sum = 0
ch = 0
for a in numbers:
    if a is not None:
        sum = sum + a
        ch = ch + 1
srednee = sum/ch
numbers[x] = srednee
print("Измененный список:", numbers)