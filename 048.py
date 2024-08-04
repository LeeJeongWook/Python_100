triangle = list(map(int,input().split()))

longest = triangle.pop(triangle.index(max(triangle)))

if triangle[0] + triangle[1] > longest:
    print("삼각형 가능")
else:
    print("삼각형 불가")