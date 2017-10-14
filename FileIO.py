# 파일 만들기
f = open('test.txt', 'w')
for i in range(3):
    str = "%d번째 줄입니다.\n" % i
    f.write(str)
f.close()

# 파일 한줄씩 읽기
f = open('test.txt', 'r')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()

# 0번째 줄입니다.
# 1번째 줄입니다.
# 2번째 줄입니다.


# 파일 한번에 읽기1
f = open('test.txt', 'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()


# 파일 한번에 읽기2
f = open('test.txt', 'r')
data = f.read()
print(data)
f.close()


# with 문으로 파일 닫기 자동으로 하기
with open('test.txt', 'r') as f:
    data = f.read()
    print(data)
    
    
# 프로그램 실행 인수 얻기
import sys
args = sys.argv[1:]
for arg in args:
    print(arg)
    
