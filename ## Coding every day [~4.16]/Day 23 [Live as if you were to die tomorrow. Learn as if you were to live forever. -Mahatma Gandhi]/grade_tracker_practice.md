# 📊 Python 연습: 시험 성적 분석기 만들기!

여러분, 안녕하세요! 오늘은 실제 데이터를 다루는 성적 분석 프로그램을 만들어볼 거예요.

## 🎯 미션

여러분은 대학교 조교(TA)입니다! 교수님이 이런 부탁을 했어요:

> "이번 학기 시험 점수 데이터가 있는데, 분석 좀 해줄 수 있어요? 최고 점수, 최저 점수, 평균 점수가 필요해요. 그리고 낙제 위험 학생도 파악해야 해요!"

리스트(list)와 반복문(loop)을 활용해서 이 기능들을 구현해봅시다.

## 📋 만들어야 할 함수들

### 1️⃣ `get_highest(scores)`
점수 리스트에서 가장 높은 점수를 반환합니다.
• 반환값: 최고 점수 (숫자)
• **`max()` 사용 금지!** 반복문으로 직접 찾으세요.

### 2️⃣ `get_lowest(scores)`
점수 리스트에서 가장 낮은 점수를 반환합니다.
• 반환값: 최저 점수 (숫자)
• **`min()` 사용 금지!** 반복문으로 직접 찾으세요.

### 3️⃣ `get_average(scores)`
점수 리스트의 평균을 계산하여 반환합니다.
• 반환값: 평균 점수 (소수점 포함)
• **`sum()` 사용 금지!** 반복문으로 직접 합계를 구하세요.

### 4️⃣ `get_failing(scores, passing_score)`
`passing_score` 미만인 점수들을 모아서 새 리스트로 반환합니다.
• 반환값: 낙제 점수들의 리스트
• `passing_score`는 기본값이 60입니다

## 💡 예제

```python
scores = [85, 92, 78, 60, 45, 99, 72, 55]

print(get_highest(scores))        # 99
print(get_lowest(scores))         # 45
print(get_average(scores))        # 73.25
print(get_failing(scores, 60))    # [45, 55]
```

## 🎓 알아야 할 것

코딩 시작 전, 다음 개념을 떠올려보세요:
• `for` 반복문으로 리스트 순회하기
• 비교 연산자 (`>`, `<`) 로 값 비교하기
• 변수에 값 누적하기 (`total = total + score`)
• `len()` 으로 리스트 길이 구하기
• `append()` 로 새 리스트에 항목 추가하기

## ✅ 과제

아래 함수 시그니처를 사용해서 코드를 완성하세요:

```python
def get_highest(scores: list) -> int:
    # TODO: 여기에 코드 작성
    pass

def get_lowest(scores: list) -> int:
    # TODO: 여기에 코드 작성
    pass

def get_average(scores: list) -> float:
    # TODO: 여기에 코드 작성
    pass

def get_failing(scores: list, passing_score: int = 60) -> list:
    # TODO: 여기에 코드 작성
    pass
```

## 🎪 코드 테스트

```python
# 테스트 1: 기본 케이스
scores = [85, 92, 78, 60, 45, 99, 72, 55]
print(get_highest(scores))      # 예상: 99
print(get_lowest(scores))       # 예상: 45
print(get_average(scores))      # 예상: 73.25
print(get_failing(scores, 60))  # 예상: [45, 55]

# 테스트 2: 점수가 하나뿐일 때
single = [77]
print(get_highest(single))      # 예상: 77
print(get_lowest(single))       # 예상: 77
print(get_average(single))      # 예상: 77.0

# 테스트 3: 모두 합격일 때
all_pass = [70, 80, 90]
print(get_failing(all_pass, 60))  # 예상: []

# 테스트 4: 모두 같은 점수일 때
same = [75, 75, 75]
print(get_highest(same))        # 예상: 75
print(get_lowest(same))         # 예상: 75
print(get_average(same))        # 예상: 75.0
```

