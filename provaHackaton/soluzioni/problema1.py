import os

class Solution:

    inputFolder = os.path.join('soluzioni', 'input', '1')
    outputFolder = os.path.join('soluzioni', 'output', '1')
    
    @staticmethod
    def solve(key: str, text: str) -> str:
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        setOfAlphabet = {ch: i + 1 for i, ch in enumerate(alphabet)}
        returnString = []
        i = 0
        for char in text:
            if char in setOfAlphabet:
                offset = (setOfAlphabet[char] + setOfAlphabet[key[i]]) % 26
                returnString.append(alphabet[offset - 1])                    
                i = (i + 1) % len(key)
            else:
                returnString.append(char)
        return "".join(returnString)
        
    @staticmethod
    def loadInput(i: int) -> str:
        files = os.listdir(Solution.inputFolder)
        files.sort()

        with open(os.path.join(Solution.inputFolder, files[i])) as file:
            string = ''
            key = ''
            for i, line in enumerate(file):
                if i == 0:
                    key = line.strip()
                else:
                    string += line
            
        return key, string
    

    @staticmethod
    def loadOutput(i: int) -> str:
        files = os.listdir(Solution.outputFolder)
        files.sort()

        with open(os.path.join(Solution.outputFolder, files[i])) as file:
            string = ''
            for line in file:
                string += line
        return string