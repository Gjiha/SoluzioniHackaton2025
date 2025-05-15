class Solution:

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
    def solve(costs: list[int], maxF: int):
        # BLACK == True
        # WHITE == False

        white = Solution.colorSum(costs, len(costs), maxF, False)
        black = Solution.colorSum(costs, len(costs), maxF - 1, True)

        return max(white, black)

    @staticmethod
    def loadinput():
        with open("9/input.txt", "r") as file:
            lines = file.readlines()
            maxW = int(lines[0].strip())
            costs = list(map(int, lines[1].strip().split(", ")))
        return costs, maxW

    @staticmethod
    def loadOutput():
        with open("9/input.txt", "r") as file:
            return int(file.readline().strip())


sol = Solution()
x, w = sol.loadinput()
print(sol.solve(x, w))
