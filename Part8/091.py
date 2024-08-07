hawaii = {'윤진', '시은', '우진'}
italia = {'형우', '윤진', '시은'}
dubai = {'시은', '우진', '메이킷'}

print('하와이, 이탈리아, 두바이 모두 여행을 다녀온 사람은?')
name = hawaii & italia & dubai # & 교집합 연산을 통해 하와이,이탈리아,두바이 모두 다녀온 사람 집합 만들기 
print(name)

print('하와이 또는 이탈리아 여행을 다녀온 사람은?')
name = hawaii | italia  # | 합집합 연산을 통해 하와이 또는 이탈리아 둘 중에 한 곳이라도 다녀온 사람 집합 만들기
print(name)

print('두바이 여행은 다녀왔고 하와이와 이탈리아 여행 경험이 없는 사람은?')
name = dubai - hawaii - italia # - 차집합 연산을 통해 집합에서 다른 집합의 원소를 빼기
print(name)