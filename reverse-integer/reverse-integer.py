class Solution:
    def reverse(self, x: int) -> int:
        xstr,ystr=str(x),str()
        if x==0:
            return x
        elif x<0:
            ystr=xstr[1:]
            if -int(ystr[::-1]) < -2**31:
                return 0
            else:
                return -int(ystr[::-1])
        else:
            if int(xstr[::-1]) > 2**31 -1:
                return 0
            else:
                return int(xstr[::-1])