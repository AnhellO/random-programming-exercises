from __future__ import annotations

class Node:
    def __init__(self, data) -> None:
        self._data = data
        self._next = None

    def __str__(self) -> str:
        return str(self._data)
  
class LinkedList:
    def __init__(self) -> None:
        self._head = self._tail = None
        
    def __str__(self) -> str:
        return ' -> '.join([str(node) for node in self])

    def __iter__(self) -> LinkedList:
        self._current = self._head
        return self
  
    def __next__(self) -> Node:
        if not self._current:
            raise StopIteration
        
        item = self._current
        self._current = self._current._next
        return item
    
    def is_empty(self) -> bool:
        return self._head == None
    
    def add(self, item) -> LinkedList:
        new_node = Node(item)
        
        if self._head is None:
            self._tail = self._head = new_node
            return self

        new_node._next = self._head
        self._head = new_node
        return self
    
    def append(self, item) -> LinkedList:
        new_node = Node(item)
        
        if self._head is None:
            self._tail = self._head = new_node
            return self

        self._tail._next = new_node
        self._tail = self._tail._next
        return self
    
    def insert_after(self, target_node, new_data) -> LinkedList:
        if target_node is None:
            return self
        
        for node in self:
            if node._data == target_node:
                new_node = Node(new_data)
                new_node._next = node._next
                node._next = new_node
                return self
        
        return self
    
    def insert_before(self, target_node, new_data) -> LinkedList:
        if self._head is None or target_node is None:
            return self
        
        if self._head == target_node:
            return self.add(new_data)
        
        previous = self._head
        for node in self:
            if node._data == target_node:
                new_node = Node(new_data)
                new_node._next = node
                previous._next = new_node
                return self
            
            previous = node
        
        return self
    
    def delete(self, target_node) -> LinkedList:
        if self._head is None or target_node is None:
            return self
        
        if self._head._data == target_node:
            self._head = self._head._next
            return self
        
        previous = self._head
        for node in self:
            if node == self._tail:
                previous._next = None
                self._tail = previous
                node = None
                return self

            if node._data == target_node:
                previous._next = node._next
                node = None
                return self
            
            previous = node
        
        return self
        
def main():
    l = LinkedList()
    print(f"Is the list empty? {l.is_empty()}")
    
    # Add nodes to the beginning of the list
    l.add(1).add('two').add(3)
    print(f"### Linked list representation: {l}")
    
    # Add node to the end
    l.append('four')
    print(f"### Linked list representation: {l}")
    
    # Add more nodes
    l.append(5).append(6).add('seven').add('eight').add(9)
    print(f"### Linked list representation: {l}")
    
    # Insert nodes in the middle of the list
    l.insert_after('eight', 10).insert_after('seven', 11).insert_before(5, 'twelve')
    print(f"### Linked list representation: {l}")
    
    # Delete some nodes from the list & also test head & tail continue working normally
    l.delete(1).delete('seven').delete(6).append('tail').append('works').add('and-also-the-head')
    print(f"### Linked list representation: {l}")
  
    # Iterate the list
    print("### Iterating sequentially over the list:")
    it = iter(l)
    for item in it:
        print(item._data)

    print(f"Is the list empty? {l.is_empty()}")

if __name__ == '__main__':
    main()