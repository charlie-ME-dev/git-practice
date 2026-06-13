# 🐍 Python 연습 Day 4: 안전한 은행 계좌 만들기!

> "좋은 클래스는 사용자가 잘못 사용할 수 없도록 설계되어 있다."
> — 캡슐화의 핵심 아이디어

여러분, 안녕하세요! 오늘은 **캡슐화(encapsulation)** 라는 객체지향의 핵심 개념을 배워봅시다.

## 🏦 시나리오

여러분은 **MintBank**라는 새로운 핀테크 스타트업의 백엔드 개발자로 입사했습니다. 첫 번째 임무는 고객의 은행 계좌를 표현하는 `BankAccount` 클래스를 설계하는 것입니다.

**왜 중요한가요?** 만약 계좌 잔액(`balance`)을 누구나 마음대로 바꿀 수 있다면 어떻게 될까요?

```python
# 끔찍한 시나리오 😱
account.balance = -999999  # 음수 잔액?!
account.balance = "공짜 돈"  # 문자열을 잔액으로?!
```

이런 일이 일어나지 않도록, 우리는 **데이터를 보호**해야 합니다. 이것이 바로 **캡슐화**입니다.

## 🎯 미션

`BankAccount` 클래스를 만들어서 다음 두 가지를 동시에 달성하세요:

1. **데이터 보호**: 잔액은 외부에서 직접 수정할 수 없어야 함
2. **안전한 접근**: 입금/출금은 반드시 검증을 거쳐야 함

## 📋 규칙

*만들어야 할 것:*
- `BankAccount` 클래스
- 속성(attributes): 소유자 이름, 잔액, 거래 횟수
- 메서드(methods): 조회용 getter들, 그리고 `deposit()` / `withdraw()`

*캡슐화 규칙 (오늘의 핵심!):*
- 속성 이름은 **밑줄(`_`)로 시작**해야 합니다 (예: `self._balance`)
  - 이것은 "외부에서 직접 건드리지 마세요"라는 **약속**입니다
- 외부에서 잔액을 보려면 **getter 메서드**를 통해서만 가능해야 합니다
- 외부에서 잔액을 바꾸려면 **deposit/withdraw 메서드**를 통해서만 가능해야 합니다

*반드시 따라야 할 제약사항:*
- ❌ 초기 잔액이 **음수면 거부** (`ValueError` 발생)
- ❌ **음수 또는 0인 금액**은 입금/출금 불가 (`False` 반환)
- ❌ **잔액보다 큰 금액**은 출금 불가 (`False` 반환)
- ✅ 성공한 거래만 거래 횟수에 카운트

## 💡 예제

**예제 1: 정상적인 사용**
```python
account = BankAccount("Alice", 1000.0)
account.deposit(500.0)         # True 반환, 잔액 1500
account.withdraw(200.0)        # True 반환, 잔액 1300
print(account.get_balance())   # 1300.0
print(account.get_transaction_count())  # 2
```

**예제 2: 잘못된 사용 차단**
```python
account = BankAccount("Bob", 100.0)
account.deposit(-50)           # False 반환 (음수 입금 거부)
account.withdraw(99999)        # False 반환 (잔액 부족)
account.withdraw(0)            # False 반환 (0원 출금 거부)
print(account.get_balance())   # 100.0 (변화 없음!)
print(account.get_transaction_count())  # 0 (실패는 카운트 안 됨)
```

**예제 3: 초기 잔액 검증**
```python
account = BankAccount("Eve", -100)  # ValueError 발생!
```

## 🎓 알아야 할 것

오늘 사용할 개념들 (모두 이미 배운 것들입니다):
- 클래스 정의 (`class`, `__init__`, `self`)
- 인스턴스 속성 (`self.something`)
- 메서드 정의
- 조건문 (`if`, `else`)
- 함수의 반환값 (`return True` / `return False`)
- 예외 발생 (`raise ValueError(...)`)

**오늘의 새로운 관례 하나만:**
```python
self._balance = 0  # 밑줄로 시작하면 "private"이라는 약속
```

Python에는 진짜 private 키워드가 없습니다. 대신 **개발자들 간의 약속**으로 `_`를 붙입니다.
> "We're all consenting adults here." — Python 커뮤니티의 유명한 문구

## ✅ 과제

다음 시그니처로 클래스를 작성하세요:

```python
class BankAccount:
    def __init__(self, owner_name: str, initial_balance: float = 0.0):
        # 여기에 코드 작성
        pass

    def get_owner_name(self) -> str:
        pass

    def get_balance(self) -> float:
        pass

    def get_transaction_count(self) -> int:
        pass

    def deposit(self, amount: float) -> bool:
        # 성공하면 True, 실패하면 False 반환
        pass

    def withdraw(self, amount: float) -> bool:
        # 성공하면 True, 실패하면 False 반환
        pass
```

