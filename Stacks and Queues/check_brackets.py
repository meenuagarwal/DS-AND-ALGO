# python2

# Code to check if brackets are balanced and return the index of first unbalanced bracket.
import sys

class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False

if __name__ == "__main__":
    text = raw_input()
    res = "True"
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next == '(' or next == '[' or next == '{':
            # Process opening bracket
            opening_brackets_stack.append(Bracket(next,i))

        if next == ')' or next == ']' or next == '}':
            # Process closing bracket
            if (not opening_brackets_stack):
                print (i+1)
                res = "False"
                break
            else:
                popped = opening_brackets_stack.pop()
                if (popped.Match(next) == False):
                    print (i+1)
                    res = "False"
                    break

    if (res == "True"):
        if (len(opening_brackets_stack) == 0):
            print ("Success")
        else:
            unmatched = opening_brackets_stack.pop()
            print (unmatched.position + 1)




   
