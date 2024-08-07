store = {'새우칩':1500, '옥수수칩':1800,'콜라':700,'양파칩':1300}
count = int(1)
for i in store:
    print(f"{count} 번 물품은 {i} 이고 가격은 {store.get(i)} 입니다")
    count += 1
print(f"우리 가게는 모두 {len(store)} 개 종류의 물건이 있습니다")
print(f"우리 가게 물건들의 가격 총합은 {sum(store.values())} 입니다")