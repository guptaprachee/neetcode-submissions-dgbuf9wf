class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num=0
        numstr=''
        for i in digits:
            numstr += str(i)
        num =int(numstr)+1

        result =[]
        while num:
            temp= num%10
            result.append(temp)
            num=num//10
        return result[::-1]


