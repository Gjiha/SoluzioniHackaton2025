import os
import pprint as pp

class Solution:

    inputFolder = os.path.join('soluzioni', 'input', '7')
    outputFolder = os.path.join('soluzioni', 'output', '7')
    
    @staticmethod
    def solve(wagons: list[tuple[int, int]]) -> int:
        return Solution.matrix_mul(wagons, 0, len(wagons) - 1)

    @staticmethod
    def matrix_mul(n: list[tuple[int, int]], i: int, j: int, OPT: dict = None) -> int:
        if OPT == None:
            OPT = {}
        if (i, j) in OPT:
            return OPT[(i, j)]

        if i == j:
            OPT[(i, i)] = 0
        else:
            OPT[(i, j)] = min(
                [
                    Solution.matrix_mul(n, i, k, OPT)
                    + Solution.matrix_mul(n, k + 1, j, OPT)
                    + n[i][0] * n[k][1] * n[j][1]
                    for k in range(i, j)
                ]
            )

        return OPT[(i, j)]
    
    @staticmethod
    def loadInput(i: int) -> str:
        files = os.listdir(Solution.inputFolder)
        files.sort()

        with open(os.path.join(Solution.inputFolder, files[i])) as file:
            input = []
            for line in file.readlines():
                temp = line.strip().split(', ')
                input.append(tuple(map(int, temp)))
        return input
    
    @staticmethod
    def loadOutput(i: int) -> str:
        files = os.listdir(Solution.outputFolder)
        files.sort()

        with open(os.path.join(Solution.outputFolder, files[i])) as file:
            for line in file:
                return int(line.strip())
