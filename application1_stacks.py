# Matching Paranthesis in an arithemetic expression using Stacks
# Problem  : To match paranthesis ([{}])
# Logic :
# For opening paranthesis (, {, [ in an expression, push it to Stack
# For closing paranthesis ), }, ] in an expression, pop it. We need to match that the popped value is matching to its 
# corresponding closing paranthesis. 
# Return True if there is empty Stack

from stacks import StacksList, EmptyStackException

OPENING_PARANTHESIS = '(, {, ['
CLOSING_PARANTHESIS = '), }, ]'

def checkExpression(expr):
    S = StacksList()
    for x in expr:
        if x in OPENING_PARANTHESIS:
            S.push(x)
        elif x in CLOSING_PARANTHESIS:
            if S.isEmpty():
                return False
            retValue = S.pop()
            # Rather than using switch statement to compare the paranthesis, we use index to get the value
            if OPENING_PARANTHESIS.index(retValue) != CLOSING_PARANTHESIS.index(x): 
                return False
    return S.isEmpty()

print checkExpression('[(x+2)]')
print checkExpression('{[()]}')
print checkExpression('{[((')
print checkExpression(')}')
print checkExpression('{(}))}')
print checkExpression('((())')