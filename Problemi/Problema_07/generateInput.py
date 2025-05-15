import random as rd
import pprint as pp

def generaInput(n: int, fin: int) -> None:
    number = []
    for _ in range(n + 1):
        new = rd.randint(1,fin)
        number.append(new)

    output = []
    for i in range(len(number) - 2):
        output.append((number[i], number[i+1]))
    return output

def writeInput(input: list[tuple[int]]) -> None:
    with open('7.5/input.txt', 'w') as file:
        for couple in input:
            n1, n2 = couple
            file.write(f'{n1}, {n2}\n')
    return


x = generaInput(200, 1000)
writeInput(x)



