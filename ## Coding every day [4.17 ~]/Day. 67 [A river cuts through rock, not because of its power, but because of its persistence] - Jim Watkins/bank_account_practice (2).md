# 🏦 Python 연습: FinTech 은행 계좌 시스템 구축하기!

안녕하세요, 미래의 개발자 여러분! 오늘은 우리가 배운 **캡슐화(Encapsulation)** 와 **상속(Inheritance)** 을 실제 금융 시스템에 적용해볼 시간입니다.

## 🎯 미션

여러분은 신생 핀테크(FinTech) 스타트업의 백엔드 개발자입니다. CEO가 방금 회의실에서 외쳤습니다:

> *"우리 앱의 은행 계좌 시스템이 너무 위험해요! 누구나 잔액을 직접 수정할 수 있어요! 그리고 일반 계좌, 적금 계좌, 입출금 계좌가 모두 똑같이 작동해요. 이거 다시 설계해주세요!"*

여러분의 임무는 **안전한** 은행 계좌 클래스를 설계하고, 그것을 확장하여 두 가지 특수 계좌 타입을 만드는 것입니다.

## 📋 두 단계 미션

이 과제는 **두 부분(Part)** 으로 나뉩니다. 순서대로 진행하세요!

### 🥚 Part 1: `BankAccount` 클래스 만들기 (캡슐화)

기본 은행 계좌 클래스를 만듭니다. **핵심 원칙**: 잔액(balance)은 절대 외부에서 직접 수정할 수 없어야 합니다!

**필수 요구사항:**

| 항목 | 설명 |
|------|------|
| `__init__(owner_name, initial_balance=0.0)` | 소유자 이름과 초기 잔액으로 계좌 생성 |
| `__balance` (private 속성) | 이중 언더스코어 사용 — 외부 직접 접근 불가! |
| `_owner_name` (protected 속성) | 단일 언더스코어 사용 |
| `_transaction_history` (protected 속성) | 거래 내역을 저장할 빈 리스트로 시작 |
| `balance` (`@property`) | 읽기 전용 — 잔액 조회만 가능, 수정 불가 |
| `owner_name` (`@property`) | 읽기 전용 — 소유자 이름 조회 |
| `deposit(amount)` | 입금 → 성공 시 `True`, 실패 시 `False` 반환 |
| `withdraw(amount)` | 출금 → 성공 시 `True`, 실패 시 `False` 반환 |
| `get_transaction_history()` | 거래 내역 리스트의 **복사본** 반환 |

**입금/출금 규칙:**
- 금액이 0 이하면 → 에러 메시지 출력 후 `False` 반환
- 출금 금액이 잔액보다 크면 → 에러 메시지 출력 후 `False` 반환
- 성공 시 → 거래 내역에 기록 추가 후 `True` 반환

> 💡 **왜 캡슐화인가?** 만약 `account.balance = 999999999` 같은 코드가 가능하다면 어떻게 될까요? 해커들의 천국이 되겠죠! 😱

### 🐣 Part 2: 특수 계좌 만들기 (상속 + 메서드 오버라이딩)

이제 `BankAccount`를 **상속**받아 두 가지 특수 계좌를 만듭니다. 각자 `withdraw()` 메서드를 **오버라이드(override)** 해야 합니다!

#### 🏦 `SavingsAccount` (적금 계좌)

- **최소 잔액 규칙**: 출금 후 잔액이 `$100` 미만이 되면 안 됨
- 생성자: `__init__(owner_name, initial_balance=0.0, interest_rate=0.02)`
- `_interest_rate` 속성 추가
- `withdraw()` 오버라이드: 최소 잔액 규칙 확인 후, `super().withdraw()` 호출

#### 💳 `CheckingAccount` (입출금 계좌)

- **마이너스 통장 허용**: 잔액이 `-$500`까지 내려가도 됨
- 마이너스가 되면 **$35 수수료** 부과
- `withdraw()` 오버라이드: 마이너스 통장 한도 확인 후 처리

