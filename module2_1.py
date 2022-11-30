# 클래스나 변수들을 포함한 모듈

import module2
print(module2.PI)

# 결과 값 : 3.141592

# 위 예서 볼 수 있는거 처럼 module2.PI 처럼 입력하면 module2.py 의 변수 값을 가져온다.


a = module2.Math()
print(a.area(2))

# 위 예는 module2.py에 있는 Math 클래스를 사용하는 방법이다.
# 클래스를 사용 하려면 "." 도트 연산자로 클래스 이름 앞에 모듈 이름을 먼저 입력한다.

print(module2.add( module2.PI,  4.4 )) # 함수 add를 사용도 가능

# add 함수 또한 출력 가능하다.

# 중요한 부분이니 한번 더 체크 한다.


