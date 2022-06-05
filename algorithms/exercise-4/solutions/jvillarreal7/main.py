class Node:
    """
    Class that represents a binary tree node.
    """

    def __init__(self, data) -> None:
        self.data = data
        self.left = self.right = None


def invert(node: Node) -> None:
    """
    Inverts the binary tree recursively.
    """
    if not node:
        return

    invert(node.left)
    invert(node.right)

    node.left, node.right = node.right, node.left


def traverse_tree(node: Node) -> None:
    """
    Traverses (prints) tree inorder.
    """
    if not node:
        return

    traverse_tree(node.left)
    print(node.data, end=" ")
    traverse_tree(node.right)


# Tree initialization
root = Node(2)
root.left = Node(1)
root.left.left = Node(7)
root.right = Node(4)
root.right.left = Node(3)
root.right.left.left = Node(6)
root.right.right = Node(5)


print("Initial tree traversal")
traverse_tree(root)
print()

invert(root)

print("Inverted tree traversal")
traverse_tree(root)
print()
