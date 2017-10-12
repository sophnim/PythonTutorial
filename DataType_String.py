#문자열
s1 = "test1"
s2 = 'test2'
s3 = "\"test3\""
s4 = "Python's favorite food is perl"
s5 = '''
    line1
    line2
    line3
    '''
print(s1,s2,s3,s4,s5)
print(s1 + s2) # 문자열 붙이기
print(s1 * 2) # 문자열 2번 반복
print(s1[0]) # 문자열의 특정 위치 문자 참조
print(s1[-1]) # 맨뒤 첫번째 문자
print(s1[0:3]) # 0 부터 3개 문자열
print(s1[2:]) # 2 부터 끝까지 문자열
print(s1[:2]) # 처음부터 2까지 문자열
print(s1[:]) # 처음부터 끝까지 문자열

#문자열의 요소값은 참조만 가능하고 변경은 불가능하다.

#문자열 포매팅 https://wikidocs.net/13
f1 = " I Eat %d %s Apples "
r1 = f1 % (5, "fresh")
print(r1)

a = 'abc'
b = 'def'
c = a + b
print(c)

#문자 개수 세기
print(f1.count('s'))

#문자 위치 찾기
print(f1.find('e'))
print(f1.index('s'))

#대문자로 바꾸기
print(f1.upper())
print(f1.lower())

#공백 지우기
print(f1.lstrip())
print(f1.rstrip())
print(f1.strip())

#문자열 바꾸기
print(f1.replace('Eat', 'Dispose'))

#문자열 나누기
str="a,b,c,d,e"
tokens = str.split(',')
print(tokens)
for v in tokens:
    print(v)

#문자열 포매팅
str = '{0} {1} {2} {3}'
str = str.format('aaa', 'bbb', 'ccc', 'ddd')
print(str)


