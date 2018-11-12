top=-1
l=[]
def push(x):
    global top
    top=top+1
    l.append(x)
    print("Push Performed",l)
def pop():
    global top
    if(top<0):
        print("Stack is empty so popping can't be performed")
    else:
        l.remove(l[top])
        top=top-1
        print("Pop performed",l)
push(2)
push(3)
push(4)
pop()
push(5)
