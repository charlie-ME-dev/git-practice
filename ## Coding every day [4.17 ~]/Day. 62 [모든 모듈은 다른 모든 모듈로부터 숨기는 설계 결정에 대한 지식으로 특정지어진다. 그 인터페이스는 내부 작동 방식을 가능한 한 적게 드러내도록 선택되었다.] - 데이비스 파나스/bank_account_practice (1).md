# 🏦 Python 연습: 은행 계좌의 비밀을 지켜라!

여러분, 안녕하세요! 오늘은 진짜 핀테크 회사의 개발자처럼 코딩해볼 시간입니다. 💳

## 🌟 배경 스토리

여러분이 새로 입사한 핀테크 스타트업 "**SafeBank**"에서 디지털 지갑 시스템을 개발하게 되었어요!

CTO가 여러분에게 이렇게 말합니다:

> *"잔액(balance)을 외부에서 마음대로 바꾸면 큰일이에요. 누군가 `account.balance = 1000000000`이라고 적으면 그냥 돈이 생기는 거잖아요? 절대 안 됩니다!"*

그래서 오늘 배울 것: **이름 맹글링(Name Mangling)** — Python에서 가장 강력한 캡슐화 도구입니다. 🔒

## 🎯 미션

`BankAccount` 클래스를 만들어서 다음을 보장해야 합니다:
- 잔액(`__balance`)은 **외부에서 직접 변경할 수 없어야** 함
- 소유자 이름(`__owner_name`)은 **외부에서 직접 읽거나 변경할 수 없어야** 함
- 입금/출금은 반드시 **메서드를 통해서만** 가능
- 모든 거래는 **유효성 검사**를 통과해야 함

## 🎓 핵심 개념: Name Mangling (이름 맹글링)

### 복습: 이미 배운 것
지난 시간에 우리는 `_attr` (single underscore)를 배웠어요:
```python
self._balance = 1000  # "건드리지 말아주세요" (약속일 뿐!)
```

이건 그냥 **"신사 협정"**이에요. 외부에서 `account._balance = 99999` 하면 그대로 바뀝니다. 😱

### 오늘의 신무기: `__attr` (double underscore)
```python
self.__balance = 1000  # "진짜로 못 건드림!"
```

`__`로 시작하면 Python이 자동으로 이름을 **변경(mangling)**합니다:
- 클래스 내부에서: `self.__balance`
- 실제 저장된 이름: `_BankAccount__balance`

외부에서 `account.__balance = 99999`라고 쓰면? **새로운 속성이 만들어질 뿐, 진짜 잔액은 안 바뀝니다!** 🎉

### 비교표

| 방식 | 작성 | 외부 접근 | 보안 수준 |
|------|------|-----------|-----------|
| `balance` | 공개 | `acc.balance` 가능 | ⭐ 없음 |
| `_balance` | 약한 보호 | `acc._balance` 가능 | ⭐⭐ 관습 |
| `__balance` | 강한 보호 | `acc.__balance` 불가 | ⭐⭐⭐ 강제 |

## 📋 규칙

*주어지는 것:*
- 소유자 이름 (문자열)
- 초기 입금액 (선택사항, 기본값 0)

*BankAccount 클래스 요구사항:*

**비공개 속성 (반드시 `__`로 시작):**
- `__owner_name`: 소유자 이름
- `__balance`: 현재 잔액 (절대 음수 불가)
- `__is_active`: 계좌 활성 상태 (True/False)

**공개 메서드:**
| 메서드 | 동작 | 반환값 |
|--------|------|--------|
| `get_owner_name()` | 소유자 이름 조회 | 문자열 |
| `get_balance()` | 현재 잔액 조회 | 정수 |
| `is_active()` | 활성 상태 확인 | True/False |
| `deposit(amount)` | 입금 (양수만, 활성 계좌만) | True/False |
| `withdraw(amount)` | 출금 (양수, 잔액 충분, 활성 계좌만) | True/False |
| `close_account()` | 계좌 폐쇄 | None |

## 💡 예제

