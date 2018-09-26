"""	Написать программу, начинающуюся со строки вида n = <целое число>.
Программа должна найти и напечатать все простые
числа, которые меньше n. Простые числа — это натуральные числа,
имеющие ровно два делителя (единица и само число)."""

n = 100
simple_numbers = []

for x in range(2, n):
    for each in simple_numbers:
        if x % each == 0:
            break
    else:
        simple_numbers.append(x)

print(simple_numbers)