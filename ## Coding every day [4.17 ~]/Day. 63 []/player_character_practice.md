# 🎮 Python 연습: 게임 캐릭터의 비밀 — `_` vs `__`

여러분, 안녕하세요! 오늘은 캡슐화의 마지막 퍼즐 조각을 맞춰볼 시간입니다.

## 🎯 미션

여러분은 멀티플레이어 RPG 게임의 백엔드 개발자입니다. 플레이어 캐릭터 클래스를 만들고 있는데, 보안팀에서 까다로운 요구를 했어요:

> "체력(health)이랑 데미지 배율(damage multiplier)은 절대로 외부에서 직접 조작 못하게 막아주세요. 핵쟁이들이 메모리 치트로 건드리는 거 잘 알잖아요. 근데 경험치(experience)나 스태미나(stamina) 같은 건 굳이 그렇게까지 막을 필요는 없어요."

> "한 클래스 안에서 '강한 보호'와 '약한 보호'를 모두 표현해야 한다는 뜻이죠. Python에 그런 방법이 있나요?"

있습니다! 바로 **언더스코어 개수의 차이**입니다.

## 📋 규칙

*주어지는 것:*
- 캐릭터 이름과 시작 레벨
- 게임 규칙: 체력은 0~100 범위, XP가 쌓이면 자동 레벨업

*핵심 학습 목표:*
1. `_` (single underscore)의 의미와 동작
2. `__` (double underscore)의 의미와 동작
3. **언제 어떤 것을 써야 하는지** 판단

*제약사항:*
- 외부에서 `player.__health` 직접 접근 시 에러가 나야 합니다
- 외부에서 `player._experience` 접근은 **가능**해야 합니다 (의도된 동작!)
- 모든 보호된 속성은 getter 메서드로 읽을 수 있어야 합니다

---

## 🎓 핵심 개념: `_` vs `__`

### 🚪 Single Underscore (`_name`) — "약한 보호" (Weak Protection)

> "출입 금지 표지판은 있지만, 문은 잠겨있지 않습니다."

```python
class Player:
    def __init__(self):
        self._stamina = 100  # 내부 사용 권장

p = Player()
print(p._stamina)  # ✅ 작동함! Python이 막지 않음
p._stamina = 999   # ✅ 이것도 작동함!
```

**핵심:** `_`는 **순전히 관례(convention)**입니다. Python은 아무것도 막지 않습니다. 다른 개발자에게 "이건 내부용이니까 만지지 마세요"라고 **요청**하는 것뿐이에요.

**언제 쓰나?** 클래스 내부에서 사용하지만, 서브클래스나 같은 모듈의 다른 코드가 접근해야 할 수도 있을 때.

---

### 🔒 Double Underscore (`__name`) — "강한 보호" (Strong Protection)

> "출입 금지 표지판 + 자물쇠 + 보안 시스템."

```python
class Player:
    def __init__(self):
        self.__health = 100  # 진짜로 막을 거예요!

p = Player()
print(p.__health)  # ❌ AttributeError!
```

**핵심:** `__`로 시작하는 속성은 Python이 자동으로 **이름을 바꿔버립니다** (name mangling). `__health`는 실제로 `_Player__health`로 저장돼요.

**언제 쓰나?** 클래스의 핵심 정체성과 관련된 데이터로, 외부 접근을 정말로 막고 싶을 때.

---

### 🔍 Name Mangling이 정확히 뭔가요?

> "이름을 비틀어서 충돌을 피하는 기술"

`__health`라고 쓰면 Python은 내부적으로 `_ClassName__health`로 저장합니다:

```python
class Player:
    def __init__(self):
        self.__health = 100  # 실제 이름: _Player__health

p = Player()
print(p.__health)              # ❌ AttributeError
print(p._Player__health)       # 🔓 100 (정말 접근하고 싶다면...)
```

**중요:** 이것은 **보안 기능이 아닙니다.** 진짜로 접근하려면 가능합니다. 하지만 **실수로 건드릴 가능성을 크게 줄여줍니다.**

---

### 🤔 그래서 언제 어떤 걸 써야 하나요?

| 상황 | 사용 | 이유 |
|------|------|------|
| 외부에서 안 보였으면 좋겠지만, 가끔 접근 필요 | `_name` | 융통성 있음 |
| 절대로 외부에서 건드리면 안 되는 핵심 데이터 | `__name` | 강력하게 보호 |
| 일반 공개 속성 | `name` | 자유롭게 접근 |
| 매직 메서드 | `__name__` | Python 예약 (예: `__init__`) |

