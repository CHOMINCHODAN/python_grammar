# 모듈이랑 무엇인가?
# 함수와 변수 또는 클래스를 모아 놓은 파이썬 파일이다.

# 모듈은 다른 파이썬 프로그램에서 불러와 사용할 수 있게끔 만든 파이썬 파일이라고 할 수 있다.

# 매우매우매우 간단한 모듈 만들기를 한번 해보자

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

if __name__ == "__main__":
    print(add(1, 4))
    print(sub(4, 2))

# 명령 프론포트가서 그 디렉토리 들어가서  파일을 열면
# 2022-11-25  오후 02:35               393 module1.py 오 이렇게 형식이 나온다.

# 그다음 일단 import module1.py 모듈을 불러오자

# import는 이미 만들어 놓은 파이썬 모듈을 사용할 수 있게 해주는 명령어 이다!!!

# 우리가 이제 module.py를 부르기 위해서는 import를 사용한다. 
# 지금 module에 있는 add 함수를 사용하기 위해서는 위 예의 module1.add 처럼 모듈 이름 뒤에 "." (도트 연산자)를 붙이고 함수 이름을 쓰면 된다.

# 2. 우리가 이제 여기에 추가로 add, sub를 사용 한다면

# print(add(100,200))
# print(sub(100,200))

# import 할때 자동으로 값이 출력된다 이를 방지 하기위해서

# 우리가 if __name__ == "__main__" 을 사용하면 
# C:\doit>python mod1.py처럼 직접 이 파일을 실행했을 때는 __name__ == "__main__"이 참이 되어 if문 다음 문장이 수행된다. 

# _name__ 란?
# 변수는 내부적으로 사용하는 특별한 변수 이름이다.
# C:\doit>python mod1.py처럼 직접 mod1.py 파일을 실행할 경우 mod1.py의 __name__ 변수에는 __main__ 값이 저장된다. 
# 하지만 파이썬 셸이나 다른 파이썬 모듈에서 mod1을 import 할 경우에는 mod1.py의 __name__ 변수에는 mod1.py의 모듈 이름 값 mod1이 저장된다.