> 🌟 **새로운 개념: 메서드 오버라이딩(Method Overriding)**
> 자식 클래스에서 부모 클래스와 **같은 이름**의 메서드를 정의하면, 그 자식 클래스에서는 새로운 버전이 사용됩니다. 이것이 객체지향의 강력한 기능 중 하나인 **다형성(Polymorphism)** 입니다!

## 💡 예제 살펴보기

### 예제 1: 기본 `BankAccount`
```python
acc = BankAccount("Alice", 500)
print(acc.balance)              # 500
acc.deposit(200)                # True
print(acc.balance)              # 700
acc.withdraw(300)               # True
print(acc.balance)              # 400
acc.withdraw(1000)              # False (잔액 부족!)
acc.balance = 999999            # AttributeError! (읽기 전용)
```

### 예제 2: `SavingsAccount`의 최소 잔액
```python
sav = SavingsAccount("Bob", 1000, 0.03)
sav.withdraw(900)               # True → 잔액 100 (정확히 최소값)
sav.withdraw(50)                # False! → 50은 최소 잔액 미만
```

### 예제 3: `CheckingAccount`의 마이너스 통장
```python
chk = CheckingAccount("Carol", 200)
chk.withdraw(300)               # True → 잔액 -100, 수수료 $35 부과
print(chk.balance)              # -135
chk.withdraw(1000)              # False! → 한도 초과
```

## 🎓 알아야 할 것

코딩을 시작하기 전에 다음을 이해하고 있는지 확인하세요:

- `class`, `__init__`, `self`의 의미
- Private (`__name`) vs Protected (`_name`) 속성
- `@property` 데코레이터로 읽기 전용 속성 만들기
- `class Child(Parent):` 상속 문법
- `super().__init__(...)` 와 `super().method_name(...)` 사용법
- 자식 클래스에서 같은 이름의 메서드를 다시 정의하는 것이 **오버라이딩**

## ✅ 과제

다음 시그니처로 세 개의 클래스를 작성하세요:

```python
class BankAccount:
    def __init__(self, owner_name: str, initial_balance: float = 0.0):
        # 여기에 코드 작성
        pass

    @property
    def balance(self) -> float:
        pass

    def deposit(self, amount: float) -> bool:
        pass

    def withdraw(self, amount: float) -> bool:
        pass

    # ... 기타 메서드들

class SavingsAccount(BankAccount):
    MINIMUM_BALANCE = 100.0
    # 오버라이드할 메서드들

class CheckingAccount(BankAccount):
    OVERDRAFT_LIMIT = 500.0
    OVERDRAFT_FEE = 35.0
    # 오버라이드할 메서드들
```

**시작하는 데 도움이 될 팁:**

- 부모 클래스에서 `_apply_balance_change(change)` 같은 protected 헬퍼 메서드를 만들면 자식 클래스가 잔액을 수정할 때 깔끔합니다
- `withdraw()` 를 오버라이드할 때, 검증 후 가능하면 `super().withdraw(amount)` 를 호출하는 패턴을 활용하세요
- 클래스 상수 (`MINIMUM_BALANCE = 100.0`) 는 대문자로 표기합니다

## 🎪 코드 테스트

다음 테스트 케이스를 실행해보세요:

```python
# Part 1 테스트: 기본 BankAccount
acc = BankAccount("Alice", 500)
assert acc.balance == 500
assert acc.owner_name == "Alice"
assert acc.deposit(200) == True
assert acc.balance == 700
assert acc.deposit(-50) == False        # 음수 입금 거부
assert acc.withdraw(300) == True
assert acc.balance == 400
assert acc.withdraw(1000) == False      # 잔액 부족

# 캡슐화 확인: balance는 읽기 전용!
try:
    acc.balance = 999999
    print("❌ FAIL: balance가 수정 가능합니다!")
except AttributeError:
    print("✓ balance는 읽기 전용입니다!")

# Part 2 테스트: SavingsAccount
sav = SavingsAccount("Bob", 1000, 0.03)
assert sav.withdraw(900) == True        # 잔액 100 (최소값)
assert sav.balance == 100
assert sav.withdraw(50) == False        # 최소 잔액 미만
assert sav.balance == 100

# Part 2 테스트: CheckingAccount
chk = CheckingAccount("Carol", 200)
assert chk.withdraw(300) == True        # 오버드래프트 발생
assert chk.balance == -135              # -100 - $35 수수료
chk2 = CheckingAccount("Dave", 100)
assert chk2.withdraw(700) == False      # 한도 초과
```

