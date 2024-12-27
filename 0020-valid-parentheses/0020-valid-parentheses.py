class Solution(object):
    def isValid(self, s):
        stack = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i]) 
            else:
                if len(stack) == 0:
                    return False
                char = stack.pop()
                if char == '(':
                    if s[i] != ')':
                        return False
                elif char == '[':
                    if s[i] != ']':
                        return False
                elif char == '{':
                    if s[i] != '}':
                        return False
            
        return len(stack) == 0
        """
        :type s: str
        :rtype: bool
        """
        