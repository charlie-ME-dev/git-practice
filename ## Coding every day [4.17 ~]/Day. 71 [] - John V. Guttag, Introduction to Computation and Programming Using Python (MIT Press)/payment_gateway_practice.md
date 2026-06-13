# 🏦 Python 연습: Wonder Pay 결제 게이트웨이 만들기!

> *"Don't check whether it IS-a duck: check whether it QUACKS-like-a duck."*
> — Alex Martelli (duck typing의 기원, comp.lang.python, 2000)

여러분, 안녕하세요! 지금까지 캡슐화, 상속, 다형성을 배웠습니다. 오늘은 OOP의 마지막 기둥인 **추상화(Abstraction)** 를 배워봅니다. 추상 베이스 클래스(ABC)를 사용해서 "모든 하위 클래스가 반드시 지켜야 하는 약속"을 코드로 강제하는 방법을 익혀봅시다!

## 🎯 미션

여러분은 핀테크 회사 **Wonder Pay** 의 백엔드 개발자입니다. 결제 게이트웨이는 여러 결제 수단(신용카드, 계좌이체, 모바일페이)을 지원해야 합니다.

문제는 이것입니다: **모든 결제 수단은 똑같은 결제 흐름**(금액 검증 → 수수료 적용 → 영수증 발급)을 따르지만, **수수료율과 이름은 각각 다릅니다.**

여러분의 임무는 추상 베이스 클래스로 "공통 흐름"을 한 번만 작성하고, 각 결제 수단은 자기만의 부분만 채우도록 만드는 것입니다.

**실전 적용 분야:**
- 💳 **결제 시스템**: 다양한 결제 수단을 동일한 인터페이스로 처리
- 🔌 **플러그인 아키텍처**: 모든 플러그인이 같은 규약을 따르도록 강제
- 📦 **데이터 내보내기**: CSV/JSON/XML 내보내기 클래스가 같은 메서드를 갖도록 보장
- 🎮 **게임 개발**: 모든 적(Enemy) 클래스가 `attack()`을 반드시 구현하도록 강제

## 🆕 새로운 개념: 추상 베이스 클래스 (ABC)

지금까지는 부모 클래스를 만들고 자식이 메서드를 **선택적으로** 오버라이드했습니다. 하지만 가끔은 "이 메서드는 반드시 구현해야 한다"고 **강제** 하고 싶을 때가 있습니다. 그것이 ABC입니다.

```python
from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def fee_rate(self) -> float:
        ...
```

두 가지가 핵심입니다:
- `ABC`를 상속하면 이 클래스는 **직접 인스턴스를 만들 수 없습니다.**
- `@abstractmethod`가 붙은 메서드는 모든 자식 클래스가 **반드시 구현** 해야 합니다. 빠뜨리면 인스턴스 생성 시 `TypeError`가 발생합니다.

```python
PaymentMethod()          # ❌ TypeError: Can't instantiate abstract class
```

> 💡 **왜 다형성 다음에 추상화일까요?**
> 다형성은 "같은 메서드 호출에 객체마다 다르게 반응하는 능력"을 줬습니다. 추상화는 그 구현을 **강제** 합니다 — 모든 결제 수단이 `fee_rate()`를 반드시 갖고 있으니, 여러 결제 수단을 하나의 반복문으로 처리해도 절대 "메서드 없음" 오류가 나지 않습니다.

## 🧩 핵심 개념: 템플릿 메서드 (Concrete Method)

ABC는 추상 메서드만 갖는 게 아닙니다. **실제 동작하는 메서드(concrete method)** 도 가질 수 있습니다. 이것이 ABC가 강력한 이유입니다.

베이스 클래스가 **공통 흐름**을 한 번 작성하고, 그 안에서 추상 메서드를 호출합니다. 자식은 빈칸만 채우면 됩니다.

```python
class PaymentMethod(ABC):
    @abstractmethod
    def fee_rate(self) -> float: ...

    @abstractmethod
    def label(self) -> str: ...

    def process_payment(self, amount: int) -> str:   # ← 공통 흐름 (템플릿)
        if amount <= 0:
            raise ValueError("amount must be positive")
        fee = round(amount * self.fee_rate())        # ← 자식이 채운 부분 사용
        total = amount + fee
        return f"[{self.label()}] amount={amount}, fee={fee}, total={total}"
```

