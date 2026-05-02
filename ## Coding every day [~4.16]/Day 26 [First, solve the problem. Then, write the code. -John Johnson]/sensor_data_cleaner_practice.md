# 🌡️ Python 연습: 센서 데이터 정리하기!

여러분, 안녕하세요! 오늘은 실제 데이터 분석 현장에서 꼭 필요한 "데이터 정제(cleaning)" 작업을 구현해봅니다.

## 🎯 미션

여러분은 스마트 팩토리의 주니어 데이터 엔지니어입니다! 팀장이 이렇게 요청했어요:

> "공장 온도 센서에서 데이터가 들어오는데, 가끔 센서가 오작동해서 말도 안 되는 값이 섞여요. 정상 범위를 벗어난 값들을 걸러내고, 얼마나 많은 오류가 있었는지 분석해주세요!"

리스트와 반복문을 활용해서 이 데이터 정제 시스템을 만들어봅시다.

## 📋 만들어야 할 함수들

### 1️⃣ `is_valid(reading, min_val, max_val)`
온도 측정값이 유효한지 판단합니다.
• `min_val` 이상이고 `max_val` 이하이면 `True` 반환
• 그 외에는 `False` 반환
• **이 함수가 "오류"의 기준을 정의합니다 — 여러분이 직접 범위를 설계하세요!**

### 2️⃣ `clean_readings(readings, min_val, max_val)`
측정값 리스트에서 유효하지 않은 값들을 걸러냅니다.
• `is_valid()`를 재사용해야 합니다
• 반환값: 유효한 값들만 담긴 새 리스트

### 3️⃣ `count_errors(readings, min_val, max_val)`
측정값 리스트에서 오류 값의 개수를 셉니다.
• `is_valid()`를 재사용해야 합니다
• 반환값: 오류 개수 (정수)

### 4️⃣ `error_rate(readings, min_val, max_val)`
전체 측정값 중 오류 비율을 계산합니다.
• 반환값: 0.0 ~ 100.0 사이의 퍼센트 값 (float)
• 빈 리스트가 들어오면 `0.0` 반환
• `count_errors()`를 재사용하세요

## 💡 예제

공장 온도 센서의 정상 범위는 **-10°C ~ 120°C** 라고 가정해봅시다.

```python
readings = [23.5, -999.0, 45.2, 87.1, 999.9, 30.0, -50.0, 101.3]
min_val = -10
max_val = 120

print(is_valid(23.5, min_val, max_val))    # True
print(is_valid(-999.0, min_val, max_val))  # False
print(is_valid(120.0, min_val, max_val))   # True  ← 경계값!
print(is_valid(120.1, min_val, max_val))   # False ← 경계값 바로 위!

cleaned = clean_readings(readings, min_val, max_val)
print(cleaned)
# [23.5, 45.2, 87.1, 30.0, 101.3]

print(count_errors(readings, min_val, max_val))   # 3
print(error_rate(readings, min_val, max_val))     # 37.5
```

## 🎓 알아야 할 것

코딩 시작 전, 다음 개념을 떠올려보세요:
• `for` 반복문으로 리스트 순회하기
• 비교 연산자 (`>=`, `<=`) 와 논리 연산자 (`and`)
• `append()` 로 새 리스트에 항목 추가하기
• `len()` 으로 리스트 길이 구하기
• 함수 안에서 다른 함수 호출하기 (함수 재사용!)

## ✅ 과제

아래 함수 시그니처를 사용해서 코드를 완성하세요:

```python
def is_valid(reading: float, min_val: float, max_val: float) -> bool:
    # TODO: 여기에 코드 작성
    pass

def clean_readings(readings: list, min_val: float, max_val: float) -> list:
    # TODO: 여기에 코드 작성
    pass

def count_errors(readings: list, min_val: float, max_val: float) -> int:
    # TODO: 여기에 코드 작성
    pass

def error_rate(readings: list, min_val: float, max_val: float) -> float:
    # TODO: 여기에 코드 작성
    pass
```

**💭 코딩 전에 생각해보세요:**
`is_valid()`를 먼저 완성하세요. 나머지 세 함수는 모두 이 함수를 재사용합니다!

## 🎪 코드 테스트

```python
min_val = -10
max_val = 120

# 테스트 1: is_valid 경계값 확인
print(is_valid(-10, min_val, max_val))    # 예상: True  ← 최솟값 포함
print(is_valid(-10.1, min_val, max_val))  # 예상: False ← 최솟값 바로 아래
print(is_valid(120, min_val, max_val))    # 예상: True  ← 최댓값 포함
print(is_valid(120.1, min_val, max_val))  # 예상: False ← 최댓값 바로 위

# 테스트 2: 기본 정제
readings = [23.5, -999.0, 45.2, 87.1, 999.9, 30.0, -50.0, 101.3]
print(clean_readings(readings, min_val, max_val))
# 예상: [23.5, 45.2, 87.1, 30.0, 101.3]

# 테스트 3: 오류 개수 및 비율
print(count_errors(readings, min_val, max_val))  # 예상: 3
print(error_rate(readings, min_val, max_val))    # 예상: 37.5

# 테스트 4: 오류 없음
clean_data = [10.0, 50.0, 90.0]
print(count_errors(clean_data, min_val, max_val))  # 예상: 0
print(error_rate(clean_data, min_val, max_val))    # 예상: 0.0

# 테스트 5: 전부 오류
all_errors = [-999.0, 999.9, -500.0]
print(count_errors(all_errors, min_val, max_val))  # 예상: 3
print(error_rate(all_errors, min_val, max_val))    # 예상: 100.0

# 테스트 6: 빈 리스트
print(error_rate([], min_val, max_val))            # 예상: 0.0
```

