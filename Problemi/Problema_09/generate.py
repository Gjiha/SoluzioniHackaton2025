import random as rd


def generate(n: int, maxInt: int):
    return [rd.randint(-maxInt, maxInt) for _ in range(n)]


def writeinput(x: int):
    with open("9/input.txt", "w") as file:
        file.write(", ".join(list(map(str, x))) + "\n")


x = generate(200, 50)
print(x)
writeinput(x)
