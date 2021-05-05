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
greet('철수')



