import pprint as pp
import time 

class Solution:

    @staticmethod
    def elaborateinput(matrix: list[list[int]]):
        Solution.partialSum = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]
        Solution.partialSum[0][0] = matrix[0][0]

        rows = len(matrix)
        cols = len(matrix[0])

        for r in range(1, rows):
            Solution.partialSum[r][0] = matrix[r][0] + Solution.partialSum[r-1][0]
        
        for c in range(1, cols):
            Solution.partialSum[0][c] = matrix[0][c] + Solution.partialSum[0][c-1]

        for r in range(1, rows):
            for c in range(1, cols):
                Solution.partialSum[r][c] = matrix[r][c] + Solution.partialSum[r][c-1] + Solution.partialSum[r-1][c] - Solution.partialSum[r-1][c-1]
        
        
    @staticmethod
    def computeSolution(row1: int, col1: int, row2: int, col2: int) -> int:
        return Solution.partialSum[row2][col2] - (Solution.partialSum[row2][col1-1] + Solution.partialSum[row1-1][col2]) + Solution.partialSum[row1-1][col1-1]
    
    # @staticmethod
    # def solve(matrix: list[list[int]], squares: list[list[int,int,int,int]]) -> list[int]:
    #     returnList = []
    #     for row1, col1, row2, col2 in squares:
    #         value = 0
    #         for j in range(row1, row2 + 1):
    #             for i in range(col1, col2 + 1):
    #                 value += matrix[j][i]
    #         returnList.append(value)
    #     return returnList
    
    @staticmethod
    def solve(matrix: list[list[int]], squares: list[list[int,int,int,int]]) -> list[int]:
        Solution.elaborateinput(matrix)
        listToReturn = []
        for square in squares:
            row1, col1, row2, col2 = square
            listToReturn.append(Solution.computeSolution(row1, col1, row2, col2))
        return listToReturn

    @staticmethod
    def loadInput():
        with open('4/testcase.txt', 'r') as file:
            matrix = []
            squares = []
            for i, line in enumerate(file):
                if i == 0:
                    j = int(line.strip())
                elif i <= j:
                    matrix.append(list(map(int,line.strip().split(','))))
                elif i > j:
                    squares.append(list(map(int,line.strip().split(','))))
        return matrix, squares
    
    @staticmethod
    def loadOutput():
        with open("4/output.txt", 'r') as file:
            for line in file:
                list = line.strip().split(',')
                for i in range(len(list)):
                    list[i] = int(list[i])
        return list
    
    @staticmethod
    def writeOutput(list):
        with open("4/output.txt", 'w') as file:
            list = str(list)
            file.write(list[1:-1])
        return
                

sol = Solution()
#x = sol.solve([[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]],[[2,1,4,3],[1,1,2,2],[1,2,2,4]])
matrix, squares = sol.loadInput()

start = time.time()

x = sol.solve(matrix, squares)

print(time.time() - start)

sol.writeOutput(x)

y = sol.loadOutput()

if x == y:
    print('ok')
else:
    print('no')