## 🌟 보너스 챌린지

기본 과제를 다 끝냈나요? 단계별로 도전해봅시다!

---

### 🥉 Easy: `print_summary(readings, min_val, max_val)`

분석 결과를 보기 좋게 출력하는 함수를 만드세요.
위에서 만든 **네 함수를 모두 활용**해야 합니다.

```
예상 출력 (readings = [23.5, -999.0, 45.2, 87.1, 999.9, 30.0, -50.0, 101.3]):

====== 센서 데이터 분석 리포트 ======
총 측정 횟수:  8회
유효 데이터:   5개
오류 데이터:   3개
오류 비율:     37.5%
정상 범위:     -10 ~ 120
정제된 데이터: [23.5, 45.2, 87.1, 30.0, 101.3]
=====================================
```

---

### 🥈 Medium: `get_stats(readings, min_val, max_val)`

정제된 데이터의 최솟값, 최댓값, 평균을 계산해서 딕셔너리로 반환하는 함수를 만드세요.

```python
readings = [23.5, -999.0, 45.2, 87.1, 999.9, 30.0]
result = get_stats(readings, -10, 120)
# 반환: {"min": 23.5, "max": 87.1, "average": 46.5}
```

제약사항:
• `clean_readings()`로 먼저 정제하세요
• `min()`, `max()`, `sum()` 사용 금지 — 반복문으로 직접 계산하세요
• 정제 후 데이터가 없으면 `None` 반환

---

### 🥇 Hard: `find_error_streaks(readings, min_val, max_val)`

연속으로 이어진 오류 구간을 찾아서 리스트로 반환하는 함수를 만드세요.

```python
readings = [10, -999, -888, 50, 70, -777, -666, -555, 30]
#                ^^^^^^^^^^             ^^^^^^^^^^^^^^^^^^
#                오류 2개 연속           오류 3개 연속

find_error_streaks(readings, -10, 120)
# 반환: [2, 3]   ← 각 연속 오류 구간의 길이
```

• 연속 오류가 없으면 빈 리스트 `[]` 반환
• 오류가 1개만 이어져도 `[1]` 로 포함
• 힌트: 현재 연속 오류 길이를 추적하는 카운터 변수를 사용하세요

## 🤔 생각해보기

1. `is_valid()`를 따로 만드는 이유가 뭘까요? 조건을 `clean_readings()` 안에 바로 써도 되지 않을까요?
2. 유효한 범위를 `-10 ~ 120` 으로 정했는데, 실제 센서라면 어떤 기준으로 범위를 결정해야 할까요?
3. `error_rate()`에서 빈 리스트를 따로 처리하지 않으면 어떤 일이 생길까요?

막히면 스레드에 질문 남겨주세요! 완성보다 이해가 목표입니다. 천천히, 하나씩! 💪

행운을 빕니다! 🚀

---
---

# 🌡️ Python Practice: Clean Up Sensor Data!

Hey team! Today we're building something used in real data pipelines — a sensor data cleaner.

## 🎯 Your Mission

You're a junior data engineer at a smart factory! Your team lead just said:

> "Our temperature sensors occasionally malfunction and send back garbage values. We need to filter out anything outside the valid range and track how many errors we're seeing!"

Let's build a data cleaning system using Python lists and loops.

## 📋 Functions to Build

### 1️⃣ `is_valid(reading, min_val, max_val)`
Determines whether a temperature reading is valid.
• Returns `True` if `reading` is between `min_val` and `max_val` (inclusive)
• Returns `False` otherwise
• **This function defines what "error" means — you design the condition!**

### 2️⃣ `clean_readings(readings, min_val, max_val)`
Filters out invalid values from a list of readings.
• Must reuse `is_valid()`
• Returns: a new list containing only valid values

### 3️⃣ `count_errors(readings, min_val, max_val)`
Counts how many readings in the list are invalid.
• Must reuse `is_valid()`
• Returns: the error count (integer)

### 4️⃣ `error_rate(readings, min_val, max_val)`
Calculates the percentage of readings that are errors.
• Returns: a float between 0.0 and 100.0
• Returns `0.0` if the list is empty
• Must reuse `count_errors()`

## 💡 Example

Let's say a factory temperature sensor has a valid range of **-10°C to 120°C**.

