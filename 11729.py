cal = []
def func(n,x,y):
    global cal
    if n == 0 : return
    func(n-1, x, 6-x-y)
    cal.append(str(x)+" "+str(y))
    func(n-1, 6-x-y, y)


n = int(input())
func(n,1,3)
result = ""
for c in cal:
    result += c + '\n'
print(len(cal))
print(result)
