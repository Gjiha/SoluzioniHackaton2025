import os

class Solution:

    inputFolder = os.path.join('soluzioni', 'input', '10')
    outputFolder = os.path.join('soluzioni', 'output', '10')
   
    @staticmethod
    def solve(args: list[str], chapters: list[int, int, list[str]]) -> list[int]:
        l = []
        for x in range(len(chapters)):
            l.append(chapters[x][0])
        return l
    
    @staticmethod
    def loadInput(i: int) -> tuple[list[str], list[int, int, list[str]]]:
        files = os.listdir(Solution.inputFolder)
        files.sort()

        with open(os.path.join(Solution.inputFolder, files[i])) as file:
            universe = []
            listOfSets = []
            for i, line in enumerate(file.readlines()):
                if i == 0:
                    universe = line.strip().split(', ')
                else:
                    sets = line.strip().split(", ")
                    name = int(sets[0])
                    weight = int(sets[1])
                    insieme = sets[2:]
                    listOfSets.append((name, weight, insieme))
            
            return universe, listOfSets
                    
    
    @staticmethod
    def loadOutput(i: int) -> list[str]:
        files = os.listdir(Solution.outputFolder)
        files.sort()

        with open(os.path.join(Solution.outputFolder, files[i])) as file:
            output = []
            for line in file.readlines():
                for args in line.strip().split(", "):
                    output.append(args)
        return output
    
    @staticmethod
    def evaluateSolution(args: list[str], chapters: list[int, int, list[str]]) -> int:
        dictOfChapters = {}
        for name, weight, argomenti in chapters:
            dictOfChapters[name] = {'w':weight, 'args':argomenti}
        
        listOfName = Solution.solve(args, chapters)
        setOfArgs = set()
        total = 0
        for name in listOfName:
            newWeight = dictOfChapters[name]['w']
            newArgs = dictOfChapters[name]['args']
            for a in newArgs:
                setOfArgs.add(a)
            total += newWeight
        
        listOfArgs = sorted(list(setOfArgs))
        if args == listOfArgs:
            return total
        else:
            return float('inf')

