n=int(input())
l=[]
for i in range(n):
    temp=input()
    l.append(temp)
for i in l:
    seven=''
    sodd=''
    for j in range(len(i)):
        if(j%2==0):
            seven+=i[j]
        else:
            sodd+=i[j]
    print(seven+' '+sodd)
