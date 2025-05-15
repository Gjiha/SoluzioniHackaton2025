import os

class Solution:

    inputFolder = os.path.join('soluzioni', 'input', '5')
    outputFolder = os.path.join('soluzioni', 'output', '5')
    
    @staticmethod
    def solve(edges: list[list[str, int, str, str]], targetSum: int) -> int:
        currentSum = 0
        dictOfSums = {0:1}
        Solution.elaborateInput(edges)
        # count = Solution.dfsRic(Solution.tree['root'], targetSum, [])
        count = Solution.dfsRic(Solution.tree['root'], targetSum, currentSum, dictOfSums)
        return count
    
    @staticmethod
    def elaborateInput(edges: list[list[str, int, str, str]]):
        tree = {}
        for i, (name, val, left, right) in enumerate(edges):
            if i == 0:
                tree['root'] = name
            if name not in tree:
                tree[name] = {'val': int(val),
                            'left': left if left != 'None' else None,
                            'right': right if right != 'None' else None}
        Solution.tree = tree
        return 
    
    # @staticmethod
    # def dfsRic(node, targetSum, value):
    #     count = 0

    #     value = value[:]

    #     for i in range(len(value)):
    #         value[i] += Solution.tree[node]['val']
    #         if value[i] == targetSum:
    #             count += 1
        
    #     value.append(Solution.tree[node]['val'])
    #     if value[-1] == targetSum:
    #         count += 1

    #     if Solution.tree[node]['left'] != None:
    #         count += Solution.dfsRic(Solution.tree[node]['left'], targetSum, value)
    #     if Solution.tree[node]['right'] != None:
    #         count += Solution.dfsRic(Solution.tree[node]['right'], targetSum, value)
        
    #     return count
        
        


    @staticmethod
    def dfsRic(node: str, targetSum: int, currentSum:int, dictOfSums:dict[int:int]) -> int:
        count = 0

        currentSum += Solution.tree[node]['val']

        if currentSum - targetSum in dictOfSums:
            count += dictOfSums[currentSum - targetSum]

        if currentSum not in dictOfSums:
            dictOfSums[currentSum] = 1
        else:
            dictOfSums[currentSum] += 1

        if Solution.tree[node]['left'] != None:
            count += Solution.dfsRic(Solution.tree[node]['left'], targetSum, currentSum, dictOfSums)
        if Solution.tree[node]['right'] != None:
            count += Solution.dfsRic(Solution.tree[node]['right'], targetSum, currentSum, dictOfSums)

        dictOfSums[currentSum] -= 1        

        return count
        

    @staticmethod
    def loadInput(i: int) -> str:
        files = os.listdir(Solution.inputFolder)
        files.sort()
        edges = []
        targetSum = 0
        with open(os.path.join(Solution.inputFolder, files[i])) as file:
            for i, line in enumerate(file):
                if i == 0:
                    targetSum = int(line.strip())
                else:
                    edges.append(line.strip().split(', '))
        return edges, targetSum

    @staticmethod
    def loadOutput(i: int) -> str:
        files = os.listdir(Solution.outputFolder)
        files.sort()

        with open(os.path.join(Solution.outputFolder, files[i])) as file:
            for line in file:
                return int(line.strip())


