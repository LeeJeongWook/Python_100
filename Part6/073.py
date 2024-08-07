num = int(input())
result = list()
for i in range(1, num+1):
    if num % i:
        continue
    else:
        result.append(i)
for j in result:
    print(j, end=' ')
print()
for k in reversed(result):
    print(k, end=' ')