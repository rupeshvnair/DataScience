import pdb
#incorrect code
# class Solution(object):
#     def canBeValid(self, s, locked):
#         #pdb.set_trace()
#         if len(s) % 2 != 0:
#             return False
#         if len(s)==2 and (s[0]=='(' or locked[0]=='0') and (s[1]==')' or locked[1]=='0'):
#             return True
#         if (s[0]=='(' or locked[0]=='0') and (s[len(s)-1]==')' or locked[len(s)-1]=='0'):
#             s = s[1:len(s)-2]
#             locked = locked[1:len(locked)-2]
#             self.canBeValid(s,locked)
#         return False

#correct code
def can_be_valid(s: str, locked: str) -> bool:
    n = len(s)

    # A valid parentheses string must have an even length.
    if n % 2 != 0:
        return False

    # Check if it can be valid by ensuring enough flexibility.
    open_needed = 0
    for i in range(n):
        if locked[i] == '0':
            open_needed += 1
        elif s[i] == '(':
            open_needed += 1
        else:
            open_needed -= 1
        if open_needed < 0:  # Too many closing parentheses encountered.
            return False

    # Check for balance in the reverse direction.
    close_needed = 0
    for i in range(n - 1, -1, -1):
        if locked[i] == '0':
            close_needed += 1
        elif s[i] == ')':
            close_needed += 1
        else:
            close_needed -= 1
        if close_needed < 0:  # Too many opening parentheses encountered.
            return False

    return True

# Example usage
s = "(()))"
locked = "01001"
print(can_be_valid(s, locked))  # Output: True or False based on the given input

s ="())(()(()(())()())(())((())(()())((())))))(((((((())(()))))("
print(len(s))
locked = "100011110110011011010111100111011101111110000101001101001111"
print(len(locked))
obj1 = Solution()
print(obj1.canBeValid(s,locked))