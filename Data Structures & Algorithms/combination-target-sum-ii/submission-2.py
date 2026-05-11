class Solution:

    def comb(self, i, candidates, target, newl, result):
        
        if i > len(candidates) - 1:
            if target == 0:
                result.append(newl[:])
                return
            else:
                return
        
        if target == 0:
            result.append(newl[:])
            return
        
        if target < 0:
            return

        for j in range(i, len(candidates)):
            if j > i and candidates[j] == candidates[j-1]:
                continue
            newl.append(candidates[j])
            self.comb(j+1, candidates, target - candidates[j], newl, result)
            newl.pop()


    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        result = []
        newl = []


        candidates.sort()

        self.comb(0, candidates, target, newl, result)

        return result
        