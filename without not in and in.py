s = "Python is fun"
print("th" in s) #True
print("abc" not in s) #True


string_to_find = "th"

def contains(s, string_to_find):
    if s.__contains__(string_to_find):
        print(True)
    else:
        print(False)


contains(s, string_to_find)

string_to_find = "xyz"

contains(s, string_to_find)