from collections import deque
import pprint as pp
import random

class Solution:

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
    def elaborateInput(grid: list[list[int]]) -> list[list[int]]:
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

        grid = Solution.elaborateInput(grid)

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
    def generate_emote_matrix(n, m):
        matrix = [["--" for _ in range(m)] for _ in range(n)]

        # Lista di emote senza END
        emote_list = [value for key, value in Solution.emotes.items() if key != "END"]

        # Scegli una posizione casuale per END
        end_row = random.randint(0, n - 1)
        end_col = random.randint(0, m - 1)

        startCol = random.randint(0, m-1)
        startRow = random.randint(0, n-1)

        for i in range(n):
            for j in range(m):
                choice = random.randint(0,4)
                if choice > 2:
                    newEmote = emote_list[random.randint(0,len(emote_list) - 1)]
                    matrix[i][j] = newEmote
        
        matrix[end_row][end_col] = Solution.emotes['END']
        matrix[startRow][startCol] = '🐹'

        return matrix , startRow, startCol



def loadTeastcase(startY, startX, grid):
    with open('6/testcase0.txt', 'w') as file:
        print(startY, startX, file=file)
        for row in grid:
            print(', '.join(row), file=file)

def loadInput():
    with open('6/testcase0.txt', 'r') as file:
        grid = []
        for i, line in enumerate(file):
            if i == 0:
                startY, startX = line.strip().split(' ')
            else:
                grid.append(line.strip().split(', '))
    
    return grid, int(startY), int(startX)

        
sol = Solution()
x, startY, startX= sol.generate_emote_matrix(1000,1000)
loadTeastcase(startY, startX, x)
grid, y, x = loadInput()
print(sol.solve(y, x, grid))




        



            



