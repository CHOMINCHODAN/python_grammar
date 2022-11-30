# while 문
# tree_hit = 0
# while tree_hit < 10:
#     tree_hit = tree_hit + 1
#     print("hit count %d" %tree_hit)
#     if tree_hit == 10:
#         print("tree falldown")
#
#
# # while문을 이용한 input
# prompt = """
# 1.Add
# 2.Del
# 3.list
# 4.Quit
#
# Enter number:"""
#
# number = 0
# while number != 4:
#     print(prompt)
#     number = int(input())
#
# # while문 강제로 빠져나가기
#
# coffee = 10
# coffee_cnt = 30
# bus = 10
# money = 300
# while money:
#     print("커피구매")
#     coffee =coffee-1
#     print("coffee Left %d" %coffee)
#     if coffee == 0:
#         print("coffee end ")
#         break
#
#
# # 자판기 형식
#
# coffee = 10
# while True:
#     money = int(input("돈넣어주세용:")) # 값을넣는다
#     if money == 300:
#         print("커피 나왔습니다")
#         coffee = coffee -1
#     elif money > 300:
#         print("커피 나왔습니다")
#         print("잔돈: %d" %(money-300))
#         coffee =coffee - 1
#         print("남은커피: %d" % coffee)
#     else:
#         print("금액이 부족합니다")
#         print("남은커피: %d" %coffee)
#     if coffee == 0:
#         print("커피매진")
#         break


# while문의 맨 처음으로 돌아가기 실패 후  맨처음으로 돌아가기

a = 0
while a < 10:
    a = a + 1
    if a % 2 == 0: continue
    print(a)


    


