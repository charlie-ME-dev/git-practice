# 🐍 Python 연습: 예외 처리로 안전한 환전 계산기 만들기!

여러분, 안녕하세요! 오늘은 실제 핀테크 회사에서 일어날 법한 시나리오로 Python 예외 처리(Exception Handling)를 연습해봅시다.

## 🎯 미션

여러분은 **Wonder Exchange Co.** 라는 핀테크 스타트업의 신입 개발자입니다. 회사의 환전 계산기 앱이 사용자가 이상한 값을 입력했을 때 그냥 멈춰버리는(crash) 문제가 있어요. 여러분의 임무는 **잘못된 입력을 정중하게 거부하는 안전한 환전 함수**를 만드는 것입니다.

> 💡 **핵심:** 프로그램이 죽지 않게 만드는 것이 아닙니다. **잘못된 상황을 명확하게 알리는 예외(exception)를 발생시키는 것**이 목표입니다. 그래야 프로그램의 다른 부분이 그 문제를 처리할 수 있어요.

## 📋 규칙

**주어지는 것:**

- 사용자 입력값 (문자열일 수도 있고, 숫자일 수도 있음)
- 자국 통화 금액과 외국 통화 금액

**해야 할 일:**

1. 두 개의 함수를 작성합니다 (`safe_exchange_rate`, `convert_money`)
2. 각 함수에서 잘못된 입력에 대해 적절한 예외를 발생시킵니다
3. `try` / `except` / `else` / `finally` / `raise` 를 모두 사용해봅니다
4. 예외 메시지에는 **사용자가 이해할 수 있는 설명**을 포함합니다

**반드시 따라야 할 제약사항:**

- 함수 이름과 변수 이름은 모두 **snake_case** (PEP 8 규칙)
- 잘못된 입력을 만나면 **반드시 예외를 발생시켜야 합니다** (`return None`이나 `return -1`로 숨기면 안 됩니다)
- 적절한 예외 타입을 골라야 합니다 (`ValueError` vs `TypeError`)
- 예외를 발생시킬 때 메시지를 꼭 포함합니다

## 💡 예제

**예제 1: `safe_exchange_rate(home_amount, foreign_amount)`**

```
입력: safe_exchange_rate(100, 130)
출력: 1.3
의미: 100원으로 130달러를 살 수 있다면 환율은 1.3
```

```
입력: safe_exchange_rate(0, 130)
출력: ValueError 발생 → "home_amount must be positive"
의미: 0원으로 나누면 ZeroDivisionError가 나기 전에 미리 막아야 합니다!
```

```
입력: safe_exchange_rate("100", 130)
출력: TypeError 발생 → "home_amount must be a number"
의미: 문자열은 숫자가 아니므로 거부합니다
```

**예제 2: `convert_money(amount_str, rate_str)`**

```
입력: convert_money("100", "1.3")
출력: 130.0
의미: input()으로 받은 문자열도 처리할 수 있어야 합니다
```

```
입력: convert_money("abc", "1.3")
출력: ValueError 발생 → "amount must be a number, got: 'abc'"
의미: float() 변환 실패를 우리만의 메시지로 다시 발생시킵니다
```

## 🎓 알아야 할 것

코딩을 시작하기 전에, 다음을 이해하고 있는지 확인하세요:

- `try` / `except` 블록의 기본 구조
- 특정 예외 타입 잡기: `except ValueError as e:`
- `else` 절: 예외가 발생하지 **않았을** 때 실행
- `finally` 절: **항상** 실행 (예외 발생 여부와 무관)
- `raise` 문: 직접 예외 발생시키기 — `raise ValueError("메시지")`
- 자주 쓰이는 내장 예외: `ValueError`, `TypeError`, `ZeroDivisionError`

## ✅ 과제

다음 두 함수를 작성하세요:

```python
def safe_exchange_rate(home_amount: float, foreign_amount: float) -> float:
    """자국 통화 대비 외국 통화의 환율을 계산.
    잘못된 입력은 예외를 발생시킵니다."""
    pass

def convert_money(amount_str, rate_str) -> float:
    """문자열로 받은 금액과 환율을 변환하여 환전 결과를 반환.
    파싱 실패나 잘못된 값은 ValueError를 발생시킵니다."""
    pass
```

