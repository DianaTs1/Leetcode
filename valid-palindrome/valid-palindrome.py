class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.replace(" ","")
        
        list_string=[]
        for val in s:
            if val.isalnum():
                list_string.append(val)
        
        
        new_string="".join(list_string)
        new_string=new_string.lower()
        if new_string==new_string[::-1]:
            return True
        else:
            return False