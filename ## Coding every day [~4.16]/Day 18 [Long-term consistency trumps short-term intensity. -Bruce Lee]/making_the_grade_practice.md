# 🐍 Python 연습: 성적 처리 시스템 만들기!

안녕하세요, 여러분! 오늘은 실제 업무에서 바로 쓸 수 있는 성적 처리 프로그램을 만들어 볼 거예요.

## 🎭 시나리오

여러분은 대학교 조교(Teaching Assistant)로 채용됐습니다! 🎓
기말고사 채점이 끝났는데... 점수 정리가 아직 하나도 안 됐어요.
교수님은 내일까지 다음 자료들을 요청하셨습니다:

- 점수를 정수로 반올림한 목록
- 불합격 학생 수
- 상위권 학생들의 점수 목록
- 학생 이름과 점수를 매칭한 순위표

Python 함수들을 만들어서 이 작업을 자동화해봅시다!

---

## 📋 오늘 만들 함수들

### 함수 1️⃣ `round_scores(student_scores)` — 점수 반올림

시험 점수는 소수점이 있을 수 있어요 (부분 점수 때문에).
하지만 최종 성적은 반드시 정수여야 합니다!

*주어지는 것:*
• `student_scores` — 소수점이 포함된 점수들의 리스트

*해야 할 일:*
• 각 점수를 `round()`로 반올림해서 새 리스트로 반환

*예제:*
```
입력: [90.33, 40.5, 55.44, 70.05, 30.55]
출력: [90, 40 또는 41*, 55, 70, 31]
```
> 💡 Python의 `round()` 함수를 사용하세요!
> ⚠️ `round(40.5)`의 결과가 예상과 다를 수 있어요 — 직접 확인해보세요!

---

### 함수 2️⃣ `count_failed_students(student_scores)` — 불합격자 수 세기

교수님이 "몇 명이나 떨어졌어?" 라고 물어보셨어요.
**40점 이하**면 불합격입니다.

*주어지는 것:*
• `student_scores` — 정수 점수들의 리스트

*해야 할 일:*
• 40점 **이하**인 학생의 수를 세어서 반환

*예제:*
```
입력: [90, 40, 55, 70, 30, 25, 80, 95, 38, 40]
출력: 5
```
> 💡 40점은 불합격입니다! `<=` 를 사용하세요.
> 💡 반복문 안에서 조건을 확인하고, 카운터 변수를 활용하세요.

---

### 함수 3️⃣ `above_threshold(student_scores, threshold)` — 상위권 학생 찾기

교수님이 "기준 점수 이상인 학생들만 뽑아줘" 라고 하셨어요.
기준은 매번 달라지니까, 함수가 유연해야 해요!

*주어지는 것:*
• `student_scores` — 점수들의 리스트
• `threshold` — 기준 점수

*해야 할 일:*
• 기준 점수 **이상(`>=`)** 인 점수들만 모아서 새 리스트로 반환

*예제:*
```
입력: student_scores=[90, 40, 55, 70, 30, 68, 70, 75, 83, 96], threshold=75
출력: [90, 75, 83, 96]
```
> 💡 새 리스트를 만들고, 조건에 맞는 점수만 담으세요.
> 💡 아직 `.append()`를 안 배웠죠? 힌트: `for` 루프 안에서 `print()` 대신 리스트에 담는 방법을 생각해보세요.

---

### 함수 4️⃣ `student_ranking(student_scores, student_names)` — 순위표 만들기

드디어 마지막! 점수와 이름을 연결해서 순위표를 만들어야 해요.
두 리스트는 **이미 같은 순서로 정렬**되어 있어요 (1등 학생이 두 리스트 모두 첫 번째).

*주어지는 것:*
• `student_scores` — 높은 점수 순으로 정렬된 점수 리스트
• `student_names` — 같은 순서로 정렬된 이름 리스트

*해야 할 일:*
• `"순위. 이름: 점수"` 형식의 문자열들을 모아서 리스트로 반환

*예제:*
```
입력:
  student_scores = [100, 99, 90, 84, 66]
  student_names  = ['지수', '민준', '서연', '하은', '준서']

출력:
  ['1. 지수: 100', '2. 민준: 99', '3. 서연: 90', '4. 하은: 84', '5. 준서: 66']
```
> 💡 `range(len(student_scores))`로 인덱스를 순서대로 만들 수 있어요!
> 💡 `student_scores[i]`와 `student_names[i]`로 같은 위치의 값에 접근할 수 있어요.
> 💡 `i + 1`이 순위가 됩니다 (인덱스는 0부터 시작하니까요).

