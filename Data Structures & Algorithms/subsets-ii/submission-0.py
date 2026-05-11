class Solution:

    def subset(self, i, nums, result, newl, seen):
        
        if tuple(newl) not in seen:
            result.append(newl[:])
            seen.add(tuple(newl))

        for j in range(i, len(nums)):
            newl.append(nums[j])
            self.subset(j+1, nums, result, newl, seen)
            newl.pop()


    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        result = []

        newl = []

        seen = set()

        self.subset(0, nums, result, newl, seen)

        return result
        