## 🤔 생각해보기

코딩을 시작하기 전에 답변해보세요:

1. 왜 `balance`를 `__balance` (이중 언더스코어) 로 만들었을까요? 단일 언더스코어 `_balance`와 어떻게 다를까요?
2. `@property` 없이 `self.balance` 를 그냥 public 속성으로 만들면 어떤 문제가 생길까요?
3. `withdraw()` 를 오버라이드할 때, 왜 자식 클래스에서 `super().withdraw()` 를 호출하는 것이 좋을까요?
4. 같은 `withdraw(450)` 호출이 계좌 타입에 따라 다르게 동작하는 것 — 이것이 왜 강력한 설계 패턴일까요?

## 🎁 보너스 챌린지

핵심 과제를 끝냈다면, 다음 단계로 도전해보세요!

### 🥉 Easy: 거래 수수료 (Transaction Fee)

`BankAccount`에 `_transaction_fee = 0.0` 속성을 추가하고, `withdraw()` 시에 수수료를 함께 차감하세요.

```python
acc = BankAccount("Alice", 500)
acc._transaction_fee = 2.0
acc.withdraw(100)                  # 잔액: 500 - 100 - 2 = 398
```

### 🥈 Medium: 계좌 간 이체 (`transfer`)

`BankAccount`에 `transfer(other_account, amount)` 메서드를 추가하세요.
- 자기 자신에게 이체 시도 → `False` 반환
- 출금 실패 시 → 입금하지 않고 `False` 반환
- 성공 시 → 양쪽 계좌의 거래 내역에 기록

```python
alice = BankAccount("Alice", 500)
bob = BankAccount("Bob", 100)
alice.transfer(bob, 200)           # True
# alice.balance == 300, bob.balance == 300
```

### 🥇 Hard: 이자 적용 (`apply_interest`)

`SavingsAccount`에만 `apply_interest()` 메서드를 추가하세요. 현재 잔액에 `_interest_rate`를 곱한 만큼 이자를 더합니다.

또한, `apply_interest()` 가 **`SavingsAccount` 에는 있지만 `BankAccount` 와 `CheckingAccount` 에는 없는** 메서드라는 점에 주목하세요. 이것이 왜 좋은 설계인지 생각해보세요!

```python
sav = SavingsAccount("Bob", 1000, 0.05)
sav.apply_interest()               # 잔액: 1000 + (1000 * 0.05) = 1050
```

> 💡 **Preview (다음 수업 미리보기):** Hard 단계를 완료했다면, `isinstance()` 함수를 한번 검색해보세요. 같은 `withdraw()` 명령이라도 객체 타입에 따라 다른 동작을 하는 — 이것이 **다형성(Polymorphism)** 입니다. 다음 시간에 본격적으로 다룰 예정입니다!

막히면 스레드에 질문을 남겨주세요! 목표는 끝내는 것이 아니라 **객체지향의 진정한 힘을 이해하는 것**입니다. 천천히, 한 클래스씩 완성하세요.

행운을 빕니다! 🚀

---
---

# 🏦 Python Practice: Build a FinTech Bank Account System!

Hey future developers! Today we'll apply what we learned about **encapsulation** and **inheritance** to a real-world financial system.

## 🎯 Your Mission

You're a backend developer at a hot new FinTech startup. The CEO just stormed into the meeting room and shouted:

> *"Our app's bank account system is way too dangerous! Anyone can modify the balance directly! And our regular accounts, savings accounts, and checking accounts all behave identically! Redesign it — NOW!"*

