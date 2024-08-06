result = int(0)
for i in range (256):
    for j in range (256):
        for k in range (256):
            result += 1
print(f"가능한 색깔 개수는 {result}")