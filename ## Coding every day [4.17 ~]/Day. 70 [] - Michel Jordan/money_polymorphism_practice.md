# 💰 Python 연습: 폴리모피즘으로 Money 클래스 만들기!

여러분, 안녕하세요! 어제 배운 던더(dunder) 메서드를 활용해서 진짜 핀테크 회사에서 쓸 법한 클래스를 만들어볼 시간입니다.

## 🎯 미션

여러분은 한국의 한 핀테크 스타트업에 인턴으로 합류했습니다. 회사는 다양한 통화(USD, KRW, JPY...)를 다루는 결제 시스템을 만들고 있는데, 개발팀장이 여러분에게 핵심 작업을 맡겼습니다:

> "돈을 단순한 숫자가 아니라 **객체**로 다뤄야 합니다. 사용자가 자연스럽게 `+`, `-`, `*`, `==`, `<` 같은 연산자를 쓸 수 있게 만들어주세요. Python의 폴리모피즘을 활용하면 됩니다!"

`Money` 클래스를 설계하고, **던더 메서드(매직 메서드)** 를 활용해 Python의 내장 연산자들이 우리 클래스에서도 자연스럽게 작동하도록 만드는 것이 여러분의 임무입니다.

## 📋 규칙

**주어지는 것:**
- 던더 메서드에 대한 어제 수업 내용
- 클래스와 `__init__`에 대한 사전 지식

**구현해야 할 던더 메서드:**

| 던더 메서드 | 트리거 | 역할 |
|------------|--------|------|
| `__init__` | `Money(100, "USD")` | 객체 초기화 |
| `__str__` | `str(m)`, `print(m)` | 사람이 읽기 좋은 형식 |
| `__repr__` | `repr(m)`, REPL 출력 | 개발자용 형식 |
| `__eq__` | `m1 == m2` | 동등 비교 |
| `__lt__` | `m1 < m2`, `sorted()` | 크기 비교 |
| `__add__` | `m1 + m2` | 더하기 |
| `__sub__` | `m1 - m2` | 빼기 |
| `__mul__` | `m * 3` | 정수 곱하기 |

**반드시 지켜야 할 제약사항:**
- 모든 변수와 메서드 이름은 **snake_case** 사용 (예: `total_amount`)
- **통화가 다르면 더하기/빼기/비교 불가** → `ValueError` 발생시키기
- `__eq__`는 통화가 다르면 무조건 `False` 반환 (에러 발생 X)
- `__mul__`은 `Money * 정수` 형태만 지원 (정수 배수 — 예: 사과 3개)

## 💡 예제

**예제 1: 기본 출력**

```python
salary = Money(3000, "USD")
print(salary)        # 3000.00 USD
print(repr(salary))  # Money(3000, 'USD')
```

**예제 2: 동등 비교**

```python
a = Money(100, "USD")
b = Money(100, "USD")
c = Money(100, "KRW")

print(a == b)  # True
print(a == c)  # False  (통화가 다름)
```

**예제 3: 산술 연산**

```python
coffee = Money(5, "USD")
lunch  = Money(15, "USD")

total = coffee + lunch          # Money(20, 'USD')
print(total)                    # 20.00 USD

monthly_coffee = coffee * 20    # Money(100, 'USD')
print(monthly_coffee)           # 100.00 USD
```

**예제 4: 정렬과 비교 (폴리모피즘의 힘!)**

```python
prices = [Money(50, "USD"), Money(10, "USD"), Money(100, "USD")]
prices.sort()
# [Money(10, 'USD'), Money(50, 'USD'), Money(100, 'USD')]

print(max(prices))  # 100.00 USD
print(min(prices))  # 10.00 USD
```

> 💡 `sort()`, `max()`, `min()`은 우리가 만든 클래스인지 전혀 모릅니다. 그저 `__lt__` 메서드를 호출할 뿐이에요. **이게 바로 폴리모피즘입니다!**

