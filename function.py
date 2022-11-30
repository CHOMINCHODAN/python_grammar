# 함수의 기본의 기본 적용하는 방법
#def 함수명(매개변수)

def plus(a, b):
    return a + b
# "이 함수의 이름은 add이고 입력으로 2개의 값을 받으며 리턴값(출력값)은 2개의 입력값을 더한 값이다."

a = 3
b = 4
c = plus(a,b)
print(c)

#매개변수와 인수 혼용

def add(a,b): #매개변수 함수에 전달된 값을 저장하는 변수
    return a+b

print(add(3,4)) # 인수 함수에 전달하는 값


# 함수가 들어오고   입력값 ---> 함수 ----> 리턴값 4가지 형태로 존재한다.

# 일반적인 함수
# def 함수이름(매개변수):
#     <수행할 문장>
#     ...
#     return 리턴값

def view (a, b):
    result = a+b
    return result

# 일반적인 함수 사용법

# 리턴값을 받을 변수 = 함수이름(입력인수1, 입력인수2, ...)

# 입력값이 없는 함수

def say():
    return 'hi'

a =say()
print(a)

# 리턴값이 없는 함수

# def add(a, b):
#     print("%d, %d 의 합은  %d 입니다" % (a, b, a+b))
#
#    add(10,12)

# 입력값도 리턴값도 없는 함수

def say():
    print('HI')

    print(say())

#매개변수 지정하여 호출하기

def sub(a,b):
    return a - b

result = sub(a=7, b=3)
print(result)

# 매개변수를 지정하면 순서에 상관없이 사용 할수 있음

result = sub(b=10, a=5)
print(result)

# 여러개의 입력값을 받는 함수 만들기
# * args 지정 변수

def add_many(*args):
    result = 0
    for i in args:
        result =result + 1
        return result

    result =add_many(1,2,3)
    print(result)

# * args 지정 변수

