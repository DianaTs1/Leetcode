class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        left = 0
        right = len(s)
        perm = []
        for char in s:
            if char == "I":
                perm.append(left)
                left += 1
            else:
                perm.append(right)
                right -= 1
        perm.append(right)
        return perm