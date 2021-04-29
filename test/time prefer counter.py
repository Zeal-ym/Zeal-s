def ParameterValueSolver(name,aa,bb,cc,zz = None):
    if not zz:
        zz = []
    zz.append("{0} {1} {2} {3}".format(name,aa,bb,cc))
    return zz

L1 = ParameterValueSolver("bana","aa","ss","zz")

ParameterValueSolver("aa","aa","ss","zz",L1)

L2 = ParameterValueSolver("cc","cc","cc","cc")

print(L1)
print((L2))

if L1 is L2:
    print("same")
else:
    print("not same")
