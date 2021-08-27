class Solution:
    def romanToInt(self, s: str) -> int:
        dt = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
              'C': 100, 'D': 500, 'M': 1000}
        length = len(s)
        total = 0
        for index in range(length-1):
            num = dt.get(s[index])
            if num >= dt.get(s[index+1]):
                total += num
            else:
                total -= num
        return total+dt.get(s[-1])