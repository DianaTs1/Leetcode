import string 

class Solution:
    def generateTheString(self, n: int) -> str:
        
#         alphabet = string.ascii_lowercase

#         final_string = ""
#         j = 0

#         for i in range(1, n, 2):
#             while i != 0:
#                 final_string+= alphabet[j]
#                 i -= 1
#             j+=1


#         return final_string


        result=""
        if(n%2==0):
            result+="a"*(n-1)+"b"
        else:
            result+="a"*n
        return result