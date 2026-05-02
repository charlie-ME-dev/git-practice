# 🐍 Python 연습: 여러 값을 한 번에 반환하기!

여러분, 안녕하세요! 오늘은 함수에서 값을 하나가 아닌 **여러 개** 동시에 돌려주는 방법을 배워봅시다.

---

## 💡 개념 먼저 이해하기

지금까지 배운 함수는 값을 하나만 반환했죠:

```python
def add(a, b):
    return a + b

result = add(3, 4)   # result = 7
```

그런데 현실에서는 여러 정보를 한꺼번에 돌려줘야 할 때가 많아요.
예를 들어 영수증 계산기라면 팁, 합계, 1인당 금액 — 세 값이 모두 필요합니다.

Python에서는 `return` 뒤에 쉼표로 값을 나열하면 됩니다:

```python
def get_min_max(a, b, c):
    return a, b, c          # ← 세 값을 한 번에 반환!
```

받을 때는 변수를 쉼표로 나열해서 받으면 됩니다:

```python
x, y, z = get_min_max(10, 20, 30)
print(x)   # 10
print(y)   # 20
print(z)   # 30
```

이렇게 여러 변수에 동시에 값을 받는 것을 **튜플 언패킹(tuple unpacking)** 이라고 해요.

---

## 📌 핵심 규칙

```python
# ✅ 여러 값 반환
def calc(a, b):
    total = a + b
    diff  = a - b
    return total, diff          # 쉼표로 나열

# ✅ 받는 방법 1: 각각 언패킹
t, d = calc(10, 3)
print(t)   # 13
print(d)   # 7

# ✅ 받는 방법 2: 하나의 변수로 받기 (튜플)
result = calc(10, 3)
print(result)        # (13, 7)
print(result[0])     # 13
print(result[1])     # 7
```

---

## 🏢 실전 시나리오

여러분은 앱 개발 팀의 주니어 개발자입니다. 팀장님이 이렇게 말했어요:

> "함수 하나로 여러 계산 결과를 한꺼번에 돌려주게 해줘.
> 불필요하게 함수를 여러 개 만들지 말고!"

실제로 이런 패턴은 실무에서 매우 흔합니다:
• **날씨 앱**: 온도 하나로 섭씨·화씨·체감온도를 동시에 반환
• **성적 시스템**: 점수 하나로 등급·합불·피드백 메시지를 동시에 반환
• **지도 앱**: 두 점 사이의 거리·방향·이동 시간을 동시에 반환

---

## ✅ 과제: 함수 4개 완성하기

### 📝 함수 1: `split_bill`

식당에서 계산서를 나눠 내는 함수입니다. 팁, 총액, 1인당 금액을 동시에 반환하세요.

```python
def split_bill(total: float, num_people: int, tip_rate: float = 0.1):
```

반환 순서: `tip, total_with_tip, per_person`

계산 공식:
```
tip           = total × tip_rate
total_with_tip = total + tip
per_person     = total_with_tip ÷ num_people
```

| 호출 | tip | total_with_tip | per_person |
|------|-----|----------------|------------|
| `split_bill(100000, 4)` | `10000.0` | `110000.0` | `27500.0` |
| `split_bill(80000, 2, 0.15)` | `12000.0` | `92000.0` | `46000.0` |
| `split_bill(60000, 3, 0.0)` | `0.0` | `60000.0` | `20000.0` |

💡 **힌트:** `tip_rate`의 기본값은 `0.1` (10%)이에요!

---

### 📝 함수 2: `get_grade`

시험 점수를 받아 등급, 합불 여부, 피드백 메시지를 동시에 반환하는 함수입니다.

```python
def get_grade(score: int):
```

반환 순서: `letter, status, message`

| 점수 범위 | letter | status | message |
|----------|--------|--------|---------|
| 90 이상 | `"A"` | `"Pass"` | `"Excellent!"` |
| 80 이상 | `"B"` | `"Pass"` | `"Good job!"` |
| 70 이상 | `"C"` | `"Pass"` | `"Keep it up!"` |
| 60 이상 | `"D"` | `"Pass"` | `"Needs improvement."` |
| 60 미만 | `"F"` | `"Fail"` | `"Please retake."` |

| 호출 | 반환값 |
|------|--------|
| `get_grade(95)` | `"A", "Pass", "Excellent!"` |
| `get_grade(83)` | `"B", "Pass", "Good job!"` |
| `get_grade(71)` | `"C", "Pass", "Keep it up!"` |
| `get_grade(65)` | `"D", "Pass", "Needs improvement."` |
| `get_grade(50)` | `"F", "Fail", "Please retake."` |
| `get_grade(90)` | `"A", "Pass", "Excellent!"` (경계값!) |
| `get_grade(60)` | `"D", "Pass", "Needs improvement."` (경계값!) |

