def gg(fn,*args,rep,**kwargs):
    print(fn)
    for h in range(rep):
        fn(*args,**kwargs)

gg(print,1,2,3,sep="-",end="_*\n",rep=5)


    print(*args,**kwargs)

def aa(*args,**kwargs):
    print(*args,**kwargs)

for h in range(5):
    aa(1,2,3,sep="*",end="_\n")