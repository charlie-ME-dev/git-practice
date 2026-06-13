# 🏋️ Python 연습 Day 5: 헬스장 회원권 시스템 만들기!

여러분, 안녕하세요! 오늘은 캡슐화(Encapsulation)를 한 번 더 연습하는 다섯 번째 날입니다. 💪

지난 시간(Day 4)에는 은행 계좌로 캡슐화를 배웠죠? 오늘은 같은 개념을 **다른 시나리오**로 다시 연습합니다. 반복은 실력의 어머니입니다!

## 🌟 배경 스토리

여러분이 **FitLife**라는 헬스장 체인에 취업했어요! 회원 관리 시스템을 다시 만들어야 하는데, 기존 코드가 엉망입니다. 누구나 회원 등급(tier)을 마음대로 바꿀 수 있고, 만료일을 거꾸로 되돌릴 수도 있고, 출석 횟수를 조작할 수도 있어요. 😱

여러분의 임무: **캡슐화로 데이터를 보호하라!** 🛡️

## 🎯 미션

`GymMembership` 클래스를 만드세요. 각 회원권은 다음 정보를 가집니다:

| 속성 | 의미 | 변경 가능? |
|---|---|---|
| `_member_id` | 회원 번호 | ❌ 생성 후 변경 불가 (read-only) |
| `_name` | 회원 이름 | ✅ 수정 가능 (빈 문자열 금지) |
| `_tier` | 등급: `"basic"`, `"premium"`, `"vip"` | ✅ 수정 가능 (정해진 값만) |
| `_expiration_date` | 만료일 `"YYYY-MM-DD"` | ✅ 수정 가능 (날짜 형식만) |
| `_check_in_count` | 출석 횟수 | ❌ 외부에서 직접 변경 불가 (read-only) |

## 🎓 알아야 할 것 (복습)

### 캡슐화(Encapsulation)란?
**중요한 데이터를 보호하는 것.** 외부에서 함부로 못 만지게 하고, 정해진 방법(메서드)으로만 접근하게 합니다.

### 핵심 규칙 (Day 4 복습)
1. **언더스코어 `_` 접두사**: "이건 private이에요, 직접 만지지 마세요"라는 약속
2. **Getter 메서드**: 값을 읽을 때 사용 (`get_name()`)
3. **Setter 메서드**: 값을 바꿀 때 사용 (`set_name(new_name)`)
4. **검증(Validation)**: setter 안에서 값이 유효한지 확인

### 🆕 Day 5의 새로운 점

**① Setter에서 `raise ValueError`로 잘못된 값 거부하기**

Day 4에서는 `print("잘못된 값입니다")`로 끝났지만, 오늘은 진짜 프로처럼 **예외(exception)를 발생시켜서** 잘못된 값을 거부합니다.

```python
def set_tier(self, tier):
    if tier not in ("basic", "premium", "vip"):
        raise ValueError(f"잘못된 등급입니다: {tier}")
    self._tier = tier
```

**왜 `raise`가 더 좋나요?**
- `print`는 그냥 메시지만 출력하고 코드는 계속 실행됩니다 → 잘못된 값이 그대로 저장될 수 있어요
- `raise`는 잘못된 값을 **확실하게 거부**하고 프로그램에 "문제 발생!"을 알립니다
- 호출하는 쪽에서 `try/except`로 처리할 수 있어요

**② Read-only 속성 (Getter만 있고 Setter는 없음)**

어떤 속성은 **읽기만 가능하고, 외부에서 바꿀 수 없어야** 합니다.
- `_member_id`: 회원 번호는 가입할 때 한 번 정해지면 평생 바뀌면 안 됩니다
- `_check_in_count`: 출석 횟수는 `check_in()` 메서드로만 늘어나야지, 외부에서 마음대로 100으로 바꾸면 안 되겠죠?

**해결법: Setter를 아예 만들지 않으면 됩니다!**
```python
class GymMembership:
    def get_member_id(self):
        return self._member_id
    
    # set_member_id 메서드는 만들지 않습니다 → read-only!
```

## 📋 단계별 미션

### 🎯 미션 1: `__init__` 메서드

회원권 생성 시 모든 속성을 초기화하세요.

**요구사항:**
- 파라미터: `member_id`, `name`, `tier`, `expiration_date`
- 모든 값을 검증한 후 저장 (setter 메서드 재활용 추천!)
- `_check_in_count`는 항상 `0`으로 시작
- `member_id`가 빈 문자열이면 `ValueError`

**예제:**
```python
m = GymMembership("M001", "박지우", "basic", "2026-12-31")
print(m.get_member_id())  # "M001"
print(m.get_check_in_count())  # 0
```

