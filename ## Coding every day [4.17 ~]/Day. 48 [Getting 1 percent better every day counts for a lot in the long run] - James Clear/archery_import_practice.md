# 🏹 Python 연습: 양궁 점수 계산기 — `import` 문법 마스터하기!

여러분 안녕하세요! 오늘은 Python의 모듈 시스템과 친해지는 시간입니다.

## 🎯 미션

여러분은 **서울 양궁 챔피언십**의 데이터 분석 인턴이 되었습니다. 선수들의 화살이 과녁에 꽂힌 좌표 `(x, y)`가 매번 기록되는데, 코치님께서 이걸 점수로 자동 변환해주는 함수를 부탁하셨어요.

화살이 정중앙(0, 0)에서 멀어질수록 점수가 낮아집니다. 거리는 **피타고라스 정리**로 계산해야 하니, Python의 `math` 모듈을 import해서 사용해야 합니다!

> 💡 **핵심 학습 목표:** 이 과제는 "함수를 푸는 것"보다 **`import`의 3가지 문법**을 모두 익히는 것이 목적입니다. 같은 문제를 세 가지 방식으로 풀어볼 거예요.

## 📋 규칙

**주어지는 것:**
- 화살이 꽂힌 좌표 `x` (float), `y` (float) — 단위는 cm
- 정중앙(bullseye)은 `(0, 0)`

**해야 할 일:**
1. `math` 모듈을 import 한다
2. `math.sqrt`로 정중앙으로부터의 거리를 계산한다
3. 거리에 따라 점수를 반환한다

**점수 규칙:**
- 거리가 50cm를 초과하면 → 0점 (과녁을 벗어남)
- 그 외에는 → `10 - (거리 / 5)`를 내림(floor)한 값

**제약사항:**
- 반드시 `math` 모듈을 사용할 것 (직접 `x**0.5` 같은 것 금지)
- `math.sqrt`와 `math.floor` 두 함수만 사용

## 💡 예제

**예제 1:**
```
입력: x = 0, y = 0
출력: 10
```
왜? 정중앙에 명중! 거리 = 0, 점수 = floor(10 - 0/5) = 10

**예제 2:**
```
입력: x = 3, y = 4
출력: 9
```
왜? 거리 = √(9+16) = 5, 점수 = floor(10 - 5/5) = floor(9) = 9

**예제 3:**
```
입력: x = 30, y = 40
출력: 0
```
왜? 거리 = √(900+1600) = 50, 점수 = floor(10 - 50/5) = floor(0) = 0

**예제 4:**
```
입력: x = 60, y = 0
출력: 0
```
왜? 거리 = 60 > 50, 과녁을 벗어남 → 0점

## 🎓 알아야 할 것

코딩 시작 전에 다음을 확인하세요:
- `import math` 가 무엇을 하는지
- `math.sqrt(x)` 와 `math.floor(x)` 의 사용법
- `**` 연산자 (제곱)
- `if`/`else` 조건문
- 함수가 값을 `return`하는 방법

## ✅ 과제

다음 시그니처로 함수를 작성하세요:

```python
import math

def calculate_arrow_score(x: float, y: float) -> int:
    # 여기에 코드 작성
    pass
```

**시작 팁:**
- 거리 공식: `√(x² + y²)`
- `x ** 2` 는 `x`의 제곱입니다
- 거리를 변수에 먼저 저장한 뒤, `if`로 50cm 초과 여부를 확인하세요
- `math.floor()` 는 소수점을 버리고 내림합니다 (예: `floor(8.7) = 8`)

## 🎪 코드 테스트

```python
# 테스트 1: 정중앙
print(calculate_arrow_score(0, 0))      # 예상: 10

# 테스트 2: 3-4-5 직각삼각형
print(calculate_arrow_score(3, 4))      # 예상: 9

# 테스트 3: 거리 정확히 50
print(calculate_arrow_score(30, 40))    # 예상: 0

# 테스트 4: 과녁 벗어남
print(calculate_arrow_score(60, 0))     # 예상: 0

# 테스트 5: 음수 좌표도 OK (제곱이라 부호 무관)
print(calculate_arrow_score(-6, -8))    # 예상: 8
```

## 🤔 생각해보기

1. 왜 `x`나 `y`가 음수여도 같은 점수가 나올까요?
2. `math.floor` 대신 `int()`를 써도 같은 결과가 나올까요? 어떤 경우에 다를까요?
3. 만약 `math` 대신 `from math import sqrt, floor` 라고 쓴다면, 함수 본문은 어떻게 바뀔까요?

## 🎁 보너스 챌린지 (선택)

기본 함수가 완성됐다면 도전해보세요!

### 🥉 Easy: `import` 스타일 바꾸기
같은 함수를 `from math import sqrt, floor` 스타일로 다시 작성하세요. 함수 이름은 `calculate_arrow_score_v2`로.

### 🥈 Medium: `as`로 별칭 사용하기
`import math as m` 스타일로 다시 작성하세요. 함수 이름은 `calculate_arrow_score_v3`로. 그리고 세 함수가 모두 같은 결과를 내는지 테스트로 확인하세요.

