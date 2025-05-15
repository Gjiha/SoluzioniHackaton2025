import os


class Solution:

    inputFolder = os.path.join("soluzioni", "input", "8")
    outputFolder = os.path.join("soluzioni", "output", "8")

    @staticmethod
    def solve(
        firstStack: list[int],
        secondStack: list[int],
        maxWeight: int,
    ) -> tuple[int, int]:

        n = len(firstStack)
        m = len(secondStack)

        firstSum = []
        newFirst = 0
        for t in range(n):
            newFirst += firstStack[t]
            firstSum.append(newFirst)

        secondSum = []
        newSecond = 0
        for k in range(m):
            newSecond += secondStack[k]
            secondSum.append(newSecond)

        weight = 0
        index = (-1, -1)
        i = -1
        j = m - 1
        while i < n and j >= -1:
            newWeight = 0
            if i != -1:
                newWeight += firstSum[i]
            if j != -1:
                newWeight += secondSum[j]

            if newWeight >= weight and newWeight <= maxWeight:
                weight = newWeight
                index = (i, j)

            if newWeight < maxWeight:
                i += 1
            elif newWeight >= maxWeight:
                j -= 1

        return index

    # @staticmethod
    # def solve(
    #     firstStack: list[int],
    #     secondStack: list[int],
    #     maxWeight: int,
    # ) -> tuple[int, int]:

    #     n = len(firstStack)
    #     m = len(secondStack)

    #     firstSum = []
    #     newFirst = 0
    #     for t in range(n):
    #         newFirst += firstStack[t]
    #         firstSum.append(newFirst)

    #     index = (-1, -1)
    #     weight = 0

    #     for i in range(-1, n):
    #         if i >= 0:
    #             newWeight = firstSum[i]
    #         else:
    #             newWeight = 0

    #         j = -1
    #         while j < m:
    #             if j != -1:
    #                 newWeight += secondStack[j]
    #             if newWeight < maxWeight:
    #                 j += 1
    #             elif newWeight > maxWeight:
    #                 newWeight -= secondStack[j]
    #                 j -= 1
    #                 break
    #             else:
    #                 break

    #         if newWeight >= weight and newWeight <= maxWeight:
    #             weight = newWeight
    #             index = (i, j)

    #     return index

    # @staticmethod
    # def solve(
    #     firstStack: list[int],
    #     secondStack: list[int],
    #     maxWeight: int,
    # ) -> tuple[int, int]:

    #     n = len(firstStack)
    #     m = len(secondStack)

    #     firstSum = []
    #     newFirst = 0
    #     for t in range(n):
    #         newFirst += firstStack[t]
    #         firstSum.append(newFirst)

    #     secondSum = []
    #     newSecond = 0
    #     for k in range(m):
    #         newSecond += secondStack[k]
    #         secondSum.append(newSecond)

    #     weight = 0
    #     index = (-1, -1)
    #     for i in range(-1, n):
    #         if i == -1:
    #             newWeight = 0
    #         else:
    #             newWeight = firstSum[i]

    #         j = Solution.binarySearch(secondSum, maxWeight - newWeight, 0, m - 1)

    #         if j != -1:
    #             newWeight += secondSum[j]

    #         if newWeight >= weight and newWeight <= maxWeight:
    #             weight = newWeight
    #             index = (i, j)

    #     return index

    # @staticmethod
    # def binarySearch(
    #     arr: list[int],
    #     target: int,
    #     left: int,
    #     right: int,
    #     best: int = -1,
    # ) -> int:
    #     if left > right:
    #         return best

    #     mid = (left + right) // 2

    #     if arr[mid] == target:
    #         return mid

    #     elif arr[mid] < target:

    #         return Solution.binarySearch(arr, target, mid + 1, right, mid)
    #     else:

    #         return Solution.binarySearch(arr, target, left, mid - 1, best)

    @staticmethod
    def loadInput(i: int) -> str:
        files = os.listdir(Solution.inputFolder)
        files.sort()

        with open(os.path.join(Solution.inputFolder, files[i])) as file:
            lines = file.readlines()
            maxWeight = int(lines[0].strip())
            first = list(map(int, lines[1].strip().split(", ")))
            second = list(map(int, lines[2].strip().split(", ")))
        return first, second, maxWeight

    @staticmethod
    def loadOutput(i: int) -> int:
        files = os.listdir(Solution.outputFolder)
        files.sort()

        with open(os.path.join(Solution.outputFolder, files[i])) as file:
            return int(file.readline().strip())

    @staticmethod
    def evaluateSolution(
        firstStack: list[int],
        secondStack: list[int],
        maxWeight: int,
    ) -> int:

        n = len(firstStack)
        m = len(secondStack)

        firstSum = []
        newFirst = 0
        for t in range(n):
            newFirst += firstStack[t]
            firstSum.append(newFirst)

        secondSum = []
        newSecond = 0
        for k in range(m):
            newSecond += secondStack[k]
            secondSum.append(newSecond)

        i, j = Solution.solve(firstStack, secondStack, maxWeight)
        output = 0
        if i != -1:
            output += firstSum[i]
        if j != -1:
            output += secondSum[j]

        return output
