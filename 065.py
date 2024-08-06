amount = 1
idx = 8
for i in range(10):
    if i < 5:
        print(f"{i * ' '}{'*'}{idx * ' '}{'*'}{i * ' '}")
        idx -= 2
    else:
        i -= amount
        amount += 2
        idx += 2
        print(f"{i * ' '}{'*'}{idx * ' '}{'*'}{i * ' '}")