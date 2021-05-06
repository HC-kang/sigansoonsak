def print_address():
    print('서울특별시 종로구 1번지')
    print('파이썬 빌딩 7층')
    print('홍길동')

print_address()

print('서울특별시 종로구 1번지')
print('파이썬 빌딩 7층')
print('홍길동')
print('서울특별시 종로구 1번지')
print('파이썬 빌딩 7층')
print('홍길동')



def print_address(name):
    print('서울특별시 종로구 1번지')
    print('파이썬 빌딩 7층')
    print(name)

print_address('가나다')

def get_sum(start, end):
    sum = 0
    for i in range(start, end+1):
        sum += i
    print('sum = ', sum)

get_sum(1, 10)
get_sum(1, 20)


def inc(a, step = 1):
    print(a+step)

inc(10)
inc(10, 50)

def calculate_area(radius):
    area = 3.14 * radius ** 2  
    return area

c_area = calculate_area(5.0)
print(c_area)

area_sum = calculate_area(5.0) + calculate_area(10.0)
print( area_sum)

def get_input():
    return 2, 3

x, y = get_input()

print(x,",", y)

def judge(num):
    if num % 2 ==0:
        print('짝수')
        return
    print('홀수')

num = int(input('자연수를 입력하시오 : '))
judge(num)

#####
# 망할 터틀
###
# 반복문 ver
import turtle
t = turtle.Turtle()
t.shape('turtle')

for i in range(4):
    t.forwadt(100)
    t.left(90)
t.up()
t.goto(-200, 0)
t.down()

for i in range(4):
    t.forward(100):
    t.left(90)

# 함수 ver
import turtle
t = turtle.Turtle()
t.shape('turtle')

def square(length):
    for i in range(4):
        t.forward(length)
        t.left(90)

sqaure(100)
t.up()
t.goto(-200, 0)
t.down()
square(100)


#####
# 지역변수와 전역변수
###

def calculate_area():
    result = 3.14 * r ** 2
    return result

r = float(input('원의 반지름 : '))
area = calculate_area()
print(area)

#####
# 지역변수, 전역변수
###

result = 0
def calculate_area():
    result = 3.14 * r **2

r = float(input('원의 반지름 : '))
calculate_area()
print(result)

#####
# global 적용
###
result = 0
def calculate_area():
    global result
    result = 3.14*r**2

r = float(input('원의 반지름 : '))
calculate_area()
print(result)


#####
# 디폴트 인수
###
# 변수 두개
def greet(name, msg):
    print('안녕', name + ', '+msg)

greet('철수', '좋은 아침')

# 변수 누락
def greet(name, msg):
    print('안녕', name + ', '+msg)
greet('철수')

# 디폴트 인수
def greet(name, msg = '잘 지내죠?'):
    print('안녕', name + ', '+msg)
greet('영희')

# 키워드 인수
def calc(x, y):
    return x-y

print(calc(10, 20))
print(calc(20, 10))

def calc(x, y):
    return x-y

print(calc(x = 10, y = 20))
print(calc(y = 20, x = 10))

# 주의사항
def calc(x,y,z):
    return x+y+z

print(calc(10, y=20, z=30))
print(calc(x=10, 20, 30))
print(calc(20, 30, x=10))

def func1(x, y, z):
    return x*y*z

func1(1,3,5)
func1(y=7, z = 5, x = 2)
func1(z=2, x=4, y=5)
func1(5, z=10, y=2)
func1(z=10, 20, x=2)
func1(5, x=2, z=20)


#####
# BMI 계산기
###

def calc_BMI():
    weight = float(input('체중(kg)을 입력하세요. : '))
    height = float(input('키(cm)를 입력하세요. : ')) / 100
    BMI = weight / height**2
    return BMI

calc_BMI()

#####
# 환전계산기
###
def cal_money():
    rate_dict = {
        '미국' : ['달러', 1182.5], 
        '일본' : ['엔', 1.07814],
        '유럽' : ['유로', 1286.74],
        '중국' : ['위안', 169.22]
    }
    money = int(input('환전 금액(원)을 입력하세요 : '))
    country = input('국가를 입력하세요 : ')
    if country in rate_dict:
        print('{0} 원은 {1} {2} 입니다.'.format(money, round(money / rate_dict[country][1], 2), rate_dict[country][0]))
    else:
        print('해당 국가의 정보가 없습니다.')

cal_money()

#####
# N각형을 그리는 함수 작성
###
# 아 터틀좀 제발