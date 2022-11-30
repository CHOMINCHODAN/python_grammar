# import는 이미 만들어 놓은 파이썬 모듈을 사용할 수 있게 해주는 명령어 이다!!!

# 우리가 이제 module.py를 부르기 위해서는 import를 사용한다. 
# 지금 module에 있는 add 함수를 사용하기 위해서는 위 예의 module1.add 처럼 모듈 이름 뒤에 "." (도트 연산자)를 붙이고 함수 이름을 쓰면 된다.

print("------import-----")


import module1

print(module1.add(3,4))
print(module1.sub(4,2))

# import는 현재 디렉터리에 있는 파일이나 파이썬 라이브러리가 저장된 디렉터리에 있는 모듈만 불러올 수 있다. 파이썬 라이브러리는 파이썬을 설치할 때 자동으로 설치되는 파이썬 모듈을 말한다.

# 기본적인 형태는 
# [ import 모듈이름 ] 이렇게 다.

# 여기서 추가로 그 모듈에 add, 혹은 sub 처럼 모듈 이름 없이 함수만 쓰고 싶은 경우에도 사용가능하다.
# [ from 모듈이름 import 모듈함수 ] 이렇게 된다.

# 위 형태 처럼  모듈 이름을 사용하지 않고도 해당 모듈 함수를 쓸수 있다.

print("------import 특정 함수만-----")

from module1 import add

print(add(10,4))


# 다수의 함수를 사용 하고 싶으면

from module1 import add, sub

print(add(10,100))
print(sub(100,10))

from module1 import *

print(add(33,44))
print(sub(10,100))




