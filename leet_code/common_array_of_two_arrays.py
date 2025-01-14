"""
You are given two 0-indexed integer permutations A and B of length n.

A prefix common array of A and B is an array C such that C[i] is equal to the count of numbers that are present at or before the index i in both A and B.

Return the prefix common array of A and B.

A sequence of n integers is called a permutation if it contains all integers from 1 to n exactly once.

Example 1:

Input: A = [1,3,2,4], B = [3,1,2,4]
Output: [0,2,3,4]
Explanation: At i = 0: no number is common, so C[0] = 0.
At i = 1: 1 and 3 are common in A and B, so C[1] = 2.
At i = 2: 1, 2, and 3 are common in A and B, so C[2] = 3.
At i = 3: 1, 2, 3, and 4 are common in A and B, so C[3] = 4.
"""
import pdb
#Bruteforce
class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        sol = []
        for i in range(len(A)):
            arr_1 = A[0:i+1]
            arr_2 = B[0:i+1]
            counter = 0
            for j in arr_1:
                if j in arr_2:
                    counter += 1
            sol.append(counter)
        return sol


# less time version
class Solution2(object):
    def findThePrefixCommonArray(self, A, B):
        result = []
        frequency = [0] * (len(A) + 1)
        pdb.set_trace()

        common = 0
        for i in range(len(A)):
            frequency[A[i]] += 1
            frequency[B[i]] += 1

            # если общий элемент, то +1 к общим элементам на префиксе
            if A[i] == B[i]:
                common += 1
                result.append(common)
                continue

            # если до этого уже встречали nums1[i], то +1
            if frequency[A[i]] == 2:
                common += 1
            # если до этого уже встречали nums2[i], то +1
            if frequency[B[i]] == 2:
                common += 1

            result.append(common)
        return result

A = [1,3,2,4]
B = [1,2,3,4]
obj2 = Solution2()
res = obj2.findThePrefixCommonArray(A,B)
print(res)