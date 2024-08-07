num = input()
iter_count = len(num)
sum_val = int(0)
num = int(num)
for i in range(iter_count):
    sum_val += (num % 10)
    num //= 10
print(sum_val)