import random as rd
import pprint as pp

def generate(n, m, maxValue):
    first = [rd.randint(0,maxValue) for _ in range(n)]
    second = [rd.randint(0,maxValue) for _ in range(m)]

    return first, second

def writeInput(first, second):
    with open("8/input.txt", "w") as file:
        file.write(", ".join(map(str, first)) +'\n')
        file.write(", ".join(map(str, second)) +'\n')
    return



first, second = generate(10,10,15)
writeInput(first, second)





