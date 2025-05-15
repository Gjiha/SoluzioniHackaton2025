import os


class Solution:

    inputFolder = os.path.join("soluzioni", "input", "4")
    outputFolder = os.path.join("soluzioni", "output", "4")

    @staticmethod
    def elaborateinput(matrix: list[list[int]]):
        Solution.partialSum = [
            [0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)
        ]
        Solution.partialSum[0][0] = matrix[0][0]

        rows = len(matrix)
        cols = len(matrix[0])

        for r in range(1, rows):
            Solution.partialSum[r][0] = matrix[r][0] + Solution.partialSum[r - 1][0]

        for c in range(1, cols):
            Solution.partialSum[0][c] = matrix[0][c] + Solution.partialSum[0][c - 1]

        for r in range(1, rows):
            for c in range(1, cols):
                Solution.partialSum[r][c] = (
                    matrix[r][c]
                    + Solution.partialSum[r][c - 1]
                    + Solution.partialSum[r - 1][c]
                    - Solution.partialSum[r - 1][c - 1]
                )

    @staticmethod
    def computeSolution(row1: int, col1: int, row2: int, col2: int) -> int:
        return (
            Solution.partialSum[row2][col2]
            - (
                Solution.partialSum[row2][col1 - 1]
                + Solution.partialSum[row1 - 1][col2]
            )
            + Solution.partialSum[row1 - 1][col1 - 1]
        )

    @staticmethod
    def solve(
        matrix: list[list[int]], squares: list[list[int, int, int, int]]
    ) -> list[int]:
        Solution.elaborateinput(matrix)
        listToReturn = []
        for square in squares:
            row1, col1, row2, col2 = square
            listToReturn.append(Solution.computeSolution(row1, col1, row2, col2))
        return listToReturn

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
    def loadInput(i: int) -> tuple[list[list[int]], list[list[int, int, int, int]]]:
        files = os.listdir(Solution.inputFolder)
        files.sort()

        with open(os.path.join(Solution.inputFolder, files[i])) as file:
            matrix = []
            squares = []
            for i, line in enumerate(file):
                if i == 0:
                    j = int(line.strip())
                elif i <= j:
                    matrix.append(list(map(int, line.strip().split(","))))
                elif i > j:
                    squares.append(list(map(int, line.strip().split(","))))
        return matrix, squares

    @staticmethod
    def loadOutput(i: int) -> list[int]:
        files = os.listdir(Solution.outputFolder)
        files.sort()

        with open(os.path.join(Solution.outputFolder, files[i])) as file:
            for line in file:
                list = line.strip().split(",")
                for i in range(len(list)):
                    list[i] = int(list[i])
        return list
