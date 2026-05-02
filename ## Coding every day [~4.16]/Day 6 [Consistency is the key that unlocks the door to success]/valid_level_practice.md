# 🐍 Python 연습: 범위 안에 있는지 확인하기!

여러분, 안녕하세요! 이번 문제는 숫자가 특정 범위 안에 들어오는지 확인하는 문제입니다. 그런데 Python에는 다른 언어에서는 찾아볼 수 없는 특별한 문법이 숨어 있어요. 마지막 힌트까지 잘 읽어보세요! 👀

## 🎯 미션

게임 서버 개발팀에 합류했습니다! 플레이어가 캐릭터 레벨을 입력할 때, 유효한 범위인지 검사하는 기능이 필요해요. 캐릭터 레벨은 **1 이상 100 이하**만 허용됩니다. `n`이 유효한 레벨인지 `True` 또는 `False`로 출력하세요.

## 📋 규칙

*주어지는 것:*
• 정수 `n` — 플레이어가 입력한 캐릭터 레벨

*해야 할 일:*
1. `n`이 1 이상인지 확인
2. `n`이 100 이하인지 확인
3. 두 조건을 **동시에** 만족하면 `True`, 그렇지 않으면 `False` 출력

*반드시 따라야 할 제약사항:*
• `print()` 함수 **한 줄**로 결과를 출력해야 합니다
• `if` 조건문은 사용하지 않아도 됩니다!
• 입력은 코드 스켈레톤에 이미 제공되어 있습니다 — `input()` 부분은 건드리지 마세요!

## 💡 예제

**예제 1:**
```
입력: n = 50
출력: True
```
왜? 50은 1 이상(50 >= 1 ✅)이고 100 이하(50 <= 100 ✅)입니다. 유효한 레벨!

**예제 2:**
```
입력: n = 0
출력: False
```
왜? 0은 1보다 작습니다(0 >= 1 ❌). 범위를 벗어났어요!

**예제 3:**
```
입력: n = 101
출력: False
```
왜? 101은 100보다 큽니다(101 <= 100 ❌). 최대 레벨 초과!

**예제 4:**
```
입력: n = 1
출력: True
```
왜? 딱 최솟값! 1은 1 이상(1 >= 1 ✅)이고 100 이하(1 <= 100 ✅)입니다.

**예제 5:**
```
입력: n = 100
출력: True
```
왜? 딱 최댓값! 100은 1 이상(100 >= 1 ✅)이고 100 이하(100 <= 100 ✅)입니다.

## 🎓 알아야 할 것

코딩을 시작하기 전에, 다음을 이해하고 있는지 확인하세요:
• `>=` 연산자 (이상) 와 `<=` 연산자 (이하) 의 차이
• 두 조건을 동시에 만족시키는 방법
• `print()` 안에 식을 바로 넣을 수 있다는 것

## ✅ 과제

다음 시그니처로 함수를 작성하세요:
```python
def is_valid_level(n: int) -> None:
    # 여기에 코드 작성 (한 줄이면 충분해요!)
    pass
```

**시작하는 데 도움이 될 팁:**
• 지난 문제들처럼 `print()` 안에 비교식을 바로 넣을 수 있어요
• 두 조건을 연결하는 방법, 지난 문제에서 배웠죠? 😉
• 풀었다면, 아래 🌟 보너스 섹션도 꼭 읽어보세요!

## 🌟 보너스: Python만의 특별한 문법!

풀이를 완성했나요? 잘했어요! 이제 Python만의 특별한 트릭을 소개할게요.

다른 언어(Java, C, JavaScript 등)에서는 범위 검사를 이렇게 써야 해요:
```
n >= 1 and n <= 100
```

그런데 Python에서는 수학 표기법처럼 **조건을 연결(chaining)**할 수 있어요:
```python
1 <= n <= 100
```

이게 바로 Python의 **비교 연산자 연결(comparison chaining)** 입니다! 수학 시간에 `1 ≤ n ≤ 100`이라고 쓰는 것과 똑같이 읽혀요. Java나 C에서는 이 문법이 작동하지 않지만, Python에서는 완벽하게 동작합니다.

```python
print(1 <= n <= 100)   # 완전히 동일한 결과!
```

두 버전 모두 정답으로 인정됩니다. 하지만 Python다운 코드를 쓰고 싶다면 chaining을 기억해두세요! 🐍

## 🎪 코드 테스트

다음 테스트 케이스를 실행해보세요:

```python
# 테스트 1: 범위 안
is_valid_level(50)
# 예상 출력: True

# 테스트 2: 최솟값보다 작음
is_valid_level(0)
# 예상 출력: False

# 테스트 3: 최댓값보다 큼
is_valid_level(101)
# 예상 출력: False

# 테스트 4: 정확히 최솟값
is_valid_level(1)
# 예상 출력: True

# 테스트 5: 정확히 최댓값
is_valid_level(100)
# 예상 출력: True

# 테스트 6: 음수
is_valid_level(-10)
# 예상 출력: False
```

