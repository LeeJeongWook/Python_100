store = {'새우칩':1500, '옥수수칩':1800,'콜라':700,'양파칩':1300}
print("물품을 입력하면 가격을 알려드립니다")
while True:
    stuff = input("물품 이름은?")
    if stuff in store:
        print(f"{stuff}의 가격은 {store.get(stuff)} 입니다")
    else:
        print(f"{stuff}는 등록되어 있지 않습니다")
        break