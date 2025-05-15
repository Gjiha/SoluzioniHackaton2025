import pprint as pp

class Solution:

    def elaborateInput(self, edges: list[list[str, int, str, str]]):
        tree = {}
        for i, (name, val, left, right) in enumerate(edges):
            if i == 0:
                tree['root'] = name
            if name not in tree:
                tree[name] = {'val': int(val),
                            'left': left if left != 'None' else None,
                            'right': right if right != 'None' else None}
        self.tree = tree
        return 
            
    def pathSum(self, edges: list[list[str, int, str, str]], targetSum: int) -> int:
        currentSum = 0
        dictOfSums = {0:1}
        self.elaborateInput(edges)
        count = self.dfsRic(self.tree['root'], targetSum, currentSum, dictOfSums)
        return count
    
    def dfsRic(self, node: str, targetSum: int, currentSum:int, dictOfSums:dict[int:int]) -> int:
        count = 0

        currentSum += self.tree[node]['val']

        if currentSum - targetSum in dictOfSums:
            count += dictOfSums[currentSum - targetSum]

        if currentSum not in dictOfSums:
            dictOfSums[currentSum] = 1
        else:
            dictOfSums[currentSum] += 1

        if self.tree[node]['left'] != None:
            count += self.dfsRic(self.tree[node]['left'], targetSum, currentSum, dictOfSums)
        if self.tree[node]['right'] != None:
            count += self.dfsRic(self.tree[node]['right'], targetSum, currentSum, dictOfSums)

        dictOfSums[currentSum] -= 1        

        return count



    
def readFile():
    edges = []
    with open("temp/5/Prova_testcase0.txt", "r") as file:
        for line in file:
            edges.append(line.strip().split(', '))
    return edges

list = readFile()
sol = Solution()
x = sol.pathSum(list, 100)
#pp.pprint(sol.tree)
print(x)