```python
acc = BankAccount("김민준", 1000)
print(acc.get_owner_name())   # 김민준
print(acc.get_balance())      # 1000

acc.deposit(500)
print(acc.get_balance())      # 1500

acc.withdraw(200)
print(acc.get_balance())      # 1300

acc.withdraw(99999)           # 잔액 부족!
print(acc.get_balance())      # 1300 (변화 없음)

acc.deposit(-100)             # 음수 입금 거부!
print(acc.get_balance())      # 1300

# 🔒 직접 접근 차단 확인
try:
    print(acc.__balance)      # AttributeError 발생!
except AttributeError:
    print("못 봐요! 🔒")

acc.__balance = 99999999      # 안 바뀜!
print(acc.get_balance())      # 여전히 1300 💪
```

## ✅ 과제

다음 시그니처로 클래스를 작성하세요:

```python
class BankAccount:
    def __init__(self, owner_name: str, initial_deposit: int = 0):
        # 여기에 코드 작성
        pass
    
    def get_owner_name(self) -> str:
        pass
    
    def get_balance(self) -> int:
        pass
    
    def is_active(self) -> bool:
        pass
    
    def deposit(self, amount: int) -> bool:
        pass
    
    def withdraw(self, amount: int) -> bool:
        pass
    
    def close_account(self) -> None:
        pass
```

## 🎪 코드 테스트

```python
# 테스트 1: 기본 생성
acc = BankAccount("김민준", 1000)
assert acc.get_balance() == 1000
assert acc.is_active() == True

# 테스트 2: 입금
acc.deposit(500)
assert acc.get_balance() == 1500

# 테스트 3: 출금
acc.withdraw(300)
assert acc.get_balance() == 1200

# 테스트 4: 잘못된 거래 거부
assert acc.deposit(-100) == False    # 음수 거부
assert acc.withdraw(99999) == False  # 잔액 부족
assert acc.get_balance() == 1200     # 변화 없음

# 테스트 5: 계좌 폐쇄
acc.close_account()
assert acc.is_active() == False
assert acc.deposit(100) == False     # 폐쇄된 계좌

# 테스트 6: 🔒 캡슐화 확인 (가장 중요!)
acc2 = BankAccount("이서연", 5000)
try:
    secret = acc2.__balance
    print("❌ 보안 실패!")
except AttributeError:
    print("✅ 잔액 비공개 확인!")

print("🎉 모든 테스트 통과!")
```

## 🎁 보너스 챌린지

### 🥉 Easy: PIN 번호 추가하기

계좌에 4자리 숫자 PIN을 추가하세요!
- 생성 시 PIN 설정 (4자리 숫자 문자열만 허용)
- `verify_pin(pin_attempt)` 메서드: PIN이 맞으면 True
- `change_pin(old_pin, new_pin)` 메서드: 기존 PIN 확인 후 변경
- PIN은 절대 외부에서 읽을 수 없어야 함! (`__pin` 사용)

### 🥈 Medium: 거래 내역 (Transaction History)

모든 거래를 기록하는 비공개 로그를 추가하세요!
- `__history` 리스트에 모든 입금/출금 기록
- 형식: `(거래종류, 금액, 거래후잔액)` 튜플로 저장
- `get_history()` 메서드로 조회 가능
- **중요:** 외부에서 history를 수정할 수 없어야 함 (복사본 반환)

```python
acc = BankAccount("강도윤", 1000)
acc.deposit(500)
acc.withdraw(200)
print(acc.get_history())
# [('deposit', 1000, 1000), ('deposit', 500, 1500), ('withdraw', 200, 1300)]
```

### 🥇 Hard: `@property` 데코레이터 맛보기 (미리보기)

진짜 Python 개발자처럼 `@property`를 사용해보세요!
- `balance`에 접근할 때 메서드 호출 없이 `acc.balance`처럼 쓰고 싶어요
- `@property`를 사용하면 가능합니다!
- `@balance.setter`로 값 변경도 제어할 수 있어요
- 힌트: 다음 시간에 더 자세히 배울 예정이니, 일단 도전해보세요!

```python
acc = ModernBankAccount("윤채원", 500)
print(acc.balance)        # 500 (메서드가 아니라 속성처럼!)
acc.balance = 1000        # setter가 호출됨
acc.balance = -50         # ValueError 발생!
```

