n=int(input())
total=[]
for i in range(n):
    orders=input().split()
    ord=int(orders[0])
    prep=int(orders[1])
    time=ord+prep
    total.append(time)
result= sorted(range(len(total)), key=lambda k: total[k]) #i have copied this line
for r in result:
    print(r+1,end=" ")