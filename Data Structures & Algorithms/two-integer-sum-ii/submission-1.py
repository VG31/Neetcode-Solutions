class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        n = len(numbers)

        result = []

        i = 0

        while i <= n-2:
            j = i + 1
            while j <= n-1:
                if numbers[i] + numbers[j] == target:
                    result.append(i + 1)
                    result.append(j + 1)
                    break;

                j = j + 1

            i = i + 1
                

        return result


        