## 🤔 생각해보기

코딩 후 다음 질문에 답해보세요:

1. **왜 `_balance` 대신 `__balance`를 써야 할까요?** 어떤 보안 차이가 있나요?
2. **`acc.__balance = 9999`** 라고 쓰면 실제로 무슨 일이 일어나나요? (힌트: `dir(acc)` 결과 확인)
3. **메서드를 통해서만 잔액을 변경**하게 하는 것의 장점은 무엇인가요?
4. 만약 여러분이 은행 시스템을 설계한다면, 어떤 정보를 비공개로 만들고 싶나요?

## 🌍 실무 연결

오늘 배운 캡슐화는 실제로 이런 곳에서 사용됩니다:
- 💳 **토스, 카카오뱅크** - 잔액과 거래 내역 보호
- 🔐 **비밀번호 관리자 (1Password 등)** - 비밀번호 암호화 저장
- 🏥 **병원 EMR 시스템** - 환자 정보 보호 (HIPAA 준수)
- 🎮 **게임 서버** - 캐릭터 능력치 해킹 방지

막히면 스레드에 질문 남겨주세요! 천천히 논리를 이해하면서 진행하세요. 행운을 빕니다! 🚀

---
---

# 🏦 Python Practice: Guard the Bank's Secrets!

Hey team! Today we're coding like real engineers at a FinTech company. 💳

## 🌟 The Story

You just joined a FinTech startup called "**SafeBank**" to build a digital wallet system!

The CTO tells you:

> *"If the balance can be changed from outside the class, we're done. Imagine someone writing `account.balance = 1000000000` — that's just free money. Absolutely not allowed!"*

So today we learn: **Name Mangling** — Python's strongest encapsulation tool. 🔒

## 🎯 Your Mission

Build a `BankAccount` class that guarantees:
- The balance (`__balance`) **cannot be modified directly from outside**
- The owner name (`__owner_name`) **cannot be read or modified from outside**
- Deposits/withdrawals must go through **methods only**
- All transactions must pass **validation**

## 🎓 Core Concept: Name Mangling

### Review: What you already know
Last time you learned `_attr` (single underscore):
```python
self._balance = 1000  # "Please don't touch" (just a convention!)
```

That's a **"gentleman's agreement"**. Anyone can still write `account._balance = 99999` and it works. 😱

### Today's new weapon: `__attr` (double underscore)
```python
self.__balance = 1000  # "You literally can't touch this!"
```

When a name starts with `__`, Python automatically **mangles** it:
- Inside the class: `self.__balance`
- Actual storage name: `_BankAccount__balance`

If outside code writes `account.__balance = 99999`? **It just creates a brand-new attribute — the real balance doesn't change!** 🎉

### Comparison

| Style | Syntax | External Access | Privacy Level |
|-------|--------|-----------------|---------------|
| `balance` | Public | `acc.balance` works | ⭐ None |
| `_balance` | Weak hint | `acc._balance` works | ⭐⭐ Convention |
| `__balance` | Strong | `acc.__balance` fails | ⭐⭐⭐ Enforced |

## 📋 The Rules

*Given:*
- Owner name (string)
- Initial deposit (optional, defaults to 0)

*BankAccount class requirements:*

**Private attributes (must start with `__`):**
- `__owner_name`: account owner's name
- `__balance`: current balance (never negative)
- `__is_active`: account status (True/False)

**Public methods:**
| Method | Behavior | Returns |
|--------|----------|---------|
| `get_owner_name()` | Get owner name | string |
| `get_balance()` | Get current balance | int |
| `is_active()` | Check if account is active | True/False |
| `deposit(amount)` | Deposit (positive only, active only) | True/False |
| `withdraw(amount)` | Withdraw (positive, sufficient funds, active) | True/False |
| `close_account()` | Close the account | None |

## 💡 Example

