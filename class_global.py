# 전역 변수에 대해서
# def test():
#     a = 3 # 여기서는 우리가 선언한 a는 지역 변수로 사용 되고 있다.
#     b = 2
#     return a + b
# print(test())
# print(a) # 그렇기 때문에 함수 바깥 부분에서 a를 사용이 불가능하다.


# 전체 코드에서 체크해야 하는 값이 있을 때 전역변수를 사용하면 편리하다

# 전역 변수를 선언하는 방법은 변수명 앞에 global을 붙여 준다.
def test():
    global a
    a = 3
    b = 2
    return a + b

print(test())
print(a)

# 함수 밖에서 global 전역 변수 선언하기

