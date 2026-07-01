class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_s = "".join([char for char in s if char.isalnum()])
        isPal = True

        for i in range(len(cleaned_s)):
            if i >= (len(cleaned_s)/2) or isPal == False:
                break

            isPal = cleaned_s[i].lower() == cleaned_s[len(cleaned_s) - 1 - i].lower()

        
        return isPal



        