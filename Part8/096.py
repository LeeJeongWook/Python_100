n = input('괄호의 자료를 입력하세요:')
def makit(n):
    if n[0] == ')':
        return False
    elif n.count('(') == n.count(')'):
        return True

if makit(n): # 괄호 검사 함수 호출
    print('성공')
else:
    print('실패')