import pprint as pp
import random as rd
import time

class Solution():

    def ElaborateInput(self, matrix: list[list[str]]) -> list[list[str]]:
        
        n = len(matrix)
        m = len(matrix[0])

        matrix.insert(0, ['#']* (m))
        matrix.append(['#'] * (m))
        n += 2
        for i in range(n):
            matrix[i].insert(0,'#')
            matrix[i].append('#')
        
        return matrix


    def Esecution(self, matrix: list[list[int]], k: int, digit: str) -> int:
        
        self.visited = set()
        matrix = self.ElaborateInput(matrix)
        n = len(matrix)
        m = len(matrix[0])

        valueToReturn = 0

        for r in range(1,n-1):
            for c in range(1,m-1):
                if matrix[r][c] == digit:
                    valueToReturn += self.CountUp(matrix, r, c, k)
                    valueToReturn += self.CountDown(matrix, r, c, k)
                    valueToReturn += self.CountRight(matrix, r, c, k)
                    valueToReturn += self.CountLeft(matrix, r, c, k)
                    valueToReturn += self.CountUpRight(matrix, r, c, k)
                    valueToReturn += self.CountUpLeft(matrix, r, c, k)
                    valueToReturn += self.CountDownLeft(matrix, r, c, k)
                    valueToReturn += self.CountDownRight(matrix, r, c, k)
        
        return valueToReturn
                    

    def CountUp(self, matrix: list[list[int]], r: int, c: int, k: int) -> bool:
        listToControl = []
        i = 0
        while i < k and matrix[r-i][c] != '#':
            listToControl.append(matrix[r-i][c])
            i += 1
        if len(listToControl) == k:
            string = "".join(listToControl)
            if string == string[::-1] and (r, c) not in self.visited:
                self.visited.add((r - (k - 1), c))
                return True
        return False
    
    def CountDown(self, matrix: list[list[int]], r: int, c: int, k: int) -> bool:
        listToControl = []
        i = 0
        while i < k and matrix[r+i][c] != '#':
            listToControl.append(matrix[r+i][c])
            i += 1
        if len(listToControl) == k:
            string = "".join(listToControl)
            if string == string[::-1] and (r, c) not in self.visited:
                self.visited.add((r + (k - 1), c))
                return True
        return False
    
    def CountLeft(self, matrix: list[list[int]], r: int, c: int, k: int) -> bool:
        listToControl = []
        i = 0
        while i < k and matrix[r][c-i] != '#':
            listToControl.append(matrix[r][c-i])
            i += 1
        if len(listToControl) == k:
            string = "".join(listToControl)
            if string == string[::-1] and (r, c) not in self.visited:
                self.visited.add((r, c - (k - 1)))
                return True
        return False
    
    def CountRight(self, matrix: list[list[int]], r: int, c: int, k: int) -> bool:
        listToControl = []
        i = 0
        while i < k and matrix[r][c+i] != '#':
            listToControl.append(matrix[r][c+i])
            i += 1
        if len(listToControl) == k:
            string = "".join(listToControl)
            if string == string[::-1] and (r, c) not in self.visited:
                self.visited.add((r, c + (k - 1)))
                return True
        return False
    
    def CountUpRight(self, matrix: list[list[int]], r: int, c: int, k: int) -> bool:
        listToControl = []
        i = 0
        while i < k and matrix[r-i][c+i] != '#':
            listToControl.append(matrix[r-i][c+i])
            i += 1
        if len(listToControl) == k:
            string = "".join(listToControl)
            if string == string[::-1] and (r, c) not in self.visited:
                self.visited.add((r - (k - 1), c + (k - 1)))
                return True
        return False
    
    def CountUpLeft(self, matrix: list[list[int]], r: int, c: int, k: int) -> bool:
        listToControl = []
        i = 0
        while i < k and matrix[r-i][c-i] != '#':
            listToControl.append(matrix[r-i][c-i])
            i += 1
        if len(listToControl) == k:
            string = "".join(listToControl)
            if string == string[::-1] and (r, c) not in self.visited:
                self.visited.add((r - (k - 1), c - (k - 1)))
                return True
        return False
    
    def CountDownRight(self, matrix: list[list[int]], r: int, c: int, k: int) -> bool:
        listToControl = []
        i = 0
        while i < k and matrix[r+i][c+i] != '#':
            listToControl.append(matrix[r+i][c+i])
            i += 1
        if len(listToControl) == k:
            string = "".join(listToControl)
            if string == string[::-1] and (r, c) not in self.visited:
                self.visited.add((r + (k - 1), c + (k - 1)))
                return True
        return False
    
    def CountDownLeft(self, matrix: list[list[int]], r: int, c: int, k: int) -> bool:
        listToControl = []
        i = 0
        while i < k and matrix[r+i][c-i] != '#':
            listToControl.append(matrix[r+i][c-i])
            i += 1
        if len(listToControl) == k:
            string = "".join(listToControl)
            if string == string[::-1] and (r, c) not in self.visited:
                self.visited.add((r + (k - 1), c - (k - 1)))
                return True
        return False


    def creatInput(self, n: int, m: int) -> None:
        with open("input.txt", 'w') as file:
            for _ in range(n):
                newLine = [str(rd.randint(0, 9)) for _ in range(m)]
                string = "".join(newLine)
                print(string, file=file)
    
    def readInput(self) -> list[list[str]]:
        matrix = []
        with open("input.txt") as file:
            for line in file:
                newLine = []
                for char in line.strip():
                    newLine.append(char)
                matrix.append(newLine)
        
        return matrix

       

sol = Solution()
x = [
    ['2','1'],
    ['1','1']
    ]
x = sol.readInput()
#sol.creatInput(1000,1000)
start = time.time()
sol.Esecution(x, 7, '3')
end = time.time() - start
print(end)








