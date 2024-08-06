height = int(input())
tunnel = list(map(int, input().split()))
not_tunnel = list()

flag = False
for i in tunnel:
    if i <= height:
        flag = True
        not_tunnel.append(i)
if flag :
    print("터널 통과 불가능")
    for j in not_tunnel:
        print(j)
else:
    print("터널 통과 가능")