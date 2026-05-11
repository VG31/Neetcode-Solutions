class Solution:

    def comb(self, i, target, nums, result, newl):
        if i > len(nums) - 1:
            if target == 0:
                result.append(newl[:])
            else:
                return
        
        if target < 0:
            return 

        if target == 0:
            result.append(newl[:])

        for j in range(i, len(nums)):
            newl.append(nums[j])
            self.comb(j, target - nums[j], nums, result, newl)
            newl.pop()


    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        result = []

        newl = []

        self.comb(0, target, nums, result, newl)

        return result



        