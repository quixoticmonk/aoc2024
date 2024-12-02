first_numbers = []
second_numbers = []

with open('a.txt', 'r') as file:
    for line in file:
        num1, num2 = map(int, line.strip().split())
        first_numbers.append(num1)
        second_numbers.append(num2)

first_numbers.sort()
second_numbers.sort()

frequency = {}
for num in second_numbers:
    frequency[num] = frequency.get(num, 0) + 1

total = 0
for num in first_numbers:
    total += num * frequency.get(num, 0)

print(f"Final sum: {total}")
