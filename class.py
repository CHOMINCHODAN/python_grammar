# 클래스 문에 대해서
# 함수를 이용해 구현 해보는거 중요하다.

result = 0

def add(num):
    global result
    result += num
    return result

print(add(3))
print(add(4))
print(add(5))

print("--------------------------")

# 만약에 2개의 계산기가 필요한 상황이라면

result_fir = 0
result_sec = 0

def add_f(num):
    global result_fir
    result_fir += num
    return result_fir


def add_s(num):
    global result_sec
    result_sec += num
    return result_sec

print(add_f(10))
print(add_f(15))
print(add_s(14))
print(add_s(28))

print("--------------------------")
# 서로에게 아무 영향도 주지 못한다.
# 이러한 상황을 보다 효율적으로 하기 위해 클래스를  사용한다.

class Calculator:
    def __init__(self):
        self.result =0

    def __add__(self, num):
        self.result += num
        return self.result

    # def sub(self, num):
    #     self.result -= num
    #     return self.result

cal1 = Calculator()
cal2 = Calculator()

print(add_f(10))
print(add_f(15))
print(add_s(14))
print(add_s(28))
print("--------------------------")

# 클래스와 객체
# 추상적으로 표현하자면 
# 뭔가 만들때 틀을 class 라고 하고 그것으로 만들어진 것들을 객체 라고 한다.

#간단한 예를 들어보자면

# 클래스를 선언해준다. 클래스 이름은 tool로 이건 껍데기 뿐이다.
# 또한 동일한 클래스로 만들은 객체들은 서로 전혀 영향을 주지 않는다.


# 파이썬 클래스의 가장 간단한 예
# class tool:
#     pass

# 객체들 : 결괏값을 돌려받은 a와 b가 바로 객체이다.
# a = tool()
# b = tool()


# 객체와 인스턴스의 차이

# 클래스로 만든 객체를 인스턴스라도 한다. 
# 위에 작성한 비유대로 하면  a = tool() 이렇게 만든 a는 객체이다. 그리고 a 객체는 tool '인스턴스'이다.
# "a는 인스턴스"보다는 "a는 객체"라는 표현이 어울리며 "a는 tool 의 객체"보다는 "a는 tool 의 인스턴스"


# 사칙연산의 클래스 만들기

# 클래스명은 Calcul + , * , -, / 사칙연산 하기

# a= Calcul() 객체 만들기

# a.setdata(4, 2)  대입할 데이터들 지정

# print(a.add())  더하기

# print(a.mul())  곱하기

# print(a.sub())  빼기

# print(a.div())  나누기


#클레스를 만들어준다.

# class Calcul:
#     pass    # pass는 아무것도 수행하지 않는 문법으로 임시로 코드를 작성 시 사용한다.

# a = Calcul()

# print(type(a))  # 클래스를 선언하고 나서 보면 객체 a의 타입을 출력해보면 <class '__main__.Calcul'> 가 출력된다.
                # 객체 a가 Calcul의 인스턴스로 생성됬다.


# 이제부터
# 만들어진 객체에 이제 숫자를 지정해보자

class Calcul:
    def setdata(self, first, second):  # 메서드의 매개변수
                                       # setdata의 이름의 함수를 만들어주자 그엔에 있는건 전에 말했던 매개변수고    
                                       # !!!! 여기서 중요한게 앞으로 클래스 안에서 구현 된 함수를 메소드로 선언해준다. (Method) 매우매우 평생 들을 말
        self.first = first  # 메서드의 수행문
        self.second  =second  # 메서드의 수행문  


## 매우매우 즁요 ## 
## 매우매우 즁요 ## 
## 매우매우 즁요 ## 

## 메서드의 매개 변수들 ##

#위에 코드를 보면 우리가 매개변수가 3개 있는데 
# 여기서 매소드에서의 특징이 ""맨 첫번째"" 로 오는 매개변수는 self는 특별한 의미를 가진다.



