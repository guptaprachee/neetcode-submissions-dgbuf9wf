class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mi= 1
        ma= 1
        final = nums[0]
        # 1,2,-3,4
        for i in nums:
            if i ==0:
                final = max(final, i)

                mi =1
                ma= 1
                continue
            temp = mi *i
            mi = min(temp, ma*i, i)
            ma = max(temp, ma*i, i)
            print(mi, ma)
            final = max(final, mi, ma, i)
        return final




        