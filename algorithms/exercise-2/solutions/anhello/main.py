from collections import deque

class Queue:
    def __init__(self) -> None:
        self._queue = deque()
    
    def enqueue(self, item: str) -> None:
        self._queue.append(item)
    
    def dequeue(self) -> str:
        return self._queue.popleft()

    def empty(self) -> bool:
        return len(self._queue) == 0
    
    def size(self) -> int:
        return len(self._queue)
    
    def front(self) -> str:
        return self._queue[0]
    
    def rear(self) -> str:
        return self._queue[-1]

def main():
    queue = Queue()
    queue.enqueue('item-1')
    queue.enqueue('item-2')
    queue.enqueue('item-3')
    
    print(f"### Initial queue size: {queue.size()}")
    print(f"### Front item: {queue.front()}")
    print(f"### Rear item: {queue.rear()}")
    
    while not queue.empty():
        print(f"### Dequeue item: {queue.dequeue()}")
    
    print(f"### Final queue size: {queue.size()}")
    print(f"### Is my queue empty?: {queue.empty()}")

if __name__ == "__main__":
    main()