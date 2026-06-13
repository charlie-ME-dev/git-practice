# 🐍 Python 연습: 출석부에 번호 매기기 — `enumerate()`

안녕하세요 여러분! 이번에는 조교(TA)가 되어 수업 출석부 시스템을 만들어 봅니다. 리스트를 다룰 때 "지금 몇 번째인지"와 "그 값이 무엇인지"를 **동시에** 알아야 하는 순간이 정말 많습니다. 바로 그럴 때 쓰는 도구가 `enumerate()`입니다.

> 💡 **새로 배우는 문법: 짝 풀기(tuple unpacking)**
> `enumerate()`는 매 반복마다 `(번호, 값)` 두 개를 한꺼번에 건네줍니다. 그래서 변수를 두 개 적어서 한 번에 받습니다.
> ```python
> for number, name in enumerate(names):
>     print(number, name)
> ```
> 여기서 `number`에는 순서(0부터), `name`에는 실제 값이 들어갑니다. 변수 두 개를 쉼표로 나란히 적는 이 방식을 이번 과제에서 처음 사용합니다.

## 🎯 미션

이름이 담긴 리스트를 받아서, (1) 번호가 붙은 출석부를 만들고, (2) 특정 학생이 몇 번인지 찾고, (3) 출석/결석을 정리하는 함수 세 개를 작성합니다.

## 📋 규칙

**주어지는 것**

- `names`: 학생 이름이 순서대로 들어 있는 리스트 (예: `["김민준", "이서연", "박도윤"]`)
- 출석 여부가 담긴 `present_flags`: `True`(출석)/`False`(결석)가 `names`와 같은 순서로 들어 있는 리스트

**지켜야 할 것**

- 모든 함수·변수 이름은 **snake_case**로 작성합니다.
- 번호를 직접 세는 변수(`count = count + 1` 같은 방식)를 만들지 말고, `enumerate()`가 주는 번호를 사용하세요.
- `for i in range(len(names))` 대신 `enumerate()`를 쓰는 것이 이번 과제의 핵심 목표입니다.

## 💡 `enumerate()` 빠르게 보기

`enumerate()`는 리스트를 돌면서 **번호와 값을 같이** 줍니다. `start`를 주면 번호가 시작하는 값을 바꿀 수 있습니다.

```python
fruits = ["사과", "바나나", "포도"]

for i, fruit in enumerate(fruits):        # 번호가 0부터
    print(i, fruit)
# 0 사과
# 1 바나나
# 2 포도

for n, fruit in enumerate(fruits, start=1):   # 번호가 1부터
    print(n, fruit)
# 1 사과
# 2 바나나
# 3 포도
```

사람이 보는 목록은 보통 1번부터 시작하죠? 그럴 때 `start=1`이 아주 유용합니다.

## 🎓 알아야 할 것

시작하기 전에 다음을 이해하고 있는지 확인하세요.

- `for` 반복문으로 리스트를 도는 방법
- 변수 두 개를 동시에 받는 짝 풀기: `for a, b in ...`
- `start` 매개변수가 번호의 시작값을 바꾼다는 점
- f-문자열로 값을 끼워 넣는 방법: `f"{n}. {name}"`
- 리스트 인덱싱: `present_flags[i]`

## ✅ 과제

아래 세 함수를 완성하세요.

**과제 1 — `make_numbered_roster(names)`**
1번부터 번호가 붙은 출석부 문자열 리스트를 반환합니다.

```python
make_numbered_roster(["김민준", "이서연", "박도윤"])
# 반환: ["1. 김민준", "2. 이서연", "3. 박도윤"]
```

**과제 2 — `find_position(names, target)`**
`target` 학생이 몇 번째(1부터)인지 반환합니다. 없으면 `0`을 반환합니다.

```python
find_position(["김민준", "이서연", "박도윤"], "박도윤")   # 반환: 3
find_position(["김민준", "이서연", "박도윤"], "홍길동")   # 반환: 0
```

