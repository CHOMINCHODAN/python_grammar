# money = 'Ture'
# if money:
#     print("hello")

money = 2000
if money >= 3000:
    print("이상이다")
else:
    print("이하다")

# or
money_cho = 3000
card = 'Ture'
if money_cho >=4500 or card:
    print("지불가능")
else:
    print("불가능")

#and
money_cho = 3000
card = 'Ture'
if money_cho >=4500 and card:
    print("지불가능")
else:
    print("불가능")

#not
money_cho = 3000
card = 'Ture'
if not True:
    print("지불가능")
else:
    print("불가능")

# in, not in
# tuple을 이용한다

#list
ls = [1,2,3]
ls1 = 1 in [1,2,3]
print(ls1)

ls1 = 1 not in [1,2,3]
print(ls1)

#tuple

rastech = ('cho', 'pak', 'jeon', 'che')
menver = 'cho' in rastech
print(menver)

# if문이랑 합친거
wishlist = ['girlfirend', 'joden', 'money', 'car']
if 'girlfirend' in wishlist:
    print("여자친구있음")
else:
    print("없스어영요")


# if elif 문

wishlist = ['girlfirend', 'joden', 'money', 'car']
if 'boyfirend' in wishlist:
    print("있음")
else:
    if 'girlfirend' in wishlist:
        print("여친있음")
    else:
        print("없음")

# if문 한줄로 줄이기
pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket: pass
else:
    print("카드를 꺼내라")
    



