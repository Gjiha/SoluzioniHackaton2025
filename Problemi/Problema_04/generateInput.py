import random as rd
import pprint as pp

def generateMatrix(row: int, col: int) -> list[list[int]]:
    matrix = []
    for _ in range(row):
        newLine = [str(rd.randint(0, 100)) for _ in range(col)]
        matrix.append(newLine)
    return matrix

def generateSquare(row: int, col: int, number: int) -> list[list[int,int,int,int]]:
    squares = []
    for _ in range(number):
        row1 = rd.randint(0, row - 2)
        col1 = rd.randint(0, col - 2)
        row2 = rd.randint(row1+1, row-1)
        col2 = rd.randint(col1+1, col-1)
        squares.append([row1, col1, row2, col2])
    return squares

x = generateMatrix(1500,1500)
y = generateSquare(1500, 1500, 1250)

with open("4/testcase.txt", "w") as file:
    file.write(str(len(x)) + '\n')
    for riga in x:
        string = ','.join(str(x) for x in riga)
        file.write(string + '\n')
    for riga in y:
        string = ','.join(str(x) for x in riga)
        file.write(string + '\n')


# pp.pprint(x)
# pp.pprint(y)