Your job is to design a **secure** bank account class and extend it to create two specialized account types.

## 📋 Two-Part Mission

This assignment has **two parts**. Complete them in order!

### 🥚 Part 1: Build the `BankAccount` Class (Encapsulation)

Create a base bank account class. **The core principle**: balance must NEVER be modifiable from outside!

**Required components:**

| Item | Description |
|------|-------------|
| `__init__(owner_name, initial_balance=0.0)` | Create account with owner name and initial balance |
| `__balance` (private attribute) | Use double underscore — no external direct access! |
| `_owner_name` (protected attribute) | Single underscore convention |
| `_transaction_history` (protected attribute) | Start as empty list to store transactions |
| `balance` (`@property`) | Read-only — query only, no setter |
| `owner_name` (`@property`) | Read-only — query owner name |
| `deposit(amount)` | Returns `True` on success, `False` on failure |
| `withdraw(amount)` | Returns `True` on success, `False` on failure |
| `get_transaction_history()` | Returns a **copy** of the transaction list |

**Deposit/Withdraw rules:**
- If amount ≤ 0 → print error message, return `False`
- If withdrawal amount > balance → print error message, return `False`
- On success → record in transaction history, return `True`

> 💡 **Why encapsulation?** What if code like `account.balance = 999999999` were allowed? It would be a hacker's paradise! 😱

### 🐣 Part 2: Specialized Accounts (Inheritance + Method Overriding)

Now **inherit** from `BankAccount` to create two specialized account types. Each must **override** the `withdraw()` method!

#### 🏦 `SavingsAccount`

- **Minimum balance rule**: Balance cannot drop below `$100` after withdrawal
- Constructor: `__init__(owner_name, initial_balance=0.0, interest_rate=0.02)`
- Adds `_interest_rate` attribute
- Override `withdraw()`: validate minimum balance, then call `super().withdraw()`

#### 💳 `CheckingAccount`

- **Overdraft allowed**: Balance can go as low as `-$500`
- When going negative: charge a **$35 fee**
- Override `withdraw()`: check overdraft limit and apply fee logic

> 🌟 **New Concept: Method Overriding**
> When a child class defines a method with the **same name** as one in the parent class, the new version is used for that child class. This is one of the most powerful OOP features — called **polymorphism**!

## 💡 Example Time

### Example 1: Basic `BankAccount`
```python
acc = BankAccount("Alice", 500)
print(acc.balance)              # 500
acc.deposit(200)                # True
print(acc.balance)              # 700
acc.withdraw(300)               # True
print(acc.balance)              # 400
acc.withdraw(1000)              # False (insufficient funds!)
acc.balance = 999999            # AttributeError! (read-only)
```

### Example 2: `SavingsAccount` Minimum Balance
```python
sav = SavingsAccount("Bob", 1000, 0.03)
sav.withdraw(900)               # True → balance 100 (exactly minimum)
sav.withdraw(50)                # False! → would drop below minimum
```

### Example 3: `CheckingAccount` Overdraft
```python
chk = CheckingAccount("Carol", 200)
chk.withdraw(300)               # True → balance -100, plus $35 fee
print(chk.balance)              # -135
chk.withdraw(1000)              # False! → exceeds overdraft limit
```

## 🎓 What You Should Know

Before you start coding, make sure you understand:

- `class`, `__init__`, and `self`
- Private (`__name`) vs Protected (`_name`) attributes
- `@property` decorator for read-only attributes
- `class Child(Parent):` inheritance syntax
- `super().__init__(...)` and `super().method_name(...)`
- Redefining a same-named method in a child class is **overriding**

## ✅ Your Task

Write three classes with these signatures:

```python
class BankAccount:
    def __init__(self, owner_name: str, initial_balance: float = 0.0):
        # Your code here
        pass

    @property
    def balance(self) -> float:
        pass

    def deposit(self, amount: float) -> bool:
        pass

    def withdraw(self, amount: float) -> bool:
        pass

    # ... other methods

class SavingsAccount(BankAccount):
    MINIMUM_BALANCE = 100.0
    # Methods to override

class CheckingAccount(BankAccount):
    OVERDRAFT_LIMIT = 500.0
    OVERDRAFT_FEE = 35.0
    # Methods to override
```

