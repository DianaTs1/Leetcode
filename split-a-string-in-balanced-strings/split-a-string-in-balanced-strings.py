class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        answer = 0
        for ch in s:
            if ch == 'R':
                count += 1
            elif ch == 'L':
                count -= 1
            if count == 0:
                answer += 1
        return answer