---

## 🎪 코드 테스트

아래 테스트를 복사해서 실행해보세요:

```python
# 테스트 1: round_scores
scores1 = [90.33, 40.5, 55.44, 70.05, 30.55, 25.45, 80.45, 95.3, 38.7, 40.3]
print("반올림 결과:", round_scores(scores1))
# 참고: round(40.5)의 결과를 꼭 직접 확인해보세요!

# 테스트 2: count_failed_students
scores2 = [90, 40, 55, 70, 30, 25, 80, 95, 38, 40]
print("불합격자 수:", count_failed_students(scores2))
# 예상: 5

# 테스트 3: above_threshold
scores3 = [90, 40, 55, 70, 30, 68, 70, 75, 83, 96]
print("75점 이상:", above_threshold(scores3, 75))
# 예상: [90, 75, 83, 96]

scores4 = [90, 40, 55, 70, 30, 68, 70, 75, 83, 96]
print("100점 이상:", above_threshold(scores4, 100))
# 예상: []

# 테스트 4: student_ranking
s_scores = [100, 99, 90, 84, 66, 53, 47]
s_names  = ['지수', '민준', '서연', '하은', '준서', '다인', '승현']
ranking = student_ranking(s_scores, s_names)
for line in ranking:
    print(line)
# 예상:
# 1. 지수: 100
# 2. 민준: 99
# 3. 서연: 90
# 4. 하은: 84
# 5. 준서: 66
# 6. 다인: 53
# 7. 승현: 47
```

---

## 🤔 시작 전 생각해보기

코딩 전에 아이디어를 스케치해보세요:

1. 반복문을 돌면서 각 점수에 어떤 처리를 해야 할까요?
2. 조건에 맞는 것만 골라낼 때, 결과를 어떻게 모을까요?
3. 두 리스트에서 **같은 인덱스**의 값을 동시에 쓰려면 어떻게 해야 할까요?

막히면 스레드에 질문해주세요! 🙋
목표는 **완성**이 아니라 **이해**입니다. 천천히 논리를 따라가세요.

---

## 🌟 보너스 도전 (다 끝낸 사람만!)

*쉬움 🟢* — `count_failed_students`에서, 불합격자 수 대신 불합격자들의 **점수 리스트**를 반환하는 버전을 만들어보세요.

*중간 🟡* — `student_ranking`에서, `enumerate()`를 사용해서 같은 결과를 만들어보세요. (`enumerate()`가 무엇인지 검색해보세요!)

*어려움 🔴* — `above_threshold`와 `student_ranking`을 합쳐서, 기준 점수 **이상인 학생들의 순위표**만 출력하는 새 함수 `honor_roll(student_scores, student_names, threshold)`를 만들어보세요.

행운을 빕니다! 🚀

---
---

# 🐍 Python Practice: Build a Grade Processing System!

Hey team! Today you're going to build something you could actually use in real life.

## 🎭 The Scenario

You've just been hired as a Teaching Assistant at a university! 🎓
The final exam is done, but the scores are a complete mess.
Your professor needs the following by tomorrow:

- Scores rounded to whole numbers
- A count of students who failed
- A list of scores above a certain threshold
- A ranked list matching student names to their scores

Let's automate all of this with Python functions!

---

## 📋 Functions to Build Today

### Function 1️⃣ `round_scores(student_scores)` — Round the Scores

Exam scores can include decimals (partial credit). But final grades must be whole numbers!

*What you're given:*
• `student_scores` — a list of scores with decimal points

*What to do:*
• Use `round()` on each score and return a new list of integers

*Example:*
```
Input:  [90.33, 40.5, 55.44, 70.05, 30.55]
Output: [90, 40 or 41*, 55, 70, 31]
```
> 💡 Use Python's built-in `round()` function!
> ⚠️ The result of `round(40.5)` might surprise you — check it yourself!

---

### Function 2️⃣ `count_failed_students(student_scores)` — Count Who Failed

The professor asked "How many students didn't pass?"
A score of **40 or below** is a failing grade.