## 🤔 생각해보기

1. `n >= 1 and n <= 100` 과 `1 <= n <= 100` 은 결과가 같을까요? 직접 테스트해보세요!
2. Java나 C처럼 다른 언어를 배운다면, `1 <= n <= 100` 문법을 그대로 쓸 수 있을까요?
3. `1 <= n < 100` 으로 바꾸면 결과가 달라지는 경우는 언제일까요?

막히면 스레드에 질문을 남겨주세요! 목표는 끝내는 것이 아니라 배우는 것입니다. 천천히 논리를 이해하면서 진행하세요.

행운을 빕니다! 🚀

---
---

# 🐍 Python Practice: Is the Number In Range?

Hey team! This time we're checking whether a number falls within a specific range. But there's a secret Python trick hiding in this problem that you won't find in most other languages — make sure you read all the way to the end! 👀

## 🎯 Your Mission

You've joined a game server development team! When players enter their character level, the system needs to validate it. Only levels **between 1 and 100 (inclusive)** are allowed. Print `True` or `False` depending on whether `n` is a valid level.

## 📋 The Rules

*What you're given:*
• An integer `n` — the character level entered by the player

*What you need to do:*
1. Check whether `n` is greater than or equal to 1
2. Check whether `n` is less than or equal to 100
3. Print `True` if **both** conditions are satisfied, `False` otherwise

*Constraints you must follow:*
• Print the result using **just one** `print()` call
• You do NOT need an `if` statement!
• The input section is already provided in the skeleton — don't touch the `input()` lines!

## 💡 Example Time

**Example 1:**
```
Input: n = 50
Output: True
```
Why? 50 is at least 1 (50 >= 1 ✅) and at most 100 (50 <= 100 ✅). Valid level!

**Example 2:**
```
Input: n = 0
Output: False
```
Why? 0 is less than 1 (0 >= 1 ❌). Out of range!

**Example 3:**
```
Input: n = 101
Output: False
```
Why? 101 is greater than 100 (101 <= 100 ❌). Exceeds max level!

**Example 4:**
```
Input: n = 1
Output: True
```
Why? Exactly the minimum! 1 is at least 1 (1 >= 1 ✅) and at most 100 (1 <= 100 ✅).

**Example 5:**
```
Input: n = 100
Output: True
```
Why? Exactly the maximum! 100 is at least 1 (100 >= 1 ✅) and at most 100 (100 <= 100 ✅).

## 🎓 What You Should Know

Before you start coding, make sure you understand:
• The difference between `>=` (greater than or equal) and `<=` (less than or equal)
• How to satisfy two conditions at the same time
• That you can put expressions directly inside `print()`

## ✅ Your Task

Write a function with this signature:
```python
def is_valid_level(n: int) -> None:
    # Your code here (one line is enough!)
    pass
```

**Tips to get you started:**
• Just like the previous problems, you can put comparison expressions directly inside `print()`
• You already know how to connect two conditions — remember last time? 😉
• Once you're done, make sure to read the 🌟 Bonus section below!

## 🌟 Bonus: A Python-Exclusive Trick!

Got your solution working? Great! Now let me show you something special about Python.

In other languages (Java, C, JavaScript, etc.), a range check has to be written like this:
```
n >= 1 and n <= 100
```

But in Python, you can **chain** comparisons just like in math:
```python
1 <= n <= 100
```

This is called **comparison chaining** — and it reads exactly like the math notation `1 ≤ n ≤ 100`. It works perfectly in Python, but won't work in Java or C!

```python
print(1 <= n <= 100)   # Identical result!
```

Both versions are accepted as correct answers. But if you want to write code that feels truly Pythonic, keep chaining in your toolkit! 🐍

## 🎪 Test Your Code

Try running these test cases:

```python
# Test 1: inside range
is_valid_level(50)
# Expected output: True

# Test 2: below minimum
is_valid_level(0)
# Expected output: False

# Test 3: above maximum
is_valid_level(101)
# Expected output: False

# Test 4: exactly the minimum
is_valid_level(1)
# Expected output: True

# Test 5: exactly the maximum
is_valid_level(100)
# Expected output: True

# Test 6: negative number
is_valid_level(-10)
# Expected output: False
```

## 🤔 Think About It

1. Do `n >= 1 and n <= 100` and `1 <= n <= 100` give the same result? Try both and see!
2. If you were learning Java or C, could you use the `1 <= n <= 100` syntax there?
3. If you changed it to `1 <= n < 100`, when would the result be different?

Drop your questions in the thread if you get stuck! Remember, the goal is to learn, not just to finish. Take your time and understand the logic.

Good luck! 🚀
