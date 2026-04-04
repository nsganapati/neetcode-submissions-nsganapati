class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)
        if m != n:
            return False
        #Solution 3
        countS,countT = {},{}
        
        for i in range(n):
            c=s[i]
            if c in countS:
                countS[c]=countS.get(c)+1
            else:
                countS[c]=1
            d=t[i]
            if d in countT:
                countT[d]=countT.get(d)+1
            else:
                countT[d]=1
        if countS == countT:
            return True
        else:
            return False

        

        
        #solution 1
        # str1 = sorted(s)
        # str2 = sorted(t) 
        # if str1 == str2:
        #     return True 
        # else:
        #     return False 
        
        #solution 2
        # for i in range(len(str1)):
        #     if str1[i] != str2[i]:
        #         return False
        # return True


              

    
        