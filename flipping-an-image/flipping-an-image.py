class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        
        reversed_image = []
        
        for i in image:
            flipped_list = i[::-1]
            for j in range(len(flipped_list)):
                if flipped_list[j] == 0:
                    flipped_list[j] = 1
                else:
                    flipped_list[j] = 0
            reversed_image.append(flipped_list)
                
        return reversed_image