**예제 5: 통화 불일치 에러**

```python
usd = Money(100, "USD")
krw = Money(100000, "KRW")

usd + krw   # ValueError 발생: Cannot add USD and KRW
```

## 🎓 알아야 할 것

시작하기 전에 다음을 확실히 이해하세요:
- 클래스 정의 (`class`, `self`, `__init__`)
- 던더 메서드는 Python이 **자동으로 호출** 한다는 점
- `__add__`는 새로운 객체를 반환 (원본을 수정하지 않음)
- `raise ValueError("메시지")` 문법

## ✅ 과제

다음 시그니처로 `Money` 클래스를 작성하세요:

```python
class Money:
    def __init__(self, amount, currency):
        # 여기에 코드 작성
        pass

    def __str__(self):
        pass

    def __repr__(self):
        pass

    def __eq__(self, other):
        pass

    def __lt__(self, other):
        pass

    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass

    def __mul__(self, multiplier):
        pass
```

**시작하는 데 도움이 될 팁:**
- 금액은 `:.2f` 포맷을 써서 항상 소수점 2자리로 출력
- 통화 검사 로직(`if self.currency != other.currency`)이 여러 메서드에서 반복됨 — 도우미 메서드를 만들면 깔끔해집니다
- `__eq__`만 에러 대신 `False` 반환 (다른 통화의 돈은 같지 않을 뿐, 에러는 아님)
- `__add__`는 `self.amount`를 수정하지 말고 **새 `Money` 객체** 를 반환하세요

## 🎪 코드 테스트

다음 테스트 케이스를 실행해보세요:

```python
# 테스트 1: 기본 생성 및 출력
m = Money(1500, "USD")
assert str(m) == "1500.00 USD"
assert repr(m) == "Money(1500, 'USD')"

# 테스트 2: 동등 비교
assert Money(100, "USD") == Money(100, "USD")
assert Money(100, "USD") != Money(100, "KRW")
assert Money(100, "USD") != Money(50, "USD")

# 테스트 3: 크기 비교
assert Money(50, "USD") < Money(100, "USD")

# 테스트 4: 산술 연산
assert Money(100, "USD") + Money(50, "USD") == Money(150, "USD")
assert Money(100, "USD") - Money(30, "USD") == Money(70, "USD")
assert Money(25, "USD") * 4 == Money(100, "USD")

# 테스트 5: 통화 불일치 에러
try:
    Money(100, "USD") + Money(100, "KRW")
    assert False, "에러가 발생해야 합니다"
except ValueError:
    pass

# 테스트 6: 폴리모피즘 (정렬, max, min)
prices = [Money(50, "USD"), Money(10, "USD"), Money(100, "USD")]
prices.sort()
assert prices[0] == Money(10, "USD")
assert max(prices) == Money(100, "USD")

print("🎉 모든 테스트 통과!")
```

## 🤔 생각해보기

코딩 전에 다음을 스케치해보세요:
1. `__str__`과 `__repr__`의 차이는 무엇인가요? 언제 어떤 게 호출되나요?
2. `__eq__`는 왜 에러를 던지지 않고 `False`를 반환할까요?
3. `prices.sort()`가 어떻게 우리가 만든 `Money` 객체를 정렬할 수 있을까요?
4. `__add__`가 `self.amount`를 직접 수정하면 어떤 문제가 생길까요?

## 🏆 보너스 챌린지

**🥉 Easy: `__hash__` 추가하기**
`Money` 객체를 `set`이나 `dict`의 키로 사용할 수 있게 만들어보세요. (힌트: `__eq__`가 있으면 `__hash__`도 같이 정의해야 합니다.)

```python
unique_prices = {Money(100, "USD"), Money(100, "USD"), Money(50, "USD")}
# 길이는 2여야 합니다
```

**🥈 Medium: `__neg__`와 `__abs__` 추가하기**
음수 금액(빚, 환불)을 표현할 수 있게 단항 연산자를 지원하세요.

