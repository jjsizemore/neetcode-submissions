class HashTable:
    
    def __init__(self, capacity: int):
        self.map = {}
        self.capacity = capacity

    def insert(self, key: int, value: int) -> None:
        if key not in self.map and len(self.map) + 1 >= self.capacity / 2:
            self.resize()
        self.map[key] = value

    def get(self, key: int) -> int:
        if key in self.map:
            return self.map[key]
        return -1

    def remove(self, key: int) -> bool:
        if key in self.map:
            self.map.pop(key)
            return True
        return False

    def getSize(self) -> int:
        return len(self.map)

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        self.capacity *= 2
