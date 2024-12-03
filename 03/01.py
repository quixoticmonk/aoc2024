import re

def cal_sum(filename):
    total_sum = 0
    pattern = r'mul\((\d+),\s*(\d+)\)'
    
    with open(filename, 'r') as file:
        content = file.read()
        
        matches = re.finditer(pattern, content)
        
        for match in matches:
            num1 = int(match.group(1))
            num2 = int(match.group(2))
            product = num1 * num2
            total_sum += product
    return total_sum

result = cal_sum("input.txt")
print(f"Sum of all products: {result}")