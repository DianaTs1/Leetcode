class Solution(object):
    def freqAlphabets(self, s): 
        
        inversed_string=s[::-1]
        final_string = ""
        
        i=0
        while i < len(inversed_string):
            if inversed_string[i] != "#":
                final_string+=chr(96+int(inversed_string[i]))
                i+=1               
            else:
                final_string+= chr( 96+int(inversed_string[i+2]+inversed_string[i+1]))
                i+=3
        return final_string[::-1]       
    
    
    