def readInput(key: str):
    matrix = []
    with open("prova.txt") as file:
        setOfAlphabet = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26}
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

        for line in file:
            i = 0
            newLine = []
            
            for char in line:
                
                if char in setOfAlphabet:
                    offset = (setOfAlphabet[char] - setOfAlphabet[key[i]]) % 26
                    newLine.append(alphabet[offset - 1])                    
                    i = (i + 1) % len(key)

                else:
                    newLine.append(char)

            matrix.append("".join(newLine))

    with open("exit.txt", "w") as file:
        for line in matrix:
            print(line, file=file,end = '')
    
    return 


def decryptInput(key: str):
    matrix = []
    with open("exit.txt") as file:
        setOfAlphabet = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26}
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        i = 0
        for line in file:
            newLine = []
            
            for char in line:
                
                if char in setOfAlphabet:
                    offset = (setOfAlphabet[char] + setOfAlphabet[key[i]]) % 26
                    newLine.append(alphabet[offset - 1])                    
                    i = (i + 1) % len(key)

                else:
                    newLine.append(char)


            matrix.append("".join(newLine))

    with open("new.txt", "w") as file:
        for line in matrix:
            print(line, file=file , end = '')
    
    return 



# readInput('baaaa')
# decryptInput('baaaa')

with open("prova.txt") as file:
    for i, line in enumerate(file):
        if i == 0:
            print(line.strip())