```python
debt = Money(50, "USD")
refund = -debt           # Money(-50, 'USD')
absolute = abs(refund)   # Money(50, 'USD')
```

**🥇 Hard: 반사 연산자(reflected operator) 구현하기**
지금은 `money * 3`은 되지만 `3 * money`는 안 됩니다. `__rmul__`을 구현해서 양방향 모두 작동하게 만드세요. 추가로 음수 곱셈도 처리해보세요.

```python
m = Money(10, "USD")
assert m * 3 == 3 * m         # 둘 다 Money(30, 'USD')
assert m * (-1) == Money(-10, "USD")
```

막히면 스레드에 질문 남겨주세요! 목표는 **완성** 이 아니라 **이해** 입니다. Python이 어떻게 우리 클래스를 "자기 것처럼" 다룰 수 있는지 그 신기함을 느껴보세요.

행운을 빕니다! 🚀

---
---

# 💰 Python Practice: Build a Money Class with Polymorphism!

Hey team! Time to apply yesterday's dunder method lesson to build something a real FinTech company would actually use.

## 🎯 Your Mission

You've just joined a Korean FinTech startup as an intern. The company is building a payment system that handles multiple currencies (USD, KRW, JPY...), and your team lead has given you a critical task:

> "Money shouldn't just be raw numbers — it should be **objects**. Make it so users can naturally use operators like `+`, `-`, `*`, `==`, `<`. Python's polymorphism makes this possible!"

Your mission: design a `Money` class and use **dunder methods (magic methods)** to make Python's built-in operators work naturally with your class.

## 📋 The Rules

**What you're given:**
- Yesterday's lesson on dunder methods
- Prior knowledge of classes and `__init__`

**Dunder methods you must implement:**

| Dunder Method | Triggered By | Purpose |
|---------------|--------------|---------|
| `__init__` | `Money(100, "USD")` | Object initialization |
| `__str__` | `str(m)`, `print(m)` | Human-readable format |
| `__repr__` | `repr(m)`, REPL output | Developer-readable format |
| `__eq__` | `m1 == m2` | Equality comparison |
| `__lt__` | `m1 < m2`, `sorted()` | Less-than comparison |
| `__add__` | `m1 + m2` | Addition |
| `__sub__` | `m1 - m2` | Subtraction |
| `__mul__` | `m * 3` | Integer multiplication |

**Constraints you must follow:**
- All variable and method names use **snake_case** (e.g., `total_amount`)
- **Different currencies cannot be added, subtracted, or compared** → raise `ValueError`
- `__eq__` should return `False` for different currencies (NOT raise an error)
- `__mul__` only supports `Money * integer` (integer multiplier, e.g., "3 apples")

## 💡 Examples

**Example 1: Basic output**

```python
salary = Money(3000, "USD")
print(salary)        # 3000.00 USD
print(repr(salary))  # Money(3000, 'USD')
```

**Example 2: Equality comparison**

```python
a = Money(100, "USD")
b = Money(100, "USD")
c = Money(100, "KRW")

print(a == b)  # True
print(a == c)  # False  (different currency)
```

**Example 3: Arithmetic operations**

```python
coffee = Money(5, "USD")
lunch  = Money(15, "USD")

total = coffee + lunch          # Money(20, 'USD')
print(total)                    # 20.00 USD

monthly_coffee = coffee * 20    # Money(100, 'USD')
print(monthly_coffee)           # 100.00 USD
```

**Example 4: Sorting and comparison (the power of polymorphism!)**

```python
prices = [Money(50, "USD"), Money(10, "USD"), Money(100, "USD")]
prices.sort()
# [Money(10, 'USD'), Money(50, 'USD'), Money(100, 'USD')]

print(max(prices))  # 100.00 USD
print(min(prices))  # 10.00 USD
```

> 💡 `sort()`, `max()`, and `min()` have no idea your class even exists. They simply call `__lt__`. **This is polymorphism in action!**

