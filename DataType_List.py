def printLn(ln):
    print('')
    print(ln)

def printLoop(array):
    print('')
    for v in array:
        print(v)

list1 = [ 1,2,3,4,5,6,7,8,9 ]
printLn(list1)

printLoop(list1)

list2 = [1,2,'abc']
list3 = [1,2,['abc',4]]

# 리스트 요소 참조
printLn(list2[1])

# 리스트 인덱스 검색
printLn(list2.index('abc'))

# 동적 리스트 추가
listArray = []
''' 이런식으로 동적할당 못함
listArray[0] = [1,2,3]
listArray[1] = [6,5,4]
'''
# 동적 리스트 요소 추가는 append
listArray.append([1,2,3])
listArray.append([4,5,6,7])
printLoop(listArray)

# 리스트 요소 정렬
listArray[1].sort()
printLoop(listArray)

# 리스트 요소 역순
listArray[1].reverse()
printLoop(listArray)

# 리스트의 인덱스 위치 요소 삭제 (이게 좀 유별나네... remove일줄 알았더니)
listArray[1][0:1] = []
printLoop(listArray)

#혹은 del을 사용
del listArray[1][0]
printLoop(listArray)

#리스트 요소에서 검색해서 제거 (인덱스 위치 요소 제거가 아님에 주의!)
listArray[1].remove(5)
printLoop(listArray)

list = [1,2,3,4,5]
list.pop() # 맨마지막 요소를 추출
printLn(list)

list.pop(0) # 인덱스 위치의 요소를 추출
printLn(list)


#리스트에 포함된 요소 개수 세기
list = [1,1,2,3,4,5,5,5]
printLn(list.count(1))
printLn(list.count(5))


list = [1,2,3,4]
list.extend([5,6])
printLn(list)
# [1,2,3,4,5,6]
