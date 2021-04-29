def r (a,c,*v,p=0):
    print(a,c,v)
    print(p)

#h=[7,8,9,0]
#r(*h,p=100)

def myfun(*g,h):
    print(h)

#myfun(h="a")

def per(g,*,h,j):
    print(g,h,j)

per(3,h='f',j='j')