---

### 🎯 미션 2: Getter 메서드 5개

모든 속성에 대한 getter를 만드세요:
- `get_member_id()`
- `get_name()`
- `get_tier()`
- `get_expiration_date()`
- `get_check_in_count()`

---

### 🎯 미션 3: Setter 메서드 3개 (검증 포함!)

**`set_name(name)`**
- 빈 문자열이나 공백만 있는 문자열이면 `ValueError`
- 양쪽 공백은 `.strip()`으로 제거 후 저장

**`set_tier(tier)`**
- `"basic"`, `"premium"`, `"vip"` 중 하나가 아니면 `ValueError`

**`set_expiration_date(expiration_date)`**
- `"YYYY-MM-DD"` 형식이 아니면 `ValueError`
- 힌트: `from datetime import date` 후 `date.fromisoformat(...)` 사용

> ⚠️ **`set_member_id`와 `set_check_in_count`는 만들지 마세요!** Read-only 속성이니까요.

---

### 🎯 미션 4: `check_in(today)` 메서드

회원이 헬스장에 도착했을 때 호출됩니다.

**요구사항:**
- `today` 파라미터는 `"YYYY-MM-DD"` 형식 문자열 (기본값 없이 항상 받기)
- 만료일이 `today`보다 이전이면 `ValueError` ("이미 만료된 회원권입니다")
- 통과하면 `_check_in_count`를 1 증가

**예제:**
```python
m = GymMembership("M002", "이수호", "basic", "2027-06-30")
m.check_in("2026-05-18")
m.check_in("2026-05-19")
print(m.get_check_in_count())  # 2
```

---

### 🎯 미션 5: `upgrade_tier(new_tier)` 메서드

등급을 올릴 수 있지만, **올리는 것만** 가능합니다.

**등급 순위:** `basic` < `premium` < `vip`

**요구사항:**
- `new_tier`가 현재 등급보다 높으면 변경
- 같거나 낮으면 `ValueError`
- 유효하지 않은 등급이면 `ValueError`

**예제:**
```python
m = GymMembership("M004", "한도윤", "basic", "2027-12-31")
m.upgrade_tier("premium")  # OK
m.upgrade_tier("vip")  # OK
m.upgrade_tier("basic")  # ValueError!
```

---

### 🎯 미션 6: `renew(new_expiration_date)` 메서드

만료일을 연장합니다.

**요구사항:**
- 새 만료일이 현재 만료일보다 **이후**여야 함
- 그렇지 않으면 `ValueError`
- 날짜 형식 검증도 필요 (기존 setter 재활용 가능)

---

### 🎯 미션 7: `is_active(today)` 메서드

회원권이 아직 유효한지 확인합니다.

**요구사항:**
- `today`가 만료일 이전이거나 같으면 `True`
- 만료일을 넘었으면 `False`
- 파라미터: `today` (`"YYYY-MM-DD"` 형식)

---

### 🎯 미션 8: `__str__` 메서드

`print(m)`을 호출하면 회원 정보가 보기 좋게 출력되도록 하세요.

**예제 출력:**
```
GymMembership(id=M007, name=배은우, tier=vip, expires=2027-08-15, check_ins=2)
```

## 🎪 코드 테스트

```python
from datetime import date

# 테스트 1: 생성과 getter
m = GymMembership("M001", "박지우", "basic", "2026-12-31")
assert m.get_member_id() == "M001"
assert m.get_tier() == "basic"
assert m.get_check_in_count() == 0

# 테스트 2: 잘못된 등급은 거부
try:
    m.set_tier("gold")
    print("❌ 실패")
except ValueError:
    print("✅ ValueError 발생!")

# 테스트 3: check_in
m.check_in("2026-05-18")
m.check_in("2026-05-19")
assert m.get_check_in_count() == 2

# 테스트 4: 만료된 회원권은 check_in 불가
m_expired = GymMembership("M003", "최하나", "vip", "2026-01-01")
try:
    m_expired.check_in("2026-05-18")
    print("❌ 실패")
except ValueError:
    print("✅ 만료된 회원권 거부됨!")

# 테스트 5: read-only 확인
assert not hasattr(m, "set_member_id"), "member_id는 read-only여야 합니다!"
assert not hasattr(m, "set_check_in_count"), "check_in_count는 read-only여야 합니다!"
print("✅ Read-only 속성 확인 완료!")
```

## 💪 보너스 챌린지

### 🥉 Easy: `freeze()` / `unfreeze()` 메서드
회원이 휴면 상태가 되면 `check_in()`이 안 되어야 합니다.
- `_is_frozen` 속성 추가 (default `False`)
- 휴면 중 `check_in()` 호출 시 `ValueError`
- Getter `is_frozen()`도 만드세요

