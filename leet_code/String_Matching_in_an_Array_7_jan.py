class Solution(object):
    def stringMatching(self, words):
        val = len(words)
        list_val = []
        for i in range(len(words)):
            if words[i] in ('|'.join(words[0:i])+'|'.join(words[i+1:val])):
                list_val.append(words[i])
        return list_val

words = ["mass","as","hero","superhero"]
nw_obj = Solution()
value = nw_obj.stringMatching(words)
print(value)