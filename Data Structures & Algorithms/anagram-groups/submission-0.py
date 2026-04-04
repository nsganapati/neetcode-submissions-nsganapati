class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        count=0
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


            
 