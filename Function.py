def test():
    print('this is test')

test()
# this is test


def add(a,b):
    return a+b

print(add(1,2))
# 3


# 여러값을 동시에 리턴
def add2(a,b):
    return a,b,a+b

a,b,c = add2(1,2)
print(a,b,c)
# 1 2 3

# 리턴값이 여러개인 함수의 결과를 하나로 받으면 튜플에 저장된다
d = add2(1,2)
print(d)
# (1, 2, 3)


# 가변 인자
# 인자앞에 *를 붙인다
def vargfunc(*args):
    for v in args:
        print(v)

vargfunc(1,2,3,'a',5)
# 1
# 2
# 3
# a
# 5

def vargfunc2(format, *args):
    print(format)
    for v in args:
        print(v)

vargfunc2("test", 1,2,3,4)
# test
# 1
# 2
# 3
# 4


# 인수 초기값 설정
def func(a = 1, b = 2):
    print(a,b)

func(10)
# 10 2

