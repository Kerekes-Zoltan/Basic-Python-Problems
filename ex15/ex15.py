
priority = {
    '+': 0,
    '-': 0,
    '*': 1,
    '/': 1
}

def check(operator1, operator2):
    return priority[operator1] >= priority[operator2]

print(check('*','-'))
print(check('+','-'))
print(check('+','*'))