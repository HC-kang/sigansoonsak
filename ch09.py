phone_book = {}
phone_book['홍길동'] = '010-1234-5678'
print(phone_book)


phone_book = {
    '고길동' : '010-1234-5678'
}
print(phone_book)


dict = {'Name' : '홍길동', 'Age' : 7, 'Class' : '초급'}
print(dict['Name'])
print(dict['Age'])
print(dict['Class'])


# 딕셔너리 탐색
phone_book = {
    '홍길동' : '010-1234-5678',
    '강감찬' : '010-1111-1111',
    '이순신' : '010-3333-3333'
}

print(phone_book['강감찬'])


# 딕셔너리에서 키를 모르는 경우
print(phone_book.keys())


# 딕셔너리 출력 정리
for key in sorted(phone_book.keys()):
    print(key, phone_book[key])


# 딕셔너리에서 사용되는 모든 값
print(phone_book.values())


# 딕셔너리의 수정
phone_book['강감찬'] = '010-1234-1234' # 수정
print(phone_book)


# 딕셔너리 수정 및 삭제
del phone_book['홍길동']
print(phone_book)

print(phone_book.pop('이순신'))
print(phone_book)


# 딕셔너리 모든 항목 삭제
phone_book = {
    '홍길동' : '010-1234-5678',
    '강감찬' : '010-1111-1111',
    '이순신' : '010-3333-3333'
}

phone_book.clear(  )  # 모든 항목 삭제
print(phone_book)


# 딕셔너리를 사용한 영한사전 작성
english_dict = {}
english_dict['one'] = '하나'
english_dict['two'] = '둘'
english_dict['three'] = '셋'

word = input('단어를 입력하세요 : ')
print(english_dict[word])


# 편의점 재고 관리 프로그램 작성
items = {
    '커피' : 7,
    '펜' : 3, 
    '종이컵' : 10,
    '우유' : 5,
    '콜라' : 4,
    '라면' : 11
}

print('판매 전 재고', items)

sell = input('판매할 물건을 입력하세요 : ')

if sell in items:
    items[sell] -= 1
else:
    print('판매하는 제품이 아닙니다.')
print('판매 후 재고', items)


# 딕셔너리와 반복문의 궁합
phone_book = {
    '홍길동' : '010-1234-5678',
    '강감찬' : '010-1111-1111',
    '이순신' : '010-3333-3333'
}
for i in phone_book.keys():
    print(i)
for i in phone_book.values():
    print(i)


# 반복문과 딕셔너리의 items를 이용하여 key와 value를 동시에 출력
phone_book = {
    '홍길동' : '010-1234-5678',
    '강감찬' : '010-1111-1111',
    '이순신' : '010-3333-3333'
}
for k, v in phone_book.items():
    print('{}의 전화번호는 {}입니다.'.format(k, v))


# 가위바위보 게임
import random

def match(c, m):
    if c ==m : 
        return '비겼습니다.'
    elif match_table[c] == m:
        return '졌습니다.'
    else:
        return '이겼습니다.'

rps_dic = {1:'가위', 2:'바위',3: '보'}
match_table = {'가위' : '보', '바위':'가위', '보': '바위'}
computer = rps_dic[random.randint(1,3)]
mine = input('가위, 바위, 보 입력 : ')
result = match(computer, mine)
print(result)


# 행성까지 여행 시간은?

planet_dict = {
    '수성':91700000, '금성':41400000 , '화성':78400000,
          '목성':628700000, '토성':1277400000, '천왕성':275400000,
          '해왕성':4347400000
}

planet = input('행성 이름 : ')
speed = int(input('이동 속도 : '))
distance = planet_dict[planet]

time = distance / speed

year = int(time) // (365*24)
month = int(time - (year*365*24)) //(30*24)
day = int(time - (year*365*24) - (month*30*24)) // 24
hour = int(time - (year*365*24) - (month*30*24) - (day*24))

print('이동시간 : 약', time, '시간')
print('이동시간 : 약', year,'년', month, '월',day,'일',hour,'시간')


# 맨델의 유전법칙
import random

descendant = []
def make_descendant():
    h1 = random.randrange(0, 2)
    h2 = random.randrange(0,2)

    if h1 == 0 and h2 == 0:
        h = 'RR'
    elif h1 ==0 and h2 == 1:
        h = 'Rr'
    elif h1 == 1 and h2 == 0:
        h = 'rR'
    else:
        h = 'rr'
    descendant.append(h)

def count_descendant(d):
    d_dict = {}
    for n in d : 
        if n in d_dict:
            d_dict[n] += 1
        else:
            d_dict[n] = 1
    print(d_dict)
    cal_rate(d_dict)

def cal_rate(d):
    rate = (d['RR']+d['Rr']+d['rR'])/d['rr']
    print(rate, " : 1")

for n in range(100):
    make_descendant()

count_descendant(descendant)


# 튜링상 수상자 데이터 분석
awards = [ ]
awards.append({'이름':'팀 버너스리', '수상년도':2016, '국적':'영국', '대표업적':'월드 와이드 웹의 하이퍼텍스트 시스템을 고안하여 개발'})
awards.append({'이름':'리처드 해밍', '수상년도':1968, '국적':'미국', '대표업적':'오류 검출 부호 및 오류 정정 부호'})
awards.append({'이름':'에츠허르 데이크스트라', '수상년도':1972, '국적':'네덜란드', '대표업적':'프로그래밍 언어 연구, 데이크스트라 알고리즘'})
awards.append({'이름':'더글러스 엥겔바트', '수상년도':1977, '국적':'미국', '대표업적':'마우스의 발명, 대화형 컴퓨팅'})
awards.append({'이름':'데니스 리치', '수상년도':1983, '국적':'미국','대표업적':'유닉스 운영 체제 개발, C언어 개발'})

for award in awards:
    print(award)

print('수상자 명단')
for award in awards:
    print(award['이름'])

print()
print('==수상자 명단과 수상년도==')
for award in awards:
    if award['수상년도'] <= 1990:
        print(award['이름'], award['수상년도'])
    
print()
print('==수상자 국가==')
nationality = set()
for award in awards:
    nationality.add(award['국적'])

print(nationality)


#CH09-Lab05 파이썬으로 e-mail 보내기


import smtplib
from email.mime.text import MIMEText 
 
me = 'abc@server.kr'     # 보내는 사람 메일 주소 
you = 'def@server.com'  # 받는 사람 메일 주소 
contents = '12월 20일에 동창회가 있으니 참석해주시기 바랍니다.' 

msg = MIMEText(contents, _charset='euc-kr') 
msg['Subject'] = '동창회 모임' 


msg['From'] = me 
msg['To'] = you 

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()

 

server.login("자신의 아이디", "패스워드")

server.sendmail(me, you, msg.as_string()) 
server.quit()