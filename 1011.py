import math
N = int(input())

A = [i**2 for i in range(100000)]

for testcase in range(N):
    x, y = map(int, input().split(" "))
    first_distance = y - x
    min_number = 0
    max_speed = 0
    for_surplus = 0
    for i in range(len(A)-1):
        if A[i] <= first_distance < A[i+1]:
            min_number = 2 * i - 1
            for_surplus = A[i]
            max_speed = math.sqrt(A[i])
            break

    surplus_distance = first_distance - for_surplus
    surplus_number = math.ceil(surplus_distance / max_speed)
    result = min_number + surplus_number
    print(result)
    
