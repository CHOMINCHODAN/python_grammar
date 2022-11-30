import sys

# FOR 문이 랑 섞어서 출력
# a = int(input().sprit()
# print(a-543)

# k, q, r, v, n, p = map(int, input())
# chess = [k, q, r, v, n, p]
# chess_real = [1, 1, 2, 2, 2, 8]
#
# for real in range(len(chess)):
#     chess[i] = chess_real[i] - chess[i]
#     print(chess)
#

# (A+B)%C는 ((A%C) + (B%C))%C 와 같을까?
# (A×B)%C는 ((A%C) × (B%C))%C 와 같을까?

# A,B,C=map(int,input().split())

# A = 10
# B = 20
# C = 4

# line1 = (A+B) % C
# line2 = ((A % C) + (B % C)) % C
# line3 = (A*B) % C
# line4 = ((A % C)*(B % C)) % C

# print(line1)
# print(line2)
# print(line3)
# print(line4)

# 나의 이름을 만들은다.
# 

class Name:
    def name_studio(start, fir, sec, thr): # 매소드와 매개변수 선언 
        start.fir = fir 
        start.sec = sec
        start.thr = thr

    def korea(start):
        result =start.fir + start.sec + start.thr
        return result

a = Name()
a.name_studio('조','윤','구')
print(a.korea())

class Calcul: # 클래스 선언
    def setdata(self, first, second): # 함수(메소드) 생성 ( 맨 처음 오는 매개 변수 객체 그 자체 두에 오는건 값들) 
        self.first = first  #매소드 수행문 
        self.second  =second #매소드 수행문 

    def add(self): # 더하기에 대한 메소드를 생성한다. 그리고 객체를 지정하여 위에 꺼 활용
        result =self.first + self.second # 결과를 매소드 수행문 활용
        return result

a = Calcul()    # 이제 클래스에 관련한 객체 (인스턴스 생성)
a.setdata(15,20) # 객체 안에 (first 와 second 생성 )
print(a.add())