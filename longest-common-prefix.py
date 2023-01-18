class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        for st in zip(*strs):
            if len(set(st)) == 1:
                res += st[0]
            else: 
                break
        return res
