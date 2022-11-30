# 매개변수에서 choice 를 고르고 for문으로 더하기 // 함수 값을 안 주워줌 그래서 출력이 안됨

# def add_many(*args):
#     result = 0
#     for arg in args:
#         result = result + arg
#     return result
#
# print(add_many(1,2,3))


def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for arg in args:
            result = result + arg
    elif choice == "mul":
            result = 1
            for arg in args:
                result = result * arg
            return result
# print(add_mul('add', 1,2,3,4)) 왜 값이 null로 나오는걸까요

print(add_mul('mul', 1,2,3,4,5,6))

