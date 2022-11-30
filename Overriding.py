# 오버라이딩 

class Calcul: # 클래스 선언
    def __init__(self, first, second):
        self.first = first  #매소드 수행문 
        self.second  =second #매소드 수행문 
    def add(self): 
        result =self.first + self.second 
        return result  
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result
       
a = Calcul(15,20)    
# a.setdata(15,20) 
print(a.add()) 

a = Calcul(15,5)
# a.setdata(15,5) 
print(a.mul())

a = Calcul(100,1)
# a.setdata(100,1)
print(a.sub())


#나누기 오버라이딩 하기
# a = Calcul(99,3)
# #a.setdata(99,3)
# print(a.div())


print("-------------오버라이딩--------------")

# a = Calcul(4, 0)
# a.div()

# 실행시 이런 에러가 나온다 Exception has occurred: ZeroDivisionError division by zero

#만약 0으로 나눌 때 오류가 아닌 0을 리턴하도록 만들고 싶다면 어떻게 해야할까

class SafeCalcul(Calcul): #우선적으로 부모클래스를 상속을 받고
    def div(self):  # 부모클래스에 있든 메소드 (div) 나누기 기능을 가져온다. 
        if self.second == 0: # 그리고 두번째 값을 0으로 리턴하도록 수정 했다.
            return
        else:
            return self.first / self.second

# 우리가 이제 다른 SafeCalcul클래스 Calcul에 있는  div 메소드 와 동일 한이름에 메소드를 쓰고 있다.

# 이렇게 하면 부모 클래스에 있는 메소드를 동일한 이름으로 다시 만들은것을  ""메소드 모버라이딩"" 이라고 한다.

# 이렇게 메소드를 오버라이딩하면 부모클래스의 메소드 대신 오버라이딩한 메소드가 호출된다.
# 그리고 나누는 값 0인 경우에 0으로 리턴을 수정해준다, 

# 그리고 다시 한번 더 부모클래스(Calcul) 대신 SafeCalcul 클래스를 사용해본다.
a = SafeCalcul(4,0)
print(a.div())
# 놀랍게도 두번째 값이 0이라 내가 적은 99가 그대로 출력된다.


