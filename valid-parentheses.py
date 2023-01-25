"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'
"""

class Solution:
    def isValid(self, s: str) -> bool:
        # mapper = {")" : "(", "]": "[", "}": "{"}
        # new_str = ""
        # if len(s) % 2 != 0:
        #     return False
        # else:
        #     for i in range(len(s)//2, len(s)):
        #         mapp = str(s[i])
        #         new_str += mapper[mapp]
        #     if s[:len(s)//2] == reversed(new_str):
        #         return True 
        while '()' in s or '[]'in s or '{}' in s:
            s = s.replace('()','').replace('[]','').replace('{}','')
        return False if len(s) != 0 else True
      
      
      # Stacks data structure can also be used to solve this problem. You just have to remove one element and add another then compare the two of them.