**Tips to get you started:**

- A protected helper method like `_apply_balance_change(change)` in the parent class keeps child classes clean when modifying balance
- When overriding `withdraw()`, validate first, then call `super().withdraw(amount)` when possible — DRY principle!
- Class constants like `MINIMUM_BALANCE = 100.0` are written in uppercase

## 🎪 Test Your Code

Try running these test cases:

```python
# Part 1 tests: Basic BankAccount
acc = BankAccount("Alice", 500)
assert acc.balance == 500
assert acc.owner_name == "Alice"
assert acc.deposit(200) == True
assert acc.balance == 700
assert acc.deposit(-50) == False        # negative deposit rejected
assert acc.withdraw(300) == True
assert acc.balance == 400
assert acc.withdraw(1000) == False      # insufficient funds

# Encapsulation check: balance is read-only!
try:
    acc.balance = 999999
    print("❌ FAIL: balance is mutable!")
except AttributeError:
    print("✓ balance is read-only!")

# Part 2 tests: SavingsAccount
sav = SavingsAccount("Bob", 1000, 0.03)
assert sav.withdraw(900) == True        # balance 100 (minimum)
assert sav.balance == 100
assert sav.withdraw(50) == False        # below minimum
assert sav.balance == 100

# Part 2 tests: CheckingAccount
chk = CheckingAccount("Carol", 200)
assert chk.withdraw(300) == True        # overdraft triggered
assert chk.balance == -135              # -100 - $35 fee
chk2 = CheckingAccount("Dave", 100)
assert chk2.withdraw(700) == False      # exceeds limit
```

## 🤔 Think About It

Before you start coding, answer these:

1. Why did we make `balance` a `__balance` (double underscore)? How is that different from single underscore `_balance`?
2. Without `@property`, if `self.balance` were just a public attribute, what could go wrong?
3. When overriding `withdraw()`, why is it good practice to call `super().withdraw()` from the child class?
4. The same `withdraw(450)` call behaves differently based on account type — why is this a powerful design pattern?

## 🎁 Bonus Challenges

Finished the core task? Level up with these!

### 🥉 Easy: Transaction Fee

Add a `_transaction_fee = 0.0` attribute to `BankAccount` and deduct it together with `withdraw()`.

```python
acc = BankAccount("Alice", 500)
acc._transaction_fee = 2.0
acc.withdraw(100)                  # balance: 500 - 100 - 2 = 398
```

### 🥈 Medium: Transfer Between Accounts

Add a `transfer(other_account, amount)` method to `BankAccount`.
- Transfer to self → return `False`
- If withdrawal fails → don't deposit, return `False`
- On success → record in both accounts' transaction histories

```python
alice = BankAccount("Alice", 500)
bob = BankAccount("Bob", 100)
alice.transfer(bob, 200)           # True
# alice.balance == 300, bob.balance == 300
```

### 🥇 Hard: Apply Interest

Add an `apply_interest()` method **only to `SavingsAccount`**. It adds interest based on current balance × `_interest_rate`.

Notice that `apply_interest()` exists **only on `SavingsAccount`**, not on `BankAccount` or `CheckingAccount`. Think about why this is good design!

```python
sav = SavingsAccount("Bob", 1000, 0.05)
sav.apply_interest()               # balance: 1000 + (1000 * 0.05) = 1050
```

> 💡 **Preview (next class teaser):** Once you finish Hard, try searching for the `isinstance()` function. The fact that `withdraw()` behaves differently based on object type is called **polymorphism** — we'll dive into it properly next class!

Drop your questions in the thread if you get stuck! Remember, the goal isn't just to finish — it's to **understand the real power of OOP**. Take your time and build it class by class.

Good luck! 🚀
