class Solution:
    
    def comb(self, i, nums, result, newl):
        
        result.append(newl[:])

        for j in range(i, len(nums)):
            newl.append(nums[j])
            self.comb(j+1, nums, result, newl)
            newl.pop()


    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        newl = []

        self.comb(0, nums, result, newl)
    

        return result