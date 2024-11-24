### 문자열 자료형
# 문자열 더해서 연결
head  = 'python'
tail = ' is fun'
print(head+tail)

# 문자열 곱하기
a = 'python'
print(a*2)
print(len(a))

# 문자열 인덱싱
print(a[3])
print(a[0:3])
# 문자열 슬라이싱
b = a[0]+a[1]
print(b)
# 문자열 대입
b = a[:1] + 'i' + a[2:]
print(b)
# 문자열 포매팅
## 숫자 바로 대입
a = "i eat %d" % 3
print(a)
## 문자열 바로 대입
b = 'i eat %s' %'five'
print(b)
## format함수
c = 'i eat {0}' .format(3)
d = ' i eat {0}'.format('5')
print(c)
print(d)
## f 문자열 포매팅
name = '홍'
age = 30
print(f'my {name} . 나이 {age}')

# 문자 개수 세기
a = 'abc'
print(a.count('b'))
# 위치 알려주기 
print(a.find('b'))
print(a.index('a')) # 찾는 문자열 없을 시 오류 발생 
# 문자열 삽입
print(".".join('abc'))
# 양쪽 공백 지우기
a = " hi "
print(a.strip())
# 문자열 바꾸기
a = 'my name'
print(a.replace("my", "is"))
# 문자열 나누기
print(a.split())