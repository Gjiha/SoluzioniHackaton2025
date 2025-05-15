import os
import pprint as pp

class Solution:

    inputFolder = os.path.join('soluzioni', 'input', '3')
    outputFolder = os.path.join('soluzioni', 'output', '3')

    @staticmethod
    def solve(matrix: list[list[int]], k: int, start: str) -> int:
        
        Solution.visited = set()
        matrix = Solution.ElaborateInput(matrix)
        n = len(matrix)
        m = len(matrix[0])

        valueToReturn = 0

        for r in range(1,n-1):
            for c in range(1,m-1):
                if matrix[r][c] == start:
                    valueToReturn += Solution.CountUp(matrix, r, c, k)
                    valueToReturn += Solution.CountDown(matrix, r, c, k)
                    valueToReturn += Solution.CountRight(matrix, r, c, k)
                    valueToReturn += Solution.CountLeft(matrix, r, c, k)
                    valueToReturn += Solution.CountUpRight(matrix, r, c, k)
                    valueToReturn += Solution.CountUpLeft(matrix, r, c, k)
                    valueToReturn += Solution.CountDownLeft(matrix, r, c, k)
                    valueToReturn += Solution.CountDownRight(matrix, r, c, k)
        
        return valueToReturn
    
    @staticmethod
    def ElaborateInput(matrix: list[list[str]]) -> list[list[str]]:
        
        n = len(matrix)
        m = len(matrix[0])

        matrix.insert(0, ['#']* (m))
        matrix.append(['#'] * (m))
        n += 2
        for i in range(n):
            matrix[i].insert(0,'#')
            matrix[i].append('#')
        
        return matrix
                    
    @staticmethod
    def CountUp(matrix: list[list[int]], r: int, c: int, k: int) -> bool:
        listToControl = []
        i = 0
        while i < k and matrix[r-i][c] != '#':
            listToControl.append(matrix[r-i][c])
            i += 1
        if len(listToControl) == k:
            string = "".join(listToControl)
            if string == string[::-1] and (r, c) not in Solution.visited:
                Solution.visited.add((r - (k - 1), c))
                return True
        return False
    
    @staticmethod
    def CountDown(matrix: list[list[int]], r: int, c: int, k: int) -> bool:
        listToControl = []
        i = 0
        while i < k and matrix[r+i][c] != '#':
            listToControl.append(matrix[r+i][c])
            i += 1
        if len(listToControl) == k:
            string = "".join(listToControl)
            if string == string[::-1] and (r, c) not in Solution.visited:
                Solution.visited.add((r + (k - 1), c))
                return True
        return False
    
    @staticmethod
    def CountLeft(matrix: list[list[int]], r: int, c: int, k: int) -> bool:
        listToControl = []
        i = 0
        while i < k and matrix[r][c-i] != '#':
            listToControl.append(matrix[r][c-i])
            i += 1
        if len(listToControl) == k:
            string = "".join(listToControl)
            if string == string[::-1] and (r, c) not in Solution.visited:
                Solution.visited.add((r, c - (k - 1)))
                return True
        return False
    
    @staticmethod
    def CountRight(matrix: list[list[int]], r: int, c: int, k: int) -> bool:
        listToControl = []
        i = 0
        while i < k and matrix[r][c+i] != '#':
            listToControl.append(matrix[r][c+i])
            i += 1
        if len(listToControl) == k:
            string = "".join(listToControl)
            if string == string[::-1] and (r, c) not in Solution.visited:
                Solution.visited.add((r, c + (k - 1)))
                return True
        return False
    
    @staticmethod
    def CountUpRight(matrix: list[list[int]], r: int, c: int, k: int) -> bool:
        listToControl = []
        i = 0
        while i < k and matrix[r-i][c+i] != '#':
            listToControl.append(matrix[r-i][c+i])
            i += 1
        if len(listToControl) == k:
            string = "".join(listToControl)
            if string == string[::-1] and (r, c) not in Solution.visited:
                Solution.visited.add((r - (k - 1), c + (k - 1)))
                return True
        return False
    
    @staticmethod
    def CountUpLeft(matrix: list[list[int]], r: int, c: int, k: int) -> bool:
        listToControl = []
        i = 0
        while i < k and matrix[r-i][c-i] != '#':
            listToControl.append(matrix[r-i][c-i])
            i += 1
        if len(listToControl) == k:
            string = "".join(listToControl)
            if string == string[::-1] and (r, c) not in Solution.visited:
                Solution.visited.add((r - (k - 1), c - (k - 1)))
                return True
        return False
    
    @staticmethod
    def CountDownRight(matrix: list[list[int]], r: int, c: int, k: int) -> bool:
        listToControl = []
        i = 0
        while i < k and matrix[r+i][c+i] != '#':
            listToControl.append(matrix[r+i][c+i])
            i += 1
        if len(listToControl) == k:
            string = "".join(listToControl)
            if string == string[::-1] and (r, c) not in Solution.visited:
                Solution.visited.add((r + (k - 1), c + (k - 1)))
                return True
        return False
    
    @staticmethod
    def CountDownLeft(matrix: list[list[int]], r: int, c: int, k: int) -> bool:
        listToControl = []
        i = 0
        while i < k and matrix[r+i][c-i] != '#':
            listToControl.append(matrix[r+i][c-i])
            i += 1
        if len(listToControl) == k:
            string = "".join(listToControl)
            if string == string[::-1] and (r, c) not in Solution.visited:
                Solution.visited.add((r + (k - 1), c - (k - 1)))
                return True
        return False
        

    @staticmethod
    def loadInput(i: int) -> str:
        files = os.listdir(Solution.inputFolder)
        files.sort()

        matrix = []
        with open(os.path.join(Solution.inputFolder, files[i])) as file:
            for i, line in enumerate(file):
                if i == 0:
                    len, key = line.strip().split(',')
                else:    
                    newLine = []
                    for char in line.strip():
                        newLine.append(char)
                    matrix.append(newLine)
        return matrix, int(len), key
    

    @staticmethod
    def loadOutput(i: int) -> int:
        files = os.listdir(Solution.outputFolder)
        files.sort()

        with open(os.path.join(Solution.outputFolder, files[i])) as file:
            value = ''
            for line in file:
                value += line.strip()
        return int(value)     
