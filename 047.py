data = list(map(float,input().split()))

bmi = float(data[1] / ((data[0] * 0.01) * (data[0] * 0.01)))

if bmi < 18.5:
    result = "저체중입니다"
elif 18.5 <= bmi < 23:
    result = "정상 체중입니다"
elif(23 <= bmi < 25):
    result = "과체중입니다"
elif(25 <= bmi < 30):
    result = "경도 비만입니다"
else:
    result = "고도 비만입니다"

print("BMI 지수는", bmi, "이고", result)