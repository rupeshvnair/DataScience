class Solution(object):
    def minimumLength(self, s):
        val = len(s)
        for i in range(val):
            if i ==0:
                s = s
            elif i>=1 and i < len(s)-1 and s[i-1]==s[i] and s[i]==s[i+1]:
                s = s[0:i-1]+s[i+2:len(s)]
            else:
                s = s
            print(f"The i is {i}")
            print(f"the new s is {s}")

        return len(s)

obj = Solution()
obj.minimumLength('abaacbcbb')

