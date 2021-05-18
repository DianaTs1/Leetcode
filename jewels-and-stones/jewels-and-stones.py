class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        output = 0
        
        for jewel in jewels:
            for stone in stones:
                if jewel == stone:
                    output +=1
        
        return output