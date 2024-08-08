name = ['메이킷', '소피아', '우진', '시은', '하워드'] # 학생 이름 리스트
score = [92, 75, 95, 96, 89] # 학생 점수 리스트

n = int(input('몇 등 학생 자료를 알고 싶나요? '))

student = {}
idx = 0
for i in name:
    student[i] = score[idx]
    idx += 1
student = list(sorted(student.items(), key=lambda x : x[1], reverse=True))

print(n, '등 학생은', student[n-1][1], '점이고 이름은', student[n-1][0], '입니다') # 결과 출력