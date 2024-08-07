#print("# 입력")
n = int(input())
num = n
result = int(0)
while n > 0:
    result += n
    n -= 1
#print("# 출력")
print("1부터", num, "까지 모두 더한 합은", result)