from collections import defaultdict
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count=[0]*26
        for i in range(len(s)):
            c,d=s[i],t[i]
            count[ord(c)-ord('a')] += 1
            count[ord(d)-ord('a')] -= 1
        
        for i in range(26):
            if count[i]!=0:
                return False
        return True 


        # m = len(t)
        # if m != n:
        #     return False
        # countS, countT = Counter(s), Counter(t)
        # print(set(s))
        # k = list(set(s))
        # for i in range(len(k)):
        #     print(k[i])
        # # print(Counter(s))
        # return Counter(s) == Counter(t)

        #Solution 3
        # countS,countT = {},{}
        
        # for i in range(n):
        #     c=s[i]
        #     if c in countS:
        #         countS[c]=countS.get(c)+1
        #     else:
        #         countS[c]=1
        #     d=t[i]
        #     if d in countT:
        #         countT[d]=countT.get(d)+1
        #     else:
        #         countT[d]=1
        # if countS == countT:
        #     return True
        # else:
        #     return False

        

        
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


              

    
        