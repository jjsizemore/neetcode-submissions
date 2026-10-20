from bisect import bisect_right

class TimeMap:

    def __init__(self):
        self.my_dict = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.my_dict[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.my_dict:
            return ""
        
        if self.my_dict[key][0][0] > timestamp:
            return ""

        
        idx = bisect_right(self.my_dict[key], timestamp, key = lambda x: x[0])

        return self.my_dict[key][idx - 1][1]