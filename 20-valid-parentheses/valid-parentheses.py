class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        valid_parenthesis = set([("(",")"),("{","}"),("[","]")])
        opening = set(["(","{","["])
        closing = set([")","}","]"])
        if len(s) <2:
            return False
        for i,elem in enumerate(s):
            
            if elem in opening: # if its opening bracket
                stack.append(elem)
                
            else: # if its closing bracket
                if stack:
                    
                    latest_elem = stack.pop()
                    if (latest_elem,elem) not in valid_parenthesis:
                        
                        return False
                else:
                    return False
        if len(stack) == 0:
            return True 
        return False

