class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        limit = 9999999999
        for i in range(len(strs)):
            if len(strs[i]) < limit:
                limit = len(strs[i])

            if strs[i] == "" or strs[i][0] != strs[0][0]:
                return ""

        for i in range(1, limit+1):
            for j in range(1, len(strs)):
                if strs[0][0:i] != strs[j][0:i]:
                    return strs[0][0:i-1]
        
        return strs[0][0:limit]