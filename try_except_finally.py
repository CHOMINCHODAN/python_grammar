# 예외 처리
# 오류를 처리하는 방법을 공부 하기전 

# flie = open("edd.txt" , 'r')

# 존재 하지 않는 파일을 읽기 시 가정해 하면 메세지가 뜬다 [Errno 2] No such file or directory: 'edd.txt'

# 4 / 0

# 0으로 다른 숫자를 나눌시에 오류 ZeroDivisionError에 division by zero 등등 뭐 많다 자주하는 오류들은
# 다음 오류 처리 위한 try, except문의 기본구조

# try:
#     ...
# except [발생오류 [as 오류변수]]:

# 크게 3가지 방법이 있는데

# 1. try, except만 쓰는 방법

try: 
    4 /0
except ZeroDivisionError as e:
    print(e)

print ("0으로 나눌수 없습니다") # 에러 처리를 통해서 코드가 끝까지 나오게 해줌

# 2번 try else

try: 
    f = open ('none', 'r')
except FileNotFoundError as e:
    print(str(e))
else:
    data = f.read()
    print(data)
    f.close

# 3번 파일 입력 쓰기
f = open('none', 'w')
try:
    # 무언가를 수행한다.
    data = f.read()
    print(data)
except Exception as e:
    print(e)
finally:
    f.close()

# 예외 처리를 사용 하는 경우는 DB를 자료를 왔다가 갔다 할때 트라이를 하기 위해서 아니면 프로그램이 갑자기 꺼질 수 있다.

# 일부로 오류 회피하기 FileNotFoundError 을 사용한다.

try:
    f = open("나없는파일", 'r')
except FileNotFoundError:
    pass

# 우리가 예를 들어서 부모클래스를 만들고 싶어서 자식을 변형 해서 사용하고 싶을 시 강제 처리

class Bird:
    def fly(self):
        raise NotImplementedError

class Eagle(Bird):
    def fly(self):
        print("very fast")

eagle = Eagle()
eagle.fly()