## 📋 규칙

*만들어야 할 것:*

1. **`PaymentMethod`** (추상 베이스 클래스, `ABC` 상속)
   - `fee_rate(self) -> float` : **추상 메서드**. 수수료율을 소수로 반환 (예: `0.03` = 3%)
   - `label(self) -> str` : **추상 메서드**. 결제 수단 이름 반환
   - `process_payment(self, amount: int) -> str` : **일반 메서드 (템플릿)**. 아래 흐름을 구현
     - `amount`가 0 이하이면 `ValueError("amount must be positive")` 발생
     - `fee = round(amount * self.fee_rate())`
     - `total = amount + fee`
     - `f"[{self.label()}] amount={amount}, fee={fee}, total={total}"` 반환

2. **`CardPayment`** : `fee_rate` = `0.03`, `label` = `"Credit Card"`
3. **`BankTransfer`** : `fee_rate` = `0.0`, `label` = `"Bank Transfer"`
4. **`MobilePay`** : `fee_rate` = `0.015`, `label` = `"Mobile Pay"`

*제약사항:*
- `process_payment`는 **베이스 클래스에 단 한 번만** 작성하세요. 자식 클래스에 복사-붙여넣기 금지!
- 자식 클래스는 `fee_rate`와 `label`만 구현하면 됩니다.
- 수수료는 반드시 `round()`로 반올림하세요 (정수 원 단위).

## 💡 예제

**예제 1: 신용카드 결제**
```python
card = CardPayment()
print(card.process_payment(1000))
# 출력: [Credit Card] amount=1000, fee=30, total=1030
# 왜? 1000 * 0.03 = 30
```

**예제 2: 계좌이체 (수수료 없음)**
```python
bank = BankTransfer()
print(bank.process_payment(1000))
# 출력: [Bank Transfer] amount=1000, fee=0, total=1000
```

**예제 3: 반올림 처리**
```python
mobile = MobilePay()
print(mobile.process_payment(333))
# 출력: [Mobile Pay] amount=333, fee=5, total=338
# 왜? 333 * 0.015 = 4.995 → round() → 5
```

**예제 4: 추상 클래스는 만들 수 없음**
```python
PaymentMethod()
# ❌ TypeError: Can't instantiate abstract class PaymentMethod
#    with abstract methods fee_rate, label
```

## 🎓 알아야 할 것

코딩을 시작하기 전에 다음을 이해하고 있는지 확인하세요:
- 클래스 정의와 상속 (`class Child(Parent):`)
- 메서드 오버라이딩 (다형성에서 배운 내용)
- `self`와 인스턴스 메서드
- `round()` 내장 함수
- f-string 포맷팅

## ✅ 과제

스켈레톤 파일의 TODO를 채워 네 개의 클래스를 완성하세요.

## 🎪 코드 테스트

```python
# 테스트 1: 추상 클래스는 인스턴스화 불가
try:
    PaymentMethod()
    print("❌ 실패: ABC가 생성되면 안 됩니다")
except TypeError:
    print("✅ 통과: ABC는 직접 생성 불가")

# 테스트 2: 다형성 — 같은 반복문, 다른 동작
methods = [CardPayment(), BankTransfer(), MobilePay()]
for m in methods:
    print(m.process_payment(2000))
# 예상:
# [Credit Card] amount=2000, fee=60, total=2060
# [Bank Transfer] amount=2000, fee=0, total=2000
# [Mobile Pay] amount=2000, fee=30, total=2030
```

## 🤔 생각해보기

1. 만약 `process_payment`를 자식마다 따로 작성했다면 어떤 문제가 생길까요? (힌트: 흐름을 바꾸려면 몇 군데를 고쳐야 할까요?)
2. 새 결제 수단 `CryptoPayment`를 추가하려면 무엇을 작성해야 하나요? 무엇을 작성하지 *않아도* 되나요?
3. `@abstractmethod`를 빼면 어떤 일이 벌어질까요? 자식이 구현을 깜빡하면요?

## 🏆 보너스 챌린지