class Calcul:
    def setdata(self, first, second): 
        self.first = first  #매소드 수행문 
        self.second  =second    #매소드 수행문

        a = Calcul()
        a.setdata(10,3) # a 객체를 만들고 a객체를 통해 setdata 메서드를 호출한다.

                        # 여기서 특이한점이 매개변수 self는 왜 있는걸까? 매개 변수 2개만 입력 했는데
                        # 그 이유는 setdata 메서드의 첫 번째 매개변수 self에는 setdata메서드를 호출한 객체 a가 자동으로 전달되기 때문이다.
                        # 자바같은 경우 이렇지 않는데 파이썬의 "매우매우매우" 중요하고 특이한 특징이다.



# 여기서 이제 또 중요한게 이제 
# 다시 위로 올라가서                     

# def setdata(self, first, second): 
#         self.first = first  #매소드 수행문 
#         self.second  =second    #매소드 수행문

# 아까 호출한 (10,3)처럼 이제 setdata 메서드의 매개변수 first, second에는 각 10, 3이 전달된다 그럼 이제 "메소드 수행문에 대한 이해가 편해진다."

# self.first = 10
# self.second = 3
# 아래와 같이 해석된다 대박스 오우 쉣~~

# 그리고 나아가서 self는 전달된 객체 a이르모 다시 한번 더 말하면 2번 넘어가면

# a.first = 10 이거고
# a.second -= 3 인것이다 대박이다!

# 객체에 생성되는 객체만의 변수를 객체변수라고 부른다.



class Calcul:
    def setdata(self, first, second): 
        self.first = first  #매소드 수행문 
        self.second  =second    #매소드 수행문

a = Calcul()        # 들여쓰기 매우매우 중요 왜 안되는지 10분째 고민함 ㅎ
a.setdata(10,3)
        
print(a.first)
print(a.second)     # 그럼 이제 10과 3이 출력된다.

print("--------------------------")

a =Calcul()
b =Calcul()

a.setdata(4,8)
print(a.first)

b.setdata(6,12)
print(b.first)

# 여기서 책에서 말하기 또 중요한 부분이 지금처럼 객체 b에서 first값을 6으로 주었다 그러면 a의 first값 또한 영향을 받아 6으로 되야하는거 아닌가?

print(a.first) #그런데 영향을 주지 않다.

#여기서 또 매우매우매우 중요한  """" 클래스 안에서 만들어진 객체의 객체변수는 다른 객체의 개체 변수에 상관 없이 독립적인 값을 유지한다~!!!!! """"

# 다시 정리하면 매우매우매우무 중요한 걸 했다네여
# 지금까지 나온 내용을 코드로 작성하면 딱 4줄이다.

print("------------ 사칙연산 클래스 --------------")

class Calcul: # 클래스 선언
    def setdata(self, first, second): # 함수(메소드) 생성 ( 맨 처음 오는 매개 변수 객체 그 자체 두에 오는건 값들) 
        self.first = first  #매소드 수행문 
        self.second  =second #매소드 수행문 

# 더하기 기능 만들기
    def add(self): # 더하기에 대한 메소드를 생성한다. 그리고 객체를 지정하여 위에 꺼 활용
        result =self.first + self.second # 결과를 매소드 수행문 활용
        return result  
    
    # print(a.mul())  곱하기
    # 곱하기 하다가 한가지 알게 된점 다시 한번더 함수는 항상 위에 선언하는게 중요하다. 안그럼 에러뜬다.

    def mul(self):
        result = self.first * self.second
        return result
    # print(a.sub())  빼기
    def sub(self):
        result = self.first - self.second
        return result
    # print(a.div())  나누기
    def div(self):
        result = self.first / self.second
        return result
       
print("------------ 더하기--------------")

a = Calcul()    # 이제 클래스에 관련한 객체 (인스턴스 생성)
a.setdata(15,20) # 객체 안에 (first 와 second 생성 )
print(a.add()) # 함수 출력해준다.

print("------------ 곱하기 --------------")

a = Calcul()
a.setdata(15,5)
print(a.mul())

print("------------ 빼기 --------------")

a = Calcul()
a.setdata(100,1)
print(a.sub())

print("------------ 나누기 --------------")

a = Calcul()
a.setdata(99,3)
print(a.div())









