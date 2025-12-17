B = list(map(int, input().split()))

n = len(B) // 2
result = []

for i in range(n):
    result.append(B[i])
    result.append(B[i + n])

print(result)
