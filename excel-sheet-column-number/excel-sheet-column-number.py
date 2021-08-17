class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        coefficient=0
        answer=0
        for i in columnTitle:
            value=ord(i)%64
            answer=(coefficient*26)+value
            coefficient=answer
        return answer