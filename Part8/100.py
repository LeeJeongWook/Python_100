a = [13, 7, 2, 199, 24, 5]

def makit_selection(a):
    for i in range(len(a)):
        print(a)
        min_val = int(999)
        idx = int(0)
        for j in range(i+1, len(a)):
            if a[j] < min_val:
                min_val = a[j]
            idx = a.index(min_val)
        if a[i] > min_val:
            a.remove(min_val)
            a.insert(idx, a[i])
            a[i] = min_val
    return a

print('최종 정렬 결과', makit_selection(a))