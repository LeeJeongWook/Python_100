student_data = {'우진':{'코딩':95, '수학':99},
           '시은':{'과학':100, '코딩':99},
           '메이킷':{'영어':85, '코딩':100}}

print(f"우진이의 코딩 점수는?{student_data['우진']['코딩']}")
print(f"시은이의 과학 점수는?{student_data['시은']['과학']}")
print(f"메이킷의 영어 점수는?{student_data['메이킷']['영어']}")
"""
student = list(student_data.keys())
print(f"{student[0]}이의 {list(student_data[student[0]].keys())[0]} 점수는?{list(student_data[student[0]].values())[0]}")
print(f"{student[1]}이의 {list(student_data[student[1]].keys())[0]} 점수는?{list(student_data[student[1]].values())[0]}")
print(f"{student[2]}의 {list(student_data[student[2]].keys())[0]} 점수는?{list(student_data[student[2]].values())[0]}")
"""