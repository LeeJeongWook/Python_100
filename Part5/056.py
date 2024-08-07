a = int(input("첫 번째 숫자를 입력하세요"))
b = int(input("두 번째 숫자를 입력하세요"))
result = 0
for i in range(a, b+1):
    result += i
    if i == b:
        print(i, end='')
        print('=', result)
        break
    print(i, end='')
    print('+', end='')