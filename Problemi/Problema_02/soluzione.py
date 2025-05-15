import time

def readInput()-> list[str]:
    string = ''
    with open("input.txt") as file:
        for riga in file:
            string += str(riga.strip())
    return string 


def checkMul(input: str)-> int:
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

        

# x = readInput()
# y = checkMul(x)
x = readInput()
startTime = time.time()
z = checkMul(x)
endingTime = time.time() -  startTime
print(z)
with open('output.txt', 'w') as file:
    file.write(str(z))
print(endingTime)


    

