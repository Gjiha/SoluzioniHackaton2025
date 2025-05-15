import os

class Solution:

    inputFolder = os.path.join('soluzioni', 'input', '0')
    outputFolder = os.path.join('soluzioni', 'output', '0')
   
    @staticmethod
    def solve(n: int, k: int) -> int:
        '''
        Scrivi la tua soluzione qui
        '''
        # n deve essere multiplo di k
        res = ((n) * (n + 1)) / 2
        first = (k*(k+1))/2
        # print(f"\nn: {n} | k: {k} | res: {res}\n")
        return int(res - first)
    
    @staticmethod
    def loadInput(i: int) -> str:
        files = os.listdir(Solution.inputFolder)
        files.sort()

        with open(os.path.join(Solution.inputFolder, files[i])) as file:
            line = file.readline()
            line = line.split(",")
            n, k = int(line[0]), int(line[1])

        return n, k
    
    @staticmethod
    def loadOutput(i: int) -> int:
        files = os.listdir(Solution.outputFolder)
        files.sort()

        with open(os.path.join(Solution.outputFolder, files[i])) as file:
            line = file.readline()
        return int(line)

