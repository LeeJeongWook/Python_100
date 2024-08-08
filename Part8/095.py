left  = ['초록', '초록', '빨강', '노랑', '노랑', '파랑', '남색', '보라']
right = ['파랑', '초록', '초록', '보라', '보라', '노랑', '빨강', '빨강', '파랑']

def makit(left,right):
    color = ['빨강', '주황', '노랑', '초록', '파랑', '남색', '보라']

    # num = [0]*len(color) 또는 num = [0 for i in range(7)]

    #left_num = [0, 0, 0, 0, 0, 0, 0] # 무지개 색깔 순서대로 왼손 장갑 개수
    #right_num = [0, 0, 0, 0, 0, 0, 0] # 무지가 색깔 순서대로 오른손 장갑 개수
    
    total = int(0)
    for i in color:
        pair = int((left.count(i) + right.count(i)) / 2)
        print(f"{i} 색으로 만들 수 있는 장갑은 {pair} 개")
        total += pair

    return total
print('최대로 만들 수 있는 장갑 쌍은', makit(left,right), '개')