# for문
# for 변수 in 리스트(또는 튜플, 문자열):
#     수행할 문장1
#     수행할 문장2


#1
ex_list = ['one', 'two', 'three']

for i in ['one', 'two', 'three']:
    print(i)

#2
ex_tuple = [(1,2), (3,4), (5,6)]

for (fir, last) in ex_tuple:
    print(fir + last)

#3 총 5명의 학생이 시험을 보았는데 시험 점수가 60점 이상이면 합격이고 그렇지 않으면 불합격이다. 합격인지 불합격인지 결과를 보여 주시오.
# marks = [90, 25, 67, 45, 80]
#
# count =0
# for pas in marks:
#     count = count + 1
#     if pas >= 60:
#
#         print("%d번 학생 합격입니다" %count)
#     else:
#         print("%d번 학생 불합격입니다" % count)

    # if pas > 60:
    #     print("합격입니다")
    # else:
    #     print("불합격입니다")

    # if print(pas) > 60 :
    #     print("합격입니다!")
    # else:
    #     print("불학격입니다")
    #     break

#4 for 문과 continue
# 앞에서 for문 응용 예제를 그대로 사용해서 60점 이상인 사람에게는 축하 메시지를 보내고 나머지 사람에게는 아무 메시지도 전하지 않는 프로그램

# marks = [90, 25, 67, 45, 80]
#
# count =0
# for pas in marks:
#     count = count + 1
#     if pas >= 60:
#
#         print("%d번 학생 합격입니다" %count)
#     else:
#         continue
#         print("%d번 학생 불합격입니다" % count)
#

# for문과 자주쓰는 갓 range

# a =range(1,11)
# print(a)
# range 특징은 마지막 숫자를 제외한다

add = 0
for i in range(1, 11, 2):
    add = add + i
    print(add)

# range 함수를 통해서
marks = [90, 25, 67, 45, 80]

for number in range(len(marks)):
    if marks[number] < 60:
        continue
    print("%d번 학생 합격입니다" %(number+1))

    


