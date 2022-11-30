# 이미 만들어져 있는 함수들을 혼자 공부하겠다고 직접 만들지 않는 한 활용하느것는 것도 중요하다.

# emumerate

for i, name in enumerate(['body', 'foo', 'bar']):
    print(i, name)


# filter : 무언가를 걸러 낼때 사용 된다.

def positive(x):
    return x >0

print(list(filter(positive, [1,3,4,-2,10,-5])))

# 만약 내장 함수를 사용하지 않고 그냥 직접 작성한다면 if을 통해서 조건을 주고 복잡하게 된다.


