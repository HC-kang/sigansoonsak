2+17

2-17

17**2

10*2**7

2**2**3

17/5

17//5

p = int(input('나누어지는 수를 입력하시오 : '))
q = int(input('나누는 수를 입력하시오 : '))
print('나눗셈의 몫 : ', p//q)
print('나눗셈의 나머지 : ', p%q)

sec = 1000
min = sec //60
remainder = sec % 60
print(min, '분', remainder, '초')

x = y = 100
print(x)
print(y)

x += 2
x = x+2

x = x*2+3
x *= 2+3

x = 1000
print('초깃값 x= ',x)
x+=2
print('x += 후의 x= ',x)
x-=2
print('x -= 후의 x= ',x)

x = int(input('첫 번째 수 : '))
y = int(input('두 번째 수 : '))
z = int(input('세 번째 수 : '))

avg = (x+y+z)/3
print('평균=', avg)

x = -1
y = 3

print(
    (-y)**3 + 2*x**2*y
)

f = int(input('화씨온도 : '))
print('섭씨온도 : ', (f-32)*5/9)

x1 = int(input('x1 : '))
y1 = int(input('y1 : '))
x2 = int(input('x2 : '))
y2 = int(input('y2 : '))

print(((x2-x1)**2 + (y2-y1)**2)**(1/2))

import datetime

a = time.time()

print(a//60//60%24+9, a//60%60)

input_money = int(input('투입한 돈 : '))
price = int(input('물품 가격 : '))
output_money = input_money - price

big_coin = output_money//500
small_coin = output_money%500//100

print(big_coin)
print(small_coin)

