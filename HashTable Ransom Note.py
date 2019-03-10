import collections
def checkMagazine(magazine, note):
    flag=True
    m=magazine.split(" ")
    n=note.split(" ")
    for words in n:
        if words in magazine:
            countinnote=note.count(words)
            countinmagazine=magazine.count(words)
            if(countinmagazine!=countinnote):
                flag=False
                break
        else:
            flag=False
    if(flag==False):
        return "No"
    else:
        return "Yes"
mn=input().split()
m=mn[0]
n=mn[1]
magazine=input()
note=input()
result=checkMagazine(magazine,note)
print(result)