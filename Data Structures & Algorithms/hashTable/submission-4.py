class HashNode:

    def __init__(self, key: int, value: int, next: Optional[HashNode] = None):
        self.key = key
        self.value = value
        self.next = next

class HashTable:
    
    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity
        self.table = [None] * capacity

    def hashFunction(self, key: int) -> int:
        return key % self.capacity

    def insert(self, key: int, value: int) -> None:
        node = self.getNode(key)
        if node:
            node.value = value
        else:
            self.size += 1
            while self.getSize() >= self.getCapacity() / 2:
                self.resize()
            idx = self.hashFunction(key)
            
            new_head = HashNode(key, value)

            if self.table[idx]:
                new_head.next = self.table[idx]
            self.table[idx] = new_head
        return

    def getNode(self, key: int) -> Optional[HashNode]:
        idx = self.hashFunction(key)
        cur = self.table[idx]
        while cur and cur.key != key:
            cur = cur.next
        return cur

    def get(self, key: int) -> int:
        return self.getNode(key).value if self.getNode(key) else -1

    def remove(self, key: int) -> bool:
        node = self.getNode(key)

        if not node:
            return False
        else:
            idx = self.hashFunction(key)
            dummy = HashNode(-1, -1)
            dummy.next = self.table[idx]
            cur = dummy
            while cur.next:
                if cur.next.key == key:
                    cur.next = cur.next.next
                    break
                else:
                    cur = cur.next

            self.table[idx] = dummy.next
            self.size -= 1
            return True

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        self.capacity *= 2
        new_table = [None] * self.capacity

        for node in self.table:
            cur = node
            while cur:
                idx = self.hashFunction(cur.key)
                new_table[idx] = HashNode(cur.key, cur.value, new_table[idx])
                cur = cur.next
        self.table = new_table
