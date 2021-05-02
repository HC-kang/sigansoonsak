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