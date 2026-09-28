first = 0
second = 1
print(first)
print(second)
i = 0
while(first + second < 1000):
    temp = first
    first = second
    second = temp + second
    print(second)