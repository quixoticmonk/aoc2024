def find_xmas(grid):
    grid = grid.split("\n")
    rows = len(grid)
    cols = len(grid[0])
    print(rows,cols)
    count=0
    for r in range(rows):
        for c in range(cols):
            if c+3 < cols and grid[r][c] == "X"  and grid[r][c+1] == "M" and grid[r][c+2] == "A" and grid[r][c+3] == "S" :
                count+=1 
                # X M A S
                # . . . .
                # . . . . 
                # . . . .
            if c+3 < cols and  grid[r][c] == "S"  and grid[r][c+1] == "A" and grid[r][c+2] == "M" and grid[r][c+3] == "X" :
                count+=1
                # S A M X
                # . . . .
                # . . . . 
                # . . . .                    
            if r+3 < rows and grid[r][c] == "X"  and grid[r+1][c] == "M" and grid[r+2][c] == "A" and grid[r+3][c] == "S" :
                count+=1 
                # X . . .
                # M . . .
                # A . . .
                # S . . .

            if r+3 < rows and grid[r][c] == "S" and grid[r+1][c] == "A" and grid[r+2][c] == "M" and grid[r+3][c] == "X":
                count+=1
                # S . . .
                # A . . .
                # M . . .
                # X . . .

            if r+3 < rows and c+3 < cols and grid[r][c] == "X" and grid[r+1][c+1] == "M" and grid[r+2][c+2] == "A" and grid[r+3][c+3] == "S" :
                count+=1
                # X . . .
                # . M . .
                # . . A . 
                # . . . S

            if 0<=r-3 and c+3 < cols and grid[r][c] == "S" and grid[r-1][c+1] == "A" and grid[r-2][c+2] == "M" and grid[r-3][c+3] == "X" :
                count+=1
                # . . . X
                # . . M .
                # . A . . 
                # S . . .                
            if r+3 < rows and c+3 < cols and grid[r][c] == "S" and grid[r+1][c+1] == "A" and grid[r+2][c+2] == "M" and grid[r+3][c+3] == "X" :
                count+=1
                # S . . .
                # . A . .
                # . . M . 
                # . . . X                
            if 0<=r-3 and c+3<cols and grid[r][c] == "X" and grid[r-1][c+1] == "M" and grid[r-2][c+2] == "A" and grid[r-3][c+3] == "S" :
                count+=1       
                # . . . S
                # . . A .
                # . M . . 
                # X . . .                             
    
    return count

answer=0
with open("./input.txt", "r") as file:
    answer+=find_xmas(file.read())

print(answer)