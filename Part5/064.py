idx = 1
for i in range(2,-1,-1):
    print(f"{i * ' '}{idx * '*'}{i * ' '}")
    idx += 2