# 클래스 변수
#객체변수는 다른 객체들의 영향을 받지 않고 독립적으로 그 값으로 유지한다는 점을 알았다.
#이번엔 좀 다른 클래스 변수에 대해 알아보자

# 클래스 변수를 작성했다.

class Family:
    lastname = "김"

# print(Family.lastname)
# Family 클래스에 선언한 lastname이 바로 클래스 변수이다.

# 클래스 변수는 클래스 안에 함수를 선언하는 것과 마찬가지로 클래스 안에 변수를 선언하여 생성한다.
# 클래스 변수는 위 예와 같이 "" 클래스이름. 클래스 변수"" 로 사용된다.

a = Family()
b = Family()

# print(a.lastname)
# print(b.lastname)

# 만약 Famlily 클래스의 lastname을 바꾸고 싶으면  어떻게 해야할까

Family.lastname = "박" 

print(a.lastname)
print(b.lastname)


