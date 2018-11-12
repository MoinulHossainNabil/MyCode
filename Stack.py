top=-1
l=[]
def push(x):
    global top
    top=top+1
    l.append(x)
    print("Push Performed",l)
def pop():
    global top
    top=top-1
    l.remove(l[top])
    print("Pop performed",l)
push(2)
push(3)
push(4)
pop()
push(5)
