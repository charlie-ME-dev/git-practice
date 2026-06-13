# 🐍 Python 연습: 정렬된 손익을 위험도로 변환하기

> *"파이썬다운 코드를 작성한다는 것은, 언어가 이미 제공하는 도구를 신뢰하는 법을 배우는 것이다."*
> — 파이썬 커뮤니티 격언

안녕하세요 여러분! 이번에는 **Wonder Pay**의 실제 데이터 처리 상황으로 파이썬다운(Pythonic) 코딩을 연습해 봅니다.

## 🎯 미션

Wonder Pay의 한 계정에서 하루 동안 발생한 **순손익 기록**이 작은 값부터 큰 값 순으로 정렬되어 들어옵니다. 손실은 음수, 이익은 양수입니다.

리스크 팀은 각 기록의 **위험도 점수**(손익을 제곱한 값)를 알고 싶어 합니다. 손실이든 이익이든, 절댓값이 클수록 위험도가 커지기 때문입니다. 여러분의 임무는 모든 기록을 제곱한 뒤, **다시 작은 값부터 큰 값 순으로 정렬된 리스트**로 반환하는 것입니다.

## 📋 규칙

**주어지는 것:**

- `nums`라는 정수 리스트 (작은 값부터 큰 값 순으로 정렬됨)
- 음수(손실), 0, 양수(이익)가 섞여 있을 수 있음

**해야 할 일:**

1. 각 숫자를 제곱한다
2. 제곱된 값들을 작은 값부터 큰 값 순으로 정렬한다
3. 정렬된 새 리스트를 반환한다

> ⚠️ **함정 주의:** 음수를 제곱하면 양수가 됩니다. 그래서 `-4`의 제곱(16)이 `3`의 제곱(9)보다 큽니다. 입력이 정렬되어 있다고 해서 제곱한 결과가 자동으로 정렬되는 것은 **아닙니다!**

## 💡 예제

**예제 1:**

```
입력:  nums = [-4, -1, 0, 3, 10]
출력:  [0, 1, 9, 16, 100]
```

왜? 제곱하면 `[16, 1, 0, 9, 100]`이 되고, 이것을 정렬하면 `[0, 1, 9, 16, 100]`이 됩니다.

**예제 2:**

```
입력:  nums = [-7, -3, 2, 3, 11]
출력:  [4, 9, 9, 49, 121]
```

왜? 제곱하면 `[49, 9, 4, 9, 121]`이 되고, 정렬하면 `[4, 9, 9, 49, 121]`이 됩니다.

## 🎓 알아야 할 것

시작하기 전에 다음을 이해하고 있는지 확인하세요:

- 리스트 컴프리헨션(list comprehension)으로 새 리스트를 만드는 방법: `[표현식 for 변수 in 리스트]`
- 내장 함수 `sorted()`가 **새로운 정렬된 리스트를 반환**한다는 점 (`.sort()`는 원본을 직접 바꿈)
- 제곱 연산: `n * n` 또는 `n ** 2`
- 음수의 제곱은 양수라는 점

## ✅ 과제

다음 시그니처로 함수를 작성하세요 (snake_case를 지킵니다):

```python
def sorted_squares(nums: list[int]) -> list[int]:
    # 여기에 코드 작성
    pass
```

**시작하는 데 도움이 될 팁:**

- 먼저 "각 숫자를 제곱한 리스트"를 만드는 데 집중하세요
- 그다음 그 리스트를 정렬하면 됩니다
- 리스트 컴프리헨션 한 줄과 `sorted()` 한 번이면 핵심 로직이 끝납니다 — 이것이 파이썬다운 방식입니다

## 🎪 코드 테스트

```python
# 테스트 1
print(sorted_squares([-4, -1, 0, 3, 10]))
# 예상: [0, 1, 9, 16, 100]

# 테스트 2
print(sorted_squares([-7, -3, 2, 3, 11]))
# 예상: [4, 9, 9, 49, 121]

# 테스트 3
print(sorted_squares([-5, -2, 0, 1, 4]))
# 예상: [0, 1, 4, 16, 25]
```

## 🤔 생각해보기

코딩을 시작하기 전에 접근 방법을 스케치해 보세요:

1. 반복문(`for`)으로 푸는 방법과 리스트 컴프리헨션으로 푸는 방법은 무엇이 다를까요?
2. `sorted()`와 `.sort()`의 차이는 무엇일까요? 이 문제에서는 어느 쪽이 더 자연스러울까요?
3. 입력이 이미 정렬되어 있다는 사실을 활용할 방법이 있을까요? (보너스 과제에서 다룹니다)

## 🎁 보너스 과제

### 🥉 Easy — 가장 큰 위험도

`sorted_squares`의 결과에서 **가장 큰 위험도 점수 하나**만 반환하는 함수를 작성하세요. 내장 함수 `max()`를 활용해 보세요.

```python
def biggest_risk(nums: list[int]) -> int:
    ...
```

### 🥈 Medium — 위험도 합계

