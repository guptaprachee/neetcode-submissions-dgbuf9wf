class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        for i in range(len(temp)):
            prev =temp[i]
            for j in range(i+1, len(temp)):
                if temp[i] < temp[j]:
                    temp[i] =j -i
                    break
            if temp[i] ==prev:
                temp[i] =0
        return temp
        