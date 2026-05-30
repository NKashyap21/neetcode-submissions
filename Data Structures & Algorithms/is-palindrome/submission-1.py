class Solution:
    def isPalindrome(self, s: str) -> bool:
        joined_str = "".join(word for word in s.split())
        lower_case = joined_str.lower()
        final_str = "".join(letter for letter in lower_case if letter.isalnum())

        start,end = 0,len(final_str)-1
        while start <= end:
            if final_str[start] != final_str[end]:
                return False
            start += 1
            end -= 1
        
        return True 
