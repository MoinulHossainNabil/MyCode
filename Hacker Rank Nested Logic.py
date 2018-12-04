
fine=0
def calculate_fine(l1,l2):
    if(l1[2]>l2[2]):
        fine=10000
    elif(l1[2]<l2[2]):
        fine=0
    elif(l1[1]>l2[1]):
        temp=l1[1]-l2[1]
        fine=500*temp
    elif(l1[0]>l2[0]):
        temp=l1[0]-l2[0]
        fine=15*temp
    else:
        fine=0
    return fine
actual=[int(i)for i in input().split()]
expected=[int(i)for i in input().split()]
print(calculate_fine(actual,expected))
