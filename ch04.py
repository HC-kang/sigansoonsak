x = 10
print('x = ', x)

x = 3.14
print('x = ', x)

x = 'Hello World'
print('x = ', x)


x = 123
print(x)
print(type(x))

x = -123
print(x)
print(type(x))

x = 0
print(x)
print(type(x))


x = 3.14
print(x)
print(type(x))

x = -3.14
print(x)
print(type(x))

x = 0.0
print(x)
print(type(x))

msg = 'Hello'

msg = 'Hello'


print(100+200)
print('100' + '200')

x = input('정수를 입력하세요 : ')
y = input('정수를 입력하세요 : ')
print(x+y)

t = input('정수를 입력하세요 : ')
x = int(t)

t = input('정수를 입력하세요 : ')
y = int(t)

print(x+y)


x = float(input('실수를 입력하세요 : '))
y = float(input('실수를 입력하세요 : '))

print(x+y)

print('나는 현재' + 17 + '살이다.')

print('나는 현재' + str(17) + '살이다.')

'hello' + 'world'

first_name = '길동'
last_name = '홍'
name = last_name + first_name
print(name)

message = 'Congreturation'
print(message * 3)

line = '='*30
print(line)

price = 10000
print('상품의 가격은 %s원입니다.'%price)

poem = '이렇게 정다운\n너 하나 나 하나는\n어디서 무엇이 되어\n다시 만나랴.'
print(poem)

s = 'Hello Python'
print(s[0])
print(s[1])
print(s[-1])

s = 'Hello Python'
print(s[6:10])
print(s[6:10])
print(s[0:10:2])
print(s[-1:-7:-1])

# 소금물 농도
salt = int(input('소금의 양은? : '))
water = int(input('물의 양은? : '))
print('소금물의 농도 : {}'.format(salt/(salt+water)))


# 챗봇
print('안녕하세요.')
name = input('이름이 뭐에요?')
print('만나서 반갑습니다. {} 님'.format(name))
print('{} 님, 이름의 길이는 다음과 같군요 : {}'.format(name, len(name)))
age = int(input('나이가 어떻게 되세요?'))
print('내년이면 {}세가 되시는군요'.format(age+1))

# 터틀
import turtle
t = turtle.Turtle
t.shape('turtle')
name = input('이름? : ')
print('안녕하세요 {}씨. 터틀 인사드립니다.'.format(name))
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)


# 암호 프로그램
words = input('암호? : ')
print(words[::-1])

# 2050년

import time
now = time.time()
thisYear = int(1970+now//(365*24*3600))
print('올해는 ' + str(thisYear) + '년입니다.')
age = int(input('당신의 나이를 입력하세요 : '))
print('2050년에는 {}살이군요.'.format(age + 2050 - thisYear))