**과제 3 — `make_attendance_report(names, present_flags)`**
이름과 출석 여부를 짝지어, `"이름: 출석"` 또는 `"이름: 결석"` 문자열 리스트를 반환합니다.

```python
make_attendance_report(["김민준", "이서연"], [True, False])
# 반환: ["김민준: 출석", "이서연: 결석"]
```

> 🧭 **힌트:** 과제 3에서는 `name`(값)과 함께 **번호 `i`**도 필요합니다. `present_flags[i]`로 같은 자리의 출석 여부를 꺼낼 수 있기 때문이죠. 이것이 `enumerate()`가 주는 번호가 쓸모 있는 대표적인 상황입니다.

## 🤔 생각해보기

코딩 전에 접근 방법을 스케치해보세요.

1. `enumerate()`가 매 반복마다 정확히 무엇을 주나요? (몇 개를?)
2. 과제 1에서 번호를 1부터 시작하게 하려면 무엇을 적어야 할까요?
3. 과제 2에서 학생을 찾았을 때 바로 멈추려면 어떻게 할까요? 끝까지 못 찾으면 무엇을 반환하나요?

## 🌟 보너스 도전

| 단계 | 함수 | 설명 |
|---|---|---|
| 🥉 Easy | `make_seating_chart(names, seat_start)` | 번호를 `seat_start`부터 시작하는 좌석표를 만드세요. (예: 11번 자리부터) |
| 🥈 Medium | `find_all_positions(names, letter)` | `letter`로 시작하는 모든 학생의 번호(1부터)를 리스트로 모아 반환하세요. `name.startswith(letter)`를 활용하세요. |
| 🥇 Hard | `label_positions(names)` | 각 학생에게 위치 라벨을 붙이세요: 맨 앞은 `"맨 앞"`, 맨 뒤는 `"맨 뒤"`, 가운데는 `"중간"`. 단, 학생이 한 명뿐이면 `"혼자"`. 빈 리스트도 올바르게 처리하세요. |

> 🥇 **Hard 힌트:** 새로운 문법은 필요 없습니다. `enumerate()`가 주는 번호 `i`를 `0`(맨 앞), `len(names) - 1`(맨 뒤)과 비교하면 됩니다. 학생이 한 명이면 맨 앞이면서 동시에 맨 뒤라는 점을 먼저 처리하세요.

## 🎪 코드 테스트

스켈레톤 파일(`enumerate_skeleton.py`) 아래쪽에 있는 테스트 블록을 실행하면, 통과한 개수가 출력됩니다. 직접 더 많은 경우(빈 리스트, 학생 한 명 등)도 시험해보세요!

---

> 📌 **(자리 표시) 이번 패키지 명언:** 이 자리에 주제에 맞는 출처 확인된 명언을 한국어·영어로 넣을 예정입니다. (배포 직전 확정)

막히면 스레드에 질문을 남겨주세요. 목표는 빨리 끝내는 것이 아니라 `enumerate()`가 **언제, 왜** 편한지 몸으로 익히는 것입니다. 천천히! 🚀

---
---

# 🐍 Python Practice: Numbering an Attendance Roster — `enumerate()`

Hey team! This time you're the TA building a class attendance system. When you work with lists, you constantly need to know *both* "what position am I at" *and* "what's the value here" at the same time. The tool for exactly that is `enumerate()`.

> 💡 **New syntax: tuple unpacking**
> Every loop, `enumerate()` hands you two things at once: `(number, value)`. So you write two variables to catch them together.
> ```python
> for number, name in enumerate(names):
>     print(number, name)
> ```
> `number` holds the position (starting at 0), `name` holds the actual value. Writing two comma-separated variables like this is something we use for the first time in this package.

## 🎯 Your Mission

Take a list of names and write three functions that (1) build a numbered roster, (2) find what number a given student is, and (3) summarize who's present or absent.

## 📋 The Rules

**What you're given**

