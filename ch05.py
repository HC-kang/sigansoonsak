score = 90
if score >=60:
    print('합격입니다.')
print('수고하셨습니다.')

language = int(input('언어를 선택해 주세요(1 = 한국어, 2=영어, 3=프랑스어, 4=독일어'))

######

if language==1:
    print('안녕')
if language==2:
    print('Hello')
if language==3:
    print('Bonjour')
if language==4:
    print('Guten morgen')

#######

age = int(input('나이를 입력하시오 : '))
if age >=15:
    print('영화를 관람할 수 있습니다.')
else:
    print('영화를 관람할 수 없습니다.')

#####

num = int(input('정수를 입력하시오 :'))
if num%2==0:
    print('짝수입니다.')
else:
    print('홀수입니다.')

######

num = int(input('정수를 입력하시오 : '))
if num >0:
    print('양수입니다.')
elif num==0:
    print('0입니다.')
elif num < 0:
    print('음수입니다.')

#####

num = int(input('정수를 입력하시오 : '))
if num >= 0:
    if num==0:
        print('0입니다.')
    else:
        print('양수입니다.')
else:
    print('음수입니다.')

#####
# 터틀좀 그만하고싶다.

import turtle
t= turtle.Turtle
t.shape('turtle')

num = int(input('정수를 입력하세요. : '))

if num==0 : 
    t.forward(100)
    print('0입니다.')
elif num >0 :
    t.left(45)
    t.forward(141)
    print('양수입니다.')
else:
    t.right(45)
    t.forward(141)
    print('음수입니다.')

#####
# 주민등록번호

import random
for i in range(100):
    i = random.randint(1,9)
    if i%2==0:
        print(i)
        print('여성입니다.')
    else:
        print(i)
        print('남성입니다.')

#####
# 동전 던지기

for i in range(100):
    i = random.randint(0,1)
    print(i)

#####
# 전기회로
question1 = input('1번 전지가 있습니까?(Y/N)').lower()
question2 = input('2번 전지가 있습니까?(Y/N)').lower()

if question1=='y':
    if question2=='y':
        print('직렬연결 : 전구에 불이 켜집니다.')
        print('병렬연결 : 전구에 불이 켜집니다.')
    else:
        print('직렬연결 : 전구에 불이 꺼집니다.')
        print('병렬연결 : 전구에 불이 켜집니다.')
else:
    if question2=='y':
        print('직렬연결 : 전구에 불이 꺼집니다.')
        print('병렬연결 : 전구에 불이 켜집니다.')
    else:
        print('직렬연결 : 전구에 불이 꺼집니다.')
        print('병렬연결 : 전구에 불이 꺼집니다.')

#####
# 윤년 판단

year = int(input('연도를 입력하세요 : '))
if year%4 == 0:
    print('{}년은 윤년입니다.'.format(year))
else:
    print('{}년은 윤년이 아닙니다.'.format(year))

#####
# 판별식

a = int(input('a값 입력 : '))
b = int(input('b값 입력 : '))
c = int(input('c값 입력 : '))

d = b**2 - (4*a*c)

if d==0:
    print('방정식은 서로 같은 두 실근(중근)을 가집니다.')
elif d>0:
    print('방정식은 서로 다른 두 실근을 가집니다.')
else:
    print('방정식은 서로 다른 두 허근을 가집니다.')

#####
# 사용자가 원하는 도형 그리기

import turtle
t = turtle.Turtle
t.shape('turtle')

name = input('도형을 입력하세요. : ')

if name == '원':
    radius = int(input('반지름의 길이는? : '))
    t.circle(radius)
elif name == '정삼각형':
    length = int(input('한 변의 길이는? : '))
    t.forward(length)
    t.left(120)
    t.forward(length)
    t.left(120)
    t.forward(length)
elif name == '직사각형':
    hor = int(input('가로의 길이는? : '))
    vir = int(input('세로의 길이는? : '))
    t.forward(hor))
    t.left(90)
    t.forward(vir)
    t.left(90)
    t.forward(hor))
    t.left(90)
    t.forward(vir)
else:
    print('아직 지원되지 않습니다..')

#####
# 두 원의 위치 관계

import turtle
t = turtle.Turtle
t.shape('turtle')

x1 = int(input('큰 원의 중심 좌표 x1 : '))
y1 = int(input('큰 원의 중심 좌표 y1 : '))
r1 = int(input('큰 원의 반지름 r1 : '))

x2 = int(input('작은 원의 중심 좌표 x2 : '))
y2 = int(input('작은 원의 중심 좌표 y2 : '))
r2 = int(input('작은 원의 반지름 r2 : '))

l = ((x1-x2)**2 + (y1-y2)**2)**(1/2)

if l==r1:
    print('선상에 있고 두 점에서 만남.')
elif l > r1:
    if (r1+r2) < l:
        print('안만남')
    elif  (r1+r2) == l:
        print('외접')
    else:
        print('두 점에서 만남')
else:
    l > r1:
    if (r1-r2) > l:
        print('안만남')
    elif  (r1-r2) == l:
        print('내접')
    else:
        print('두 점에서 만남')
'''
i) l > r1
    r1 + r2 < l     # 안만남
    r1 + r2 = l     # 1점에서 만남
    r1 + r2 > l     # 2점에서 만남

ii) l < r1
    r1 - r2 > l     # 안만남
    r1 - r2 = l     # 1점
    r1 - r2 < l     # 2점
'''

#####
# 