## 🌟 보너스 챌린지

기본 과제를 다 끝냈나요? 단계별로 도전해봅시다!

---

### 🥉 Easy: `print_report(scores, passing_score)`

분석 결과를 보기 좋게 출력하는 함수를 만드세요.
위에서 만든 네 함수를 **모두 활용**해야 합니다.

```
예상 출력 (scores = [85, 92, 78, 60, 45, 99, 72, 55], passing_score = 60):

========== 성적 리포트 ==========
총 학생 수:   8명
최고 점수:    99점
최저 점수:    45점
평균 점수:    73.25점
낙제 학생 수: 2명 (점수: [45, 55])
================================
```

---

### 🥈 Medium: `get_grade(score)`

점수 하나를 받아서 학점 문자열을 반환하는 함수를 만드세요.

| 점수 범위 | 학점 |
|-----------|------|
| 90 이상   | "A"  |
| 80 이상   | "B"  |
| 70 이상   | "C"  |
| 60 이상   | "D"  |
| 60 미만   | "F"  |

그 다음, `print_report`를 수정해서 각 점수 옆에 학점도 같이 출력되도록 만드세요.

```
예상 출력 (일부):
85점 → B
92점 → A
45점 → F
```

---

### 🥇 Hard: `get_curved_scores(scores, target_average)`

성적 커브를 적용하는 함수를 만드세요.

전체 평균이 `target_average`가 되도록 모든 점수에 동일한 값을 더합니다.
단, 커브 후 어떤 점수도 100을 넘으면 안 됩니다.

```python
scores = [50, 60, 70, 80]
# 현재 평균: 65.0  →  목표 평균: 75.0  →  커브: +10점

get_curved_scores(scores, 75)
# 반환: [60, 70, 80, 90]

# 하지만 커브를 적용했을 때 100을 초과하는 점수가 생기면?
scores2 = [80, 90, 95, 100]
get_curved_scores(scores2, 100)
# 반환: None  (커브 불가!)
# 출력: "커브를 적용할 수 없어요: 일부 점수가 100을 초과합니다."
```

힌트:
• 먼저 현재 평균을 구하세요 (`get_average` 활용 가능!)
• 필요한 커브 값 = `target_average` - 현재 평균
• 커브 후 점수 리스트를 만들고, 100 초과 여부를 확인하세요
• 원본 리스트를 수정하지 말고 새 리스트를 반환하세요

## 🤔 생각해보기

1. `get_highest`에서 첫 번째 점수를 시작값으로 쓰는 이유가 뭘까요?
2. `get_average`에서 `len(scores)`로 나누는 이유는 뭔가요?
3. 점수 리스트가 비어 있다면 어떻게 될까요? 어떻게 처리하면 좋을까요?

막히면 스레드에 질문 남겨주세요! 완성보다 이해가 목표입니다. 천천히, 하나씩! 💪

행운을 빕니다! 🚀

---
---

# 📊 Python Practice: Build an Exam Score Analyzer!

Hey team! Today we're building something genuinely useful — a grade analysis tool that real TAs use.

## 🎯 Your Mission

You're a Teaching Assistant (TA) and your professor just asked:

> "I've got this semester's exam scores and I need some analysis — highest score, lowest score, average, and a list of students at risk of failing. Can you build something for that?"

Let's implement these features using Python lists and loops.

## 📋 Functions to Build

### 1️⃣ `get_highest(scores)`
Returns the highest score from the list.
• Returns: the highest score (number)
• **No `max()`!** Find it yourself using a loop.

### 2️⃣ `get_lowest(scores)`
Returns the lowest score from the list.
• Returns: the lowest score (number)
• **No `min()`!** Find it yourself using a loop.

### 3️⃣ `get_average(scores)`
Calculates and returns the average score.
• Returns: the average (including decimals)
• **No `sum()`!** Add up the scores yourself using a loop.

### 4️⃣ `get_failing(scores, passing_score)`
Returns a new list of all scores below `passing_score`.
• Returns: a list of failing scores
• `passing_score` defaults to 60