*What you're given:*
• `student_scores` — a list of integer scores

*What to do:*
• Count how many scores are **40 or below** and return that count

*Example:*
```
Input:  [90, 40, 55, 70, 30, 25, 80, 95, 38, 40]
Output: 5
```
> 💡 40 is a failing score! Use `<=`.
> 💡 Use a counter variable and update it inside your loop.

---

### Function 3️⃣ `above_threshold(student_scores, threshold)` — Find the Top Scores

The professor wants to see only scores at or above a certain cutoff.
The cutoff changes each time, so your function needs to be flexible!

*What you're given:*
• `student_scores` — a list of scores
• `threshold` — the minimum score to include

*What to do:*
• Collect every score `>=` threshold and return them as a new list

*Example:*
```
Input:  student_scores=[90, 40, 55, 70, 30, 68, 70, 75, 83, 96], threshold=75
Output: [90, 75, 83, 96]
```
> 💡 Build a new list and add matching scores to it.
> 💡 Haven't learned `.append()` yet? Hint: think about how to collect values inside a `for` loop.

---

### Function 4️⃣ `student_ranking(student_scores, student_names)` — Build the Ranking

Final task! Connect each score to a student name and create a ranking.
Both lists are **already sorted in the same order** — the top student is first in both.

*What you're given:*
• `student_scores` — scores sorted highest to lowest
• `student_names` — names in the same order

*What to do:*
• Return a list of strings in the format `"rank. name: score"`

*Example:*
```
Input:
  student_scores = [100, 99, 90, 84, 66]
  student_names  = ['Joci', 'Sara', 'Kora', 'Jan', 'John']

Output:
  ['1. Joci: 100', '2. Sara: 99', '3. Kora: 90', '4. Jan: 84', '5. John: 66']
```
> 💡 Use `range(len(student_scores))` to loop through index positions.
> 💡 Access matching values with `student_scores[i]` and `student_names[i]`.
> 💡 `i + 1` gives the rank (because indexes start at 0).

---

## 🎪 Test Your Code

Copy and run these test cases:

```python
# Test 1: round_scores
scores1 = [90.33, 40.5, 55.44, 70.05, 30.55, 25.45, 80.45, 95.3, 38.7, 40.3]
print("Rounded:", round_scores(scores1))
# Note: check what round(40.5) returns — it might surprise you!

# Test 2: count_failed_students
scores2 = [90, 40, 55, 70, 30, 25, 80, 95, 38, 40]
print("Failed count:", count_failed_students(scores2))
# Expected: 5

# Test 3: above_threshold
scores3 = [90, 40, 55, 70, 30, 68, 70, 75, 83, 96]
print("Above 75:", above_threshold(scores3, 75))
# Expected: [90, 75, 83, 96]

scores4 = [90, 40, 55, 70, 30, 68, 70, 75, 83, 96]
print("Above 100:", above_threshold(scores4, 100))
# Expected: []

# Test 4: student_ranking
s_scores = [100, 99, 90, 84, 66, 53, 47]
s_names  = ['Joci', 'Sara', 'Kora', 'Jan', 'John', 'Bern', 'Fred']
ranking = student_ranking(s_scores, s_names)
for line in ranking:
    print(line)
# Expected:
# 1. Joci: 100
# 2. Sara: 99
# 3. Kora: 90
# 4. Jan: 84
# 5. John: 66
# 6. Bern: 53
# 7. Fred: 47
```

---

## 🤔 Think Before You Code

Sketch out your approach before writing anything:

1. What do you need to do to **each score** as you loop through the list?
2. When filtering values, how do you **collect** the ones that match?
3. When you need values from **two lists at the same position**, how do you access both at once?

Post your questions in the thread if you get stuck! 🙋
The goal is **understanding**, not just finishing. Follow the logic step by step.

---

## 🌟 Bonus Challenges (Only if you finish early!)

*Easy 🟢* — Modify `count_failed_students` so it returns the **list of failing scores** instead of just the count.

*Medium 🟡* — Rewrite `student_ranking` using `enumerate()`. Look it up and try it!

*Hard 🔴* — Combine `above_threshold` and `student_ranking` into a new function `honor_roll(student_scores, student_names, threshold)` that returns a ranking of only the students who scored at or above the threshold.

Good luck! 🚀
