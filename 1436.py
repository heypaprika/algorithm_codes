N = int(input())
setA = set()
for i in range(100000):
    X = str(i)
    for ind in range(len(X)):
        setA.add(int(X[:ind] + "666" + X[ind+1:]))

Alist = list(sorted(setA))
print(Alist[N-1])
