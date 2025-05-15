import os

class Solution:

    inputFolder = os.path.join('soluzioni', 'input', '2')
    outputFolder = os.path.join('soluzioni', 'output', '2')
    
    @staticmethod
    def solve(input: str)-> int:
        digit = {'1','2','3','4','5','6','7','8','9','0'}
        listToPalindrome = []
        i = 0
        while i < len(input) - 4:
            if input[i:i+4] == 'mul(':
                temp = 1
                i += 4
                while i < len(input) and input[i] in digit:
                    temp *= int(input[i])
                    i += 1
                if i == len(input):
                    return listToPalindrome
                if input[i] == ')':
                    if input[i-1] != '(':
                        listToPalindrome.append(temp)
                    i += 1

            elif input[i:i+4] == 'sum(':
                temp = 0
                i += 4
                while i < len(input) and input[i] in digit:
                    temp += int(input[i])
                    i += 1
                if i == len(input):
                    return listToPalindrome
                if input[i] == ')':
                    listToPalindrome.append(temp)
                    i += 1

            elif input[i:i+4] == 'con(':
                temp = ''
                i += 4
                while i < len(input) and input[i] in digit:
                    temp += input[i]
                    i += 1
                if i == len(input):
                    return listToPalindrome
                if input[i] == ')':
                    if temp :
                        listToPalindrome.append(int(temp))
                    i += 1

            else:
                i += 1


        return sum(listToPalindrome)
        
    @staticmethod
    def loadInput(i: int) -> str:
        files = os.listdir(Solution.inputFolder)
        files.sort()

        with open(os.path.join(Solution.inputFolder, files[i])) as file:
            string = ''
            for line in file:
                string += str(line.strip())
        return string
    

    @staticmethod
    def loadOutput(i: int) -> int:
        files = os.listdir(Solution.outputFolder)
        files.sort()

        with open(os.path.join(Solution.outputFolder, files[i])) as file:
            value = ''
            for line in file:
                value += line
        return int(value)           