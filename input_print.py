# 프로그램을 하는동안 입력과 출력에 관해서 이해
# input은 입력되는 모든 것을 문자열로 취급하기 때문에 number는 숫자가 아닌 문자열임로 출력되니 이점만 주의
#input

number = input("숫자를 입력하세요: ")
print(number)

#print문은 너무 당연하다.
#for문에 출력되는 한 줄에 결괏값을 계속 이어서 출력하려면 매개변수 end를 사용해 끝 문자를 지정
for i in range(10):
    print(i, end='')
    