# 파이썬은 객체를 통해 클래스의 함수를 호출할 때 호출한 객체 자신이 호출한 클래스 함수의 첫번째 입력 인수로 전달된다.

class Calculator:
    def __init__(self):     # 생성자
        self.result = 0     # 클래스 멤버 변수를 여기서 생성 및 초기화

    def add(self, num):
        self.result += num
        return self.result


cal = Calculator()          # 클래스 생성

print(cal.add(1))
# 1

print(cal.add(2))
# 3

print(cal.add(3))
# 6

print(cal.result)
# 6


# 클래스 변수: 인스턴스간에 공유되는 변수
class Service:
    member1 = 1
    member2 = 2

    def show(self):
        print(self.member1, self.member2)

svc1 = Service()
svc2 = Service()
svc1.show()
# 1 2

svc2.member1 = 3 # 이렇게 하면 소용 없다
svc1.show()
# 1 2

Service.member1 = 3
svc1.show()
# 3 2

# 런타임에 객체에 객체변수를 생성, 할당할 수 있다
svc1.name = 'I am svc1'
print(svc1.name)
# I am svc1


# 클래스 상속
class Parent:
    def test(self):
        print('Parent test')

class Child(Parent):
    def test(self):
        print('Child test')

child = Child()
child.test()
# Child test



