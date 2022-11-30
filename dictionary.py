# 딕셔너리 구조 키 : 값

dic_fir = { }
dic_sec = { 'cho' : 24 , 'lee' : 29 , 'gu' : '고양 '}
dic_thr = { 'yoongu' : 'men', 'hobby' : ['baskball', 'music', 'game' ]}

#복사
dic_fir = dic_sec.copy()

# 키 목록 생성
seq = ('data', 'time', 'age')
dic_sec = dic_fir.fromkeys(seq,5)

#대응키확인
print('cho' in dic_sec)

# 키에의 주소
print(dic_thr['yoongu'])

#  키 추가 삭제
dic_sec['style'] = 'cute'
print(dic_sec)

#  키 추가 삭제
# del dic_thr['hobby']
# print(dic_thr)

print(len(dic_sec))
print(str(dic_thr))
print(dic_fir)