💡 **힌트:** 경계값을 주의하세요 — 90점은 A, 60점은 D입니다.

---

### 📝 함수 3: `analyze_temperature`

온도를 받아 섭씨, 화씨, 체감 상태를 동시에 반환하는 함수입니다.

```python
def analyze_temperature(temp: float, unit: str = "C"):
```

반환 순서: `celsius, fahrenheit, condition`

변환 공식:
```
섭씨 → 화씨: fahrenheit = celsius × 9/5 + 32
화씨 → 섭씨: celsius = (fahrenheit - 32) × 5/9
```

체감 상태 기준:
| 섭씨 기준 | condition |
|----------|-----------|
| 0 이하 | `"Freezing"` |
| 0 초과 ~ 15 미만 | `"Cold"` |
| 15 이상 ~ 25 미만 | `"Comfortable"` |
| 25 이상 ~ 35 미만 | `"Warm"` |
| 35 이상 | `"Hot"` |

| 호출 | celsius | fahrenheit | condition |
|------|---------|------------|-----------|
| `analyze_temperature(0)` | `0` | `32.0` | `"Freezing"` |
| `analyze_temperature(20)` | `20` | `68.0` | `"Comfortable"` |
| `analyze_temperature(100)` | `100` | `212.0` | `"Hot"` |
| `analyze_temperature(32, "F")` | `0.0` | `32.0` | `"Freezing"` |
| `analyze_temperature(98.6, "F")` | `37.0` | `98.6` | `"Hot"` |

💡 **힌트:** `unit`의 기본값은 `"C"`예요. `unit == "F"`이면 먼저 섭씨로 변환한 후 조건 판단하세요.

---

### 📝 함수 4: `calculate_rectangle`

직사각형의 넓이, 둘레, 대각선 길이를 동시에 반환하는 함수입니다.

```python
def calculate_rectangle(width: float, height: float):
```

반환 순서: `area, perimeter, diagonal`

계산 공식:
```
area      = width × height
perimeter = 2 × (width + height)
diagonal  = √(width² + height²)   →   (width**2 + height**2) ** 0.5
```

| 호출 | area | perimeter | diagonal |
|------|------|-----------|----------|
| `calculate_rectangle(3, 4)` | `12` | `14` | `5.0` |
| `calculate_rectangle(5, 5)` | `25` | `20` | `≈7.071` |
| `calculate_rectangle(1, 1)` | `1` | `4` | `≈1.414` |
| `calculate_rectangle(10, 2)` | `20` | `24` | `≈10.198` |

💡 **힌트:** 제곱근은 `** 0.5`로 계산할 수 있어요. `import math` 없이도 가능합니다!

---

## 🎪 코드 테스트

```python
# 테스트 1 — split_bill
tip, total_with_tip, per_person = split_bill(100000, 4)
print(tip, total_with_tip, per_person)   # 10000.0 110000.0 27500.0

tip, total_with_tip, per_person = split_bill(80000, 2, 0.15)
print(tip, total_with_tip, per_person)   # 12000.0 92000.0 46000.0

tip, total_with_tip, per_person = split_bill(60000, 3, 0.0)
print(tip, total_with_tip, per_person)   # 0.0 60000.0 20000.0

# 테스트 2 — get_grade
letter, status, message = get_grade(95)
print(letter, status, message)   # A Pass Excellent!

letter, status, message = get_grade(50)
print(letter, status, message)   # F Fail Please retake.

letter, status, message = get_grade(90)
print(letter, status, message)   # A Pass Excellent!

letter, status, message = get_grade(60)
print(letter, status, message)   # D Pass Needs improvement.

# 테스트 3 — analyze_temperature
celsius, fahrenheit, condition = analyze_temperature(0)
print(celsius, fahrenheit, condition)          # 0 32.0 Freezing

celsius, fahrenheit, condition = analyze_temperature(20)
print(celsius, fahrenheit, condition)          # 20 68.0 Comfortable

celsius, fahrenheit, condition = analyze_temperature(32, "F")
print(celsius, fahrenheit, condition)          # 0.0 32.0 Freezing

# 테스트 4 — calculate_rectangle
area, perimeter, diagonal = calculate_rectangle(3, 4)
print(area, perimeter, diagonal)   # 12 14 5.0

area, perimeter, diagonal = calculate_rectangle(5, 5)
print(area, perimeter, diagonal)   # 25 20 7.07...
```

---

