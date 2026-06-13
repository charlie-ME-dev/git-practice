# 🐍 Python 연습: 나만의 통화(Money) 클래스 만들기!

여러분, 안녕하세요! 이번에는 OOP에서 가장 재미있는 부분 중 하나인 **던더 메서드(Dunder Methods)** 를 사용해서 진짜 쓸만한 클래스를 만들어봅니다.

## 🎯 미션

여러분은 글로벌 핀테크 스타트업의 주니어 개발자입니다. 회사의 결제 시스템에서 사용할 **`Money` 클래스**를 만들어야 합니다.

지금까지는 금액을 그냥 숫자로만 다뤘는데, 문제가 많았어요:
- `1500 + 200` → 이게 USD인지 KRW인지 알 수 없음 😱
- `print(salary)` → 그냥 숫자만 나옴, 통화 표시 없음
- 통화가 다른 금액을 실수로 더해도 막을 방법이 없음

이제 던더 메서드의 힘으로 `wallet + bonus`, `print(salary)`, `hourly_wage * 40` 같은 자연스러운 코드를 가능하게 만들어봅시다!

## 📋 규칙

*주어지는 것:*
- 빈 `Money` 클래스 스켈레톤
- 작성해야 할 던더 메서드 목록과 시그니처

*해야 할 일:*
1. `__init__(self, amount, currency)` — 금액과 통화 코드를 받아 초기화
2. `__str__(self)` — 사용자에게 보여줄 문자열 (예: `"1,500.00 USD"`)
3. `__repr__(self)` — 개발자/디버깅용 문자열 (예: `"Money(1500, 'USD')"`)
4. `__add__(self, other)` — 같은 통화끼리 더하기, 새 `Money` 객체 반환
5. `__sub__(self, other)` — 같은 통화끼리 빼기, 새 `Money` 객체 반환
6. `__mul__(self, scalar)` — 숫자(스칼라)와 곱하기 (예: 시급 × 시간)

*반드시 따라야 할 제약사항:*
- **다른 통화끼리 더하기/빼기는 금지!** `ValueError`를 발생시켜야 합니다
- 산술 연산(`+`, `-`, `*`)은 **항상 새로운 `Money` 객체를 반환** — 원본을 수정하지 마세요
- `__str__`은 천 단위 콤마와 소수점 2자리로 포맷팅 (예: `"1,234.56 USD"`)
- `__repr__`은 `eval()`로 다시 객체를 만들 수 있는 형태로

## 💡 예제

**예제 1: 문자열 표현**
```python
wallet = Money(1500, "USD")
print(wallet)        # 출력: 1,500.00 USD
print(repr(wallet))  # 출력: Money(1500, 'USD')
```

**예제 2: 덧셈과 뺄셈**
```python
salary = Money(3000, "USD")
bonus = Money(500, "USD")
total = salary + bonus
print(total)  # 출력: 3,500.00 USD

balance = Money(1000, "USD")
payment = Money(250, "USD")
remaining = balance - payment
print(remaining)  # 출력: 750.00 USD
```

**예제 3: 스칼라 곱셈**
```python
hourly_wage = Money(25, "USD")
weekly_pay = hourly_wage * 40
print(weekly_pay)  # 출력: 1,000.00 USD
```

**예제 4: 다른 통화 거부**
```python
usd = Money(100, "USD")
krw = Money(100, "KRW")
result = usd + krw  # ValueError 발생!
```

## 🎓 알아야 할 것

코딩을 시작하기 전에, 다음을 이해하고 있는지 확인하세요:
- 클래스와 `__init__` 작성법
- `self`가 무엇인지
- 던더 메서드(매직 메서드)가 무엇인지 — 파이썬이 자동으로 호출하는 특별한 메서드
- `__str__` vs `__repr__`의 차이
- `raise`로 에러를 발생시키는 방법
- f-string 포맷팅 (예: `f"{value:,.2f}"`)

## ✅ 과제

다음 클래스를 완성하세요:
```python
class Money:
    def __init__(self, amount, currency):
        # 여기에 코드 작성
        pass

    def __str__(self):
        # 여기에 코드 작성
        pass

    def __repr__(self):
        # 여기에 코드 작성
        pass

    def __add__(self, other):
        # 여기에 코드 작성
        pass

    def __sub__(self, other):
        # 여기에 코드 작성
        pass

    def __mul__(self, scalar):
        # 여기에 코드 작성
        pass
```

**시작하는 데 도움이 될 팁:**
- `__str__`에서 천 단위 콤마는 f-string의 `:,` 포맷 지정자로 만들 수 있어요
- 산술 연산은 **새 `Money` 객체를 반환**해야 합니다 — `return Money(...)` 형태로
- 통화 검증은 `if self.currency != other.currency:` 로 시작하세요
- `__repr__`의 따옴표 처리에 주의하세요: 통화 코드는 문자열이므로 `'USD'` 처럼 따옴표가 필요해요

## 🎪 코드 테스트

다음 테스트 케이스를 실행해보세요:

