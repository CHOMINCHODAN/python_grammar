# 2  while문을 사용해 1부터 1000까지 자연수 중에 3의 배수의 합을 구하라
result = 0
i = 1

while i <= 1000:
    if i % 3  == 0:
        result = result + i
    i += 1
    print(result)

# 3 while 문으로 피라미드 만들기

i =0
while True:
    i += 1
    if i > 5:
        break
print('*'*i)