## 🤔 생각해보기

1. `tip, total_with_tip, per_person = split_bill(100000, 4)` 에서 왼쪽 변수가 3개인 이유는 무엇일까요?
2. `result = get_grade(95)` 처럼 변수 하나로 받으면 어떤 값이 저장될까요? 직접 출력해보세요.
3. 함수 하나가 여러 값을 반환하는 것과, 함수를 여러 개 만드는 것 — 어떤 방식이 더 편리할까요? 왜 그렇게 생각하나요?

막히면 스레드에 질문을 남겨주세요! 목표는 끝내는 것이 아니라 배우는 것입니다. 🌱

행운을 빕니다! 🚀

---
---

# 🐍 Python Practice: Return Multiple Values at Once!

Hey team! Today we're unlocking one of Python's handiest features — returning **more than one value** from a single function.

---

## 💡 Understand the Concept First

Functions you've written so far return just one value:

```python
def add(a, b):
    return a + b

result = add(3, 4)   # result = 7
```

But in the real world, you often need several pieces of information at once.
A bill calculator, for example, needs the tip, the total, and each person's share — all three.

In Python, just separate values with commas after `return`:

```python
def get_min_max(a, b, c):
    return a, b, c          # ← returns three values at once!
```

To receive them, list the same number of variables on the left:

```python
x, y, z = get_min_max(10, 20, 30)
print(x)   # 10
print(y)   # 20
print(z)   # 30
```

Assigning multiple variables at once like this is called **tuple unpacking**.

---

## 📌 Key Rules

```python
# ✅ Returning multiple values
def calc(a, b):
    total = a + b
    diff  = a - b
    return total, diff          # separate with commas

# ✅ Option 1: Unpack into separate variables
t, d = calc(10, 3)
print(t)   # 13
print(d)   # 7

# ✅ Option 2: Catch everything in one variable (a tuple)
result = calc(10, 3)
print(result)        # (13, 7)
print(result[0])     # 13
print(result[1])     # 7
```

---

## 🏢 Real-World Scenario

You're a junior developer on an app team. Your team lead says:

> "Make your functions return all the related results at once.
> Don't create a bunch of separate functions for each piece of data!"

This pattern shows up everywhere in real software:
• **Weather apps**: One temperature → return Celsius, Fahrenheit, and a feel description all at once
• **Grade systems**: One score → return letter grade, pass/fail status, and a feedback message
• **Maps**: Two points → return distance, direction, and estimated travel time together

---

## ✅ Your Tasks: Complete 4 Functions

### 📝 Function 1: `split_bill`

Calculate a restaurant bill split. Return the tip, the total with tip, and each person's share.

```python
def split_bill(total: float, num_people: int, tip_rate: float = 0.1):
```

Return order: `tip, total_with_tip, per_person`

Formula:
```
tip            = total × tip_rate
total_with_tip = total + tip
per_person     = total_with_tip ÷ num_people
```

| Call | tip | total_with_tip | per_person |
|------|-----|----------------|------------|
| `split_bill(100000, 4)` | `10000.0` | `110000.0` | `27500.0` |
| `split_bill(80000, 2, 0.15)` | `12000.0` | `92000.0` | `46000.0` |
| `split_bill(60000, 3, 0.0)` | `0.0` | `60000.0` | `20000.0` |

💡 **Hint:** The default `tip_rate` is `0.1` (10%)!

---

### 📝 Function 2: `get_grade`

Take a test score and return the letter grade, pass/fail status, and a feedback message.

```python
def get_grade(score: int):
```

Return order: `letter, status, message`

| Score range | letter | status | message |
|-------------|--------|--------|---------|
| 90 and above | `"A"` | `"Pass"` | `"Excellent!"` |
| 80 and above | `"B"` | `"Pass"` | `"Good job!"` |
| 70 and above | `"C"` | `"Pass"` | `"Keep it up!"` |
| 60 and above | `"D"` | `"Pass"` | `"Needs improvement."` |
| Below 60 | `"F"` | `"Fail"` | `"Please retake."` |

| Call | Return values |
|------|--------------|
| `get_grade(95)` | `"A", "Pass", "Excellent!"` |
| `get_grade(83)` | `"B", "Pass", "Good job!"` |
| `get_grade(71)` | `"C", "Pass", "Keep it up!"` |
| `get_grade(65)` | `"D", "Pass", "Needs improvement."` |
| `get_grade(50)` | `"F", "Fail", "Please retake."` |
| `get_grade(90)` | `"A", "Pass", "Excellent!"` (boundary!) |
| `get_grade(60)` | `"D", "Pass", "Needs improvement."` (boundary!) |

