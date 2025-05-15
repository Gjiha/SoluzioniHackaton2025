import random as rd
import pprint as pp

def generate(args:list[str], setNumber: int):
    outputs = []
    n = len(args)
    setArgs = set(args)

    for i in range(setNumber):
        newSet = set()

        for _ in range(rd.randint(1,n)):
            newSet.add(args[rd.randint(0,n-1)])

        if setArgs:
            newItem = rd.choice(list(setArgs))
            newSet.add(newItem)
            setArgs.remove(newItem)

        newSet = list(newSet)
        card = len(newSet)
        weight = rd.randint(card//2 if card//2 != 0 else card//2 + 1, card*2)
        outputs.append((i, newSet, weight))

    return outputs

def writeInput(universe, input):
    with open('10/input.txt', 'w') as file:
        universe.sort()
        file.write(", ".join(universe) + '\n')
        for name, argomenti, weight in input:
            file.write(f'{name}, ')
            file.write(f'{weight}, ')
            file.write(", ".join(argomenti) + '\n')

def writeoutput(output: list[str]):
    with open('10/output.txt', 'w') as file:
        output.sort()
        file.write(", ".join(output))
    


argomenti = [
    "Linguaggi formali e grammatiche",
    "Automi a stati finiti",
    "Espressioni regolari",
    "Teorema di Kleene",
    "Automi a pila (PDA)",
    "Linguaggi liberi dal contesto",
    "Macchine di Turing",
    "Decidibilità e problemi decidibili",
    "Problemi indecidibili",
    "Riduzioni tra problemi",
    "Teorema di Rice",
    "Gerarchia di Chomsky",
    "Teoria della complessità computazionale",
    "Classi di complessità",
    "Problemi NP-completi",
    "Teorema di Cook-Levin",
    "Riduzioni polinomiali",
    "Classi PSPACE e EXPTIME",
    "Gerarchie polinomiali",
    "Problema della fermata (Halting problem)",
    "Teoria dell'informazione e compressione",
    "Nozioni di computabilità e funzioni ricorsive"
]

x = generate(argomenti,100)
writeInput(argomenti, x)
writeoutput(argomenti)

