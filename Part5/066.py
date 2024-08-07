string = input("하나의 문자열을 입력하세요:")
result = ""
for i in string:
    if i != 'a':
        result += i
print(result)