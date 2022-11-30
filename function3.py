# 함수의 리턴값은 언제나 하나이다
# 투플 형태로 리턴해준다.
# def add_and_mull(a, b):
#     return a + b, a * b
#
# result = add_and_mull(3, 4)
# print(result)

#return 다른 쓰임새


# def say_nick(nick):
#     if nick == "바보":
#         return
#     print("나의 별명은 %s 입니다." %nick)

# 매개변수에 초깃값 미리 설정하기

def say_myself(name,age, man=True):
    print('이름 %s 이다' %name)
    print('%d 살 이다' %age)
    if man:
        print('남성입니다')
    else:
        print('여성입니다')

say_myself('조윤구', 23)
say_myself('조윤구', 23, True)
say_myself("조윤구", 23, False)

#주의 해야하는점  초기화시키고 싶은 매개변수는 항상 뒤쪽에 놓아야 한다 그렇지 않으면 오류가 발생한다

# def say_myself(name, man=True, age):
#     print("나의 이름은 %s 입니다." % name)
#     print("나이는 %d살입니다." % age)
#     if man:
#         print("남자입니다.")
#     else:
#         print("여자입니다.")

#SyntaxError: non-default argument follows default argument 에러메세지 발생한다.




