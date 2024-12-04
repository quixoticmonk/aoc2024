def find_xmas(grid):
    grid = grid.split("\n")
    rows = len(grid)
    cols = len(grid[0])
    print(rows,cols)
    count=0
    for r in range(rows):
        for c in range(cols):
            if r+2 < rows and c+2 < cols and grid[r][c] == "M" and grid[r+1][c+1] == "A" and grid[r][c+2] == "S" and grid[r+2][c] == "M"  and grid[r+2][c+2] == "S":
                count+=1
                # M . S 
                # . A . 
                # M . S  

            if r+2 < rows and c+2 < cols and grid[r][c] == "S" and grid[r+1][c+1] == "A" and grid[r][c+2] == "M" and grid[r+2][c] == "S"  and grid[r+2][c+2] == "M":
                count+=1
                # S . M 
                # . A . 
                # S . M      
                       
            if r+2 < rows and c+2 < cols and grid[r][c] == "S" and grid[r+1][c+1] == "A" and grid[r][c+2] == "S" and grid[r+2][c] == "M"  and grid[r+2][c+2] == "M":
                count+=1
                # S . S 
                # . A . 
                # M . M                            
            if r+2 < rows and c+2 < cols and grid[r][c] == "M" and grid[r+1][c+1] == "A" and grid[r][c+2] == "M" and grid[r+2][c] == "S"  and grid[r+2][c+2] == "S":
                count+=1
                # M . M 
                # . A . 
                # S . S   
                                               
    return count

answer=0
with open("./input.txt", "r") as file:
    answer+=find_xmas(file.read())

print(answer)