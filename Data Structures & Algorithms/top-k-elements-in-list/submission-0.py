class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}

        for i in nums:
            count[i] = count.get(i, 0) + 1


        result = []

        
        for num, value in sorted(count.items(), key = lambda item: item[1], reverse = True):
            if k>0:
                result.append(num)
                k -= 1
                

        return result
        