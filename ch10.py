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
f = open('/Users/heechankang/projects/pythonworkspace/sigansoonsak/test.csv', 'r', encoding='utf-8')
data = csv.reader(f)

for line in data:
    print(line)
f.close()