**시작하는 데 도움이 될 팁:**

- 입력 검증은 함수의 **맨 앞에서** 하는 것이 좋습니다 (early return의 예외 버전)
- `isinstance(x, (int, float))`로 숫자 타입을 확인할 수 있습니다
- ⚠️ 주의: `isinstance(True, int)`는 `True`를 반환합니다! `bool`을 따로 걸러내야 합니다
- `try` 블록 안에는 **실패할 가능성이 있는 코드만** 넣으세요 (가능한 한 짧게)
- `raise ValueError("메시지")`처럼 메시지를 꼭 넣어야 디버깅하기 쉽습니다

## 🎪 코드 테스트

다음 테스트 케이스를 실행해보세요:

```python
# 테스트 1: 정상 케이스
print(safe_exchange_rate(100, 130))   # 1.3
print(convert_money("100", "1.3"))     # 130.0

# 테스트 2: 0으로 나누기 방지
try:
    safe_exchange_rate(0, 130)
except ValueError as e:
    print(f"예외 잡힘: {e}")

# 테스트 3: 타입 오류
try:
    safe_exchange_rate("100", 130)
except TypeError as e:
    print(f"예외 잡힘: {e}")

# 테스트 4: 파싱 실패
try:
    convert_money("abc", "1.3")
except ValueError as e:
    print(f"예외 잡힘: {e}")
```

## 🤔 생각해보기

코딩을 시작하기 전에, 접근 방법을 스케치해보세요:

1. 어떤 입력이 "잘못된" 입력인가요? (음수? 0? 문자열? `None`?)
2. 각 잘못된 입력에 대해 `ValueError`가 맞을까요, `TypeError`가 맞을까요?
3. `except`로 잡은 예외를 다시 다른 메시지로 `raise`하려면 어떻게 할까요?

## 🎁 보너스 챌린지

기본 과제를 끝냈다면 도전해보세요!

### 🥉 Easy

`safe_divide(a, b)` 함수를 작성하세요. `b`가 0이면 `ZeroDivisionError` 대신 더 친절한 메시지의 `ValueError`를 발생시키세요.

### 🥈 Medium

`convert_money_with_log(amount_str, rate_str)` 함수를 작성하세요.

- `try` 블록에서 변환 시도
- `except`에서 에러 메시지 출력 후 `raise`로 다시 발생
- `else`에서 성공 시 "Conversion successful!" 출력
- `finally`에서 항상 "Transaction logged." 출력

### 🥇 Hard

`batch_convert(amounts, rate)` 함수를 작성하세요. `amounts`는 문자열들의 리스트입니다.

- 각 amount를 환율로 변환
- 변환 실패한 항목은 건너뛰되, 어떤 인덱스에서 실패했는지 출력
- 성공한 결과만 리스트로 반환
- 모든 항목이 실패하면 `ValueError`를 발생시킴

막히면 스레드에 질문을 남겨주세요! 목표는 끝내는 것이 아니라 **왜 예외 처리가 중요한지**를 이해하는 것입니다.

행운을 빕니다! 🚀

---
---

# 🐍 Python Practice: Build a Safe Exchange Calculator with Exception Handling!

Hey team! Today we're practicing Python exception handling through a realistic FinTech scenario.

## 🎯 Your Mission

You're a junior developer at **Wonder Exchange Co.**, a FinTech startup. The company's currency exchange app crashes whenever users enter weird values. Your job is to build **safe exchange functions that politely reject invalid input**.

> 💡 **Key insight:** The goal isn't to prevent the program from "dying." The goal is to **raise clear exceptions when something is wrong**, so other parts of the program can handle the problem properly.

## 📋 The Rules

**What you're given:**

- User inputs (could be strings, could be numbers)
- Home currency amounts and foreign currency amounts

**What you need to do:**

1. Write two functions (`safe_exchange_rate`, `convert_money`)
2. Raise appropriate exceptions for invalid input
3. Use all of: `try` / `except` / `else` / `finally` / `raise`
4. Include **user-friendly messages** in exception messages

