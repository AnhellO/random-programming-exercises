from collections import deque

class Stack:
    def __init__(self) -> None:
        self._stack = deque()
    
    def push(self, item: str) -> None:
        self._stack.append(item)
    
    def pop(self) -> str:
        return self._stack.pop()

    def empty(self) -> bool:
        return len(self._stack) == 0
    
    def size(self) -> int:
        return len(self._stack)
    
    def top(self) -> str:
        return self._stack[-1]

def main():
    stack = Stack()
    stack.push('item-1')
    stack.push('item-2')
    stack.push('item-3')
    
    print(f"### Initial stack size: {stack.size()}")
    print(f"### Top item: {stack.top()}")
    
    while not stack.empty():
        print(f"### Pop item: {stack.pop()}")
    
    print(f"### Final stack size: {stack.size()}")
    print(f"### Is my stack empty?: {stack.empty()}")

if __name__ == "__main__":
    main()