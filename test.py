s = [int(i) for i in input().split()]
t = []
l = len(s)-1
i = 0
j = 0
if len(s) == 1:
    print()
else: 
    s.sort()
    for st in s:
        if s[i] in t:
            i += 1
            continue
        if i == l:
            break
        elif s[i] == s[i+1]:
            t.append(s[i])
            i += 1
        elif s[i] != s[i+1]:
            i += 1
            continue
    for st2 in t:
        print(str(t[j])+' ',end='')
        j +=1
