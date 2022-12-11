from typing import Union

sizes = []

class Tree:
    def __init__(self, root: str, parent: "Tree" = None):
        self.root = root
        self.parent = parent
        self.children = []

    def add_child(self, child: Union["Tree", int]) -> None:
        if isinstance(child, int):
            self.children.append(child)
        else:
            self.children.append(child)
            child.parent = self
        return child

    def tree_size(self, size=0) -> int:
        for child in self.children:
            if isinstance(child, Tree):
                size += child.tree_size()
            else:
                size += child
        global sizes
        sizes.append((self.root,size))
        return size

    def __str__(self):
        return self.root + " -> " + str([child.__str__() for child in self.children])




with open("input.txt") as f:
    lines = f.read().splitlines()
    
    tree = None

    for line in lines:
        if line.startswith("$ cd"):
            if line.split(" ")[2] != "..":
                if tree is None:
                    tree = Tree(line.split(" ")[2])
                else:
                    tree = tree.add_child(Tree(line.split(" ")[2], tree))
            else:
                tree = tree.parent
        elif line.split(" ")[0].isnumeric():
            tree.add_child(int(line.split(" ")[0]))
    while tree.parent is not None:
        tree = tree.parent

    total = 70000000
    unused_min = 30000000
    used = tree.tree_size()
    unused = total - used
    if unused < unused_min:
        delete = unused_min - unused
        candidates = [x for x in sizes if x[1] >= delete]
        candidates.sort(key=lambda x: x[1])
        print(candidates[0][1])

    

    # print(sum([x for x in sizes if x <= 100000]))

    # visit the tree and annotate the size of each folder >= 100000
