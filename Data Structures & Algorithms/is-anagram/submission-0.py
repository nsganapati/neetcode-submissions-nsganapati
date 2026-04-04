class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)
        if m != n:
            return False
        str1 = sorted(s)
        str2 = sorted(t) 
        # if k == l:
        #     return True 
        # else:
        #     return False 
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                return False
        return True    

              

    
        