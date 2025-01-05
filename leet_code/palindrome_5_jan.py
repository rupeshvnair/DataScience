'''
Question
You are given a string s of lowercase English letters and a 2D integer array shifts where shifts[i] = [starti, endi, directioni]. For every i, shift the characters in s from the index starti to the index endi (inclusive) forward if directioni = 1, or shift the characters backward if directioni = 0.

Shifting a character forward means replacing it with the next letter in the alphabet (wrapping around so that 'z' becomes 'a'). Similarly, shifting a character backward means replacing it with the previous letter in the alphabet (wrapping around so that 'a' becomes 'z').

Return the final string after all such shifts to s are applied.

Example 1
Input: s = "abc", shifts = [[0,1,0],[1,2,1],[0,2,1]]
Output: "ace"
Explanation: Firstly, shift the characters from index 0 to index 1 backward. Now s = "zac".
Secondly, shift the characters from index 1 to index 2 forward. Now s = "zbd".
Finally, shift the characters from index 0 to index 2 forward. Now s = "ace".

Example 2
Input: s = "dztz", shifts = [[0,0,0],[1,1,1]]
Output: "catz"
Explanation: Firstly, shift the characters from index 0 to index 0 backward. Now s = "cztz".
Finally, shift the characters from index 1 to index 1 forward. Now s = "catz".

'''


#BruteForce
s = "dztz"
shifts = [[0,0,0],[1,1,1]]
class Solution(object):
    def shiftingLetters(self, s, shifts):
        i = 0
        while i < len(shifts):
            value = shifts[i]
            step1 = value[0]
            step2 = value[1]
            converter = 1 if value[2]==1 else -1
            to_conv = s[step1:step2+1]
            converted_char = ''.join(chr((ord(c)-ord('a')+converter)%26 + ord('a')) for c in to_conv)
            s= s[0:step1]+converted_char + s[step2+1:]
            i = i + 1

new_val = Solution()
new_val.shiftingLetters(s,shifts)

#Optimized
class Solution(object):
    def shiftingLetters(self, s, shifts):
        n = len(s)
        delta = [0] * (n + 1)  # Initialize the difference array

        # Populate the difference array based on shifts
        for start, end, direction in shifts:
            delta[start] += 1 if direction == 1 else -1
            delta[end + 1] -= 1 if direction == 1 else -1

        # Compute the cumulative sum to determine net shifts
        cumulative_shift = 0
        shift_array = [0] * n
        for i in range(n):
            cumulative_shift += delta[i]
            shift_array[i] = cumulative_shift

        # Apply the shifts to the string
        result = []
        for i in range(n):
            new_char = chr((ord(s[i]) - ord('a') + shift_array[i]) % 26 + ord('a'))
            result.append(new_char)

        return ''.join(result)