> 💡 **Pythonic 격언:** "We are all consenting adults here." — Python은 신뢰 기반 언어입니다. 보통은 `_` 하나로 충분해요. `__`는 정말로 막아야 할 때만 사용하세요.

---

## 💡 예제

**예제 1: 기본 생성과 접근**
```python
hero = PlayerCharacter("아서", 5)

# Public 속성 — 자유롭게 접근
print(hero.name)            # "아서"
print(hero.level)           # 5

# Single underscore — 접근 가능하지만 권장 X
print(hero._stamina)        # 100 (작동함, 하지만 getter 쓰는 게 좋음)

# Double underscore — 직접 접근 차단
print(hero.__health)        # ❌ AttributeError!
print(hero.get_health())    # ✅ 100 (이렇게 써야 함)
```

**예제 2: 데미지와 회복**
```python
hero = PlayerCharacter("아서")
hero.take_damage(30)
print(hero.get_health())    # 70

hero.heal(20)
print(hero.get_health())    # 90

hero.take_damage(500)
print(hero.get_health())    # 0 (음수가 되지 않음)
print(hero.is_alive())      # False
```

**예제 3: 자동 레벨업**
```python
hero = PlayerCharacter("아서", 1)
hero.gain_experience(150)
print(hero.level)                       # 2 (100 XP에 레벨업)
print(hero.get_experience())            # 50 (남은 XP)
print(hero.get_damage_multiplier())     # 1.1 (레벨업 보너스)
```

---

## ✅ 과제

다음 시그니처로 `PlayerCharacter` 클래스를 작성하세요:

```python
class PlayerCharacter:
    def __init__(self, name: str, level: int = 1):
        # name, level: public
        # _experience, _stamina: single underscore (내부 사용)
        # __health, __damage_multiplier: double underscore (강한 보호)
        pass
    
    def get_health(self) -> int: ...
    def get_damage_multiplier(self) -> float: ...
    def get_experience(self) -> int: ...
    def get_stamina(self) -> int: ...
    
    def take_damage(self, amount: int) -> None: ...
    def heal(self, amount: int) -> None: ...
    def gain_experience(self, amount: int) -> None: ...
    def is_alive(self) -> bool: ...
```

**규칙:**
- 체력은 0~100 범위로 유지 (음수 불가, 100 초과 불가)
- XP가 `현재 레벨 × 100`에 도달하면 자동 레벨업 + 데미지 배율 +0.1
- 음수 입력은 `ValueError` 발생
- 모든 메서드 이름은 `snake_case`

---

## 🎪 코드 테스트

```python
# Test 1: 기본 생성
hero = PlayerCharacter("아서", 1)
print(hero.name)              # "아서"
print(hero.level)             # 1
print(hero.get_health())      # 100
print(hero.get_stamina())     # 100

# Test 2: 데미지
hero.take_damage(40)
print(hero.get_health())      # 60

# Test 3: 직접 접근 시도 (실패해야 함!)
try:
    print(hero.__health)
except AttributeError:
    print("✅ __health 직접 접근 차단됨")

# Test 4: Single underscore 접근 (작동해야 함, 하지만 권장 X)
print(hero._experience)       # 0 (Python은 막지 않음)

# Test 5: 자동 레벨업
hero.gain_experience(100)
print(hero.level)             # 2

# Test 6: 검증
try:
    hero.take_damage(-5)
except ValueError:
    print("✅ 음수 검증 작동")
```

---

## 🌟 보너스 챌린지

### 🥉 Easy: `_` vs `__` 직접 비교 실험

다음 코드를 실행하고, 결과를 관찰한 후 **왜** 그런 결과가 나오는지 주석으로 설명하세요:

```python
hero = PlayerCharacter("실험체")

# 실험 1: Single underscore
print(hero._experience)      # 결과: ___, 왜?
hero._experience = 9999      # 결과: ___, 왜?
print(hero._experience)      # 결과: ___, 왜?

# 실험 2: Double underscore  
try:
    print(hero.__health)     # 결과: ___, 왜?
except AttributeError as e:
    print(f"에러: {e}")

# 실험 3: 우회 접근
print(hero._PlayerCharacter__health)  # 결과: ___, 왜 이것은 작동할까?
```

### 🥈 Medium: `_`와 `__`를 한 클래스에서 올바르게 섞기

`PlayerCharacter`의 각 속성을 보고, **왜 그 언더스코어 개수를 선택했는지** 표로 정리하세요:

