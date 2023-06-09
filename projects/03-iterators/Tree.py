from __future__ import annotations

import typing

# ==================================================================================================================== #
class Node:
    def __init__(self, content):
        self.content = content
        self.parent = None
        self.sub_nodes = []

    def __getitem__(self, index):
        if type(index) == int:
            return self.sub_nodes[index]
        elif type(index) == tuple:
            result = self
            for index_part in index:
                result = result[index_part]
            return result

    def __setitem__(self, index, value):
        if type(index) == int:
            self.sub_nodes[index].content = value
        elif type(index) == tuple:
            node = self
            for index_part in index:
                node = node[index_part]
            node.content = value

    def __str__(self):
        return str(self.content)

    def __repr__(self):
        return f"Node(content={self.content}, sub_nodes={list(repr(sub_node) for sub_node in self.sub_nodes)})"

    def __iter__(self):
        return NodeIterator(self)

    def check_index(self, index):
        if type(index) != int:
            raise TypeError("Index must be of type int!")

        n_sub_nodes = len(self.sub_nodes)
        if not (-(n_sub_nodes + 1) <= index <= n_sub_nodes):
            raise IndexError("Index out of bounds!")

    def add_node(self, value, index = None):
        # the optional argument index specifies where to add the new node.
        # it will be added *before* index, and allows negative indices, as with lists.
        # If set to none, the new item will be added to the back of the list.

        if index is None:
            index = len(self.sub_nodes)
        self.check_index(index)

        node = Node(value)
        node.parent = self
        self.sub_nodes.insert(index, node)
        return node

    def remove_node(self, index) -> None:
        self.check_index(index)

        if index < 0:
            index += len(self.sub_nodes)

        del self.sub_nodes[index]


# ==================================================================================================================== #
class NodeIterator(typing.Iterator):
    def __init__(self, tree) -> None:
        self.tree = tree
        self.current_node = tree
        self.indices = None

    def advance_indices(self):
        current_index = self.indices[-1]

        if len(self.current_node.sub_nodes) > 0:
            self.indices.append(0)
        else:
            resolved = False
            while not resolved:
                if current_index + 1 < len(self.current_node.parent.sub_nodes):
                    self.indices[-1] += 1
                    resolved = True
                else:
                    del self.indices[-1]
                    self.current_node = self.current_node.parent

                if len(self.indices) == 0:
                    raise StopIteration
                else:
                    current_index = self.indices[-1]

    def __next__(self) -> tuple[int, Node]:
        if self.indices is None:
            result = 0, self.tree
            self.indices = [0]
        else:
            result = len(self.indices), self.current_node
            self.advance_indices()

        self.current_node = self.tree[tuple(self.indices)]
        return result

    def __iter__(self) -> NodeIterator:
        return self


# ==================================================================================================================== #

def build_tree():
    print("Building the tree ... ", end="")

    subfolders = [
        ("Documents", [
            ("Codes", []),
            ("Ebooks", []),
            ("Uni", []),
            ("Bills and Money", [])
        ]),
        ("Pictures", []),
        ("Downloads", []),
        ("Music", [
            ("no music at all", [
                ("Dummy", []),
            ]),
            ("Dan Deacon", []),
            ("Tocotronic", []),
            ("Wir Sind Helden", [
                ("Die Reklamation", []),
                ("Von Hier An Blind", []),
                ("Soundso", []),
                ("Bring Mich Nach Hause", [])
            ]),
            ("Punkreas", []),
        ]),
        ("Misc", [])
    ]

    root = Node("files")
    for substructure in subfolders:
        add_substructure(root, substructure)

    print("done")

    return root


def add_substructure(root, substructure):
    content = substructure[0]
    children = substructure[1]

    sub_node = root.add_node(content)
    for child in children:
        add_substructure(sub_node, child)


# ==================================================================================================================== #

def main():
    tree = build_tree()

    print("")
    print(tree)
    print(tree[0])
    print(tree[0, 0])
    print(repr(tree))

    print("=" * 80)
    for indent, node in tree:
        print("  " * indent, node, sep="")
    print("=" * 80)


if __name__ == '__main__':
    main()