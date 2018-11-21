n=int(input())
res=[]
eq="="
d=dict(input().split() for i in range(n))
try:
    while True:
        q=input()
        if(q==''):
            break
        if q in d.keys():
            temp=q+eq+d[q]
            res.append(temp)
        if q not in d.keys():
            temp='Not found'
            res.append(temp)
except EOFError:
    pass

for i in range(len(res)):
    print(res[i])
