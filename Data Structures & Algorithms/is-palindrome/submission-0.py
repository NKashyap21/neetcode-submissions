class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphaNum = "".join(char for char in s if char.isalnum())
        alphaNum = alphaNum.lower()
        start ,end = 0,len(alphaNum)-1
        while start <= end:
            if alphaNum[start] != alphaNum[end]:
                return False
            start += 1
            end -= 1
        return True