## 💡 Example

```python
scores = [85, 92, 78, 60, 45, 99, 72, 55]

print(get_highest(scores))        # 99
print(get_lowest(scores))         # 45
print(get_average(scores))        # 73.25
print(get_failing(scores, 60))    # [45, 55]
```

## 🎓 What You Should Know

Before you start, make sure you're comfortable with:
• Looping through a list with `for`
• Comparing values with `>` and `<`
• Accumulating values in a variable (`total = total + score`)
• Getting list length with `len()`
• Adding items to a new list with `append()`

## ✅ Your Task

Complete the functions using these signatures:

```python
def get_highest(scores: list) -> int:
    # TODO: your code here
    pass

def get_lowest(scores: list) -> int:
    # TODO: your code here
    pass

def get_average(scores: list) -> float:
    # TODO: your code here
    pass

def get_failing(scores: list, passing_score: int = 60) -> list:
    # TODO: your code here
    pass
```

## 🎪 Test Your Code

```python
# Test 1: Basic case
scores = [85, 92, 78, 60, 45, 99, 72, 55]
print(get_highest(scores))      # Expected: 99
print(get_lowest(scores))       # Expected: 45
print(get_average(scores))      # Expected: 73.25
print(get_failing(scores, 60))  # Expected: [45, 55]

# Test 2: Single score
single = [77]
print(get_highest(single))      # Expected: 77
print(get_lowest(single))       # Expected: 77
print(get_average(single))      # Expected: 77.0

# Test 3: Everyone passes
all_pass = [70, 80, 90]
print(get_failing(all_pass, 60))  # Expected: []

# Test 4: All scores the same
same = [75, 75, 75]
print(get_highest(same))        # Expected: 75
print(get_lowest(same))         # Expected: 75
print(get_average(same))        # Expected: 75.0
```

## 🌟 Bonus Challenges

Finished the main tasks? Take it further — one tier at a time!

---

### 🥉 Easy: `print_report(scores, passing_score)`

Build a function that prints a nicely formatted summary report.
You **must use all four** functions you built above.

```
Expected output (scores = [85, 92, 78, 60, 45, 99, 72, 55], passing_score = 60):

========== Grade Report ==========
Total students:  8
Highest score:   99
Lowest score:    45
Average score:   73.25
Failing students: 2 (scores: [45, 55])
==================================
```

---

### 🥈 Medium: `get_grade(score)`

Write a function that takes one score and returns a letter grade.

| Score Range | Grade |
|-------------|-------|
| 90 and above | "A"  |
| 80 and above | "B"  |
| 70 and above | "C"  |
| 60 and above | "D"  |
| Below 60     | "F"  |

Then update `print_report` to show each score alongside its letter grade.

```
Expected output (partial):
85 → B
92 → A
45 → F
```

---

### 🥇 Hard: `get_curved_scores(scores, target_average)`

Build a grade curving function.

Add the same value to every score so that the new average equals `target_average`.
However, no score may exceed 100 after curving.

```python
scores = [50, 60, 70, 80]
# current average: 65.0  →  target: 75.0  →  curve: +10

get_curved_scores(scores, 75)
# returns: [60, 70, 80, 90]

# What if curving would push a score over 100?
scores2 = [80, 90, 95, 100]
get_curved_scores(scores2, 100)
# returns: None
# prints: "Cannot apply curve: some scores would exceed 100."
```

Hints:
• First find the current average (you can reuse `get_average`!)
• Curve amount = `target_average` - current average
• Build the curved list and check if any score exceeds 100
• Don't modify the original list — return a new one

## 🤔 Think About It

1. Why do we use the first score as the starting value in `get_highest`?
2. Why do we divide by `len(scores)` in `get_average`?
3. What would happen if the scores list were empty? How would you handle that?

Drop questions in the thread if you get stuck! The goal is understanding, not just finishing. One step at a time! 💪

Good luck! 🚀