### 🥈 Medium: `apply_discount(percent)` + 등급별 한도
등급별 최대 할인율을 다르게 설정하세요.
- `basic`: 최대 10%
- `premium`: 최대 20%
- `vip`: 최대 50%
- 한도를 넘으면 `ValueError`
- 할인율 음수도 `ValueError`

### 🥇 Hard: 클래스 변수로 통계 관리
**(미리보기: 클래스 변수)**
- 클래스 변수 `_total_memberships`로 생성된 총 회원 수 추적
- 클래스 변수 `_active_check_ins`로 모든 회원의 누적 출석 횟수 추적
- 클래스 메서드 `get_statistics()`로 두 값을 dict로 반환
- 힌트: `GymMembership._total_memberships += 1` 같은 식으로 접근

## 🤔 생각해보기

코딩을 시작하기 전에 다음 질문에 답해보세요:

1. **`raise ValueError`와 `print("에러!")`의 차이는 무엇인가요?** 왜 `raise`가 더 안전한가요?

2. **`_member_id`를 read-only로 만든 이유는 무엇일까요?** 만약 변경 가능하다면 어떤 문제가 생길까요?

3. **`__init__` 안에서 `self._name = name`을 직접 쓰는 것과 `self.set_name(name)`을 호출하는 것의 차이는?** 어느 쪽이 더 좋을까요?

4. **사용자가 `m._tier = "gold"`처럼 직접 접근하면 어떻게 되나요?** Python에서 진짜로 막을 수 있나요?

## 🌍 실무에서의 의미

여러분이 만든 이 패턴은 **실제 SaaS 회사**에서 다음과 같이 쓰입니다:

- **Netflix, Spotify**: 구독 등급 관리 (Free → Premium → Family) 다운그레이드 방지
- **항공사 마일리지**: 회원 등급(Silver/Gold/Platinum)은 자동 계산되어야 하고, 고객이 임의로 못 바꿔야 함
- **헬스장/요가원**: 출석 기록은 위변조 불가, 만료된 회원권으로 입장 불가
- **온라인 게임**: 캐릭터 레벨은 게임 로직으로만 오르고, 플레이어가 직접 못 바꿈

캡슐화는 **데이터 무결성(integrity)**을 지키는 핵심 기술이에요!

막히면 스레드에 질문 남겨주세요. 천천히, 한 메서드씩! 🚀

---
---

# 🏋️ Python Practice Day 5: Build a Gym Membership System!

Hey team! Today is Day 5 — one more round of encapsulation practice. 💪

Day 4 was bank accounts. Today, same concept, **different scenario**. Repetition is how habits form!

## 🌟 The Story

You've joined **FitLife**, a gym chain. Their membership system is a mess: anyone can change tier freely, roll back expiration dates, or fake check-in counts. 😱

Your mission: **Protect the data with encapsulation!** 🛡️

## 🎯 Your Mission

Build a `GymMembership` class. Each membership has:

| Attribute | Meaning | Mutable? |
|---|---|---|
| `_member_id` | Member number | ❌ Read-only after creation |
| `_name` | Member name | ✅ Mutable (no empty strings) |
| `_tier` | `"basic"`, `"premium"`, `"vip"` | ✅ Mutable (validated) |
| `_expiration_date` | `"YYYY-MM-DD"` | ✅ Mutable (validated) |
| `_check_in_count` | Check-in counter | ❌ Read-only from outside |

## 🎓 What You Should Know (Review)

### What is Encapsulation?
**Protecting important data.** Outside code can't touch it directly — it must go through approved methods.

### Core Rules (Day 4 Recap)
1. **Underscore `_` prefix**: "This is private, don't touch directly"
2. **Getter methods**: read values (`get_name()`)
3. **Setter methods**: change values (`set_name(new_name)`)
4. **Validation**: check inputs inside setters

### 🆕 What's New in Day 5

**① Use `raise ValueError` to reject bad input**

On Day 4 you printed an error message. Today, like a real engineer, you'll **raise an exception** to truly reject bad values.

```python
def set_tier(self, tier):
    if tier not in ("basic", "premium", "vip"):
        raise ValueError(f"Invalid tier: {tier}")
    self._tier = tier
```

**Why `raise` is better than `print`:**
- `print` just shows a message but code keeps running → bad data might still get stored
- `raise` actually **rejects** the value and signals "something is wrong!"
- The caller can handle it with `try/except`

**② Read-only attributes (Getter only, no Setter)**

Some attributes should be **readable but not writable from outside**.
- `_member_id`: assigned at signup, must never change
- `_check_in_count`: should only increase via `check_in()`, never be set to 100 by outside code

