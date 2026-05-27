class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        count = {}

        for i in range(len(nums)):
            count[nums[i]] = count.get(nums[i], 0) + 1


        for key, value in count.items():
            if value > 1:
                return True

        return False


