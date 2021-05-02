# 01. 반복이 중요한 이유

print('방문을 환영합니다.')
print('방문을 환영합니다.')
print('방문을 환영합니다.')
print('방문을 환영합니다.')
print('방문을 환영합니다.')

# vs 

for i in range(5):
    print('방문을 환영합니다.')

#####
# 02. 횟수 제어 반복 - for
for 변수 in range(종료 값):
    문장

for i in range(5):
    print('방문을 환영합니다.')

for i in range(1,6,1):
    print(i, end=" ")

for i in range(10, 0, -1):
    print(i, end=' ')


sum = 0
for i in range(1, 101):
    sum+=i
print('1부터 100까지의 합은',sum,'입니다.')


n = int(input('정수 입력 : '))
fact = 1
for a in range(1, n+1):
    fact = fact*a
print(n, '! 은', fact,'이다.')


response = '아니'
while response=='아니':
    response = input('엄마, 다 됐어? : ')
print('먹자')


count = 1
sum = 0
while count <=100:
    sum = sum+count
    count+=1
print('1부터 100까지의 합은',sum,'이다.')


password = ''
while password !='pythonisfun':
    password = input('암호를 입력하시오 : ')
print('로그인 성공')


for i in range(5):
    for j in range(10):
        print('*', end = '')
    print('')


for i in range(1, 6):
    for j in range(1, i+1):
        print('*', end='')
    print('')

sign = True
while sign:
    light = input('색상을 입력 : ')
    if light =='blue':
        sign=False
print('전진!')


while True:
    light = input('신호등 색상을 입력 : ')
    if light =='blue':
        break
print('전진!')


for n in range(10):
    if n%2 ==0:
        continue
    print(n)


import turtle
t = turtle.Turtle()
t.circle(100)
t.left(60)
t.circle(100)
t.left(60)
t.circle(100)
t.left(60)
t.circle(100)
t.left(60)
t.circle(100)
t.left(60)
t.circle(100)
t.left(60)
######
import turtle
t = turtle.Turtle()
for i in range(6):
    t.circle(100)
    t.left(60)


print('A')
print('B')
for i in range(2):
    print('C')
    print('D')


# 정n각형 그리기
import turtle
t = turtle.Turtle()
a = int(input('몇각형? : '))
total_angle = 180*(a-2)
inner_angle = total_angle / a
outer_angle = 180-inner_angle
for i in range(a):
    t.forward(100)
    t.left(outer_angle)


import turtle
t = turtle.Turtle()
import random
for i in range(20):
    t.forward(rnadom.randint(1, 1000))
    t.left(random.randint(1, 361))

import random
print('범인 찾기 게임')
point = 0
while True:
    print(f'Point : {point}')
    print(' Door 1 ')
    print()
    print(' Door 2 ')
    print()
    print(' Door 3 ')
    print()
    hid_num = random.randint(1,3)
    choice = int(input('1 or 2 or 3 ? : '))
    if choice == hid_num:
        print('Got it, +100 point')
        point +=100
        print(f'Point : {point}')
        break
    else:
        print('You Missed It, -10 point')
        point -=10
        print(f'Point : {point}')


######
# 모든 약수 구하기
###
import time


def find_divisor(n):
    start = time.time()
    divisor = []
    for i in range(1, n+1):
        if n%i==0:
            divisor.append(i)
    end = time.time()
    print(divisor)
    print('소요시간 : ', end-start)

find_divisor(100000000)
find_divisor(124089723)


def find_divisor_mk2(n):
    start = time.time()
    pre_divisor = []
    divisor = []
    for i in range(1, int(n**0.5)):
        if n%i==0:
            pre_divisor.append(i)
        for j in pre_divisor:
            divisor.append(n//j)
        divisor = divisor+pre_divisor
    end = time.time()
    print(set(divisor))
    print('소요시간 : ', end-start)
find_divisor(10)
find_divisor_mk2(10)
find_divisor(100000000)
find_divisor_mk2(100000000)
find_divisor_mk2(124089723)


def find_divisor_mk3(n):
    start = time.time()
    divisor = []
    for i in range(1, int(n**0.5)):
        if n%i==0:
            divisor.append(i)
            divisor.append(n//i)
    end = time.time()
    print(set(divisor))
    print('소요시간 : ', end-start)

find_divisor(10)
find_divisor_mk3(10)
find_divisor(100000000)
find_divisor_mk2(100000000)
find_divisor_mk3(100000000)
find_divisor_mk3(124089723)



#####
# 최대공약수 구하기
#
def find_GCD(a, b):
    while a!=b:
        if a>b:
            a=a-b
        else:
            b=b-a
    if a==1:
        print('서로소입니다.')
    print(a)

find_GCD(48,72)
find_GCD(5,3)

def find_GCD_mk2(a,b):
    while b!=0:
        temp = b
        b = a%b
        a = temp
    if a==1:
        print('서로소입니다.')
    return a

find_GCD_mk2(6, 9)
find_GCD_mk2(1,2)



#####
# 터틀좀 그만했으면좋겠다.

import turtle
t = turtle.Turtle()
t.shape('turtle')

for i in range(5):
    t.forward(100)
    t.right(288)


#####
# 숫자맞추기 게임
###
import random

def game():
    num = random.randint(1, 100)
    k = 0
    cnt = 0
    while k!=num:
        k = int(input('숫자를 입력하시오(1~100) : '))
        if k>num:
            print('높음')
        else:
            print('낮음')
        cnt+=1
    print('맞췄습니다. 횟수 : ', cnt)

game()