**Solution: just don't make a setter!**
```python
class GymMembership:
    def get_member_id(self):
        return self._member_id
    
    # No set_member_id method → read-only!
```

## 📋 Step-by-Step Tasks

### 🎯 Task 1: `__init__` method

Initialize all attributes at construction time.

**Requirements:**
- Parameters: `member_id`, `name`, `tier`, `expiration_date`
- Validate all values before storing (reuse your setter methods!)
- `_check_in_count` always starts at `0`
- Empty `member_id` → `ValueError`

**Example:**
```python
m = GymMembership("M001", "Jiwoo Park", "basic", "2026-12-31")
print(m.get_member_id())  # "M001"
print(m.get_check_in_count())  # 0
```

---

### 🎯 Task 2: Five getter methods

- `get_member_id()`
- `get_name()`
- `get_tier()`
- `get_expiration_date()`
- `get_check_in_count()`

---

### 🎯 Task 3: Three setter methods (with validation!)

**`set_name(name)`** — empty/whitespace-only → `ValueError`; trim with `.strip()`

**`set_tier(tier)`** — must be `"basic"`, `"premium"`, or `"vip"` → else `ValueError`

**`set_expiration_date(expiration_date)`** — must parse as `"YYYY-MM-DD"`; use `from datetime import date` and `date.fromisoformat(...)`

> ⚠️ **Do NOT make `set_member_id` or `set_check_in_count`!** They are read-only.

---

### 🎯 Task 4: `check_in(today)` method

Called when a member arrives at the gym.

**Requirements:**
- `today` is a `"YYYY-MM-DD"` string (always required)
- If membership is expired → `ValueError`
- Otherwise increment `_check_in_count` by 1

---

### 🎯 Task 5: `upgrade_tier(new_tier)` method

Tiers can only go **up**.

**Ranking:** `basic` < `premium` < `vip`

**Requirements:**
- Higher tier → change it
- Same or lower → `ValueError`
- Invalid tier → `ValueError`

---

### 🎯 Task 6: `renew(new_expiration_date)` method

Extend the expiration date.

**Requirements:**
- New date must be **after** current expiration
- Otherwise → `ValueError`
- Reuse the date setter for format validation

---

### 🎯 Task 7: `is_active(today)` method

Check if the membership is still valid.

**Requirements:**
- `today <= expiration` → `True`
- Otherwise → `False`

---

### 🎯 Task 8: `__str__` method

```
GymMembership(id=M007, name=Eunwoo Bae, tier=vip, expires=2027-08-15, check_ins=2)
```

## 🎪 Test Your Code

```python
m = GymMembership("M001", "Jiwoo Park", "basic", "2026-12-31")
assert m.get_check_in_count() == 0

try:
    m.set_tier("gold")
except ValueError:
    print("✅ Invalid tier rejected!")

m.check_in("2026-05-18")
m.check_in("2026-05-19")
assert m.get_check_in_count() == 2

assert not hasattr(m, "set_member_id"), "member_id must be read-only!"
assert not hasattr(m, "set_check_in_count"), "check_in_count must be read-only!"
print("✅ Read-only attributes confirmed!")
```

## 💪 Bonus Challenges

### 🥉 Easy: `freeze()` / `unfreeze()`
Frozen members can't check in. Add `_is_frozen` (default `False`) and `is_frozen()` getter. `check_in()` while frozen → `ValueError`.

### 🥈 Medium: `apply_discount(percent)` with tier-based caps
- `basic`: max 10% / `premium`: max 20% / `vip`: max 50%
- Over the cap or negative → `ValueError`

### 🥇 Hard: Class variables for statistics
**(Preview: class variables)**
Track total memberships and total check-ins across the entire class using class variables. Add `get_statistics()` that returns a dict. Hint: `GymMembership._total_memberships += 1`.

## 🤔 Think About It

1. What's the difference between `raise ValueError` and `print("error!")`? Why is `raise` safer?
2. Why is `_member_id` read-only? What problems would mutability cause?
3. Inside `__init__`, is `self._name = name` the same as `self.set_name(name)`? Which is better?
4. What if a user does `m._tier = "gold"` directly? Can Python actually prevent this?

## 🌍 Real-World Relevance

This exact pattern powers:
- **Netflix, Spotify** — subscription tier changes (no silent downgrades)
- **Airline miles** — tier (Silver/Gold/Platinum) is system-managed, not user-editable
- **Gyms/yoga studios** — tamper-proof attendance, expired memberships can't enter
- **Online games** — character level set by game logic, not the player

Encapsulation is how real systems protect **data integrity**.

Drop questions in the thread. One method at a time! 🚀