### 🥇 Hard: 화살 시뮬레이션 (`random` 모듈 미리보기)
`random` 모듈의 `random.uniform(-30, 30)`을 사용해서, 무작위 화살 10발을 쏘고 총점을 출력하는 코드를 작성하세요. (힌트: `for` 반복문 + 위에서 만든 함수 활용)

```python
import random
# random.seed(42)  # 같은 결과를 재현하려면 주석 해제
# 여기에 10발 시뮬레이션 코드 작성
```

---

도움이 필요하면 스레드에 질문 남겨주세요! 목표는 빨리 끝내는 게 아니라, **`import`가 어떻게 작동하는지 손으로 직접 익히는 것**입니다.

화이팅! 🏹

---
---

# 🏹 Python Practice: Archery Score Calculator — Master `import` Syntax!

Hey team! Today we're getting comfortable with Python's module system.

## 🎯 Your Mission

You're a data analyst intern at the **Seoul Archery Championship**. Every arrow's hit position is recorded as `(x, y)` coordinates, and the coach asked you to write a function that automatically converts these into scores.

The farther from the bullseye `(0, 0)`, the lower the score. Distance must be computed using the **Pythagorean theorem**, so you'll need to import Python's `math` module!

> 💡 **Key learning goal:** This task is less about "solving the function" and more about practicing **all 3 styles of `import`**. You'll solve the same problem three different ways.

## 📋 The Rules

**What you're given:**
- Arrow's hit coordinates `x` (float), `y` (float) — units are cm
- The bullseye is at `(0, 0)`

**What you need to do:**
1. Import the `math` module
2. Use `math.sqrt` to compute distance from the bullseye
3. Return a score based on that distance

**Scoring rules:**
- Distance > 50cm → 0 points (missed the target)
- Otherwise → floor of `10 - (distance / 5)`

**Constraints:**
- Must use the `math` module (no `x**0.5` shortcuts)
- Use only `math.sqrt` and `math.floor`

## 💡 Examples

**Example 1:**
```
Input: x = 0, y = 0
Output: 10
```
Why? Bullseye! distance = 0, score = floor(10 - 0/5) = 10

**Example 2:**
```
Input: x = 3, y = 4
Output: 9
```
Why? distance = √(9+16) = 5, score = floor(10 - 5/5) = 9

**Example 3:**
```
Input: x = 30, y = 40
Output: 0
```
Why? distance = √(900+1600) = 50, score = floor(10 - 50/5) = 0

**Example 4:**
```
Input: x = 60, y = 0
Output: 0
```
Why? distance = 60 > 50, missed → 0 points

## 🎓 What You Should Know

Before coding, make sure you understand:
- What `import math` does
- How to use `math.sqrt(x)` and `math.floor(x)`
- The `**` operator (exponent)
- `if`/`else` conditions
- How a function `return`s a value

## ✅ Your Task

Write a function with this signature:

```python
import math

def calculate_arrow_score(x: float, y: float) -> int:
    # Your code here
    pass
```

**Tips to start:**
- Distance formula: `√(x² + y²)`
- `x ** 2` is `x` squared
- Save the distance to a variable first, then `if`-check whether it exceeds 50cm
- `math.floor()` rounds down (e.g., `floor(8.7) = 8`)

## 🎪 Test Your Code

```python
# Test 1: bullseye
print(calculate_arrow_score(0, 0))      # Expected: 10

# Test 2: 3-4-5 right triangle
print(calculate_arrow_score(3, 4))      # Expected: 9

# Test 3: distance exactly 50
print(calculate_arrow_score(30, 40))    # Expected: 0

# Test 4: missed the target
print(calculate_arrow_score(60, 0))     # Expected: 0

# Test 5: negative coords work too (squaring removes sign)
print(calculate_arrow_score(-6, -8))    # Expected: 8
```

## 🤔 Think About It

1. Why does the score stay the same when `x` or `y` is negative?
2. Would `int()` work instead of `math.floor`? When might they differ?
3. If you wrote `from math import sqrt, floor` instead, how would the function body change?

## 🎁 Bonus Challenges (optional)

Once your basic function works, try these!

### 🥉 Easy: Switch the import style
Rewrite the same function using `from math import sqrt, floor` style. Name it `calculate_arrow_score_v2`.

### 🥈 Medium: Use `as` for an alias
Rewrite again using `import math as m` style. Name it `calculate_arrow_score_v3`. Then write a test that confirms all three functions produce identical results.

### 🥇 Hard: Arrow simulation (`random` module preview)
Use `random.uniform(-30, 30)` from the `random` module to simulate 10 random arrows and print the total score. (Hint: `for` loop + the function you just wrote.)

```python
import random
# random.seed(42)  # uncomment to reproduce the same results
# Write your 10-arrow simulation here
```

---

Drop questions in the thread if you get stuck! The goal isn't to finish fast — it's to **feel how `import` works with your own hands**.

You got this! 🏹
