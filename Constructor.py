print("------------ 생성자 (Constructor) --------------")

# 생성자에 관해서 __init__
#위 코드를 이용해보자

# a= Calcul()
# a.add()

# Exception has occurred: AttributeError
# 'Calcul' object has no attribute 'first' 에러 메세지가 발생 한다.

# 왜냐 하면 setdata 라는  메소드 를 수행하는데 객체 a의 객체 변수 first 랑 second가 생성되기 때문이다.
# 이렇게 객체의 초깃값을 설정해야 할 필요가 있는 메소드인 (setdata)을 부르것 보다는 
# 생성자(constructor)을 사용해서 구형하는것이 안전한 방법이다.

# 결론적으로 생성자란 객체가 생성될 때 자동으로 호출되는 메서드를 의미한다.

# python에서 이름으로 __init__를 사용하면 이 메소드는 생성자가 된다.


class Calcul: # 클래스 선언
    def __init__(self, first, second): # 함수(메소드) 생성 ( 맨 처음 오는 매개 변수 객체 그 자체 두에 오는건 값들) 
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
       

a = Calcul(15,20)    # 이제 클래스에 관련한 객체 (인스턴스 생성)
# a.setdata(15,20) # 객체 안에 (first 와 second 생성 )
print(a.add()) # 함수 출력해준다.

a = Calcul(15,5)
# a.setdata(15,5) 
print(a.mul())

a = Calcul(100,1)
# a.setdata(100,1)
print(a.sub())

a = Calcul(99,3)
#a.setdata(99,3)
print(a.div())

#__init__ 메서드는 setdata 메서드와 이름만 다르고 모든 게 동일하다. 
# 단 메서드 이름을 __init__으로 했기 때문에 생성자로 인식되어 객체가 생성되는 시점에 자동으로 호출되는 차이가 있다.

# 이렇게 하고 실행 하면 오류가 발생한다
# 오류가 발생한 이유는 생성자의 매개변수 first와 second에 해당하는 값이 전달되지 않았기 때문이다.

# 이렇게 하면 메소드를 선언하지 않고도 매개변수만 전달하면 출력 가능