from Stack import Stack

# input: str
# output: is_error : bool
# output: location : int

def bracket_check(str):
    is_error = False
    location = []
    stack = Stack()

    for i in range(len(str)):
        s = str[i]
        if s == '(' or s == '[' or s == '{':
            stack.push(s)
        elif s == ')' or s == ']' or s == '}':
            if not stack.isEmpty():
                p = stack.pop()

                if not ((p == '(' and s == ')') or (p == '[' and s == ']') or (p == '{' and s == '}')):
                    is_error = True
                    location.append(i)
            else:
                is_error = True
                location.append(i)

    if not stack.isEmpty():
        is_error = True
        location.append(i)

    return is_error, location