```python
acc = BankAccount("Kim Minjun", 1000)
print(acc.get_owner_name())   # Kim Minjun
print(acc.get_balance())      # 1000

acc.deposit(500)
print(acc.get_balance())      # 1500

acc.withdraw(200)
print(acc.get_balance())      # 1300

acc.withdraw(99999)           # Insufficient funds!
print(acc.get_balance())      # 1300 (unchanged)

acc.deposit(-100)             # Negative deposit rejected!
print(acc.get_balance())      # 1300

# 🔒 Verify direct access is blocked
try:
    print(acc.__balance)      # AttributeError!
except AttributeError:
    print("Can't peek! 🔒")

acc.__balance = 99999999      # Does NOT change balance!
print(acc.get_balance())      # Still 1300 💪
```

## ✅ Your Task

Write a class with this signature:

```python
class BankAccount:
    def __init__(self, owner_name: str, initial_deposit: int = 0):
        # Your code here
        pass
    
    def get_owner_name(self) -> str:
        pass
    
    def get_balance(self) -> int:
        pass
    
    def is_active(self) -> bool:
        pass
    
    def deposit(self, amount: int) -> bool:
        pass
    
    def withdraw(self, amount: int) -> bool:
        pass
    
    def close_account(self) -> None:
        pass
```

## 🎪 Test Your Code

```python
# Test 1: Basic creation
acc = BankAccount("Kim Minjun", 1000)
assert acc.get_balance() == 1000
assert acc.is_active() == True

# Test 2: Deposit
acc.deposit(500)
assert acc.get_balance() == 1500

# Test 3: Withdraw
acc.withdraw(300)
assert acc.get_balance() == 1200

# Test 4: Reject invalid transactions
assert acc.deposit(-100) == False    # Negative
assert acc.withdraw(99999) == False  # Insufficient
assert acc.get_balance() == 1200     # Unchanged

# Test 5: Close account
acc.close_account()
assert acc.is_active() == False
assert acc.deposit(100) == False     # Closed account

# Test 6: 🔒 Encapsulation check (MOST IMPORTANT!)
acc2 = BankAccount("Lee Seoyeon", 5000)
try:
    secret = acc2.__balance
    print("❌ Security failure!")
except AttributeError:
    print("✅ Balance is private!")

print("🎉 All tests passed!")
```

## 🎁 Bonus Challenges

### 🥉 Easy: Add a PIN

Add a 4-digit PIN to the account!
- Set PIN at creation (only accept 4-digit string of digits)
- `verify_pin(pin_attempt)` method: returns True if correct
- `change_pin(old_pin, new_pin)` method: verify old before changing
- PIN must never be readable from outside! (use `__pin`)

### 🥈 Medium: Transaction History

Add a private log of all transactions!
- `__history` list records every deposit/withdrawal
- Format: `(transaction_type, amount, balance_after)` tuple
- `get_history()` method returns the log
- **Important:** External code must NOT be able to modify history (return a copy)

```python
acc = BankAccount("Kang Doyun", 1000)
acc.deposit(500)
acc.withdraw(200)
print(acc.get_history())
# [('deposit', 1000, 1000), ('deposit', 500, 1500), ('withdraw', 200, 1300)]
```

### 🥇 Hard: `@property` Decorator Preview

Code like a pro with `@property`!
- Instead of `acc.get_balance()`, write `acc.balance` directly
- `@property` makes this possible
- `@balance.setter` lets you control how values are set
- Hint: we'll cover this in depth next class — try it now!

```python
acc = ModernBankAccount("Yoon Chaewon", 500)
print(acc.balance)        # 500 (looks like an attribute, not a method!)
acc.balance = 1000        # setter is called
acc.balance = -50         # raises ValueError!
```

## 🤔 Think About It

After coding, answer these:

1. **Why use `__balance` instead of `_balance`?** What's the security difference?
2. What actually happens when you write `acc.__balance = 9999` from outside? (Hint: check `dir(acc)`)
3. What's the advantage of forcing balance changes to go through methods?
4. If you designed a banking system, what other information would you make private?

## 🌍 Real-World Connections

Today's encapsulation lessons are used in:
- 💳 **Toss, KakaoBank** - protecting balances and transaction history
- 🔐 **Password managers (1Password, etc.)** - secure password storage
- 🏥 **Hospital EMR systems** - patient privacy (HIPAA compliance)
- 🎮 **Game servers** - preventing stat hacking

Drop questions in the thread if you get stuck! Take your time to understand the logic. Good luck! 🚀
