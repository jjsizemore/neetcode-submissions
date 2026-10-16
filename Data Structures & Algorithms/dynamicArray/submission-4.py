class DynamicArray:
    
    def __init__(self, capacity: int):
        self.arr = [0] * capacity
        self.length = 0
        self.capacity = capacity

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.getSize() >= self.getCapacity():
            self.resize()

        self.arr[self.length] = n
        self.length += 1

    def popback(self) -> int:
        self.length -= 1
        return self.arr[self.length]

    def resize(self) -> None:
        self.capacity *= 2
        new_arr = [0] * self.capacity
        new_arr[:self.length] = self.arr[:self.length]
        self.arr = new_arr

    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return len(self.arr)