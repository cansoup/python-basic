# Chapter03-04
# 튜플
# 리스트와 비교 중요
# 튜플 자료형(순서o, 중복o, 수정x, 삭제x) # 불변 - 약간... const 같은 느낌이군

# 선언 - 원소가 한 개일 때는 ,를 찍어줘야 한다.
a = ()
b = (1) # type - int
c = (1,) # type - tuple
print(type(a), type(b), type(c))
d = (100, 1000, 'Ace', 'Base', 'Captine')
e = (100, 1000, ('Ace', 'Base', 'Captine'))

# 인덱싱
print('>>>>')
print('d - ', d[1])
# print('d - ', d[0] + d[1] + d[2]) # error
print('d - ', d[-1])
print('d - ', e[-1]) # return tuple
print('d - ', e[-1][1]) # return tuple
print('d - ', list(e[-1][1])) # 리스트로 형 변환하는 순간 tuple이 원래 가지고 있던 수정x, 삭제x 특성은 사라지게 된다.

# 수정 불가
# d[0] = 1500

# 슬라이싱
print('>>>>>>')
print('d - ', d[0:3])
print('d - ', d[2:])
print('d - ', e[2][1:3])

# 튜플 연산
# 내부 원소가 변경 / 삭제되지 않는다면 원소의 갯수가 늘어나거는 것은 허용한다. 
print('>>>>>')
print('c + d', c + d)
print('c * 3', c * 3)

# 튜플 함수
a = (5, 2, 3, 1, 4)
print('a - ', a)
print('a - ', a.index(3))
print('a - ', a.count(2))

# *** 패킹 & 언패킹(Packing and Unpacking) ***

# 팩킹: 튜플을 선언하는 것
t = ('foo', 'bar', 'bax', 'qux')

# 언팩킹1 -> 진짜 구조분해 같은거네....
(x1, x2, x3, x4) = t

print(type(x1), type(x2), type(x3), type(x4))
print(x1, x2, x3, x4)

# 패킹 & 언팩킹
t2 = 1, 2, 3 # 이것도 튜플
t3 = 4, # 이것도 튜플. 괄호는 생략 가능

x1, x2, x3 = t2 # 언팩킹
x4, x5, x6 = 4, 5, 6 # 언팩킹

print(t2)
print(t3)
print(x1, x2, x3)
print(x4, x5, x6)