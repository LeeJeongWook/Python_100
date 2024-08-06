count = int(0)
for i in range(1,1001):
    i = str(i)
    count += i.count('7')
print(count)