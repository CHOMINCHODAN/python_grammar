# 함수안에서 선언한 변수를 밖에서 사용가능한지

a = 1
def vartest(a):
    a = a + 1

vartest(3)
print(a)

