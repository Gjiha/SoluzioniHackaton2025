import os
from collections import deque

class Solution:

    inputFolder = os.path.join('soluzioni', 'input', '6')
    outputFolder = os.path.join('soluzioni', 'output', '6')
   
    emotes = {
        "SKULL": "💀",
        "CANDY": "🍬",
        "MUSHROOM": "🍄",
        "MIRROR": "🪞",
        "LEFT": "🠔",
        "UP": "🠕 ",
        "RIGHT": "🠖",
        "DOWN": "🠗 ",
        "END": "🏁"
    }

    @staticmethod
    def elaborateGrid(grid: list[list[int]]) -> list[list[int]]:
        n = len(grid)
        m = len(grid[0])

        for r in range(n):
            for _ in range(2):
                grid[r].insert(0,"💀")
                grid[r].append("💀")
        
        for _ in range(2):
            grid.insert(0,["💀"] * (m + 4))
            grid.append(["💀"] * (m + 4))

        return grid


    @staticmethod
    def solve(y: int, x: int, grid: list[list[int]]) -> int:

        grid = Solution.elaborateGrid(grid)

        direzioni = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        diagonali = [(1, 1), (1, -1), (-1, -1), (-1, 1)]

        visit = set((y+2, x+2))

        queue = deque([(y + 2, x + 2, 0)])
        while queue:
            y, x, cost = queue.popleft()
            cost += 1

            if grid[y][x] == Solution.emotes["SKULL"]:
                continue

            elif grid[y][x] == Solution.emotes["CANDY"]:
                for ny, nx in direzioni:
                    if (y + ny, x + nx) not in visit:
                        queue.append((y + ny, x + nx, cost))
                        visit.add((y + ny, x + nx))
                for ny, nx in diagonali:
                    if (y + ny, x + nx) not in visit:
                        queue.append((y + ny, x + nx, cost))
                        visit.add((y + ny, x + nx))

            elif grid[y][x] == Solution.emotes["MUSHROOM"]:
                for ny, nx in direzioni:
                    ny *= 2
                    nx *= 2
                    if (y + ny, x + nx) not in visit:
                        queue.append((y + ny, x + nx, cost))
                        visit.add((y + ny, x + nx))

            elif grid[y][x] == Solution.emotes["MIRROR"]:
                for ny, nx in direzioni:
                    if (x + nx, y + ny) not in visit:
                        queue.append((x + nx, y + ny, cost))
                        visit.add((x + nx, y + ny))

            elif grid[y][x] == Solution.emotes["LEFT"]:
                for ny, nx in direzioni:
                    if (y + ny, 1 + nx) not in visit:
                        queue.append((y + ny, 1 + nx, cost))
                        visit.add((y + ny, 1 + nx))

            elif grid[y][x] == Solution.emotes["RIGHT"]:
                for ny, nx in direzioni:
                    if (y + ny, len(grid[0]) + nx - 2) not in visit:
                        queue.append((y + ny, len(grid[0]) + nx - 2, cost))
                        visit.add((y + ny, len(grid[0]) + nx - 2))

            elif grid[y][x] == Solution.emotes["UP"]:
                for ny, nx in direzioni:
                    if (1 + ny, x + nx) not in visit:
                        queue.append((1 + ny, x + nx, cost))
                        visit.add((1 + ny, x + nx))

            elif grid[y][x] == Solution.emotes["DOWN"]:
                for ny, nx in direzioni:
                    if (len(grid) + ny - 2, x + nx) not in visit:
                        queue.append((len(grid) + ny - 2, x + nx, cost))
                        visit.add((len(grid) + ny - 2, x + nx))

            elif grid[y][x] == Solution.emotes["END"]:
                return cost - 1

            else:
                for ny, nx in direzioni:
                    if (y + ny, x + nx) not in visit:
                        queue.append((y + ny, x + nx, cost))
                        visit.add((y + ny, x + nx))

        return -1
        
    @staticmethod
    def loadInput(i: int) -> str:
        files = os.listdir(Solution.inputFolder)
        files.sort()

        with open(os.path.join(Solution.inputFolder, files[i])) as file:
            grid = []
            for i, line in enumerate(file):
                if i == 0:
                    startY, startX = line.strip().split(' ')
                else:
                    grid.append(line.strip().split(', '))

        return int(startY), int(startX), grid
    
    @staticmethod
    def loadOutput(i: int) -> str:
        files = os.listdir(Solution.outputFolder)
        files.sort()

        with open(os.path.join(Solution.outputFolder, files[i])) as file:
            for line in file:
                return int(line.strip())

