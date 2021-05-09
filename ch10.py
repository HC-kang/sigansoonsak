# 파일 통으로 읽어오기
infile = open('/Users/heechankang/projects/pythonworkspace/sigansoonsak/phones.txt', 'r')
lines = infile.read()
print(lines)
infile.close()


# 파일 통으로 읽어오기(readlines.())
infile = open('/Users/heechankang/projects/pythonworkspace/sigansoonsak/phones.txt', 'r')
lines = infile.readlines()
print(lines)
infile.close()


# 파일 한 줄씩 읽어오기
infile = open('/Users/heechankang/projects/pythonworkspace/sigansoonsak/phones.txt', 'r')
line1 = infile.readline()
print(line1)
line2 = infile.readline(9)
print(line2)
infile.close()


infile = open('/Users/heechankang/projects/pythonworkspace/sigansoonsak/phones.txt', 'r')
line = infile.readline().rstrip()
while line != '':
    print(line)
    line = infile.readline().rstrip()
infile.close()


infile = open('/Users/heechankang/projects/pythonworkspace/sigansoonsak/phones.txt', 'r')
for line in infile:
    line = line.rstrip()
    print(line)
infile.close()


# 파일에 데이터 쓰기
outfile = open('./phones.txt', 'w')

outfile.write('전우치 010-1234-5678\n')
outfile.write('홍길동 010-1234-1234\n')
outfile.write('김서방 010-1111-1111\n')

outfile.close()


# 파일에 데이터 이어쓰기
outfile = open('/Users/heechankang/projects/pythonworkspace/sigansoonsak/phones.txt', 'a')

outfile.write('강감찬 010-2222-2222\n')
outfile.write('김유신 010-3333-3333\n')
outfile.write('정약용 010-4444-4444\n')

outfile.close()

outfile = open('/Users/heechankang/projects/pythonworkspace/sigansoonsak/phones.txt', 'r')
for line in outfile:
    print(line.strip(), end='')
outfile.close()


a = "All's well that ends well"
a.split()


import csv
f = open('/Users/heechankang/projects/pythonworkspace/sigansoonsak/test.csv', 'r')
data = csv.reader(f)

for line in data:
    print(line)
f.close()


infile = open('/Users/heechankang/projects/pythonworkspace/sigansoonsak/phones.txt', 'r')
outfile = open('/Users/heechankang/projects/pythonworkspace/sigansoonsak/temp.txt', 'a')

for line in infile:
    outfile.write(line)

infile.close()
outfile.close()


##############
address = open('/Users/heechankang/projects/pythonworkspace/sigansoonsak/address.txt', 'a')

address.write('''Four score and seven years ago, our fathers brought forth upon this continent a new nation, conceived in liberty and dedicated to the proposition that all men are created equal.
Now we are engaged in a great civil war, testing whether that nation or any nation so conceived and so dedicated can long endure. We are met on a great battlefield of that war.
We have come to dedicate a portion of that field as a final resting place for those who here gave their lives that this nation might live. It is altogether fitting and proper that we should do this
But, in a larger sense, we cannot dedicate, we cannot consecrate, we cannot hallow this ground. The brave men, living and dead, who struggled here have consecrated it, far above our poor power
 to add or detract. 
The world will little note, nor long remember, what we say here, but it can never forget what they did here.  It is for us the living, rather, to be dedicated here to the unfinished work which they who fought here have thus far so nobly advanced. 
  It is rather for us to be here dedicated to the great task remaining before us, that from these honored dead we take increased devotion to that cause for which they gave the last full measure of devotion, that we here highly resolve that these dead shall not have died in vain, that this nation, under God, shall have a new birth of freedom, and that government of the people, by the people, for the people, shall not perish from the earth.
''')
address.close()
###############

texts = open('/Users/heechankang/projects/pythonworkspace/sigansoonsak/address.txt', 'r')

txtlist = []
for line in texts:
    txtlist.append(line.split())

texts.close()
print(txtlist)

texts = []
for t in txtlist:
    for i in t:
        texts.append(i)
print(texts)

count = {}
for i in texts:
    if i in count:
        count[i] +=1
    else:
        count[i] = 1
print( count)

###############

in_file = open('/Users/heechankang/projects/pythonworkspace/sigansoonsak/address.txt', 'r')
out_file = open('/Users/heechankang/projects/pythonworkspace/sigansoonsak/count.txt', 'w')

word_dic = {}
total_counts = 0

for line in in_file:
    line = line.rstrip()
    word_list = line.split()

    for word in word_list:
        word = word.lower()
        word = word.strip(',')
        word = word.strip('.')

        if word in word_dic :
            word_dic[word] += 1
            total_counts +=1
        else:
            word_dic[word] = 1
            total_counts += 1

result = ''
for key in sorted(word_dic.keys()):
    result = key + ' ' + str(word_dic[key]) + '\n'
    out_file.write(result)

print('총 단어 수 : ', total_counts)

in_file.close()
out_file.close()


#######################
import csv

# 입력 파일 출력 파일 열기
infile = open('/Users/heechankang/projects/pythonworkspace/sigansoonsak/weather_input.csv', 'r')
data = csv.reader(infile)
count = 0
sum = 0

for line in data :
    count += 1
    sum += float(line[2])

print("강원도 2009년 01월 부터 2019년 09월까지의 총 강수량: ", sum)
print("강원도 2009년 01월 부터 2019년 09월까지의 평균 강수량: ", sum / count)
infile.close( )

######
import random
infile = open('/Users/heechankang/projects/pythonworkspace/sigansoonsak/hangman.txt', 'r')
lines = infile.readlines()
lines
word = random.choice(lines)
word
user_pick = []
cnt = 10
while cnt>0: # 일단 작동상태 확인
    if cnt<=0:
        running = False
    # 현재 상태 보여주기
    print('남은 기회 : '+str(cnt))
    for i in word:
        if i in user_pick:
            print("'{}'".format(i), end='')
        else:
            print("'_'".format(i), end='')
    print()
    # User에게 단어선택 기회
    char = input('알파벳 선택? : ')
    user_pick.append(char)
    if char in word:
        print('맞춤. 기회 -1')
        print()
    else:
        print('틀림. 기회 -1')
        print()
    cnt-=1

    if sorted(user_pick) == sorted(list(word)):
        print('이겼습니다.')
        break
    else:
        print('졌습니다')
infile.close()



import random

# 입력 파일 열기
infile = open('/Users/heechankang/projects/pythonworkspace/sigansoonsak/hangman.txt', 'r')
lines = infile.readlines( )
word = random.choice(lines).rstrip( )
solution = list(word)   
result = list('_' * len(word))     # list()는 문자열을 받아서 리스트로 변환합니다. 
turns = 10

while turns > 0:
    guess = input("단어를 추측하세요: ")
    turns -= 1
    i = 0

    for c in word:
         if c == guess:
              result[i] = c
         i += 1

    print(result)

    if result == solution:
        print("성공입니다.")           
        break

    if turns <= 0 :
        print("실패하였습니다.")           
        break
infile.close( )