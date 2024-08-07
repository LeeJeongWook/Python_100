a = int(input("첫 번째 숫자를 입력하세요"))
b = int(input("두 번째 숫자를 입력하세요"))

result = int(0)

for i in range(a, b+1):
    if not (i % 2):
        result += i

print(f"{a}부터 {b}까지 짝수들만의 합은 {result}")