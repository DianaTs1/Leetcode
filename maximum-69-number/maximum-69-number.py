class Solution:        
        def maximum69Number (self, num: int) -> int:
            n = list(str(num))
            if n.count('6') > 0:
                n[n.index('6')] = '9'
            return int(''.join(n))