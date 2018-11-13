result=[]
n=int(input())
for f in range(n):
    s=input()
    sl=len(s)
    k=0
    l=sl-1
    for j in range(int(sl/2)):
        if((s[k]=='(' and s[l]==')') or (s[k]=='{' and s[l]=='}') or (s[k]=='[' and s[l]==']')):
            k=k+1
            l=l-1
        else:
            break
    if(k>j):
        temp='YES'
        result.append(temp)
    else:
        temp='NO'
        result.append(temp)

for r in range(len(result)):
    print(result[r])
