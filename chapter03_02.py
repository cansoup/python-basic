# Chapter03-02
# 문자형

# 문자열 생성
str1 = "I am Python"

print(len(str1)) # 공백 포함 strlen

# 빈 문자열
str1_t1 = ''
str2_t2 = str()
print()

# 이스케이프 문자 사용
print('I\'m Boy')
print('a \t b')
print('a \n b')
print('a \b b')
print()

# Raw String
raw_s = r'D:\python\test'
print(raw_s)
print()

# 멀티라인 입력
# 역슬래시 사용
multi_str = \
"""
String
Multi Line
Test
"""
print(multi_str)
print()

# 문자열 연산
str_o1 = "python"
str_o2 = "Apple"
str_o3 = "How are you doing"
str_o4 = "Seoul Daejeon Busan Jinju"

print(str_o1 * 3)
print(str_o1 + str_o2)
print('y' in str_o1) # y가 str_o1에 포함되어 있는지?
print('z' in str_o1)
print('P' not in str_o2) # P가 str_o2에 포함되지 않는지?
print()

# 문자열 형 변환
print(str(66), type(str(66)))
print(str(10.1), type(str(10.1)))
print(str(True), type(str(True)))
print()

# 문자열 함수
print("Capitalize: ", str_o1.capitalize) # 첫 번째 시작 문자를 대문자로 변환
print("endswith?: ", str_o2.endswith('s')) # 마지막 문자가 파라미터로 넘겨준 값인지 확인
print("replace: ", str_o1.replace('thon', 'Good')) # thon -> Good
print("sorted: ", sorted(str_o1)) # list형태로 정렬하여 반환
print("split: ", str_o4.split(' '))
print()

# 반복(시퀀스)
im_str = "Good Boy!"

print(dir(im_str)) # __iter__ 

for i in im_str:
  print(i)

# 슬라이싱
str_s1 = "Nice Python"

print(str_s1[0:3]) # 배열의 0번째부터 2번째까지
print(str_s1[5:]) # 5부터 끝까지
print(str_s1[:len(str_s1)]) # 처음부터 끝까지
print(str_s1[1:9:2]) # 결과: iePt (1부터 8까지 2씩 건너뛰면서)
print(str_s1[-5:])
print(str_s1[1:-2])
print(str_s1[::2])
print(str_s1[::-1]) # 역으로 출력
print()

# 아스키 코드(또는 유니코드)
a = 'z'

print(ord(a)) # 문자 -> 아스키
print(chr(122)) # 아스키 -> 문자