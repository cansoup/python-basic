# Chapter03-03
# 파이썬 리스트(배열)
# 순서o, 중복o, 수정o, 삭제o

# 선언
a = []
b = list()
c = [70, 75, 80, 85] # len
d = [1000, 10000, 'Ace', 'Base', 'Captain']
e = [1000, 10000, ['Ace', 'Base', 'Captain']]
f = [21.42, 'foobar', 3, 4, False, 3.14]

# 인덱싱
print('>>>>>>')
print('d - ', type(d), d)
print('d - ', d[1])
print('d - ', d[0] + d[1] + d[1])
print('d-', d[-1])
print('d-', e[-1][1])
print('e-', list(e[-1][1])) # 형변환

# 슬라이싱
print('>>>>>')
print('d - ', d[0:3])
print('d - ', d[2:])
print('e - ', e[-1][1:3])

# 리스트 연산
print('>>>>>')
print('c + d', c + d)
print('c * 3', c * 3)
# print("'Test' + c[0]", 'Test' + c[0]) # 에러: 문자와 숫자타입은 더할 수 없다 -> 숫자를 문자로 형변환하여 해결
print("'Test' + c[0]", 'Test' + str(c[0]))

# 값 비교
print('>>>>>>')
print(c == c[:3] + c[3:])

# Identity(id)
# 파이썬의 효율성 때문에 같은 주소값을 공유한다.
temp = c
print(temp, c)
print(id(temp))
print(id(c))

# 리스트 수정, 삭제
print('>>>>>>>')
c[0] = 4
print('c - ', c)
c[1:2] = ['a', 'b', 'c']
print('c - ', c) # c - [4, 'a', 'b', 'c', 80, 85]
c[1] = ['a', 'b', 'c']
print('c -', c) # c - [4, ['a', 'b', 'c'], 'b', 'c', 80, 85]
c[1:3] = []
print('c - ', c)
del c[2] # 삭제

# 리스트 함수
print('>>>>>>')
a = [5, 2, 3, 1, 4]

print('a - ', a)
a.append(10) # append() 리스트의 마지막에 요소를 추가할 때 사용하는 함수
print('a - ', a)
a.sort() # sort() 오름차순 정렬 함수
print('a - ', a)
a.reverse() # reverese() 들어있는 데이터를 반대로
print('a - ', a)
print('a - ', a.index(3), a[3]) # index()
a.insert(2, 7) # insert(a, b) 리스트의 a 번째 자리에 b 값을 삽입
print('a - ', a)
a.remove(10) # remove(a) 리스트의 a값을 찾아 제거한다
print('a - ', a)
print('a - ', a.pop()) # pop() 기존 리스트에서 마지막 값 하나를 return하고 기존 리스트에서 제거한다
print('a - ', a)
print('a - ', a.count(4)) # count(b) 리스트가 가지고 있는 원소 중 값이 b인 것의 갯수
ex = [8, 9]
a.extend(ex) # extend(b) 리스트 마지막에 b를 붙인다
print('a - ', a)

# 삭제: remove, pop, del

# 반복문 활용
while a:
  data = a.pop()
  print(data)