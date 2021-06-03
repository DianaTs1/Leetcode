class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        longest_prefix = ""
        first_word = strs[0]

        for i in range(1, len(first_word)+1):

            for word in range(1, len(strs)):
                if first_word[:i] != strs[word][:i]:
                    break
            else:
                longest_prefix += first_word[i-1]

        return longest_prefix