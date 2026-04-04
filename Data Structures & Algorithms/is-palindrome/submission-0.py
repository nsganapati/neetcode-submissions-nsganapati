class Solution:
    def isPalindrome(self, s: str) -> bool:
         cleaned = ''.join(char.lower() for char in s if char.isalnum())
         print(f'cleaned string {cleaned}')
         left, right= 0, len(cleaned)-1
         while left < right:
            if cleaned[left] != cleaned[right]:
                return False
            left=left+1
            right=right-1
         return True
        