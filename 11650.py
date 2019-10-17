N = int(input())
array = []
for i in range(N):
    x, y = map(int, input().split(" "))
    array.append((x, y))
string = ""
for x, y in sorted(array):
    string += str(x) + " " + str(y) + '\n'
print(string)
