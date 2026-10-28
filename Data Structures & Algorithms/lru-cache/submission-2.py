class Node:
    def __init__(self, val: int, key: Optional[int] = None, prev = None, next = None):
        self.val = val
        self.key = key
        self.prev = prev
        self.next = next

class LRUCache:
# can form a queue of the most to least recently used by creating a linked list
# map will hold KV pairs, along with prev & next pointers
# will maintain head and tail pointers, tail is least recently used
# get and set move nodes to front
    def __init__(self, capacity: int):
        self.map = {}
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.map.keys():
            node = self.map[key]
            # remove node from position
            self._remove(node)

            # place at front
            self._insert(node)

            return node.val
        
        return -1



    def put(self, key: int, value: int) -> None:
        # if over capacity, remove least recently used
        if key not in self.map.keys():
            if len(self.map.keys()) >= self.capacity:
                self._remove(self.tail.prev)

            new_node = Node(value, key, prev = self.head, next = self.head.next)
            self._insert(new_node)

        else:
            node = self.get(key)
            self.map[key].val = value

    
    def _remove(self, node):
        # remove node from position
        temp1 = node.prev
        temp2 = node.next
        temp1.next = temp2
        temp2.prev = temp1
        self.map.pop(node.key)

    def _insert(self, node):
        # place at front
        node.prev = self.head
        node.next = self.head.next
        self.head.next = node
        node.next.prev = node
        self.map[node.key] = node

