'''
You are given two string arrays words1 and words2.

A string b is a subset of string a if every letter in b occurs in a including multiplicity.

For example, "wrr" is a subset of "warrior" but is not a subset of "world".
A string a from words1 is universal if for every string b in words2, b is a subset of a.

Return an array of all the universal strings in words1. You may return the answer in any order.

Example 1:

Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"]
Output: ["facebook","google","leetcode"]
Example 2:

Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["l","e"]
Output: ["apple","google","leetcode"]

'''


from collections import Counter
from typing import List

class Solution(object):
    def wordSubsets(self, words1, words2):
        def count_freq(word):
            """
            Count character frequencies in a word.
            :param word: Input string
            :return: Counter dictionary of character frequencies
            """
            return Counter(word)

        # Step 1: Compute the maximum frequency requirement for each character from words2
        max_freq = Counter()
        for word in words2:
            freq = count_freq(word)
            for char in freq:
                max_freq[char] = max(max_freq[char], freq[char])

        # Step 2: Filter words1 to find universal strings
        result = []
        for word in words1:
            freq = count_freq(word)
            if all(freq[char] >= max_freq[char] for char in max_freq):
                result.append(word)

        return result
# import pdb
# class Solution(object):
#     def wordSubsets(self, words1, words2):
#         def modString(string, pos):
#             return string[:pos] + string[pos + 1:]
#
#         op = []
#
#         for i in words1:
#             val = 0
#             temp_word = i
#             for j in words2:
#                 pos = temp_word.find(j)
#                 if pos != -1:
#                     temp_word = modString(temp_word, pos)
#                     val += 1
#             if val == len(words2):
#                 op.append(i)
#         return op

