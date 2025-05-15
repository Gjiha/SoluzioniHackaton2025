import time

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


def deSolve(key: str, text: str) -> str:
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    setOfAlphabet = {ch: i + 1 for i, ch in enumerate(alphabet)}
    returnString = []
    i = 0
    for char in text:
        char = char.lower()
        if char in setOfAlphabet:
            offset = (setOfAlphabet[char] - setOfAlphabet[key[i]]) % 26
            returnString.append(alphabet[offset - 1])                    
            i = (i + 1) % len(key)
        else:
            returnString.append(char)
    return "".join(returnString)

x = ''
with open("prova.txt") as file:
    for line in file:
        x += line

y = deSolve("hash", x)

with open("new.txt", "w") as file:
    file.write(y)

startTime = time.time()
z = solve("hash", y)
endingTime = time.time() - startTime
print(endingTime)

with open("nuovo.txt", "w") as file:
    file.write(z)