import os


class Solution:

    inputFolder = os.path.join("soluzioni", "input", "9")
    outputFolder = os.path.join("soluzioni", "output", "9")

    @staticmethod
    def colorSum(c: list[int], i: int, f: int, color: bool, OPT: dict = None) -> int:
        # BLACK == True
        # WHITE == False
        if OPT == None:
            OPT = {}

        if (i, f, color) in OPT:
            return OPT[i, f, color]

        if i == 0:
            OPT[i, f, color] = 0
        elif f == 0:
            OPT[i, 0, color] = c[i - 1] * int(
                color
            )  # + Solution.colorSum(c, i - 1, 0, False, OPT)
        else:
            OPT[i, f, color] = max(
                [
                    c[i - 1]
                    + Solution.colorSum(c, i - 1, f - int(not color), not color, OPT),
                    Solution.colorSum(c, i - 1, f - int(color), color, OPT),
                ]
            )

        return OPT[i, f, color]

    @staticmethod
    def solve(costs: list[int], k: int):
        # BLACK == True
        # WHITE == False

        white = Solution.colorSum(costs, len(costs), k, False)
        black = Solution.colorSum(costs, len(costs), k - 1, True)

        return max(white, black)

    @staticmethod
    def loadInput(i: int) -> str:
        files = os.listdir(Solution.inputFolder)
        files.sort()

        with open(os.path.join(Solution.inputFolder, files[i])) as file:
            lines = file.readlines()
            maxColor = int(lines[0].strip())
            costs = list(map(int, lines[1].strip().split(", ")))
        return costs, maxColor

    @staticmethod
    def loadOutput(i: int) -> int:
        files = os.listdir(Solution.outputFolder)
        files.sort()

        with open(os.path.join(Solution.outputFolder, files[i])) as file:
            return int(file.readline().strip())
