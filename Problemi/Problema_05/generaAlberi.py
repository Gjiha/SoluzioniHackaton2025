import random

class Node:
    def __init__(self, name, value):
        self.name = name      # Nome univoco del nodo
        self.value = value    # Valore numerico casuale
        self.left = None
        self.right = None

def generate_random_binary_tree(max_nodes):
    if max_nodes == 0:
        return None, {}

    nodes_created = 1
    root = Node(f"N{nodes_created}", random.randint(-10, 10))
    node_list = [root]
    node_map = {root.name: root}  # Dizionario per accedere ai nodi per nome

    while nodes_created < max_nodes:
        current = random.choice(node_list)

        if current.left and current.right:
            node_list.remove(current)
            continue

        nodes_created += 1
        new_node = Node(f"N{nodes_created}", random.randint(-10, 20))

        if not current.left and not current.right:
            if random.choice([True, False]):
                current.left = new_node
            else:
                current.right = new_node
        elif not current.left:
            current.left = new_node
        else:
            current.right = new_node

        node_list.append(new_node)
        node_map[new_node.name] = new_node

    return root, node_map

def createFile(nodes):
    with open("temp/5/Prova_testcase0.txt", "w") as file:
        for node in nodes:
            print(f"{nodes[node].name}, {nodes[node].value}, {nodes[node].left.name if nodes[node].left != None else None}, {nodes[node].right.name if nodes[node].right != None else None}", file=file)
    

root, node = generate_random_binary_tree(500000)
createFile(node)