- `names`: a list of student names in order (e.g. `["김민준", "이서연", "박도윤"]`)
- `present_flags`: a list of `True` (present) / `False` (absent), in the same order as `names`

**What to follow**

- All function and variable names use **snake_case**.
- Don't make your own counter variable (`count = count + 1`); use the number `enumerate()` gives you.
- The whole point of this package is to use `enumerate()` instead of `for i in range(len(names))`.

## 💡 `enumerate()` at a Glance

`enumerate()` walks a list and gives you **the number and the value together**. Add `start` to change where the numbering begins.

```python
fruits = ["사과", "바나나", "포도"]

for i, fruit in enumerate(fruits):        # numbers from 0
    print(i, fruit)
# 0 사과
# 1 바나나
# 2 포도

for n, fruit in enumerate(fruits, start=1):   # numbers from 1
    print(n, fruit)
# 1 사과
# 2 바나나
# 3 포도
```

Human-facing lists usually start at 1, right? That's exactly when `start=1` shines.

## 🎓 What You Should Know

Before you start, make sure you understand:

- Looping through a list with `for`
- Catching two variables at once (unpacking): `for a, b in ...`
- That the `start` parameter changes the starting number
- Inserting values with f-strings: `f"{n}. {name}"`
- List indexing: `present_flags[i]`

## ✅ Your Task

Complete these three functions.

**Task 1 — `make_numbered_roster(names)`**
Return a list of roster strings numbered from 1.

```python
make_numbered_roster(["김민준", "이서연", "박도윤"])
# returns: ["1. 김민준", "2. 이서연", "3. 박도윤"]
```

**Task 2 — `find_position(names, target)`**
Return what number (from 1) the `target` student is. Return `0` if not present.

```python
find_position(["김민준", "이서연", "박도윤"], "박도윤")   # returns: 3
find_position(["김민준", "이서연", "박도윤"], "홍길동")   # returns: 0
```

**Task 3 — `make_attendance_report(names, present_flags)`**
Pair each name with its attendance flag and return strings like `"name: 출석"` or `"name: 결석"`.

```python
make_attendance_report(["김민준", "이서연"], [True, False])
# returns: ["김민준: 출석", "이서연: 결석"]
```

> 🧭 **Hint:** In Task 3 you need the **number `i`** alongside the value `name`, because `present_flags[i]` pulls the flag from the matching position. This is the classic situation where the number from `enumerate()` earns its keep.

## 🤔 Think About It

Sketch your approach before coding.

1. What exactly does `enumerate()` give you each loop? (How many things?)
2. In Task 1, what do you write to make the numbering start at 1?
3. In Task 2, how do you stop right when you find the student? What do you return if you never find them?

## 🌟 Bonus Challenges

| Tier | Function | Description |
|---|---|---|
| 🥉 Easy | `make_seating_chart(names, seat_start)` | Build a numbered chart whose numbers start at `seat_start` (e.g. seat 11 onward). |
| 🥈 Medium | `find_all_positions(names, letter)` | Return a list of the 1-based positions of every student whose name starts with `letter`. Use `name.startswith(letter)`. |
| 🥇 Hard | `label_positions(names)` | Label each student by position: first → `"맨 앞"`, last → `"맨 뒤"`, otherwise `"중간"`. But if there is only one student, label `"혼자"`. Handle an empty list correctly too. |

> 🥇 **Hard hint:** No new syntax needed. Compare the number `i` from `enumerate()` against `0` (first) and `len(names) - 1` (last). Handle the one-student case first, since that student is both first *and* last.

## 🎪 Test Your Code

Run the test block at the bottom of `enumerate_skeleton.py`; it prints how many checks passed. Try extra cases yourself too (empty list, a single student, etc.)!

---

> 📌 **(placeholder) Package quote:** A verified, on-theme quote will go here in Korean and English (finalized just before delivery).

Drop questions in the thread if you get stuck. The goal isn't to finish fast — it's to feel *when* and *why* `enumerate()` makes life easier. Take your time! 🚀
