class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)

        for i in range(len(temperatures) - 1, -1, -1):
            j = i + 1
            while j < len(temperatures) and temperatures[j] <= temperatures[i]:
                if result[j] == 0:
                    break
                else:
                    j += result[j]
            if j < len(temperatures) and temperatures[j] > temperatures[i]:
                result[i] = j - i
        
        return result
                