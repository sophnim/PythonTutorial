# 중복을 허용하지 않고 순서가 없는 자료형

set1 = set([1,2,3])
print(set1)
# {1, 2, 3}

set2 = set("abcdef")
print(set2)
# {'f', 'a', 'd', 'c', 'b', 'e'}

set3 = set(['abc', 'def', 'ghi'])
print(set3)
# {'abc', 'def', 'ghi'}

# 추가
set1.add(4)
print(set1)
# {1, 2, 3, 4}

# 여러개 추가
set1.update([5,6,7])
print(set1)
# {1, 2, 3, 4, 5, 6, 7}

# 특정 값 제거
set1.remove(1)
print(set1)
# {2, 3, 4, 5, 6, 7}
