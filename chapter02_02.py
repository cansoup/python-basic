# Chapter02-02
# 파이썬 변수

# 기본 선언
n = 700

print(n)
print(type(n)) # 자료형 출력
print()

# 동시 선언
x = y = z = 700
print(x, y, z) # 결과: 700 700 700
print()

# 선언
var = 75
# 재선언
var = 'Change Value'

# 출력: 마지막에 선언된 값이 할당
print(var)
print(type(var))
print()

# Object References
# 변수의 값 할당 상태
print()

# id(identity) 확인: 객체의 고유값 확인
m = 800
n = 655

print(id(m))
print(id(n))
print(id(m) == id(n))
print()

# 이름이 다른 두 변수에 같은 값이 할당 되어 있을 때에는 하나의 오브젝트로 생성한다.
m = 800
n = 800

print(m)
print(n)
print(id(m) == id(n))
print() 
