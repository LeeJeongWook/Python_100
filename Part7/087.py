store = {
    '새우칩': {'가격': 1500, '개수': 3},
    '옥수수칩': {'가격': 1800, '개수': 2},
    '콜라': {'가격': 700, '개수': 4},
    '양파칩': {'가격': 1300, '개수': 1},
}
for i, (item, info) in enumerate(store.items(),1):
    print(f"{i} 번 물품은 {item} 이고 가격은 {info['가격']} 이고 수량은 {info['개수']} 개입니다")

total_stock = sum(info['개수'] for info in store.values())
total_price = sum(info['가격'] * info['개수'] for info in store.values())

print(f"우리 가게는 {len(store)} 개의 물건 종류가 있습니다")
print(f"우리 가게 모든 물건 수량은 {total_stock} 개 있습니다")
print(f"우리 가게 모든 물건들의 가격 총합은 {total_price} 입니다")
print(f"우리 가게 모든 물건들의 평균 가격은 {total_price/total_stock} 원입니다")