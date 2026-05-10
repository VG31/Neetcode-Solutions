class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.lower();

        l = 0
        r = len(s) - 1

        

        while l <= r:
            if s[l] == s[r]:
                l = l + 1
                r = r - 1
            elif not s[l].isalnum():
                l = l + 1
            elif  not s[r].isalnum():
                r = r - 1
            else:
                return False


        #print(s)

        return True

        