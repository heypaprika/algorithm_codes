# Pypy3

N = int(input())
array = []
for i in range(N):
    array.append(int(input()))


print(*sorted(array), sep='\n')
# print(sorted())

