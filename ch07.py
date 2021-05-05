cart = []
cart.append('사과')
print(cart)

cart = []
cart.append('사과')
cart.append('세제')
print(cart)

slist = ['영어', '수학', '사회', '과학']
print(slist[0])
print(slist[1])
print(slist[2])


letters = 'ABCDEF'
print(letters[0:3])
print(letters[:3])
print(letters[3:])
print(letters[:])

letters = 'ABCDEF'
copy = letters[:]
print(copy)

cart = ['사과', '세제', '화장지', '치약']
cart[1] = '섬유유연제'
cart

cart[10] = '양말'

cart.append('양말')
cart

cart.insert(1, '건전지')
cart

cart = ['사과', '세제','화장지', '치약']
cart.remove('화장지')
print(cart)

cart = ['사과', '세제','화장지', '치약']
if '화장지' in cart:
    cart.remove('화장지')
print(cart)


cart = ['사과','세제','화장지','치약']
del cart[2]
print(cart)


cart = ['사과','세제','화장지','치약']
item = cart.pop()
print(cart)
print(item)

cart = ['사과','세제','화장지','치약']
print(cart.index('화장지'))

heroes = ['아이언맨','토르','헐크','스칼렛위치']
heroes.sort()
print(heroes)


heroes = ['아이언맨','토르','헐크','스칼렛위치']
new_heroes = sorted(heroes)
print(heroes)
print(new_heroes)


num = [10,20,30,40,50,60]
print(num)


num=[[10,20,30], [40,50,60]]
print(num)


num=[[10,20,30], [40,50,60]]
print(num[0][0])
print(num[0][1])
print(num[1][1])
num[1][2] = 100
print(num)


for i in [1,2,3]:
    print('i=', i)


heroes = []
for i in range(5):
    name = input('영웅들의 이름을 입력하시오 : ')
    heroes.append(name)

for i in heroes:
    print(i, end=' ')

num = [100, 96, 209, 22, 30, 117]

for i in num:
    if i % 2:
        print(i, end=' ')


#############
#####
# 주기율표를 외워보자
###
list_a = ['수헬리베붕', '탄질산불네나', '마알규', '인황염아칼칼']
for i in list_a:
    print(i)


#####
# 오늘의 명언
###
import random

apho = [
    '고생 없이 어들 수 있는 진실로 귀중한 것은 하나도 없다.',
    '꿈을 지녀라. 그러면 어려운 현실을 이길 수 있다.',
    '사람은 사랑할 때 누구나 시인이 된다.'
]
a = random.randint(0,2)
print('############################################')
print('#     오늘의 명언')
print('############################################')
print(apho[a])

#####
# 스파이럴 그리기, 오륜기 그리기
###


#####
# 습도 구하기
###
