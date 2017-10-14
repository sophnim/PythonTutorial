
# 모듈 이름은 파일명이다
import Module1 as m1
m1.doTest()
# doTest in Module1

# 모듈의 함수를 가져와서 그대로 쓰고자 할 때
from Module1 import doTest
doTest()
# doTest in Module1


# 모듈의 함수 모두를 가져올때
from Module1 import *
doTest()
doTest2()
# doTest in Module1
# doTest2 in Module2


# 모듈의 클래스 사용
import Module1 as m1
test = m1.Test()
test.show()
# show!


import sys
print(sys.path) # 파이선 라이브러리가 설치된 디렉터리 확인

sys.path.append('') # 모듈이 저장된 디렉터리 추가할 때