**시작 팁:**
- `__init__`에서 초기 잔액이 음수인지 먼저 확인하세요
- `deposit`과 `withdraw`는 검증 → 변경 → `True` 반환 순서로 작성
- 실패 케이스는 일찍 `return False` 하면 코드가 깔끔해집니다 (early return 패턴)
- 거래 횟수는 **성공했을 때만** 증가시켜야 합니다

## 🎪 코드 테스트

```python
# 테스트 1: 정상 동작
acc = BankAccount("Alice", 1000.0)
print(acc.get_balance())              # 1000.0
print(acc.deposit(500.0))             # True
print(acc.withdraw(200.0))            # True
print(acc.get_balance())              # 1300.0
print(acc.get_transaction_count())    # 2

# 테스트 2: 잘못된 입력 거부
acc2 = BankAccount("Bob", 100.0)
print(acc2.deposit(-50))              # False
print(acc2.withdraw(99999))           # False
print(acc2.withdraw(0))               # False
print(acc2.get_balance())             # 100.0
print(acc2.get_transaction_count())   # 0

# 테스트 3: 음수 초기 잔액
try:
    BankAccount("Eve", -100)
    print("실패: ValueError가 발생해야 함")
except ValueError:
    print("성공: ValueError 발생함")
```

## 🤔 생각해보기

코딩하면서 다음 질문에 답해보세요:

1. 왜 `self.balance` 대신 `self._balance`라고 쓸까요? 둘은 기술적으로 어떻게 다른가요?
2. 만약 getter 없이 `account._balance`로 직접 접근하면 어떤 일이 벌어질 수 있을까요?
3. `deposit`이 `True`/`False`를 반환하는 것과 그냥 아무것도 반환하지 않는 것 중 어떤 것이 더 좋은 설계일까요? 왜죠?
4. 우리 코드에서 "검증(validation)"은 어디에 들어가나요? 만약 검증을 빼면 어떤 버그가 생길 수 있나요?

## 🌟 보너스 챌린지

### 🥉 Easy: 이체(transfer) 기능
`transfer(other_account, amount)` 메서드를 추가하세요. 자신의 계좌에서 `amount`만큼 빼서 `other_account`에 넣습니다. 성공하면 `True`, 실패하면 `False`.

### 🥈 Medium: 거래 내역 기록
거래 내역을 저장하는 기능을 추가하세요. 예를 들어 `("deposit", 500.0)` 같은 튜플을 리스트에 저장하고, `get_history()` 메서드로 조회할 수 있게 하세요.

💡 힌트: 외부에서 내역을 수정하지 못하도록 **복사본**을 반환하는 것이 안전합니다.

### 🥇 Hard: 일일 출금 한도
하루에 출금할 수 있는 금액에 한도를 두세요 (예: 1,000,000원). 이를 위해 다음을 생각해보세요:
- 한도는 어떻게 저장할까요?
- "오늘 출금한 총액"은 어떻게 추적할까요?
- 다음 날이 되면 어떻게 리셋할까요?

(다음 주에 배울 `@property`와 데코레이터를 미리 맛볼 수 있는 문제입니다!)

---

질문이나 막히는 부분이 있다면 Slack 스레드에 남겨주세요! 오늘의 목표는 **"왜 캡슐화가 필요한가"** 를 몸으로 느끼는 것입니다. 끝내는 것보다 이해하는 것이 더 중요해요.

화이팅! 🚀

---
---

# 🐍 Python Practice Day 4: Building a Safe Bank Account!

> "A good class is designed so that users can't use it incorrectly."
> — The core idea of encapsulation

Hello team! Today we're learning **encapsulation**, one of the most important ideas in object-oriented programming.

## 🏦 The Scenario

You've just been hired as a backend developer at **MintBank**, a new fintech startup. Your first assignment is to design a `BankAccount` class to represent customer accounts.

**Why does this matter?** What would happen if anyone could change the account balance directly?

```python
# Horror scenario 😱
account.balance = -999999  # Negative balance?!
account.balance = "free money"  # A string as balance?!
```

To prevent this, we need to **protect our data**. That's exactly what **encapsulation** is.

## 🎯 Your Mission

Build a `BankAccount` class that achieves two things at once:

1. **Data protection**: The balance can't be modified directly from outside
2. **Safe access**: Deposits and withdrawals must go through validation

## 📋 The Rules

*What to build:*
- A `BankAccount` class
- Attributes: owner name, balance, transaction count
- Methods: getters for reading, plus `deposit()` / `withdraw()`

