import pprint as pp
import time

class Solution:
    @staticmethod
    def solve1(firstStack: list[int], secondStack: list[int], maxWeight: int) -> tuple[int, int]:

        n = len(firstStack)
        m = len(secondStack)

        firstSum = []
        newFirst = 0
        for t in range(n):
            newFirst += firstStack[t]
            firstSum.append(newFirst)
        
        index = (-1,-1)
        weight = 0   

        for i in range(-1, n):
            if i >= 0:
                newWeight = firstSum[i]
            else:
                newWeight = 0

            j = -1
            while j < m:
                if j != -1:
                    newWeight += secondStack[j]
                if newWeight < maxWeight:
                    j += 1
                elif newWeight > maxWeight:
                    newWeight -= secondStack[j]
                    j -= 1
                    break
                else:
                    break

            if newWeight >= weight and newWeight <= maxWeight:
                weight = newWeight
                index = (i, j)

        return index
    
    @staticmethod
    def solve2(firstStack: list[int], secondStack: list[int], maxWeight: int) -> tuple[int, int]:

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
        for i in range(-1, n):
            if i == -1:
                newWeight = 0
            else:
                newWeight = firstSum[i]

            j = Solution.binarySearch(secondSum, maxWeight-newWeight, 0, m-1)

            if j != -1:
                newWeight += secondSum[j]

            if newWeight >= weight and newWeight <= maxWeight:
                weight = newWeight
                index = (i, j)    
        
        return index

        

    @staticmethod
    def binarySearch(arr: list[int], target: int, left: int, right: int, best: int = -1) -> int:
        if left > right:
            return best  

        mid = (left + right) // 2

        if arr[mid]== target:
            return mid  

        elif arr[mid] < target:
            
            return Solution.binarySearch(arr, target, mid + 1, right, mid)
        else:
            
            return Solution.binarySearch(arr, target, left, mid - 1, best)
    
    
    @staticmethod
    def solve3(firstStack: list[int], secondStack: list[int], maxWeight: int) -> tuple[int, int]:

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
        index = (-1,-1)
        i = -1
        j = m-1
        while i < n and j >= -1:
            newWeight = 0
            if i != -1:
                newWeight += firstSum[i]
            if j != -1:
                newWeight += secondSum[j]
            
            if newWeight >= weight and newWeight <= maxWeight:
                weight = newWeight
                index = (i,j)

            if newWeight < maxWeight:
                i += 1
            elif newWeight >= maxWeight:
                j -= 1
            
        return index
    
    @staticmethod
    def evaluateSolution(firstStack: list[int], secondStack: list[int], maxWeight: int) -> int:

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
        
        i, j = Solution.solve3(firstStack, secondStack, maxWeight)
        output = 0
        if i != -1:
            output += firstSum[i]
        if j != -1:
            output += secondSum[j]

        return output
    
    @staticmethod
    def loadInput():
        with open("8/input.txt", "r") as file:
            lines = file.readlines()
            maxWeight = int(lines[0].strip())     
            first = list(map(int, lines[1].strip().split(", ")))
            second = list(map(int, lines[2].strip().split(", ")))
        return first, second, maxWeight
    
    @staticmethod
    def loadOutput():
        with open("8/output.txt", "r") as file:
            return int(file.readline().strip())

        


sol = Solution()
first = [1,2,3,4,5,6,7,8,9,10]
second = [1,2,3,4,5,6,8,9,10]
# print(sol.binarySearch(second, 7, 0, len(second)-1))
# x = 16
# print(sol.solve1(first, second, x))
# print(sol.evaluateSolution(first, second, x))
first, second, maxW = sol.loadInput()
start = time.time()
x = sol.evaluateSolution(first, second, maxW)
print(sol.solve3(first, second, maxW))
print(time.time() - start)

print(x)
#print(sol.loadOutput())



                    
            


