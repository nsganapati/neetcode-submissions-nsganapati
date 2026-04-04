class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # d = defaultdict(list)
        
        # start="".join(sorted(strs[0]))
        # d[start]=set()
        # d[start].add(strs[0])
        # for i in range(len(strs)): 
        #     for j in range(i+1,len(strs)):
        #         var="".join(sorted(strs[j]))  
        #         if var in d:
        #             d[var].add(strs[j])
        #         else:
        #             d[var]=set()
        #             d[var].add(strs[j])
        # print(d.values())
        # result=[]
        # for value in d.values():
        #     result.append(value)
        # return result


        d = defaultdict(list)
        for item in strs:
            var="".join(sorted(item))
            print(var)
            if var in d:
                d[var].append(item)
            else:
                d[var]=[item]
                
        # for value in d.values():
        print(d.values())
        return list(d.values())