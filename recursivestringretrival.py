reversed_string = []

def string_reverse(strin):
    stack = []
    if not strin and not stack:
        return "".join(reversed_string)
    else:
        for i in strin:
            stack.append(i)
        reversed_string.append(stack.pop())
        return string_reverse(stack)

print(string_reverse("hello"))

reversed_string = []

print(string_reverse("Python"))