| 속성 | 언더스코어 | 이유 |
|------|-----------|------|
| `name` | 없음 | (예: 누구나 볼 수 있는 공개 정보) |
| `level` | ? | ? |
| `_experience` | ? | ? |
| `_stamina` | ? | ? |
| `__health` | ? | ? |
| `__damage_multiplier` | ? | ? |

그리고 새로운 속성 `inventory_size`를 추가한다면, 어떤 언더스코어를 쓸지 결정하고 이유를 설명하세요.

### 🥇 Hard: 이름 충돌 시나리오 (인내심 필요!)

> 🔮 **미리보기:** 이 챌린지는 아직 배우지 않은 **상속(inheritance)** 개념을 살짝 사용합니다. 완벽히 이해할 필요는 없어요. 그냥 `class 자식(부모):` 문법은 "자식 클래스가 부모의 기능을 물려받는다"는 뜻이라고만 알고 진행하세요. **`__`가 존재하는 진짜 이유**를 보여주는 데모입니다.

다음 두 가지 시나리오를 코드로 작성하고 결과를 비교하세요:

**시나리오 A: 단일 언더스코어로 깨지는 코드**
```python
class BasicCharacter:
    def __init__(self):
        self._secret_strategy = "공격 우선"  # 부모의 비밀 전략
    
    def reveal(self):
        return self._secret_strategy

class WarriorCharacter(BasicCharacter):
    def __init__(self):
        super().__init__()
        self._secret_strategy = "방어 우선"  # 자식이 같은 이름 사용!

warrior = WarriorCharacter()
print(warrior.reveal())  # 무엇이 출력될까요?
```

**시나리오 B: 이중 언더스코어로 해결**

위 코드에서 `_secret_strategy`를 `__secret_strategy`로 바꾸고 다시 실행하세요. 결과가 어떻게 다른가요?

**질문에 답하세요:**
1. 시나리오 A에서 `warrior.reveal()`이 출력한 값은? 부모의 `reveal()` 메서드가 의도한 동작인가요?
2. 시나리오 B에서는 어떻게 다른가요?
3. `warrior._BasicCharacter__secret_strategy`와 `warrior._WarriorCharacter__secret_strategy`를 각각 출력해보세요. 둘 다 존재하나요?
4. 이 실험에서 **name mangling의 진짜 목적**이 무엇이라고 결론 내릴 수 있나요?

---

## 🤔 생각해보기

코딩이 끝나면 다음 질문에 답해보세요:

1. **`_`가 "약한 보호"라면, 도대체 왜 쓰는 건가요?** Python이 아무것도 막지 않는데요.
2. **`__`가 "강한 보호"이긴 하지만, `_ClassName__attr`로 우회 가능한데 진짜 보호가 맞나요?**
3. 만약 여러분이 게임 회사 보안팀이라면, 핵 방지에 `__`만으로 충분할까요? 부족하다면 무엇이 더 필요할까요?
4. 다음 중 `__`가 더 적절한 것은? 이유와 함께 설명하세요:
   - (a) 사용자 닉네임 (`nickname`)
   - (b) 비밀번호 해시 (`password_hash`)
   - (c) 마지막 로그인 시각 (`last_login`)
   - (d) 내부 세션 토큰 (`session_token`)

---

## 💬 명언과 함께

> *"We are all consenting adults here."*  
> — Guido van Rossum (Python 창시자가 즐겨 인용하는 Python 철학)

Python은 신뢰 기반의 언어입니다. `_`는 "이건 내부용이에요, 부탁이니까 만지지 말아주세요"라는 신사협정이고, `__`는 "정말로 만지면 안 돼요, 실수 방지 장치를 걸어둘게요"입니다. 둘 다 **완벽한 보안이 아니라 의도를 전달하는 도구**예요.

막히면 스레드에 질문 남겨주세요! 천천히 실험하고, 무엇보다 **`_`와 `__`를 직접 비교하면서 차이를 느껴보세요.** 🚀

---
---

# 🎮 Python Practice: A Game Character's Secrets — `_` vs `__`

Hey team! Today we'll fit the last puzzle piece of encapsulation into place.

## 🎯 Your Mission

You're a backend developer for a multiplayer RPG. You're building the player character class, and the security team just made a picky request:

> "Health and damage multiplier — absolutely no direct external manipulation. You know how hackers love memory cheats. But experience and stamina? Don't need to lock those down as hard."

> "So we need 'strong protection' AND 'weak protection' in the same class. Is there a way to do that in Python?"

There is! The answer lies in **how many underscores you use.**

## 📋 The Rules

*What you're given:*
- A character name and starting level
- Game rules: health is 0–100, auto level-up when XP threshold hit