*Encapsulation rules (today's main focus!):*
- Attribute names must **start with an underscore (`_`)** (e.g., `self._balance`)
  - This is a **convention** meaning "please don't touch this directly from outside"
- To read the balance from outside, you must use a **getter method**
- To change the balance from outside, you must use **deposit/withdraw methods**

*Constraints you must follow:*
- ❌ If initial balance is **negative**, raise `ValueError`
- ❌ **Zero or negative amounts** can't be deposited/withdrawn (return `False`)
- ❌ Can't withdraw **more than the balance** (return `False`)
- ✅ Only successful transactions count toward the transaction count

## 💡 Examples

**Example 1: Normal usage**
```python
account = BankAccount("Alice", 1000.0)
account.deposit(500.0)         # returns True, balance becomes 1500
account.withdraw(200.0)        # returns True, balance becomes 1300
print(account.get_balance())   # 1300.0
print(account.get_transaction_count())  # 2
```

**Example 2: Blocking invalid usage**
```python
account = BankAccount("Bob", 100.0)
account.deposit(-50)           # returns False (negative deposit rejected)
account.withdraw(99999)        # returns False (insufficient funds)
account.withdraw(0)            # returns False (zero withdrawal rejected)
print(account.get_balance())   # 100.0 (unchanged!)
print(account.get_transaction_count())  # 0 (failures don't count)
```

**Example 3: Initial balance validation**
```python
account = BankAccount("Eve", -100)  # Raises ValueError!
```

## 🎓 What You Should Know

Concepts you'll use today (all things you've already learned):
- Class definition (`class`, `__init__`, `self`)
- Instance attributes (`self.something`)
- Method definitions
- Conditionals (`if`, `else`)
- Return values (`return True` / `return False`)
- Raising exceptions (`raise ValueError(...)`)

**Just one new convention today:**
```python
self._balance = 0  # Starting with `_` means "private by convention"
```

Python doesn't have a real `private` keyword. Instead, developers **agree** to use `_` as a signal.
> "We're all consenting adults here." — A famous saying in the Python community

## ✅ Your Task

Write a class with this signature:

```python
class BankAccount:
    def __init__(self, owner_name: str, initial_balance: float = 0.0):
        # Your code here
        pass

    def get_owner_name(self) -> str:
        pass

    def get_balance(self) -> float:
        pass

    def get_transaction_count(self) -> int:
        pass

    def deposit(self, amount: float) -> bool:
        # Return True on success, False on failure
        pass

    def withdraw(self, amount: float) -> bool:
        # Return True on success, False on failure
        pass
```

**Tips to get started:**
- In `__init__`, check for negative initial balance first
- Write `deposit` and `withdraw` as: validate → modify → return `True`
- Use early return for failure cases — keeps the code clean
- Increment transaction count **only on success**

## 🎪 Test Your Code

```python
# Test 1: Normal operation
acc = BankAccount("Alice", 1000.0)
print(acc.get_balance())              # 1000.0
print(acc.deposit(500.0))             # True
print(acc.withdraw(200.0))            # True
print(acc.get_balance())              # 1300.0
print(acc.get_transaction_count())    # 2

# Test 2: Invalid input rejection
acc2 = BankAccount("Bob", 100.0)
print(acc2.deposit(-50))              # False
print(acc2.withdraw(99999))           # False
print(acc2.withdraw(0))               # False
print(acc2.get_balance())             # 100.0
print(acc2.get_transaction_count())   # 0

# Test 3: Negative initial balance
try:
    BankAccount("Eve", -100)
    print("FAIL: should have raised ValueError")
except ValueError:
    print("PASS: ValueError raised")
```

## 🤔 Think About It

While coding, try to answer these:

1. Why write `self._balance` instead of `self.balance`? What's the technical difference?
2. What could go wrong if someone bypasses the getter and writes `account._balance` directly?
3. Is it better design for `deposit` to return `True`/`False`, or to return nothing? Why?
4. Where does "validation" live in our code? What bugs could happen if we remove it?

## 🌟 Bonus Challenges

### 🥉 Easy: Transfer feature
Add a `transfer(other_account, amount)` method. It withdraws `amount` from your account and deposits it into `other_account`. Return `True` on success, `False` on failure.

### 🥈 Medium: Transaction history
Add a feature that records transaction history. Store tuples like `("deposit", 500.0)` in a list, and provide a `get_history()` method to view them.

💡 Hint: To prevent outsiders from modifying the history, returning a **copy** is safer.

### 🥇 Hard: Daily withdrawal limit
Add a daily withdrawal limit (e.g., 1,000,000 won per day). Think about:
- How will you store the limit?
- How will you track "total withdrawn today"?
- How will it reset on a new day?

(This previews `@property` and decorators, which you'll learn next week!)

---

Drop questions in the Slack thread if you get stuck! Today's goal is to **feel in your bones why encapsulation matters**. Understanding beats finishing.

Good luck! 🚀
