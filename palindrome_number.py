"""
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true

Example 2:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
"""



def isPalindrome(self, x: int) -> bool:
        number = str(x)
        left = 0
        right = len(number) - 1

        while left < right:
            if number[left] == number[right]:
                left += 1
                right -= 1
            else:
                return False
        return True
