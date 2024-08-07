num = int(input())
num_list = list(map(int,input().split()))

print(f"리스트 최댓값 {max(num_list)}")
print(f"리스트 최솟값 {min(num_list)}")
print(f"리스트 평균값 {sum(num_list)/num}")