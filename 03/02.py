import re


def cal_sum(filename):
    with open(filename, 'r') as file:
        content = file.read()

    pattern = r'mul\((\d+),\s*(\d+)\)'
    matches = list(re.finditer(pattern, content))
    
    if not matches:
        return 0
        
    total_sum = 0
    
    for i, match in enumerate(matches):
        num1 = int(match.group(1))
        num2 = int(match.group(2))
        product = num1 * num2
        
        if i == 0:
            total_sum += product
            continue
        
        text_before = content[:match.start()]
        last_do = text_before.rfind('do()')
        last_dont = text_before.rfind("don't()")
        
        if last_do == -1 and last_dont == -1:
            total_sum += product
        else:
            if last_do > last_dont:
                total_sum += product
            elif last_dont > last_do:
                continue
            # If only one instruction exists
            elif last_do != -1:
                total_sum += product
    
    return total_sum
        

result = cal_sum("input.txt" )
print(result)
