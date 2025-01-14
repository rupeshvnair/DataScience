import pdb
class Solution(object):
    def canBeValid(self, s, locked):
        #pdb.set_trace()
        if len(s) % 2 != 0:
            return False
        for i in range(len(s)):
            if (i%2 == 0 and (s[i]!='(' or locked[i]!='0')):
                return False
            elif (i%2 != 0 and (s[i]!=')' or locked[i]!='0')):
                return False
            else:
                return True