```python
readings = [23.5, -999.0, 45.2, 87.1, 999.9, 30.0, -50.0, 101.3]
min_val = -10
max_val = 120

print(is_valid(23.5, min_val, max_val))    # True
print(is_valid(-999.0, min_val, max_val))  # False
print(is_valid(120.0, min_val, max_val))   # True  ← boundary!
print(is_valid(120.1, min_val, max_val))   # False ← just above boundary!

cleaned = clean_readings(readings, min_val, max_val)
print(cleaned)
# [23.5, 45.2, 87.1, 30.0, 101.3]

print(count_errors(readings, min_val, max_val))   # 3
print(error_rate(readings, min_val, max_val))     # 37.5
```

## 🎓 What You Should Know

Before you start, make sure you're comfortable with:
• Looping through a list with `for`
• Comparison operators (`>=`, `<=`) and logical operators (`and`)
• Adding items to a new list with `append()`
• Getting list length with `len()`
• Calling one function from inside another (function reuse!)

## ✅ Your Task

Complete the functions using these signatures:

```python
def is_valid(reading: float, min_val: float, max_val: float) -> bool:
    # TODO: your code here
    pass

def clean_readings(readings: list, min_val: float, max_val: float) -> list:
    # TODO: your code here
    pass

def count_errors(readings: list, min_val: float, max_val: float) -> int:
    # TODO: your code here
    pass

def error_rate(readings: list, min_val: float, max_val: float) -> float:
    # TODO: your code here
    pass
```

**💭 Think before you code:**
Complete `is_valid()` first. The other three functions all reuse it!

## 🎪 Test Your Code

```python
min_val = -10
max_val = 120

# Test 1: is_valid boundary checks
print(is_valid(-10, min_val, max_val))    # Expected: True  ← min included
print(is_valid(-10.1, min_val, max_val))  # Expected: False ← just below min
print(is_valid(120, min_val, max_val))    # Expected: True  ← max included
print(is_valid(120.1, min_val, max_val))  # Expected: False ← just above max

# Test 2: Basic cleaning
readings = [23.5, -999.0, 45.2, 87.1, 999.9, 30.0, -50.0, 101.3]
print(clean_readings(readings, min_val, max_val))
# Expected: [23.5, 45.2, 87.1, 30.0, 101.3]

# Test 3: Error count and rate
print(count_errors(readings, min_val, max_val))  # Expected: 3
print(error_rate(readings, min_val, max_val))    # Expected: 37.5

# Test 4: No errors
clean_data = [10.0, 50.0, 90.0]
print(count_errors(clean_data, min_val, max_val))  # Expected: 0
print(error_rate(clean_data, min_val, max_val))    # Expected: 0.0

# Test 5: All errors
all_errors = [-999.0, 999.9, -500.0]
print(count_errors(all_errors, min_val, max_val))  # Expected: 3
print(error_rate(all_errors, min_val, max_val))    # Expected: 100.0

# Test 6: Empty list
print(error_rate([], min_val, max_val))            # Expected: 0.0
```

## 🌟 Bonus Challenges

Finished the main tasks? Take it further — one tier at a time!

---

### 🥉 Easy: `print_summary(readings, min_val, max_val)`

Build a function that prints a nicely formatted analysis report.
You **must use all four** functions you built above.

```
Expected output (readings = [23.5, -999.0, 45.2, 87.1, 999.9, 30.0, -50.0, 101.3]):

====== Sensor Data Analysis Report ======
Total readings:  8
Valid readings:  5
Error readings:  3
Error rate:      37.5%
Valid range:     -10 ~ 120
Cleaned data:    [23.5, 45.2, 87.1, 30.0, 101.3]
=========================================
```

---

### 🥈 Medium: `get_stats(readings, min_val, max_val)`

Calculate the min, max, and average of the **cleaned** data and return them as a dictionary.

```python
readings = [23.5, -999.0, 45.2, 87.1, 999.9, 30.0]
result = get_stats(readings, -10, 120)
# returns: {"min": 23.5, "max": 87.1, "average": 46.5}
```

Constraints:
• Use `clean_readings()` first
• No `min()`, `max()`, or `sum()` — calculate with loops
• Return `None` if no valid data remains after cleaning

---

### 🥇 Hard: `find_error_streaks(readings, min_val, max_val)`

Find all consecutive runs of errors and return their lengths as a list.

```python
readings = [10, -999, -888, 50, 70, -777, -666, -555, 30]
#                ^^^^^^^^^^             ^^^^^^^^^^^^^^^^^^
#                2 errors in a row       3 errors in a row

find_error_streaks(readings, -10, 120)
# returns: [2, 3]   ← length of each consecutive error run
```

• Return `[]` if there are no error streaks
• A single isolated error counts as `[1]`
• Hint: use a counter variable to track the current streak length

## 🤔 Think About It

1. Why do we build `is_valid()` as a separate function? Couldn't we just write the condition directly inside `clean_readings()`?
2. We chose `-10 ~ 120` as our valid range — how would you decide the right range for a real sensor?
3. What would happen in `error_rate()` if we didn't handle the empty list case separately?

Drop questions in the thread if you get stuck! The goal is understanding, not just finishing. One step at a time! 💪

Good luck! 🚀
