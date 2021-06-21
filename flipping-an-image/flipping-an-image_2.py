class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        
        for i in range(len(image)):
            flipped_image= image[i][::-1]
            for j in range(len(flipped_image)):
                if flipped_image[j] == 0:
                    flipped_image[j] = 1
                else:
                    flipped_image[j] = 0
            image[i] = flipped_image
                
        return image