**🥉 Easy — `min_fee` 추가**
모든 결제에 최소 수수료 100원을 적용하세요. `process_payment`의 `fee` 계산을 `max(round(...), 100)`로 수정 (단, `amount`가 양수일 때만).

**🥈 Medium — `@property` + `@abstractmethod`**
`label`을 메서드 대신 **추상 프로퍼티**로 바꿔보세요:
```python
@property
@abstractmethod
def label(self) -> str: ...
```
자식에서는 `@property`로 구현하고, `self.label()` 대신 `self.label`로 호출하도록 템플릿을 수정하세요.

**🥇 Hard — 결제 수단 등록 시스템**
`PaymentMethod`에 클래스 변수 `registry = {}`를 두고, 각 자식이 정의될 때 자동으로 등록되게 만드세요. (힌트: `__init_subclass__`를 미리 맛보기 — 아직 안 배운 개념이니 도전 과제입니다.) 그리고 문자열 이름으로 결제 수단을 생성하는 `create(name)` 클래스 메서드를 추가하세요.

---

막히면 스레드에 질문을 남겨주세요! 목표는 끝내는 것이 아니라 **왜 추상화가 필요한지** 이해하는 것입니다. 천천히 진행하세요. 행운을 빕니다! 🚀

---
---

# 🏦 Python Practice: Build the Wonder Pay Payment Gateway!

> *"Don't check whether it IS-a duck: check whether it QUACKS-like-a duck."*
> — Alex Martelli (origin of duck typing, comp.lang.python, 2000)

Hey team! You've now learned encapsulation, inheritance, and polymorphism. Today we tackle the final pillar of OOP: **Abstraction**. Using Abstract Base Classes (ABCs), you'll learn how to enforce, in code, a contract that every subclass must follow.

## 🎯 Your Mission

You're a backend developer at the FinTech company **Wonder Pay**. The payment gateway must support several payment methods (credit card, bank transfer, mobile pay).

Here's the catch: **every payment method follows the exact same checkout flow** (validate amount → apply fee → produce receipt), but **each has a different fee rate and name.**

Your job: write the "shared flow" exactly once in an abstract base class, and let each payment method fill in only its own piece.

**Real-world applications:**
- 💳 **Payment systems**: handle many payment methods through one interface
- 🔌 **Plugin architectures**: force every plugin to follow the same contract
- 📦 **Data export**: ensure CSV/JSON/XML exporters share the same method
- 🎮 **Game dev**: require every Enemy class to implement `attack()`

## 🆕 New Concept: Abstract Base Class (ABC)

Until now you made a parent class and children *optionally* overrode methods. But sometimes you want to **force** "this method must be implemented." That's what ABCs do.

```python
from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def fee_rate(self) -> float:
        ...
```

Two key points:
- Inheriting from `ABC` means this class **cannot be instantiated directly.**
- A method marked `@abstractmethod` **must** be implemented by every child. Skip it, and you get a `TypeError` when you try to create an instance.

```python
PaymentMethod()          # ❌ TypeError: Can't instantiate abstract class
```

> 💡 **Why abstraction right after polymorphism?**
> Polymorphism gave you the *ability* for objects to respond differently to the same call. Abstraction *enforces* that implementation — since every payment method is guaranteed to have `fee_rate()`, you can process a mixed list of them in one loop and never hit a "missing method" error.

## 🧩 Key Concept: The Template Method (Concrete Method)

An ABC isn't only abstract methods. It can also have **real, working methods (concrete methods)**. This is what makes ABCs powerful.

The base class writes the **shared flow** once, calling the abstract methods inside it. Children just fill in the blanks.

```python
class PaymentMethod(ABC):
    @abstractmethod
    def fee_rate(self) -> float: ...

    @abstractmethod
    def label(self) -> str: ...

    def process_payment(self, amount: int) -> str:   # ← shared flow (template)
        if amount <= 0:
            raise ValueError("amount must be positive")
        fee = round(amount * self.fee_rate())        # ← uses the child's piece
        total = amount + fee
        return f"[{self.label()}] amount={amount}, fee={fee}, total={total}"
```

## 📋 The Rules

*What to build:*

