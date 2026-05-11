class Solution:

    def per(self, i, nums, result):
        
        if i == len(nums):
            result.append(nums[:])
            return

        for j in range(i, len(nums)):
            nums[i] , nums[j] = nums[j], nums[i]
            self.per(i+1, nums, result)
            nums[i], nums[j] = nums[j] , nums[i]

    def permute(self, nums: List[int]) -> List[List[int]]:

        result = []

        self.per(0, nums, result)

        return result
        