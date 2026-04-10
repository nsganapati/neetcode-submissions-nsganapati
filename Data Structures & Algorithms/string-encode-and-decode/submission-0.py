class Solution:

    
    def encode(self, strs: List[str]) -> str:
        fS=''
        for item in strs:
            append = str(len(item))+'#' 
            tempS=append+item
            fS=fS+tempS
        print(fS)
        return fS
            


    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0

        while i < len(s):
            # Step 1: find length
            j = i
            while s[j] != '#':
                j += 1
            
            length = int(s[i:j])

            # Step 2: extract word
            word = s[j+1 : j+1+length]
            strs.append(word)

            # Step 3: move pointer
            i = j + 1 + length

        return strs


