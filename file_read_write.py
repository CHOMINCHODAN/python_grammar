# 파일 생성하기
# open 함수는 다음과 같이 "파일이름" 과 "파일 열기 모드"를 입력값으로 받고 결과값으로 파일 객체를 리턴한다.
#file = open("새파일.txt",'w')


# 파이썬에서는 sys 모듈을 사용하여 프로그램에 인수를 전달가능
# sys 모듈을 사용하려면 아래 예의 import sys처럼 import 명령어를 사용

# r - 읽기모드
# w - 쓰기모드
# a - 추가모드

# 파일 기본적인 생성  
# f = open("C:/Users/User/python_self/filemake.txt", 'w') # 파일 경로와 슬래시(/)를 사용한다 (\) 사용 시 \n과 같은 이스케이프 문자가 있는 경우 줄 바꿈으로 인식
# f.close()
# 항상 라인 오픈 후 close를 확인한다.

f = open("C:/Users/User/python_self/filemake.txt", 'w', encoding="UTF-8" ) #한글로 출력 시 깨실 유니코드 적어준다.

for i in range(1,11):  # range 함수 range(start, stop) 반복가능(iterable)하기 때문에 for문을 사용해 출력할 수 있다.
    data = "%d번째 줄 입니다 \n" % i
    f.write(data) # 기존의 print 문과 다르게 f.readline()으로 기록한다.
f.close()




# 파일 읽기 방식 (여러가지)
# 파이썬은 ANSI 기준으로 작성된 파일 읽어 오기깨문에  encoding="UTF-8" 로 작성

# 1. readline 함수를 사용한다. 

# 한줄만 출력

# f = open("C:/Users/User/python_self/filemake.txt", 'r', encoding="UTF-8" )
# line = f.readline() # readline() 한줄씩 출력
# print(line)
# f.close()

# 모든줄 출력

# f = open("C:/Users/User/python_self/filemake.txt", 'r', encoding="UTF-8" )
# while True:
#     line = f.readline() 
#     if not line: break # if문으로 만약 문장이 끝날시에 break 해준다.
#     print(line)
# f.close()

# 사용자가 입력을 받아서 출력하는 문의 경우

# while True:
#     data = input()
#     if not data: break
#     print(data)

# 2. readlines 함수 사용하기


#readlines 함수는 파일의 모든 줄을 읽어서 각각의 줄을 요소로 갖는 리스트를 리턴한다.

f = open("C:/Users/User/python_self/filemake.txt", 'r', encoding="UTF-8" )
line = f.readlines()
for line in f:
    print(line)
f.close

# 추가 : 줄 바꿈 현상을 막고 싶으면 뒤에 (strip) 함수를 사용해서 \n을 제거 해준다.

f = open("C:/Users/User/python_self/filemake.txt", 'r', encoding="UTF-8" )
lines = f.readlines()
for line in lines:
    line = line.strip()  # 줄 끝의 줄 바꿈 문자를 제거한다.
    print(line)
f.close()


# 3. read 함수를 사용해준다.  'r' = 읽기

f = open("C:/Users/User/python_self/filemake.txt", 'r', encoding="UTF-8" )
data = f.read()
print(data)
f.close()

 
# 4. 파일 객체를 for문과 함께 사용하기 #왜 인지 모르겠는데 읽는 방식과 다르게 간격이 생기네여? 왜지

f = open("C:/Users/User/python_self/filemake.txt", 'r', encoding="UTF-8" )
for line in f:
    print(line)
    f.close


# 파일에 새로운 내용을 추가하기  a - 추가하기
# 우리가 쓰기 모드('w')로 파일을 열 때 이미 존재하는 파일을 열면 그 파일의 내용이 모두 사라지게 된다
# 하지만 원래 있던 값을 유지하면서 단지 새로운 값만 추가해야 할 경우에 사용

f = open("C:/Users/User/python_self/filemake.txt", 'a' )
for i in range(11, 20):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
    f.close()

# for i in range(11,20): # for문에서 사용하는 range
#     data = "a를 사용해서 새로운 %d번째 줄 입니다\n" %i
#     f.write(data) # write문을 사용해서 저장 
#     f.close()

