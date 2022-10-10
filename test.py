closing_to_opening = {
    ')': '(',
    '}': '{',
    ']': ']'
}

s = "{[]}"


def is_valid(s):
    stack = []
    opening = ['(', '{', '[']
    for c in s:
        if c in opening:
            stack.append(c)
        else:
            if stack:
                size = len(stack)
                if c in closing_to_opening.keys():
                    stack.pop()
                else:
                    return False

            else:
                return False
print(is_valid(s))