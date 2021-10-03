class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for i in "abcdefghijklmnopqrstuvwqyz":
            if len(s) != len(t):
                return False
            s=s.replace(i, "")
            t=t.replace(i, "")
        
        return True