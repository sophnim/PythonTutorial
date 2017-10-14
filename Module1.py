def doTest():
    print('doTest in Module1')

def doTest2():
    print('doTest2 in Module2')

class Test:
    def show(self):
        print('show!')

# python Module1.py 로 실행하면 아래 코드가 실행되고 다른 파일에서 import 되면 실행되지 않는다
if __name__ == "__main__":
    doTest()
    doTest2()