💡 **Hint:** Watch the boundary values — 90 is an A, and 60 is a D.

---

### 📝 Function 3: `analyze_temperature`

Take a temperature and return the Celsius value, Fahrenheit value, and a feel description.

```python
def analyze_temperature(temp: float, unit: str = "C"):
```

Return order: `celsius, fahrenheit, condition`

Conversion formulas:
```
Celsius → Fahrenheit: fahrenheit = celsius × 9/5 + 32
Fahrenheit → Celsius: celsius = (fahrenheit - 32) × 5/9
```

Feel description thresholds (based on Celsius):
| Celsius | condition |
|---------|-----------|
| 0 or below | `"Freezing"` |
| above 0, below 15 | `"Cold"` |
| 15 to below 25 | `"Comfortable"` |
| 25 to below 35 | `"Warm"` |
| 35 and above | `"Hot"` |

| Call | celsius | fahrenheit | condition |
|------|---------|------------|-----------|
| `analyze_temperature(0)` | `0` | `32.0` | `"Freezing"` |
| `analyze_temperature(20)` | `20` | `68.0` | `"Comfortable"` |
| `analyze_temperature(100)` | `100` | `212.0` | `"Hot"` |
| `analyze_temperature(32, "F")` | `0.0` | `32.0` | `"Freezing"` |
| `analyze_temperature(98.6, "F")` | `37.0` | `98.6` | `"Hot"` |

💡 **Hint:** The default `unit` is `"C"`. If `unit == "F"`, convert to Celsius first, then check the condition.

---

### 📝 Function 4: `calculate_rectangle`

Calculate the area, perimeter, and diagonal of a rectangle.

```python
def calculate_rectangle(width: float, height: float):
```

Return order: `area, perimeter, diagonal`

Formulas:
```
area      = width × height
perimeter = 2 × (width + height)
diagonal  = √(width² + height²)   →   (width**2 + height**2) ** 0.5
```

| Call | area | perimeter | diagonal |
|------|------|-----------|----------|
| `calculate_rectangle(3, 4)` | `12` | `14` | `5.0` |
| `calculate_rectangle(5, 5)` | `25` | `20` | `≈7.071` |
| `calculate_rectangle(1, 1)` | `1` | `4` | `≈1.414` |
| `calculate_rectangle(10, 2)` | `20` | `24` | `≈10.198` |

💡 **Hint:** Square root is just `** 0.5` — no `import math` needed!

---

## 🎪 Test Your Code

```python
# Test 1 — split_bill
tip, total_with_tip, per_person = split_bill(100000, 4)
print(tip, total_with_tip, per_person)   # 10000.0 110000.0 27500.0

tip, total_with_tip, per_person = split_bill(80000, 2, 0.15)
print(tip, total_with_tip, per_person)   # 12000.0 92000.0 46000.0

tip, total_with_tip, per_person = split_bill(60000, 3, 0.0)
print(tip, total_with_tip, per_person)   # 0.0 60000.0 20000.0

# Test 2 — get_grade
letter, status, message = get_grade(95)
print(letter, status, message)   # A Pass Excellent!

letter, status, message = get_grade(50)
print(letter, status, message)   # F Fail Please retake.

letter, status, message = get_grade(90)
print(letter, status, message)   # A Pass Excellent!

letter, status, message = get_grade(60)
print(letter, status, message)   # D Pass Needs improvement.

# Test 3 — analyze_temperature
celsius, fahrenheit, condition = analyze_temperature(0)
print(celsius, fahrenheit, condition)          # 0 32.0 Freezing

celsius, fahrenheit, condition = analyze_temperature(20)
print(celsius, fahrenheit, condition)          # 20 68.0 Comfortable

celsius, fahrenheit, condition = analyze_temperature(32, "F")
print(celsius, fahrenheit, condition)          # 0.0 32.0 Freezing

# Test 4 — calculate_rectangle
area, perimeter, diagonal = calculate_rectangle(3, 4)
print(area, perimeter, diagonal)   # 12 14 5.0

area, perimeter, diagonal = calculate_rectangle(5, 5)
print(area, perimeter, diagonal)   # 25 20 7.07...
```

---

## 🤔 Think About It

1. In `tip, total_with_tip, per_person = split_bill(100000, 4)`, why are there exactly three variables on the left?
2. What happens if you write `result = get_grade(95)` with just one variable on the left? Try printing it and see!
3. Is it better to have one function return multiple values, or to write separate functions for each value? What are the trade-offs?

Drop your questions in the thread if you get stuck! Remember, the goal is to learn, not just to finish. 🌱

Good luck! 🚀
