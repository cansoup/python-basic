# Chapter02-01
# Print 사용법
# 기본 출력
print('Python Start!')
print("Python Start!")
print('''Python Start!''')
print("""Python Start!""")

print()


# separator 옵션
print('P', 'Y', 'T', 'H', 'O', 'N', sep=',')
print('python', 'google.com', sep='@')

print()


# end 옵션
# print의 default end 옵션은 개행
# end 옵션을 직접 지정할 수 있다. 아래 예제는 한 칸 띄기
print('Welcome to', end=' ')
print('IT News', end=' ')

print()

# file 옵션: 외부 파일 쓰기
import sys

print('Learn Python', file=sys.stdout)

print()


# format 사용(d정수, s문자열, f실수)
print('%s %s' % ('one', 'two'))
print('{} {}'.format('one', 'two'))
print('{1} {0}'.format('one', 'two')) # 순서 지정

print()


# %s
# 자릿수 지정 - 왼쪽부터 공백으로 채움
print('%10s' % ('nice'))
print('{:>10}'.format('nice'))

# 자릿수 지정 - 오른쪽부터 공백으로 채움
print('%-10s' % ('nice'))
print('{:10}'.format('nice'))

# 자릿수 지정 - 원하는 글자로 채우기
print('{:_>10}'.format('nice'))

# 자릿수 지정 - 중앙 정렬
print('{:^10}'.format('nice'))

print('%.5s' % ('pythonStudy')) # 결과: pytho
print('%5s' % ('pythonStudy')) # 결과: pythonStudy
print('{:10.5}'.format('pythonStudy')) # 총 열 글자의 자리를 확보하고 다섯 개만 출력해라

print()


# %d
print('%d %d' % (1, 2))
print('{} {}'.format(1, 2))

print('%4d' % (42))
print('{:4d}'.format(42))

print()


# %f: 정수부 소수부의 포맷 지정 가능
print('%f' % (3.144545454545))
print('%1.18f' % (3.124141423415143124))
print('{:f}'.format(3.144545454545))

print('%06.2f' % (3.1415926)) # 총 6자리, 소수부 2자리, 남는 자리는 0으로 채우기
print('{:06.2f}'.format(3.1415926))

print()