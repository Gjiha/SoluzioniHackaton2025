import pprint as pp
class Solution:
    
    @staticmethod
    def matrix_mul(n: list[tuple[int, int]], i: int, j: int, OPT: dict = dict()) -> int:
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

def loadInput():
    with open('7.5/input.txt') as file:
        input = []
        for line in file:
            temp = line.strip().split(', ')
            input.append(tuple(int(x) for x in temp))
    return input

sol = Solution()
wagons = (loadInput())
x = sol.matrix_mul(wagons, 0, len(wagons) - 1)

with open('7.5/output.txt', 'w') as file:
    file.write(str(x))