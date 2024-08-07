def makit(n1, n2):
    return sum(range(n1, n2 + 1))

n1 = int(input('첫 번째 숫자를 입력하세요'))
n2 = int(input('두 번째 숫자를 입력하세요'))

result = makit(n1, n2)
print(f"{n1} + ... + {n2} = {result}")