**Example 5: Currency mismatch error**

```python
usd = Money(100, "USD")
krw = Money(100000, "KRW")

usd + krw   # raises ValueError: Cannot add USD and KRW
```

## 🎓 What You Should Know

Before starting, make sure you understand:
- Class definition (`class`, `self`, `__init__`)
- That dunder methods are **called automatically** by Python
- `__add__` returns a new object (it doesn't modify the original)
- `raise ValueError("message")` syntax

## ✅ Your Task

Write a `Money` class with this signature:

```python
class Money:
    def __init__(self, amount, currency):
        # Your code here
        pass

    def __str__(self):
        pass

    def __repr__(self):
        pass

    def __eq__(self, other):
        pass

    def __lt__(self, other):
        pass

    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass

    def __mul__(self, multiplier):
        pass
```

**Tips to get you started:**
- Use `:.2f` format to always print amounts with 2 decimal places
- The currency check (`if self.currency != other.currency`) repeats across methods — a helper method makes it cleaner
- Only `__eq__` returns `False` instead of raising (different-currency money simply isn't equal — that's not an error)
- `__add__` should NOT modify `self.amount` — it should return a **new `Money` object**

## 🎪 Test Your Code

Run these test cases:

```python
# Test 1: Basic construction and output
m = Money(1500, "USD")
assert str(m) == "1500.00 USD"
assert repr(m) == "Money(1500, 'USD')"

# Test 2: Equality
assert Money(100, "USD") == Money(100, "USD")
assert Money(100, "USD") != Money(100, "KRW")
assert Money(100, "USD") != Money(50, "USD")

# Test 3: Less-than
assert Money(50, "USD") < Money(100, "USD")

# Test 4: Arithmetic
assert Money(100, "USD") + Money(50, "USD") == Money(150, "USD")
assert Money(100, "USD") - Money(30, "USD") == Money(70, "USD")
assert Money(25, "USD") * 4 == Money(100, "USD")

# Test 5: Currency mismatch raises error
try:
    Money(100, "USD") + Money(100, "KRW")
    assert False, "Should have raised an error"
except ValueError:
    pass

# Test 6: Polymorphism (sort, max, min)
prices = [Money(50, "USD"), Money(10, "USD"), Money(100, "USD")]
prices.sort()
assert prices[0] == Money(10, "USD")
assert max(prices) == Money(100, "USD")

print("🎉 All tests passed!")
```

## 🤔 Think About It

Before coding, sketch out your thoughts:
1. What's the difference between `__str__` and `__repr__`? When is each called?
2. Why does `__eq__` return `False` instead of raising an error?
3. How does `prices.sort()` manage to sort our custom `Money` objects?
4. What problem arises if `__add__` directly modifies `self.amount`?

## 🏆 Bonus Challenges

**🥉 Easy: Add `__hash__`**
Make `Money` objects usable as `set` or `dict` keys. (Hint: if you define `__eq__`, you should also define `__hash__`.)

```python
unique_prices = {Money(100, "USD"), Money(100, "USD"), Money(50, "USD")}
# Length should be 2
```

**🥈 Medium: Add `__neg__` and `__abs__`**
Support unary operators so you can represent negative amounts (debts, refunds).

```python
debt = Money(50, "USD")
refund = -debt           # Money(-50, 'USD')
absolute = abs(refund)   # Money(50, 'USD')
```

**🥇 Hard: Reflected operator (`__rmul__`)**
Right now `money * 3` works but `3 * money` doesn't. Implement `__rmul__` so it works both directions. Bonus: handle negative multipliers too.

```python
m = Money(10, "USD")
assert m * 3 == 3 * m         # both equal Money(30, 'USD')
assert m * (-1) == Money(-10, "USD")
```

Drop questions in the thread! The goal is **understanding**, not just **finishing**. Take a moment to appreciate how Python can treat your class as if it were its own.

Good luck! 🚀
