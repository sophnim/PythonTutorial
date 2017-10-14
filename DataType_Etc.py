a = [1,2,3,4]
while a:
    print(a)
    a.pop()

# [1, 2, 3, 4]
# [1, 2, 3]
# [1, 2]
# [1]

b = []
if b:
    print("True")
else:
    print("False")

# 자료형이 비어 있으면 False로 인식한다
# False

a = 3
b = 3

import sys
print(sys.getrefcount(3)) # 3이 객체다

# 동시 대입 가능
a, b = 1, 2

# 이 성질을 이용한 간단한 상호 교환: C처럼 중간 변수 필요 없음
a, b = b, a
print(a, b)


# 변수의 같은 객체 참조
c = [1, 2, 3]
d = c
d[0] = 0
print(c)
# c와 d가 같은 객체를 가리키고 있으므로 d를 조작하면 c도 바뀐다
#[0, 2, 3]


# 복사1
e = c[:]
e[0] = 1
print(c)
# [0, 2, 3]
print(e)
#[1, 2, 3]


# 복사2
from copy import copy
f = copy(e)
f[2] = 4
print(e)
# [1, 2, 3]
print(f)
# [1, 2, 4]

