class Solution(object):
    def isValid(self, s):
        stack = []

        mapping = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char in mapping:
                # Pop the top element from the stack if it's not empty, otherwise assign a dummy value
                top_element = stack.pop() if stack else '#'
                
                # Check if the popped element is the matching opening bracket
                if mapping[char] != top_element:
                    return False
            else:
                # If it's an opening bracket, push it onto the stack
                stack.append(char)

        # If the stack is empty, all the brackets are balanced
        return not stack






    



  

