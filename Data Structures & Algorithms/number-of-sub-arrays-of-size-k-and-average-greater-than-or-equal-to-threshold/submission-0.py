class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        #arr.sort()
        count =0
        initCount=0
        l=0
        r= k
        for i in range(k):
            initCount+=arr[i]
        if initCount//k >=threshold:
            count+=1
        while r< len(arr):
            initCount-= arr[l]
            initCount += arr[r]
            l+=1
            r+=1
            avg =initCount//k
            print(avg)
            if  avg>=threshold:
                count+=1
        return count

            

        
        