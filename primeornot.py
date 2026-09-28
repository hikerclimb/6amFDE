number = 3

def primeornot(number):
    for i in range(2, number+1 , 1):
        if(number %  i > 0 ):
            continue
        elif(number == i):
            print(number)
            return True
        else:
            return False

print(primeornot(number))