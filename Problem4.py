n = int(input())
list1 = []
list2 = []
for i in range(n):
    s = input()
    l = len(s)
    p = []
    max = 0
    m = []
    for j in range(l):
        c = 0
        for k in range(j,l):
            if s[j] == s[k]:
                c +=1
                if c > max:
                    m.append(s[j])
                    max = c
                elif c == max:
                    m.append(s[j])
        p.append(c)
        
    maxx = 0
    for i in range(l):
        if maxx < p[i]:
            maxx = p[i]
            
    q = len(m)
    d = 999
    for i in range(q):
        if d > ord(m[i]):
            d = ord(m[i])
    x = chr(d)
    list1.append(maxx)
    list2.append(chr(d))
    
for i in range(n):
    print(list1[i],list2[i])       
            