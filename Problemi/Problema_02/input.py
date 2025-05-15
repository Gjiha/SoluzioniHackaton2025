import random as rd

def creaInput(line: int):
    caratteri = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    mul_ = 'mul('
    sum_ = 'sum('
    con_ = 'con('
    end_ = ')'
    string = ''
    for _ in range(line):
        list = []
        for _ in range(100):
            newChar = rd.choice(caratteri)
            if newChar == 'm' or newChar == 'M':
                list.append(mul_)
                for _ in range(rd.randint(0,10)):
                    list.append(rd.randint(1,9))
                list.append(end_)
            elif newChar == 's' or newChar == 'S':
                list.append(sum_)
                for _ in range(rd.randint(0,10)):
                    list.append(rd.randint(0,9))
                list.append(end_)
            elif newChar == 'c' or newChar == 'C':
                list.append(con_)
                for _ in range(rd.randint(0,10)):
                    list.append(rd.randint(0,9))
                list.append(end_)
            else:
                list.append(newChar)
        list.append('\n')
        string += ''.join(str(x) for x in list)
    with open('input.txt', 'w') as file:
        file.write(string)
    return

creaInput(1)

