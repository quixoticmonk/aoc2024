
def is_valid_sequence(numbers):
    is_increasing = all(numbers[i] < numbers[i+1] for i in range(len(numbers)-1))
    is_decreasing = all(numbers[i] > numbers[i+1] for i in range(len(numbers)-1))
    
    valid_differences = all(1 <= abs(numbers[i] - numbers[i+1]) <= 3 
                          for i in range(len(numbers)-1))
    
    return (is_increasing or is_decreasing) and valid_differences

valid_rows = 0

with open('input.txt', 'r') as file:
    for line in file:
        numbers = list(map(int, line.strip().split()))
        
        if is_valid_sequence(numbers):
            valid_rows += 1
        else:
            print(f"Invalid row: {numbers}")

print(f"Number of valid rows: {valid_rows}")
