class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result=[]
        for i in range(left,right+1):
            flag=1
            if(str(i).count("0")==0):
                lis = list(str(i))
                for j in range(len(lis)):
                    if(i%int(lis[j])!=0):
                        flag=0
                        break
                if(flag==1):
                    result.append(i)
        return result
        