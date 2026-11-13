class Solution:
    def isPalindrome(self, s: str) -> bool:

        def characters(txt):
            txt = txt.lower()
            if ord("a") <= ord(txt) <= ord("z") or ord("0") <= ord(txt) <= ord("9"):
                return False
            else:
                return True
        
        i = 0
        j = len(s) - 1

        while i <= j:
            while i < j and characters(s[i]):
                i += 1
            while i < j and characters(s[j]):
                j -= 1
            
            if s[i].lower() == s[j].lower():
                i += 1
                j -= 1
            else:
                return False
        return True