```python
# 테스트 1: 문자열 표현
wallet = Money(1500, "USD")
print(str(wallet))    # 예상: 1,500.00 USD
print(repr(wallet))   # 예상: Money(1500, 'USD')

# 테스트 2: 덧셈
salary = Money(3000, "USD")
bonus = Money(500, "USD")
total = salary + bonus
print(total)  # 예상: 3,500.00 USD

# 테스트 3: 뺄셈
balance = Money(1000, "USD")
payment = Money(250, "USD")
print(balance - payment)  # 예상: 750.00 USD

# 테스트 4: 곱셈
hourly_wage = Money(25, "USD")
print(hourly_wage * 40)  # 예상: 1,000.00 USD

# 테스트 5: 다른 통화 → 에러
usd = Money(100, "USD")
krw = Money(100, "KRW")
try:
    usd + krw
    print("실패: 에러가 발생해야 함")
except ValueError as e:
    print(f"성공: 에러 발생 -> {e}")

# 테스트 6: 큰 숫자 포맷팅
big_money = Money(1234567.89, "USD")
print(big_money)  # 예상: 1,234,567.89 USD

# 테스트 7: 체이닝
chained = (Money(100, "USD") + Money(50, "USD")) * 2
print(chained)  # 예상: 300.00 USD
```

## 🤔 생각해보기

코딩을 시작하기 전에, 접근 방법을 스케치해보세요:
1. `__str__`과 `__repr__`은 누구를 위한 메서드인가요? 어떻게 다른가요?
2. `__add__`가 새 객체를 반환해야 하는 이유는 무엇일까요? 만약 `self.amount += other.amount` 처럼 자기 자신을 수정하면 어떤 문제가 생길까요?
3. 통화 검증을 `__init__`이 아니라 `__add__`/`__sub__`에서 하는 이유는?
4. `__mul__`은 왜 통화 검증이 필요 없을까요?

## 🎁 보너스 챌린지

기본 과제를 완성했다면, 한 단계 더 도전해보세요!

### 🥉 Easy: `__eq__` 추가
두 `Money` 객체가 같은지 비교할 수 있게 만드세요.
```python
Money(100, "USD") == Money(100, "USD")  # True
Money(100, "USD") == Money(100, "KRW")  # False
Money(100, "USD") == Money(200, "USD")  # False
```

### 🥈 Medium: 음수 금액 방지
`__init__`에서 음수 금액이 들어오면 `ValueError`를 발생시키세요. 그리고 `__sub__`에서 결과가 음수가 되는 경우도 막아야 합니다.
```python
Money(-100, "USD")  # ValueError!
Money(100, "USD") - Money(200, "USD")  # ValueError! (잔액 부족)
```

### 🥇 Hard: `__lt__`로 정렬 가능하게
`__lt__` (less than) 메서드를 추가해서 `Money` 객체 리스트를 `sorted()`로 정렬할 수 있게 만드세요. 단, 같은 통화끼리만 비교 가능해야 합니다.
```python
wallets = [Money(300, "USD"), Money(100, "USD"), Money(200, "USD")]
sorted_wallets = sorted(wallets)
# 예상: [Money(100, 'USD'), Money(200, 'USD'), Money(300, 'USD')]
```

막히면 스레드에 질문을 남겨주세요! 목표는 끝내는 것이 아니라 배우는 것입니다. 천천히 논리를 이해하면서 진행하세요.

행운을 빕니다! 🚀

---
---

# 🐍 Python Practice: Build Your Own Money Class!

Hey team! Today we're diving into one of the most fun parts of OOP — **dunder methods** — to build a class that actually feels professional.

## 🎯 Your Mission

You're a junior developer at a global FinTech startup. Your task: build a **`Money` class** for the company's payment system.

Up until now, the codebase has been handling amounts as plain numbers, and it's causing real problems:
- `1500 + 200` → Is this USD or KRW? Nobody knows! 😱
- `print(salary)` → Just prints a number, no currency shown
- Different currencies can be added together accidentally — no protection

With the power of dunder methods, we can make natural code like `wallet + bonus`, `print(salary)`, and `hourly_wage * 40` actually work the way you'd expect!

## 📋 The Rules

*What you're given:*
- An empty `Money` class skeleton
- A list of dunder methods to implement with their signatures

*What you need to do:*
1. `__init__(self, amount, currency)` — Initialize with amount and currency code
2. `__str__(self)` — User-facing string (e.g., `"1,500.00 USD"`)
3. `__repr__(self)` — Developer/debug string (e.g., `"Money(1500, 'USD')"`)
4. `__add__(self, other)` — Add two same-currency Money objects, return new `Money`
5. `__sub__(self, other)` — Subtract same-currency, return new `Money`
6. `__mul__(self, scalar)` — Multiply by a number (e.g., wage × hours)

*Constraints you must follow:*
- **No mixing currencies in add/subtract!** Raise `ValueError` if currencies differ
- Arithmetic operations (`+`, `-`, `*`) must **always return a new `Money` object** — never modify the original
- `__str__` must use thousand-separator commas and 2 decimal places (e.g., `"1,234.56 USD"`)
- `__repr__` should be in a form that could (theoretically) be re-evaluated to create the object

