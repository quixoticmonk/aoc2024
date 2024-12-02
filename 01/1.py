first_numbers = []
second_numbers = []

with open('a.txt', 'r') as file:
    for line in file:
        num1, num2 = map(int, line.strip().split())
        first_numbers.append(num1)
        second_numbers.append(num2)

first_numbers.sort()
second_numbers.sort()

differences = []
for x, y in zip(first_numbers, second_numbers):
    diff = abs(x - y)
    differences.append(diff)

total_sum = sum(differences)
print(f"Sum of differences: {total_sum}")