1. **`PaymentMethod`** (abstract base, inherits `ABC`)
   - `fee_rate(self) -> float` : **abstract method**. Return the fee rate as a decimal (e.g. `0.03` = 3%)
   - `label(self) -> str` : **abstract method**. Return the payment method's name
   - `process_payment(self, amount: int) -> str` : **concrete method (template)**:
     - If `amount` ≤ 0, raise `ValueError("amount must be positive")`
     - `fee = round(amount * self.fee_rate())`
     - `total = amount + fee`
     - Return `f"[{self.label()}] amount={amount}, fee={fee}, total={total}"`

2. **`CardPayment`** : `fee_rate` = `0.03`, `label` = `"Credit Card"`
3. **`BankTransfer`** : `fee_rate` = `0.0`, `label` = `"Bank Transfer"`
4. **`MobilePay`** : `fee_rate` = `0.015`, `label` = `"Mobile Pay"`

*Constraints:*
- Write `process_payment` **exactly once, in the base class**. No copy-pasting it into children!
- Children only implement `fee_rate` and `label`.
- Always round the fee with `round()` (whole-won units).

## 💡 Examples

**Example 1: Credit card**
```python
card = CardPayment()
print(card.process_payment(1000))
# Output: [Credit Card] amount=1000, fee=30, total=1030
# Why? 1000 * 0.03 = 30
```

**Example 2: Bank transfer (no fee)**
```python
bank = BankTransfer()
print(bank.process_payment(1000))
# Output: [Bank Transfer] amount=1000, fee=0, total=1000
```

**Example 3: Rounding**
```python
mobile = MobilePay()
print(mobile.process_payment(333))
# Output: [Mobile Pay] amount=333, fee=5, total=338
# Why? 333 * 0.015 = 4.995 → round() → 5
```

**Example 4: The abstract class can't be created**
```python
PaymentMethod()
# ❌ TypeError: Can't instantiate abstract class PaymentMethod
#    with abstract methods fee_rate, label
```

## 🎓 What You Should Know

Before you start, make sure you understand:
- Class definition and inheritance (`class Child(Parent):`)
- Method overriding (from the polymorphism unit)
- `self` and instance methods
- The `round()` built-in
- f-string formatting

## ✅ Your Task

Fill in the TODOs in the skeleton file to complete the four classes.

## 🎪 Test Your Code

```python
# Test 1: the abstract class cannot be instantiated
try:
    PaymentMethod()
    print("❌ Fail: ABC should not be creatable")
except TypeError:
    print("✅ Pass: ABC cannot be created directly")

# Test 2: polymorphism — same loop, different behavior
methods = [CardPayment(), BankTransfer(), MobilePay()]
for m in methods:
    print(m.process_payment(2000))
# Expected:
# [Credit Card] amount=2000, fee=60, total=2060
# [Bank Transfer] amount=2000, fee=0, total=2000
# [Mobile Pay] amount=2000, fee=30, total=2030
```

## 🤔 Think About It

1. If you wrote `process_payment` separately in each child, what problem appears? (Hint: to change the flow, how many places must you edit?)
2. To add a new `CryptoPayment`, what must you write? What do you *not* need to write?
3. What happens if you remove `@abstractmethod`? What if a child forgets to implement it?

## 🏆 Bonus Challenges

**🥉 Easy — Add `min_fee`**
Apply a minimum fee of 100 won to every payment. Change the `fee` calculation in `process_payment` to `max(round(...), 100)` (only when `amount` is positive).

**🥈 Medium — `@property` + `@abstractmethod`**
Turn `label` into an **abstract property** instead of a method:
```python
@property
@abstractmethod
def label(self) -> str: ...
```
Implement it with `@property` in the children, and update the template to use `self.label` instead of `self.label()`.

**🥇 Hard — Payment method registry**
Give `PaymentMethod` a class variable `registry = {}` and make each child auto-register when defined. (Hint: a preview of `__init_subclass__` — a concept you haven't learned yet, so this is a stretch challenge.) Then add a `create(name)` class method that builds a payment method from a string name.

---

Drop questions in the thread if you get stuck! The goal isn't to finish — it's to understand **why abstraction matters**. Take your time. Good luck! 🚀
