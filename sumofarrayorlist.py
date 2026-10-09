array = []

def sumofarray(list, sum):
    for i in list:
        array.append(i)
    if not list:
        return sum
    else:
        sum += list.pop()
        return sumofarray(list, sum)

print(sumofarray([1,2,3], 0))