**Constraints you must follow:**

- All function and variable names must be **snake_case** (PEP 8)
- For invalid input, you **must raise an exception** (don't hide errors with `return None` or `return -1`)
- Choose the right exception type (`ValueError` vs `TypeError`)
- Always include a message when raising

## 💡 Examples

**Example 1: `safe_exchange_rate(home_amount, foreign_amount)`**

```
Input: safe_exchange_rate(100, 130)
Output: 1.3
Meaning: If 100 KRW buys 130 USD, the rate is 1.3
```

```
Input: safe_exchange_rate(0, 130)
Output: Raises ValueError → "home_amount must be positive"
Meaning: Stop the ZeroDivisionError before it happens!
```

```
Input: safe_exchange_rate("100", 130)
Output: Raises TypeError → "home_amount must be a number"
Meaning: Strings are not numbers, reject them
```

**Example 2: `convert_money(amount_str, rate_str)`**

```
Input: convert_money("100", "1.3")
Output: 130.0
Meaning: Should also handle strings (as if from input())
```

```
Input: convert_money("abc", "1.3")
Output: Raises ValueError → "amount must be a number, got: 'abc'"
Meaning: Re-raise float() failures with our own message
```

## 🎓 What You Should Know

Before you start coding, make sure you understand:

- Basic `try` / `except` block structure
- Catching specific exception types: `except ValueError as e:`
- The `else` clause: runs when **no** exception occurs
- The `finally` clause: runs **always** (regardless of exceptions)
- The `raise` statement: raise your own exception — `raise ValueError("message")`
- Common built-in exceptions: `ValueError`, `TypeError`, `ZeroDivisionError`

## ✅ Your Task

Write these two functions:

```python
def safe_exchange_rate(home_amount: float, foreign_amount: float) -> float:
    """Calculate exchange rate of foreign vs home currency.
    Raise an exception for invalid input."""
    pass

def convert_money(amount_str, rate_str) -> float:
    """Convert string amount and rate, return converted money.
    Raise ValueError for parsing failures or invalid values."""
    pass
```

**Tips to get you started:**

- Validate input at the **beginning** of the function (the exception version of early return)
- Use `isinstance(x, (int, float))` to check numeric types
- ⚠️ Watch out: `isinstance(True, int)` returns `True`! Filter `bool` separately
- Keep `try` blocks **short** — only the code that might fail
- Always include a message: `raise ValueError("message")`

## 🎪 Test Your Code

Try these test cases:

```python
# Test 1: Happy path
print(safe_exchange_rate(100, 130))   # 1.3
print(convert_money("100", "1.3"))     # 130.0

# Test 2: Prevent division by zero
try:
    safe_exchange_rate(0, 130)
except ValueError as e:
    print(f"Caught: {e}")

# Test 3: Type error
try:
    safe_exchange_rate("100", 130)
except TypeError as e:
    print(f"Caught: {e}")

# Test 4: Parsing failure
try:
    convert_money("abc", "1.3")
except ValueError as e:
    print(f"Caught: {e}")
```

## 🤔 Think About It

Before coding, sketch your approach:

1. What inputs are "invalid"? (Negative? Zero? String? `None`?)
2. For each, is `ValueError` correct, or `TypeError`?
3. How do you re-raise an `except`-caught exception with a different message?

## 🎁 Bonus Challenges

Done with the core task? Try these!

### 🥉 Easy

Write `safe_divide(a, b)`. When `b` is 0, raise a friendlier-message `ValueError` instead of `ZeroDivisionError`.

### 🥈 Medium

Write `convert_money_with_log(amount_str, rate_str)`:

- `try` block: attempt conversion
- `except`: print error message, then `raise` to re-raise
- `else`: on success, print "Conversion successful!"
- `finally`: always print "Transaction logged."

### 🥇 Hard

Write `batch_convert(amounts, rate)` where `amounts` is a list of strings:

- Convert each amount with the rate
- Skip failing items, but print which index failed
- Return list of successful results only
- Raise `ValueError` if **all** items fail

Drop questions in the thread if you get stuck! Goal: not to finish, but to **understand why exception handling matters**.

Good luck! 🚀