## 💡 Example Time

**Example 1: String Representations**
```python
wallet = Money(1500, "USD")
print(wallet)        # Output: 1,500.00 USD
print(repr(wallet))  # Output: Money(1500, 'USD')
```

**Example 2: Addition and Subtraction**
```python
salary = Money(3000, "USD")
bonus = Money(500, "USD")
total = salary + bonus
print(total)  # Output: 3,500.00 USD

balance = Money(1000, "USD")
payment = Money(250, "USD")
remaining = balance - payment
print(remaining)  # Output: 750.00 USD
```

**Example 3: Scalar Multiplication**
```python
hourly_wage = Money(25, "USD")
weekly_pay = hourly_wage * 40
print(weekly_pay)  # Output: 1,000.00 USD
```

**Example 4: Rejecting Different Currencies**
```python
usd = Money(100, "USD")
krw = Money(100, "KRW")
result = usd + krw  # Raises ValueError!
```

## 🎓 What You Should Know

Before you start coding, make sure you understand:
- How to write a class and `__init__`
- What `self` is
- What dunder (magic) methods are — special methods that Python calls automatically
- The difference between `__str__` and `__repr__`
- How to raise errors with `raise`
- f-string formatting (e.g., `f"{value:,.2f}"`)

## ✅ Your Task

Complete this class:
```python
class Money:
    def __init__(self, amount, currency):
        # Your code here
        pass

    def __str__(self):
        # Your code here
        pass

    def __repr__(self):
        # Your code here
        pass

    def __add__(self, other):
        # Your code here
        pass

    def __sub__(self, other):
        # Your code here
        pass

    def __mul__(self, scalar):
        # Your code here
        pass
```

**Tips to get you started:**
- Thousand-separator commas in `__str__` come from the f-string `:,` format specifier
- Arithmetic operations must **return a new `Money` object** — use `return Money(...)`
- Start currency validation with `if self.currency != other.currency:`
- Watch out for quotes in `__repr__`: currency is a string, so it needs quotes like `'USD'`

## 🎪 Test Your Code

Try running these test cases:

```python
# Test 1: String representations
wallet = Money(1500, "USD")
print(str(wallet))    # Expected: 1,500.00 USD
print(repr(wallet))   # Expected: Money(1500, 'USD')

# Test 2: Addition
salary = Money(3000, "USD")
bonus = Money(500, "USD")
total = salary + bonus
print(total)  # Expected: 3,500.00 USD

# Test 3: Subtraction
balance = Money(1000, "USD")
payment = Money(250, "USD")
print(balance - payment)  # Expected: 750.00 USD

# Test 4: Multiplication
hourly_wage = Money(25, "USD")
print(hourly_wage * 40)  # Expected: 1,000.00 USD

# Test 5: Different currencies → error
usd = Money(100, "USD")
krw = Money(100, "KRW")
try:
    usd + krw
    print("FAIL: should have raised an error")
except ValueError as e:
    print(f"PASS: raised error -> {e}")

# Test 6: Large number formatting
big_money = Money(1234567.89, "USD")
print(big_money)  # Expected: 1,234,567.89 USD

# Test 7: Chaining
chained = (Money(100, "USD") + Money(50, "USD")) * 2
print(chained)  # Expected: 300.00 USD
```

## 🤔 Think About It

Before you start coding, sketch out your approach:
1. Who is `__str__` for, and who is `__repr__` for? How are they different?
2. Why should `__add__` return a new object? What would go wrong if you did `self.amount += other.amount` instead?
3. Why validate currency in `__add__`/`__sub__` rather than `__init__`?
4. Why doesn't `__mul__` need currency validation?

## 🎁 Bonus Challenges

Once you've finished the core task, level up!

### 🥉 Easy: Add `__eq__`
Make two `Money` objects comparable for equality.
```python
Money(100, "USD") == Money(100, "USD")  # True
Money(100, "USD") == Money(100, "KRW")  # False
Money(100, "USD") == Money(200, "USD")  # False
```

### 🥈 Medium: Prevent Negative Amounts
Raise `ValueError` in `__init__` if a negative amount is given. Also prevent `__sub__` from producing a negative result.
```python
Money(-100, "USD")  # ValueError!
Money(100, "USD") - Money(200, "USD")  # ValueError! (insufficient funds)
```

### 🥇 Hard: Make Sortable with `__lt__`
Add `__lt__` (less than) so `Money` objects can be sorted with `sorted()`. Only same-currency comparison should be allowed.
```python
wallets = [Money(300, "USD"), Money(100, "USD"), Money(200, "USD")]
sorted_wallets = sorted(wallets)
# Expected: [Money(100, 'USD'), Money(200, 'USD'), Money(300, 'USD')]
```

Drop your questions in the thread if you get stuck! Remember, the goal is to learn, not just to finish. Take your time and understand the logic.

Good luck! 🚀
