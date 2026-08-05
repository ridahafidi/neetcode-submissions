class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        m = {}

        i = 0
        for i in range(0, len(numbers)):
            if target - numbers[i]  in m:
                return [m[target - numbers[i]] , i + 1]
            else:
                m[numbers[i]] = m.get(numbers[i], 0) + i + 1
            i += 1
        return [0, 0]