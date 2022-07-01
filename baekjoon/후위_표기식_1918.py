import sys

input = sys.stdin.readline

def get_op_prec(c):
    if c == '*' or c == '/':
        return 5
    elif c == '+' or c == '-':
        return 3
    elif c == '(':
        return 1
    else:
        return -1

def who_prec_op(a, b):
    a_prec = get_op_prec(a)
    b_prec = get_op_prec(b)

    if a_prec > b_prec:
        return 1
    elif a_prec < b_prec:
        return -1
    else:
        return 0

def is_alphabet(c):
    if ord(c) >= ord('A') and ord(c) <= ord('Z'):
        return True
    else:
        return False

def conv_to_rpn(expression):
    stack = []
    len_exp = len(expression)
    output = ''

    idx = 0

    for c in expression:
        if is_alphabet(c):
            output += c
        else:
            if c == '(':
                stack.append(c)
            elif c == ')':
                while True:
                    op = stack.pop()
                    if op == '(':
                        break
                    output += op
            elif c == '+' or c == '-' or c == '*' or c == '/':
                while stack and who_prec_op(stack[-1], c) >= 0:
                    output += stack.pop()
                stack.append(c)
    
    while stack:
        output += stack.pop()
    
    return output

expression = input()[:-1]

# print(expression)

print(conv_to_rpn(expression))
