num = int(input())
num_list = list(map(int,input().split()))
min_val = int(999)
max_val = int(0)
sum_val = int(0)

for i in num_list:
    if i < min_val:
        min_val = i
    if i > max_val:
        max_val = i
    sum_val += i

print(f"리스트 최댓값 {max_val}")
print(f"리스트 최솟값 {min_val}")
print(f"리스트 평균값 {sum_val/num}")