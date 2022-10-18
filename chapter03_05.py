# Chapter03-05
# 딕셔너리 (json이랑 비슷함!!!!)
# 범용적으로 가장 많이 사용
# 딕셔너리 자료형(순서x, 키 중복x, 수정o, 삭제o)

# 선언
a = {'name': 'Kim', 'phone': '01033337777', 'birth': '870505'}
b = {0: 'Hello Python'}
c = {'arr': [1, 2, 3, 4]}
d = {
  'Name': 'Niceman',
  'City': 'Seoul',
  'Age': 33,
  'Grade': 'A',
  'Status': True
}
# 자주쓰이는 건 아니지만...
# 이렇게 쓰려면 원소(?) 하나 하나마다 튜플 처리를 해주어야 한다...
e = dict([
  ('Name', 'Niceman'),
  ('City', 'Seoul'),
  ('Age', 33),
  ('Grade', 'A'),
  ('Status', True)
])
# 좀 더 편해진 version
f = dict(
  Name = 'Niceman',
  City = 'Seoul',
  Age = 33,
  Grade = 'A',
  Status = True,
)

print('a - ', type(a), a)
print('b - ', type(b), b)
print('c - ', type(c), c)
print('d - ', type(d), d)
print('e - ', type(e), e)
print('f - ', type(f), f)

# 출력
# 데이터가 확실한 경우에는 속성으로 접근해도 무방하지만
# 속성으로 접근 시 프로퍼티가 없으면 에러가 발생한다.
print('a - ', a['name'])
# 아닐 경우에는 .get()을 사용하는 것이 안전하다
# .get()은 'name'이 없는 경우에 None을 반환한다.
print('a - ', a.get('name'))
print('b - ', b[0])
print('b - ', b.get(0))
print('f - ', f.get('City'))
print('f - ', f.get('Age'))

# 딕셔너리 추가: 동적으로 값 추가 가능, 이미 같은 속성이 존재하면 기존 값을 덮어씌운다.
a['address'] = 'Seoul'
print('a - ', a)
a['rank'] = [1, 2, 3]
print('a - ', a)

# 딕셔너리 길이
print('a - ', len(a))
print('b - ', len(b))
print('c - ', len(c))
print('d - ', len(d))

# dict_keys, dict_values, dict_items(key-value): 반복문(__iter__)에서 사용 가능
print('a - ', a.keys())
print('b - ', b.keys())
print('c - ', c.keys())
print('d - ', d.keys())

print('a - ', list(a.keys()))
print('b - ', list(b.keys()))

print()

print('a - ', a.values())
print('b - ', b.values())
print('c - ', c.values())
print('d - ', d.values())

print('a - ', list(a.values()))
print('b - ', list(b.values()))

# items: key-value 튜플로 반환
print('a - ', a.items())
print('b - ', b.items())
print('c - ', c.items())
print('d - ', d.items())

print()

print('a - ', a.pop('name'))
print('a - ', a)

print('c - ', c.pop('arr'))
print('c - ', c)

print()

# 아무거나 하나를 임의로 pop한다. 딕셔너리에 아무것도 없으면 error 발생
print('f - ', f.popitem())

print()

# in : 특정 key값이 딕셔너리 안에 존재하는지를 확인하여 boolean값을 리턴한다.
print('a - ', 'birth' in a)

# 수정 & 추가
a.update(birth='910904')
print('a - ', a)
temp = {'address': 'Busan'}
a.update(temp)
print('a - ', a)