모든 위험도 점수의 **총합**을 반환하는 함수를 작성하세요. 내장 함수 `sum()`과 리스트 컴프리헨션을 함께 써 보세요. (정렬은 필요 없습니다 — 왜 그럴까요?)

```python
def total_risk(nums: list[int]) -> int:
    ...
```

### 🥇 Hard — 정렬 없이 직접 합치기 (투 포인터)

`sorted()`를 **쓰지 않고** 정렬된 결과를 만들 수 있을까요? 입력이 이미 정렬되어 있다는 점을 이용하면, 양쪽 끝에서 절댓값이 큰 쪽부터 결과의 뒤에서부터 채워 나갈 수 있습니다. 변수 몇 개와 `while` 반복문만으로 도전해 보세요.

```python
def sorted_squares_no_sort(nums: list[int]) -> list[int]:
    ...
```

> 💬 막히면 스레드에 질문을 남겨주세요. 목표는 끝내는 것이 아니라 **파이썬다운 사고방식**을 익히는 것입니다. 천천히 논리를 이해하면서 진행하세요. 행운을 빕니다! 🚀

---
---

# 🐍 Python Practice: Turn Sorted P&L into Risk Scores

> *"Writing Pythonic code means learning to trust the tools the language already gives you."*
> — Python community maxim 

Hey team! This time we're practicing **Pythonic** coding with a real data-processing situation at **Wonder Pay**.

## 🎯 Your Mission

A single Wonder Pay account reports its **net daily P&L entries**, sorted from smallest to largest. Losses are negative, gains are positive.

The Risk team wants the **risk score** of each entry — the P&L squared — because a large loss is just as risky as a large gain. Your job: square every entry, then return a list **sorted from smallest to largest** again.

## 📋 The Rules

**What you're given:**

- A list called `nums` of integers, sorted from smallest to largest
- It may contain negatives (losses), zero, and positives (gains)

**What you need to do:**

1. Square each number
2. Sort the squared values from smallest to largest
3. Return the new sorted list

> ⚠️ **Watch the trap:** A negative squared becomes positive. So `-4` squared (16) is *larger* than `3` squared (9). A sorted input does **not** stay sorted after squaring!

## 💡 Example Time

**Example 1:**

```
Input:  nums = [-4, -1, 0, 3, 10]
Output: [0, 1, 9, 16, 100]
```

Why? Squaring gives `[16, 1, 0, 9, 100]`, and sorting that gives `[0, 1, 9, 16, 100]`.

**Example 2:**

```
Input:  nums = [-7, -3, 2, 3, 11]
Output: [4, 9, 9, 49, 121]
```

Why? Squaring gives `[49, 9, 4, 9, 121]`, and sorting gives `[4, 9, 9, 49, 121]`.

## 🎓 What You Should Know

Before you start, make sure you understand:

- How to build a new list with a list comprehension: `[expression for var in list]`
- That the built-in `sorted()` **returns a new sorted list** (while `.sort()` changes the original in place)
- Squaring: `n * n` or `n ** 2`
- That squaring a negative gives a positive

## ✅ Your Task

Write a function with this signature (keep it snake_case):

```python
def sorted_squares(nums: list[int]) -> list[int]:
    # Your code here
    pass
```

**Tips to get you started:**

- First focus on building "a list of each number squared"
- Then just sort that list
- One list comprehension plus one `sorted()` call is enough for the core logic — that's the Pythonic way

## 🎪 Test Your Code

```python
# Test 1
print(sorted_squares([-4, -1, 0, 3, 10]))
# Expected: [0, 1, 9, 16, 100]

# Test 2
print(sorted_squares([-7, -3, 2, 3, 11]))
# Expected: [4, 9, 9, 49, 121]

# Test 3
print(sorted_squares([-5, -2, 0, 1, 4]))
# Expected: [0, 1, 4, 16, 25]
```

## 🤔 Think About It

Sketch your approach before coding:

1. How does solving this with a `for` loop differ from solving it with a list comprehension?
2. What's the difference between `sorted()` and `.sort()`? Which feels more natural here?
3. Could you use the fact that the input is already sorted? (The bonus explores this.)

## 🎁 Bonus Challenges

### 🥉 Easy — Biggest Risk

Write a function that returns just the **single largest risk score**. Try the built-in `max()`.

```python
def biggest_risk(nums: list[int]) -> int:
    ...
```

### 🥈 Medium — Total Risk

Write a function that returns the **sum** of all risk scores. Combine the built-in `sum()` with a list comprehension. (No sorting needed — why?)

```python
def total_risk(nums: list[int]) -> int:
    ...
```

### 🥇 Hard — Build It Sorted Without `sorted()` (Two Pointers)

Can you produce the sorted result **without** calling `sorted()`? Since the input is already sorted, you can compare the two ends, take whichever has the larger absolute value, and fill the result from the back. Use just a few variables and a `while` loop.

```python
def sorted_squares_no_sort(nums: list[int]) -> list[int]:
    ...
```

> 💬 Drop your questions in the thread if you get stuck. The goal isn't to finish — it's to build a **Pythonic way of thinking**. Take your time with the logic. Good luck! 🚀
