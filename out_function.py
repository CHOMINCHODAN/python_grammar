# 외장 함수들 

# 라이브러리에서 가져오는 경우
# 대표적인 유명한 외작 함수들 소개 하면

#pickle 
# 딕셔너리 데이터를 저장하는것

import pickle
import time
import random
import webbrowser

f = open("test.txt", 'wb')
data = {1: 'python', 2: 'you need'}
pickle.dump(data, f)
f.close()

# time
# 현재 시간을 초로 나타낸다.

print(time.time())


# 1초씩 쉬어라
import time

for i in range(5): # 오랜만에 for과 함께 하는 range 함수 오 쉣~
    print(i)
    time.sleep(1) # 1초씩 텀을준다.

# 자주쓰는 random

lotto = sorted(random.sample(range(1,46),6))
print(lotto)

#wed 브라우저 오픈

webbrowser.open("https://www.youtube.com/watch?v=KL1MIuBfWe0")