*Core learning objectives:*
1. What `_` (single underscore) means and how it behaves
2. What `__` (double underscore) means and how it behaves
3. **When to use which** — the judgment call

*Constraints:*
- External access to `player.__health` must raise an error
- External access to `player._experience` should **work** (intended behavior!)
- All protected attributes must be readable via getter methods

---

## 🎓 Core Concept: `_` vs `__`

### 🚪 Single Underscore (`_name`) — "Weak Protection"

> "There's a 'Do Not Enter' sign, but the door isn't locked."

```python
class Player:
    def __init__(self):
        self._stamina = 100  # Intended for internal use

p = Player()
print(p._stamina)  # ✅ Works! Python doesn't block it
p._stamina = 999   # ✅ This works too!
```

**Key point:** `_` is **purely a convention**. Python blocks nothing. You're just **asking** other developers "this is internal, please don't touch."

**When to use it?** When something is for internal use, but subclasses or other code in the same module might legitimately need to access it.

---

### 🔒 Double Underscore (`__name`) — "Strong Protection"

> "'Do Not Enter' sign + lock + security system."

```python
class Player:
    def __init__(self):
        self.__health = 100  # This will actually block access!

p = Player()
print(p.__health)  # ❌ AttributeError!
```

**Key point:** Attributes starting with `__` get their names automatically **rewritten** by Python (this is called **name mangling**). `__health` is actually stored as `_Player__health`.

**When to use it?** For data tied to your class's core identity — when you genuinely want to block external access.

---

### 🔍 What's Name Mangling, Exactly?

> "Twisting the name to avoid collisions."

When you write `__health`, Python internally stores it as `_ClassName__health`:

```python
class Player:
    def __init__(self):
        self.__health = 100  # Actual name: _Player__health

p = Player()
print(p.__health)              # ❌ AttributeError
print(p._Player__health)       # 🔓 100 (if you really insist...)
```

**Important:** This is **not a security feature**. If someone really wants in, they can get in. But it **massively reduces the chance of accidental access.**

---

### 🤔 So When Do I Use Which?

| Situation | Use | Why |
|-----------|-----|-----|
| Prefer it hidden, but occasional access OK | `_name` | Flexible |
| Core data that must never be touched externally | `__name` | Strong protection |
| Normal public attribute | `name` | Free access |
| Magic methods | `__name__` | Python reserved (e.g., `__init__`) |

> 💡 **Pythonic motto:** "We are all consenting adults here." — Python is trust-based. Usually `_` is enough. Use `__` only when you really need to block access.

---

## 💡 Examples

**Example 1: Basic creation and access**
```python
hero = PlayerCharacter("Arthur", 5)

# Public attributes — free access
print(hero.name)            # "Arthur"
print(hero.level)           # 5

# Single underscore — accessible but discouraged
print(hero._stamina)        # 100 (works, but using the getter is cleaner)

# Double underscore — direct access blocked
print(hero.__health)        # ❌ AttributeError!
print(hero.get_health())    # ✅ 100 (this is the right way)
```

**Example 2: Damage and healing**
```python
hero = PlayerCharacter("Arthur")
hero.take_damage(30)
print(hero.get_health())    # 70

hero.heal(20)
print(hero.get_health())    # 90

hero.take_damage(500)
print(hero.get_health())    # 0 (no negatives)
print(hero.is_alive())      # False
```

**Example 3: Auto level-up**
```python
hero = PlayerCharacter("Arthur", 1)
hero.gain_experience(150)
print(hero.level)                       # 2 (leveled at 100 XP)
print(hero.get_experience())            # 50 (leftover)
print(hero.get_damage_multiplier())     # 1.1 (level-up bonus)
```

---

## ✅ Your Task

Write a `PlayerCharacter` class with this signature:

```python
class PlayerCharacter:
    def __init__(self, name: str, level: int = 1):
        # name, level: public
        # _experience, _stamina: single underscore (internal use)
        # __health, __damage_multiplier: double underscore (strong protection)
        pass
    
    def get_health(self) -> int: ...
    def get_damage_multiplier(self) -> float: ...
    def get_experience(self) -> int: ...
    def get_stamina(self) -> int: ...
    
    def take_damage(self, amount: int) -> None: ...
    def heal(self, amount: int) -> None: ...
    def gain_experience(self, amount: int) -> None: ...
    def is_alive(self) -> bool: ...
```

**Rules:**
- Health stays in 0–100 (no negatives, no exceeding 100)
- When XP reaches `current_level × 100`, auto level-up + damage multiplier +0.1
- Negative inputs raise `ValueError`
- All method names use `snake_case`

