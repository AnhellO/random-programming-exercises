from __future__ import annotations

class Node:
    def __init__(self, data) -> None:
        self._data = data
        self._left_child = None
        self._right_child = None

    def __str__(self) -> str:
        return str(self._data)
    
def preorder(node: Node) -> None:
    if node:
        print(node._data)
        preorder(node._left_child)
        preorder(node._right_child)

def inorder(node: Node) -> None:
    if node:
        inorder(node._left_child)
        print(node._data)
        inorder(node._right_child)

def postorder(node: Node) -> None:
    if node:
        postorder(node._left_child)
        postorder(node._right_child)
        print(node._data)

def main():
    root = Node(1)
    root._left_child = Node(2)
    root._right_child = Node(3)
    root._left_child._left_child = Node(4)
    root._left_child._right_child = Node(5)
    print(f"### Preorder traversal: {preorder(root)}")
    print(f"### Inorder traversal: {inorder(root)}")
    print(f"### Postorder traversal: {postorder(root)}")

if __name__ == '__main__':
    main()