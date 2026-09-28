from collections import defaultdict

cha = 'abcded'
dic = defaultdict(int)
isalpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for j in cha:
    charkey = str(j)
    if j in isalpha:
        dic[charkey] += 1

for key in dic:
    print(key, ':' ,dic[key])