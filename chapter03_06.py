# Chapter03-06
# 집합(Set) 특징
# 집합(Set) 자료형(순서X, 중복X)

# 선언
a = set()
b = set([1, 2, 3, 4, 4, 4])
c = set([1, 4, 5, 6])
d = set([1, 2, 'Pen', 'Cap', 'Plate'])
e = {'foo', 'bar', 'baz', 'foo', 'qux'}
f = {42, 'foo', (1, 2, 3), 3.14159}

print('a - ', type(a), a, 2 in a)
print('b - ', type(b), b)
print('c - ', type(c), c)
print('d - ', type(d), d)
print('e - ', type(e), e)
print('f - ', type(f), f)

# 튜플 변환(set -> tuple)
t = tuple(b)
print('t - ', type(t), t)
print('t - ', t[0], t[1:3])

# 리스트 변환(set -> list)
l = list(c)
l2 = list(e)

print('l - ', l)
print('l - ', l2)

# 길이
print(len(a))
print(len(b))
print(len(c))
print(len(d))
print(len(e))
print(len(f))

# 집합 자료형 활용
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

# 교집합
print('s1 & s2 : ', s1 & s2)
print('s1 & s2 : ', s1.intersection(s2))
# 합집합
print('s1 | s2 : ', s1 | s2)
print('s1 | s2 : ', s1.union(s2))
# 차집합
print('s1 - s2 : ', s1 - s2)
print('s1 - s2 : ', s1.difference(s2))
# 중복 원소 확인 - 공통 원소가 있는 경우 False
print('s1 & s2 : ', s1.isdisjoint(s2))
# 부분 집합 확인 - s1이 s2의 부분집합인지
print(s1.issubset(s2))
# 부분 집합 확인 - s1이 s2를 포함하는지
print(s1.issuperset(s2))

# 추가 & 제거
s1 = set([1, 2, 3, 4])

s1.add(5)
print('s1 - ', s1)
s1.remove(2)
print('s1 - ', s1)
# 삭제
# remove - 없는 원소를 삭제하려고 하면 key error
# s1.remove(7)
# discard - 에러 발생 x
s1.discard(3)
print('s1 - ', s1)
# 전체 삭제
s1.clear()
print('s1 - ', s1)