---

## 🎪 Test Your Code

```python
# Test 1: Basic creation
hero = PlayerCharacter("Arthur", 1)
print(hero.name)              # "Arthur"
print(hero.level)             # 1
print(hero.get_health())      # 100
print(hero.get_stamina())     # 100

# Test 2: Damage
hero.take_damage(40)
print(hero.get_health())      # 60

# Test 3: Direct access attempt (should fail!)
try:
    print(hero.__health)
except AttributeError:
    print("✅ __health direct access blocked")

# Test 4: Single underscore access (works, but discouraged)
print(hero._experience)       # 0 (Python doesn't block it)

# Test 5: Auto level-up
hero.gain_experience(100)
print(hero.level)             # 2

# Test 6: Validation
try:
    hero.take_damage(-5)
except ValueError:
    print("✅ Negative validation works")
```

---

## 🌟 Bonus Challenges

### 🥉 Easy: Direct `_` vs `__` Comparison Experiment

Run the following code, observe the results, then explain **why** each happens in a comment:

```python
hero = PlayerCharacter("TestSubject")

# Experiment 1: Single underscore
print(hero._experience)      # Result: ___, why?
hero._experience = 9999      # Result: ___, why?
print(hero._experience)      # Result: ___, why?

# Experiment 2: Double underscore
try:
    print(hero.__health)     # Result: ___, why?
except AttributeError as e:
    print(f"Error: {e}")

# Experiment 3: Backdoor access
print(hero._PlayerCharacter__health)  # Result: ___, why does THIS work?
```

### 🥈 Medium: Mixing `_` and `__` Correctly in One Class

Look at each attribute in `PlayerCharacter` and fill in this table explaining **why you chose that underscore count**:

| Attribute | Underscores | Why |
|-----------|-------------|-----|
| `name` | None | (e.g., public info anyone can see) |
| `level` | ? | ? |
| `_experience` | ? | ? |
| `_stamina` | ? | ? |
| `__health` | ? | ? |
| `__damage_multiplier` | ? | ? |

Then, if you were to add a new attribute `inventory_size`, which underscore style would you choose, and why?

### 🥇 Hard: The Name Collision Scenario (patience required!)

> 🔮 **Preview alert:** This challenge briefly uses **inheritance** — a concept you haven't learned yet. You don't need to fully understand it. Just know that `class Child(Parent):` syntax means "Child class inherits Parent's features." This demo shows the **real reason `__` exists**.

Write code for the two scenarios below and compare results:

**Scenario A: Single underscore breaks the code**
```python
class BasicCharacter:
    def __init__(self):
        self._secret_strategy = "Attack first"  # Parent's secret strategy
    
    def reveal(self):
        return self._secret_strategy

class WarriorCharacter(BasicCharacter):
    def __init__(self):
        super().__init__()
        self._secret_strategy = "Defense first"  # Child uses same name!

warrior = WarriorCharacter()
print(warrior.reveal())  # What gets printed?
```

**Scenario B: Double underscore fixes it**

Change `_secret_strategy` to `__secret_strategy` in the above code and run it again. How does the result differ?

**Answer these:**
1. In Scenario A, what did `warrior.reveal()` print? Is that what the parent's `reveal()` method intended?
2. In Scenario B, how is it different?
3. Try printing both `warrior._BasicCharacter__secret_strategy` and `warrior._WarriorCharacter__secret_strategy`. Do they both exist?
4. From this experiment, what would you say is the **real purpose** of name mangling?

---

## 🤔 Think About It

After you finish coding, reflect on these:

1. **If `_` is "weak protection," why use it at all?** Python blocks nothing.
2. **If `__` is "strong protection" but `_ClassName__attr` is a backdoor, is it really protection?**
3. If you were on a game company's security team, would `__` alone be enough to prevent cheating? If not, what else would you need?
4. Which of these is `__` more appropriate for? Explain with reasoning:
   - (a) User nickname (`nickname`)
   - (b) Password hash (`password_hash`)
   - (c) Last login time (`last_login`)
   - (d) Internal session token (`session_token`)

---

## 💬 A Quote to Remember

> *"We are all consenting adults here."*  
> — Guido van Rossum (the Python creator's favorite philosophy)

Python is a trust-based language. `_` is the gentleman's agreement saying "this is internal, please don't touch." `__` is "you really shouldn't touch this — I'll add a safety latch." Neither is perfect security; both are **tools for communicating intent**.

Drop questions in the thread if you get stuck! Experiment slowly, and above all — **directly compare `_` and `__` to feel the difference yourself.** 🚀
