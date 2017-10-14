dic1 = {
    1: 'a',
    2: 'b',
    3: 'c'
}

print(dic1[1])
# a

for v in dic1:
    print(v)

# 1 2 3

for v in dic1:
    print(dic1[v])
# a b c

# 키값만 얻기
keys = dic1.keys()
print(keys)
# dict_keys([1, 2, 3]) python 3.0 이상 사용 가능

for k in dic1.keys():
    print(k)

# 키값을 리스트로 변환
print(list(dic1.keys()))



# value만 얻기
values = dic1.values()
print(values)
# dict_values(['a', 'b', 'c'])

print(list(dic1.values()))


#key, value 쌍 얻기
print(dic1.items())
# dict_items([(1, 'a'), (2, 'b'), (3, 'c')])

for item in dic1.items():
    print(item) # item은 tuple

# (1, 'a')
# (2, 'b')
# (3, 'c')

print(list(dic1.items()))
# [(1, 'a'), (2, 'b'), (3, 'c')]


print(dic1.get(1))
# a
print(dic1.get(4)) # 키값 4 가 존재하지 않지만 오류를 발생시키지 않고 None을 리턴한다
# None


# 해당 키가 존재하는지 조사
print(1 in dic1)
# True


# 요소 삭제
del dic1[2]

for v in dic1:
    print(v)
# 1 3


# 모두 지우기
dic1.clear()
print(dic1)
# {}


