# inheritance 상속
# 자바에서 상속이 있는것 처럼 우리가 파이썬에도 클래스간에 상속을 통해서  클래스에서 다른 클래스로 그 기능을 물려줄 수 있다.

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

a = Calcul(99,3)
#a.setdata(99,3)
print(a.div())


# 상속의 개념을 사용해서 (a의 b제곱) 제곱의 기능을 추가 해보자
# 클래스 이름 뒤 괄호 안에 상속할 클래스 이름을 넣어준다.

# class MoreCalcul(Calcul):
#     a = MoreCalcul(4, 2)

# a.add()

# 상속을 하는 이유는 보통 기존 클래스를 변경하지 않고 기능을 추가하거나 기본 기능을 변경하려고 할 때 사용된다.

class MoreCalcul(Calcul):
    def pow(self):
        result = self.first ** self.second
        return result

print("-------------상속----------------")

a = MoreCalcul(5, 2)
print(a.pow())

# 오 신기스 상속이 됬네요