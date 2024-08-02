sticks = list(map(int,input().split()))

if(sticks.count(1) == 1):
    print('도')
elif(sticks.count(1) == 2):
    print('개')
elif(sticks.count(1) == 3):
    print('걸')
elif(sticks.count(1) == 4):
    print('윷')
elif(sticks.count(1) == 0):
    print('모')