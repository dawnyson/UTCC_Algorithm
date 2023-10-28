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
            #แก้ไขโดยการเพิ่ม index ไปใน stack ด้วย
            stack.push((s, i))
        elif s == ')' or s == ']' or s == '}':
            if not stack.isEmpty():
                p, index = stack.pop()

                if not ((p == '(' and s == ')') or (p == '[' and s == ']') or (p == '{' and s == '}')):
                    is_error = True
                    location.append(i)
            else:
                is_error = True
                location.append(i)

    while not stack.isEmpty():
        #กรณีเจอวงเล็บเปิด ไม่มีการปิด ทำการฟ้องทำแหน่งที่เก็บ stack ไปเลย
        p, index = stack.pop()
        is_error = True
        location.append(index)

    return is_error, location
