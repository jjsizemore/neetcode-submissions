# key -> timestamp -> value
# nested dict, key points to dict for key with timestamp -> val KV pairs

class TimeMap:

    def __init__(self):
        self.my_dict = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.my_dict[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.my_dict:
            return ""
        val_hist = self.my_dict[key]
        l, r = 0, len(val_hist) - 1

        if val_hist[0][0] > timestamp:
            return ""

        res = ""

        while l <= r:
            mid = (r - l) // 2 + l
            set_time, val = val_hist[mid][0], val_hist[mid][1]

            if timestamp == set_time:
                return val
            elif timestamp > set_time:
                res = val
                l = mid + 1
            else:
                r = mid - 1
        
        return res
