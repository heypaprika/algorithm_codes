N, M = map(int, input().split(" "))
array = []
for i in range(N):
    array.append(input())

str1 = "WBWBWBWB"
str2 = "BWBWBWBW"
result = 1000000

for i in range(N-7):
    for j in range(M-7):
        cnt1 = cnt2 = 0
        for num, elem in enumerate(array[i:i+8]):
            for idx in range(8):
                if num % 2 == 0:
                    if elem[j+idx] != str1[idx]:
                        cnt1 += 1
                    if elem[j+idx] != str2[idx]:
                        cnt2 += 1
                else :
                    if elem[j+idx] != str2[idx]:
                        cnt1 += 1
                    if elem[j+idx] != str1[idx]:
                        cnt2 += 1
        if result > min(cnt1, cnt2):
            result = min(cnt1, cnt2)
print(result)
