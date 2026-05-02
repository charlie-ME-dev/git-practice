# Python F-String 튜토리얼 / Python F-String Tutorial

## 목차 / Table of Contents
1. [f-string 소개](#1-f-string-소개--introduction)
2. [기본 사용법](#2-기본-사용법--basic-usage)
3. [표현식 사용](#3-표현식-사용--using-expressions)
4. [숫자 포맷팅](#4-숫자-포맷팅--number-formatting)
5. [문자열 정렬](#5-문자열-정렬--string-alignment)
6. [날짜/시간 포맷팅](#6-날짜시간-포맷팅--datetime-formatting)
7. [고급 기능](#7-고급-기능--advanced-features)
8. [연습 문제](#8-연습-문제--exercises)

---

## 1. f-string 소개 / Introduction

### f-string이란? / What is f-string?

**f-string**은 Python 3.6부터 도입된 문자열 포맷팅 방법입니다.  
**f-string** is a string formatting method introduced in Python 3.6.

- `f` 또는 `F`를 문자열 앞에 붙입니다 / Add `f` or `F` before the string
- 중괄호 `{}`안에 변수나 표현식을 넣습니다 / Place variables or expressions inside `{}`
- 실행 시 중괄호 내용이 값으로 치환됩니다 / Contents are replaced with values at runtime

### 기존 방법과의 비교 / Comparison with Old Methods

```python
name = "김철수"
age = 25

# 1. % 포맷팅 (구식) / Old % formatting
msg1 = "이름: %s, 나이: %d" % (name, age)

# 2. .format() 메서드 / .format() method
msg2 = "이름: {}, 나이: {}".format(name, age)

# 3. f-string (권장) / f-string (recommended) ⭐
msg3 = f"이름: {name}, 나이: {age}"
```

**결과 / Result:** 모두 `"이름: 김철수, 나이: 25"` 출력

---

## 2. 기본 사용법 / Basic Usage

### 변수 삽입 / Variable Insertion

```python
# 예제 1: 단순 변수 삽입 / Example 1: Simple variable insertion
name = "이영희"
greeting = f"안녕하세요, {name}님!"
print(greeting)  # 안녕하세요, 이영희님!

# 예제 2: 여러 변수 사용 / Example 2: Multiple variables
first_name = "John"
last_name = "Doe"
full_name = f"{first_name} {last_name}"
print(full_name)  # John Doe

# 예제 3: 숫자 변수 / Example 3: Numeric variables
age = 20
height = 175.5
info = f"나이: {age}세, 키: {height}cm"
print(info)  # 나이: 20세, 키: 175.5cm
```

### 문자열과 함께 사용 / Using with Strings

```python
# 한국어 문장 / Korean sentence
city = "서울"
weather = "맑음"
report = f"오늘 {city}의 날씨는 {weather}입니다."
print(report)  # 오늘 서울의 날씨는 맑음입니다.

# 영어 문장 / English sentence
subject = "Python"
status = "fun"
message = f"Learning {subject} is {status}!"
print(message)  # Learning Python is fun!
```

---

## 3. 표현식 사용 / Using Expressions

### 산술 연산 / Arithmetic Operations

```python
# 계산 결과 직접 출력 / Direct calculation output
width = 10
length = 15
print(f"넓이: {width * length}cm²")  # 넓이: 150cm²

# 복잡한 계산 / Complex calculations
a = 5
b = 3
result = f"{a} + {b} = {a + b}, {a} × {b} = {a * b}"
print(result)  # 5 + 3 = 8, 5 × 3 = 15
```

### 함수 호출 / Function Calls

```python
# 문자열 메서드 / String methods
text = "hello world"
print(f"대문자: {text.upper()}")  # 대문자: HELLO WORLD
print(f"단어 수: {len(text.split())}개")  # 단어 수: 2개

# 내장 함수 / Built-in functions
numbers = [1, 2, 3, 4, 5]
print(f"최댓값: {max(numbers)}, 최솟값: {min(numbers)}")
# 최댓값: 5, 최솟값: 1
```

### 조건 표현식 / Conditional Expressions

```python
# if-else 사용 / Using if-else
score = 85
result = f"결과: {score}점 - {'합격' if score >= 60 else '불합격'}"
print(result)  # 결과: 85점 - 합격

# 등급 판정 / Grade evaluation
grade = "A" if score >= 90 else "B" if score >= 80 else "C"
print(f"학점: {grade}")  # 학점: B
```

---

## 4. 숫자 포맷팅 / Number Formatting

### 소수점 자리수 / Decimal Places

```python
pi = 3.141592653589793

# 소수점 자리수 지정 / Specify decimal places
print(f"소수점 2자리: {pi:.2f}")  # 3.14
print(f"소수점 4자리: {pi:.4f}")  # 3.1416
print(f"소수점 6자리: {pi:.6f}")  # 3.141593
```

### 천단위 구분자 / Thousands Separator

```python
# 큰 숫자 표현 / Large numbers
population = 51000000
print(f"인구: {population:,}명")  # 인구: 51,000,000명

price = 1234567890
print(f"가격: {price:,}원")  # 가격: 1,234,567,890원
```

### 퍼센트 / Percentage

```python
# 비율을 퍼센트로 / Ratio to percentage
ratio = 0.856
print(f"비율: {ratio:.1%}")  # 비율: 85.6%

accuracy = 0.9234
print(f"정확도: {accuracy:.2%}")  # 정확도: 92.34%
```

### 진법 변환 / Base Conversion

```python
num = 255

print(f"10진수: {num}")      # 10진수: 255
print(f"2진수: {num:b}")     # 2진수: 11111111
print(f"8진수: {num:o}")     # 8진수: 377
print(f"16진수: {num:x}")    # 16진수: ff
print(f"16진수(대문자): {num:X}")  # 16진수(대문자): FF
```

---

## 5. 문자열 정렬 / String Alignment

### 왼쪽/가운데/오른쪽 정렬 / Left/Center/Right Alignment

```python
word = "Python"

# 기본 정렬 (20자리) / Basic alignment (20 characters)
print(f"'{word:<20}'")  # 왼쪽 정렬 / Left align
print(f"'{word:^20}'")  # 가운데 정렬 / Center align
print(f"'{word:>20}'")  # 오른쪽 정렬 / Right align
```

**출력 / Output:**
```
'Python              '
'       Python       '
'              Python'
```

### 패딩 문자 지정 / Padding Character

```python
# 특정 문자로 채우기 / Fill with specific character
print(f"'{word:*<20}'")  # 왼쪽 정렬, * 패딩
print(f"'{word:-^20}'")  # 가운데 정렬, - 패딩
print(f"'{word:=>20}'")  # 오른쪽 정렬, = 패딩
```

**출력 / Output:**
```
'Python**************'
'-------Python-------'
'==============Python'
```

### 숫자 정렬 / Number Alignment

```python
# 숫자를 0으로 패딩 / Zero padding for numbers
num = 42
print(f"{num:05d}")  # 00042
print(f"{num:08d}")  # 00000042
```

---

## 6. 날짜/시간 포맷팅 / DateTime Formatting

```python
from datetime import datetime

now = datetime.now()

# 기본 날짜 형식 / Basic date formats
print(f"전체: {now}")
print(f"날짜: {now:%Y-%m-%d}")
print(f"시간: {now:%H:%M:%S}")

# 한국식 날짜 / Korean style
print(f"한국식: {now:%Y년 %m월 %d일 %H시 %M분}")

# 영어식 날짜 / English style
print(f"영어식: {now:%B %d, %Y}")
print(f"요일: {now:%A}")
```

**주요 포맷 코드 / Key Format Codes:**
- `%Y`: 연도 (4자리) / Year (4 digits)
- `%m`: 월 (01-12) / Month (01-12)
- `%d`: 일 (01-31) / Day (01-31)
- `%H`: 시간 (00-23) / Hour (00-23)
- `%M`: 분 (00-59) / Minute (00-59)
- `%S`: 초 (00-59) / Second (00-59)

---

## 7. 고급 기능 / Advanced Features

### 딕셔너리 사용 / Using Dictionaries

```python
student = {
    "name": "박민수",
    "grade": 3,
    "major": "컴퓨터공학"
}

info = f"{student['name']}는 {student['major']} {student['grade']}학년입니다."
print(info)
# 박민수는 컴퓨터공학 3학년입니다.
```

### 디버깅 (Python 3.8+) / Debugging (Python 3.8+)

```python
# = 연산자로 변수명과 값 함께 출력 / Print variable name and value with =
x = 42
y = 3.14
name = "Python"

print(f"{x=}")        # x=42
print(f"{y=:.2f}")    # y=3.14
print(f"{name=}")     # name='Python'
```

### 멀티라인 f-string / Multi-line f-string

```python
name = "경북대학교"
dept = "컴퓨터학부"
students = 500

report = f"""
{'='*40}
대학 정보 / University Information
{'='*40}
학교: {name}
학과: {dept}
학생 수: {students}명
{'='*40}
"""
print(report)
```

### 중괄호 이스케이프 / Escaping Braces

```python
# 중괄호를 문자로 출력하려면 두 번 사용 / Double braces to print literal braces
print(f"{{중괄호}}")  # {중괄호}
print(f"{{x}} = {5}")  # {x} = 5
```

---

## 8. 연습 문제 / Exercises

### 문제 1 / Exercise 1
다음 정보를 f-string으로 출력하세요:
```python
name = "김대학"
age = 22
major = "컴퓨터공학"

# 출력 형식: "안녕하세요! 저는 김대학이고, 22세 컴퓨터공학과 학생입니다."
```

### 문제 2 / Exercise 2
직사각형의 넓이와 둘레를 계산하여 출력하세요:
```python
width = 15
height = 8

# 출력 형식: "넓이: 120cm², 둘레: 46cm"
```

### 문제 3 / Exercise 3
점수를 입력받아 학점을 출력하세요:
```python
score = 87

# 90점 이상: A, 80점 이상: B, 70점 이상: C, 그 외: F
# 출력 형식: "87점 - 학점: B"
```

### 문제 4 / Exercise 4
원주율을 다양한 형식으로 출력하세요:
```python
pi = 3.141592653589793

# 소수점 2자리, 4자리, 6자리로 각각 출력
```

### 문제 5 / Exercise 5
제품 정보를 표 형식으로 출력하세요:
```python
products = [
    {"name": "노트북", "price": 1500000},
    {"name": "마우스", "price": 25000},
    {"name": "키보드", "price": 85000}
]

# 제품명은 왼쪽 정렬(10자리), 가격은 오른쪽 정렬에 천단위 구분자
```

---

## 정리 / Summary

### f-string의 장점 / Advantages
1. ✅ **가독성** / Readability: 코드를 읽기 쉽다
2. ✅ **간결성** / Conciseness: 코드가 짧고 명확하다
3. ✅ **성능** / Performance: 다른 방법보다 빠르다
4. ✅ **유연성** / Flexibility: 표현식, 함수 호출 가능

### 주요 문법 요약 / Key Syntax Summary

| 기능 / Feature | 문법 / Syntax | 예시 / Example |
|---------------|--------------|---------------|
| 기본 변수 / Basic | `f"{var}"` | `f"{name}"` |
| 소수점 / Decimal | `f"{var:.nf}"` | `f"{pi:.2f}"` |
| 천단위 구분 / Comma | `f"{var:,}"` | `f"{price:,}"` |
| 퍼센트 / Percent | `f"{var:.n%}"` | `f"{ratio:.1%}"` |
| 정렬 / Alignment | `f"{var:<n}"` | `f"{text:<10}"` |
| 진법 / Base | `f"{var:b/o/x}"` | `f"{num:x}"` |

---

**연습을 통해 익숙해지세요! / Practice to get comfortable!** 🚀