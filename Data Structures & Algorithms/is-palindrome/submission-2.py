class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_list = s.split()
        for i in range(len(s_list)):
            res = ""
            word = s_list[i]
            for letter in word:
                if letter.isalnum():
                    res += letter
            s_list[i] = res.lower()

        cleaned = "".join(s_list)
        start,end = 0, len(cleaned)-1
        while start <= end:
            if cleaned[start] != cleaned[end]:
                return False 
            start += 1
            end -= 1

        return True
        