# 🐍 Python 연습: 숫자 크기 비교하기!

여러분, 안녕하세요! 오늘은 비교 연산자를 써볼 시간입니다. 짧지만 핵심을 꿰뚫는 문제예요!

## 🎯 미션

스타트업 입사 지원자 심사 시스템을 만들고 있어요. 두 지원자의 점수 `a`와 `b`를 받아서, `a`가 `b`보다 높은지 확인하는 기능이 필요합니다. 결과는 `True` 또는 `False`로 출력합니다.

## 📋 규칙

*주어지는 것:*
• 정수 `a` — 첫 번째 지원자의 점수
• 정수 `b` — 두 번째 지원자의 점수

*해야 할 일:*
1. `a`가 `b`보다 큰지 비교
2. 결과를 `True` 또는 `False`로 출력

*반드시 따라야 할 제약사항:*
• 비교 연산자(`>`)를 사용해야 합니다
• `print()` 함수 **한 줄**로 결과를 출력해야 합니다
• `if` 조건문은 사용하지 않아도 됩니다!
• 입력은 코드 스켈레톤에 이미 제공되어 있습니다 — `input()` 부분은 건드리지 마세요!

## 💡 예제

**예제 1:**
```
입력: a = 5, b = 3
출력: True
```
왜? 5는 3보다 크니까요!

**예제 2:**
```
입력: a = 2, b = 7
출력: False
```
왜? 2는 7보다 크지 않으니까요.

**예제 3:**
```
입력: a = 4, b = 4
출력: False
```
왜? 4는 4보다 크지 않아요 — *같은* 것은 "더 크다"가 아닙니다!

## 🎓 알아야 할 것

코딩을 시작하기 전에, 다음을 이해하고 있는지 확인하세요:
• 비교 연산자 `>` 가 무엇인지
• `True`와 `False`가 Python에서 어떤 의미인지 (대문자 주의! ✋)
• `print()` 함수 안에 식(expression)을 바로 넣을 수 있다는 것

## 💡 힌트: print() 안에 식을 넣을 수 있어요!

Python에서 `>` 같은 비교 연산자는 그 자체로 `True` 또는 `False`를 반환합니다:
```
5 > 3   →   True
2 > 7   →   False
4 > 4   →   False
```
그리고 `print()`는 어떤 값이든 바로 출력할 수 있어요:
```python
print(5 > 3)   # 출력: True
```
`a`와 `b`로도 똑같이 할 수 있을까요? 🤔

## ✅ 과제

다음 시그니처로 함수를 작성하세요:
```python
def is_a_greater(a: int, b: int) -> None:
    # 여기에 코드 작성 (딱 한 줄이면 충분해요!)
    pass
```

## 🎪 코드 테스트

다음 테스트 케이스를 실행해보세요:

```python
# 테스트 1: a가 더 큰 경우
is_a_greater(5, 3)
# 예상 출력: True

# 테스트 2: b가 더 큰 경우
is_a_greater(2, 7)
# 예상 출력: False

# 테스트 3: 같은 경우
is_a_greater(4, 4)
# 예상 출력: False

# 테스트 4: 음수 포함
is_a_greater(-1, -5)
# 예상 출력: True
```

## 🤔 생각해보기

코딩을 시작하기 전에, 스스로에게 물어보세요:
1. `a > b` 는 어떤 값을 반환할까요?
2. `print()` 안에 `a > b` 를 바로 넣으면 어떻게 될까요?
3. `a == b` 일 때 결과가 `True`여야 할까요, `False`여야 할까요?

막히면 스레드에 질문을 남겨주세요! 목표는 끝내는 것이 아니라 배우는 것입니다. 천천히 논리를 이해하면서 진행하세요.

행운을 빕니다! 🚀

---
---

# 🐍 Python Practice: Comparing Two Numbers!

Hey team! Today we're putting comparison operators to work. Short problem, big concept!

## 🎯 Your Mission

You're building a candidate scoring system for a startup. Given two applicant scores `a` and `b`, your job is to check whether `a` is higher than `b` and print the result as `True` or `False`.

## 📋 The Rules

*What you're given:*
• An integer `a` — the first applicant's score
• An integer `b` — the second applicant's score

*What you need to do:*
1. Compare whether `a` is greater than `b`
2. Print the result as `True` or `False`

*Constraints you must follow:*
• You must use the comparison operator (`>`)
• Print the result using **just one** `print()` call
• You do NOT need an `if` statement!
• The input section is already provided in the skeleton — don't touch the `input()` lines!

## 💡 Example Time

**Example 1:**
```
Input: a = 5, b = 3
Output: True
```
Why? 5 is greater than 3!

**Example 2:**
```
Input: a = 2, b = 7
Output: False
```
Why? 2 is not greater than 7.

**Example 3:**
```
Input: a = 4, b = 4
Output: False
```
Why? 4 is not greater than 4 — *equal* is not "greater than"!

## 🎓 What You Should Know

Before you start coding, make sure you understand:
• What the comparison operator `>` does
• What `True` and `False` mean in Python (capital letters matter! ✋)
• That you can put an expression directly inside `print()`

## 💡 Hint: You can put expressions inside print()!

In Python, comparison operators like `>` already return `True` or `False` on their own:
```
5 > 3   →   True
2 > 7   →   False
4 > 4   →   False
```
And `print()` can output any value directly:
```python
print(5 > 3)   # Output: True
```
Can you do the same thing with `a` and `b`? 🤔

## ✅ Your Task

Write a function with this signature:
```python
def is_a_greater(a: int, b: int) -> None:
    # Your code here (just one line is enough!)
    pass
```

## 🎪 Test Your Code

Try running these test cases:

```python
# Test 1: a is greater
is_a_greater(5, 3)
# Expected output: True

# Test 2: b is greater
is_a_greater(2, 7)
# Expected output: False

# Test 3: equal values
is_a_greater(4, 4)
# Expected output: False

# Test 4: negative numbers
is_a_greater(-1, -5)
# Expected output: True
```

## 🤔 Think About It

Before you start coding, ask yourself:
1. What value does `a > b` return on its own?
2. What happens if you put `a > b` directly inside `print()`?
3. When `a == b`, should the result be `True` or `False`?

Drop your questions in the thread if you get stuck! Remember, the goal is to learn, not just to finish. Take your time and understand the logic.

Good luck! 🚀
