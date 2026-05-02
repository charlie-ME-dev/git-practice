# 🐍 Python 연습: 기본값 파라미터(Default Parameters) 마스터하기!

여러분, 안녕하세요! 오늘은 함수를 훨씬 더 유연하고 편리하게 만드는 기술을 배워봅시다.

---

## 💡 개념 먼저 이해하기

지금까지 배운 함수는 이렇게 생겼죠:

```python
def greet(name, greeting):
    return f"{greeting}, {name}!"

greet("Alice", "Hello")   # 반드시 두 값을 모두 전달해야 함
```

만약 `greeting`을 매번 쓰는 게 귀찮다면? 대부분 `"Hello"`를 쓰고 싶다면?

**Default parameters**를 사용하면 이렇게 할 수 있어요:

```python
def greet(name, greeting="Hello"):   # ← greeting의 기본값은 "Hello"
    return f"{greeting}, {name}!"

greet("Alice")            # → "Hello, Alice!"   (기본값 사용)
greet("Bob", "Hi")        # → "Hi, Bob!"        (기본값 덮어쓰기)
```

값을 넘기면 그 값을 사용하고, 안 넘기면 기본값을 사용합니다!

---

## 📌 규칙 한 가지 — 꼭 기억하세요!

기본값이 있는 파라미터는 **반드시 오른쪽에** 놓아야 합니다.

```python
# ✅ 올바른 순서
def func(a, b, c=10):      pass
def func(a, b=5, c=10):    pass
def func(a=1, b=5, c=10):  pass

# ❌ 오류! 기본값 없는 파라미터가 오른쪽에 있으면 안 됨
def func(a=1, b):          pass   # SyntaxError!
```

왜냐하면 Python은 값을 왼쪽부터 순서대로 채우기 때문이에요.

---

## 🏢 실전 시나리오

여러분은 스타트업에 입사한 주니어 개발자입니다! 오늘 팀장님이 이런 미션을 주셨어요:

> "우리 서비스에서 자주 쓰이는 유틸리티 함수들을 만들어줘. 그런데 사용자가 매번 모든 값을 입력하기 귀찮지 않도록, 자주 쓰는 값은 기본값으로 설정해줘!"

실제로 이런 패턴은 실무에서 매우 흔합니다:
• **카카오톡 알림**: 수신자만 입력하면 나머지(소리, 진동 등)는 기본값 적용
• **쇼핑몰 결제**: 상품 가격만 넣으면 기본 배송비 자동 적용
• **게임 리더보드**: 점수와 이름만 넣으면 기본 라벨("Player") 자동 설정

---

## ✅ 과제: 함수 4개 완성하기

### 📝 함수 1: `greet_user`

사용자를 환영하는 메시지를 만드는 함수입니다.

```python
def greet_user(name: str, greeting: str = "Hello") -> str:
```

| 호출 | 반환값 |
|------|--------|
| `greet_user("Alice")` | `"Hello, Alice!"` |
| `greet_user("Bob", "Hi")` | `"Hi, Bob!"` |
| `greet_user("지수", "안녕하세요")` | `"안녕하세요, 지수!"` |
| `greet_user(greeting="Hey", name="Sam")` | `"Hey, Sam!"` |

💡 **힌트:** f-string으로 `"{greeting}, {name}!"` 형태를 만들면 돼요.

---

### 📝 함수 2: `calculate_shipping`

쇼핑몰 결제 금액을 계산하는 함수입니다. 할인율과 배송비에 기본값이 있어요.

```python
def calculate_shipping(price: float, discount_rate: float = 0.0, shipping_fee: float = 3000) -> float:
```

계산 공식:
```
할인된 가격 = price × (1 - discount_rate)
최종 금액   = 할인된 가격 + shipping_fee
```

| 호출 | 반환값 | 설명 |
|------|--------|------|
| `calculate_shipping(10000)` | `13000.0` | 할인 없음, 기본 배송비 3000 |
| `calculate_shipping(10000, 0.1)` | `12000.0` | 10% 할인, 기본 배송비 |
| `calculate_shipping(10000, 0.1, 0)` | `9000.0` | 10% 할인, 무료 배송 |
| `calculate_shipping(50000, shipping_fee=0)` | `50000.0` | 할인 없음, 무료 배송 |
| `calculate_shipping(20000, 0.2, 2500)` | `18500.0` | 20% 할인, 배송비 2500 |

💡 **힌트:** `discount_rate=0.0`이면 `price × (1 - 0.0) = price` 그대로예요.

---

### 📝 함수 3: `format_leaderboard_entry`

게임 리더보드 항목을 문자열로 만드는 함수입니다.

```python
def format_leaderboard_entry(rank: int, name: str, score: int, label: str = "Player") -> str:
```

출력 형식: `"#{rank} [{label}] {name} — {score}pts"`

| 호출 | 반환값 |
|------|--------|
| `format_leaderboard_entry(1, "Alice", 9800)` | `"#1 [Player] Alice — 9800pts"` |
| `format_leaderboard_entry(2, "Bob", 8500, "VIP")` | `"#2 [VIP] Bob — 8500pts"` |
| `format_leaderboard_entry(3, "지수", 7200, "챌린저")` | `"#3 [챌린저] 지수 — 7200pts"` |

💡 **힌트:** `—`는 일반 하이픈(`-`)이 아니라 긴 대시(`—`)예요. 복사해서 사용하세요!

---

### 📝 함수 4: `repeat_message`

메시지를 여러 번 반복하는 함수입니다. 반복 횟수와 구분자에 기본값이 있어요.

```python
def repeat_message(message: str, times: int = 3, separator: str = " | ") -> str:
```

| 호출 | 반환값 |
|------|--------|
| `repeat_message("Go!")` | `"Go! \| Go! \| Go!"` |
| `repeat_message("Go!", 2)` | `"Go! \| Go!"` |
| `repeat_message("Go!", 4, " / ")` | `"Go! / Go! / Go! / Go!"` |
| `repeat_message("Hi", 1, "---")` | `"Hi"` |
| `repeat_message("야호", 3, "🎉")` | `"야호🎉야호🎉야호"` |

💡 **힌트:** 구분자는 메시지들 **사이**에만 붙어요. 마지막 메시지 뒤에는 붙지 않아요!

---

## 🎪 코드 테스트

```python
# 테스트 1 — greet_user
print(greet_user("Alice"))                       # Hello, Alice!
print(greet_user("Bob", "Hi"))                   # Hi, Bob!
print(greet_user("지수", "안녕하세요"))             # 안녕하세요, 지수!
print(greet_user(greeting="Hey", name="Sam"))    # Hey, Sam!

# 테스트 2 — calculate_shipping
print(calculate_shipping(10000))                 # 13000.0
print(calculate_shipping(10000, 0.1))            # 12000.0
print(calculate_shipping(10000, 0.1, 0))         # 9000.0
print(calculate_shipping(50000, shipping_fee=0)) # 50000.0
print(calculate_shipping(20000, 0.2, 2500))      # 18500.0

# 테스트 3 — format_leaderboard_entry
print(format_leaderboard_entry(1, "Alice", 9800))          # #1 [Player] Alice — 9800pts
print(format_leaderboard_entry(2, "Bob", 8500, "VIP"))     # #2 [VIP] Bob — 8500pts
print(format_leaderboard_entry(3, "지수", 7200, "챌린저"))  # #3 [챌린저] 지수 — 7200pts

# 테스트 4 — repeat_message
print(repeat_message("Go!"))                     # Go! | Go! | Go!
print(repeat_message("Go!", 2))                  # Go! | Go!
print(repeat_message("Go!", 4, " / "))           # Go! / Go! / Go! / Go!
print(repeat_message("Hi", 1, "---"))            # Hi
print(repeat_message("야호", 3, "🎉"))            # 야호🎉야호🎉야호
```

---

## 🤔 생각해보기

코딩 전에 잠깐 생각해보세요:

1. `greet_user("Alice")`처럼 값을 하나만 넘기면 Python은 어떻게 어느 파라미터에 넣을지 결정할까요?
2. `calculate_shipping(50000, shipping_fee=0)` 처럼 이름을 명시하면 어떤 장점이 있을까요?
3. `repeat_message("Hi", 1, "---")`의 결과가 `"Hi"`인 이유가 무엇일까요?

막히면 스레드에 질문을 남겨주세요! 목표는 끝내는 것이 아니라 배우는 것입니다. 🌱

행운을 빕니다! 🚀

---
---

# 🐍 Python Practice: Master Default Parameters!

Hey team! Today we're leveling up our functions to be smarter and more convenient to use.

---

## 💡 Understand the Concept First

Functions you've written so far look like this:

```python
def greet(name, greeting):
    return f"{greeting}, {name}!"

greet("Alice", "Hello")   # Must pass both values every time
```

What if `"Hello"` is the most common greeting and you're tired of typing it every time?

**Default parameters** let you do this:

```python
def greet(name, greeting="Hello"):   # ← "Hello" is the default
    return f"{greeting}, {name}!"

greet("Alice")            # → "Hello, Alice!"   (default used)
greet("Bob", "Hi")        # → "Hi, Bob!"        (default overridden)
```

If you pass a value, it uses that value. If you don't, it uses the default!

---

## 📌 One Rule — Remember This!

Parameters with defaults must always go on the **right side**.

```python
# ✅ Correct order
def func(a, b, c=10):      pass
def func(a, b=5, c=10):    pass
def func(a=1, b=5, c=10):  pass

# ❌ Error! Non-default parameter cannot follow default parameter
def func(a=1, b):          pass   # SyntaxError!
```

Python fills in values left-to-right, so defaults must come last.

---

## 🏢 Real-World Scenario

You just joined a startup as a junior developer! Your team lead gives you this mission:

> "Build some utility functions for our service. But make them user-friendly — set sensible defaults so callers don't have to pass every single argument every time!"

This pattern is everywhere in real software:
• **Push notifications**: Just pass the recipient; sound, vibration, etc. use defaults
• **E-commerce checkout**: Pass the item price; default shipping fee is applied automatically
• **Game leaderboards**: Pass name and score; default label ("Player") fills in automatically

---

## ✅ Your Tasks: Complete 4 Functions

### 📝 Function 1: `greet_user`

Build a greeting message for a user.

```python
def greet_user(name: str, greeting: str = "Hello") -> str:
```

| Call | Return Value |
|------|-------------|
| `greet_user("Alice")` | `"Hello, Alice!"` |
| `greet_user("Bob", "Hi")` | `"Hi, Bob!"` |
| `greet_user("지수", "안녕하세요")` | `"안녕하세요, 지수!"` |
| `greet_user(greeting="Hey", name="Sam")` | `"Hey, Sam!"` |

💡 **Hint:** Use an f-string to build `"{greeting}, {name}!"`.

---

### 📝 Function 2: `calculate_shipping`

Calculate the final checkout amount for an online store.

```python
def calculate_shipping(price: float, discount_rate: float = 0.0, shipping_fee: float = 3000) -> float:
```

Formula:
```
discounted_price = price × (1 - discount_rate)
final_amount     = discounted_price + shipping_fee
```

| Call | Return | Notes |
|------|--------|-------|
| `calculate_shipping(10000)` | `13000.0` | No discount, default shipping 3000 |
| `calculate_shipping(10000, 0.1)` | `12000.0` | 10% off, default shipping |
| `calculate_shipping(10000, 0.1, 0)` | `9000.0` | 10% off, free shipping |
| `calculate_shipping(50000, shipping_fee=0)` | `50000.0` | No discount, free shipping |
| `calculate_shipping(20000, 0.2, 2500)` | `18500.0` | 20% off, shipping 2500 |

💡 **Hint:** When `discount_rate=0.0`, `price × (1 - 0.0) = price` — no change!

---

### 📝 Function 3: `format_leaderboard_entry`

Format a game leaderboard entry as a string.

```python
def format_leaderboard_entry(rank: int, name: str, score: int, label: str = "Player") -> str:
```

Format: `"#{rank} [{label}] {name} — {score}pts"`

| Call | Return Value |
|------|-------------|
| `format_leaderboard_entry(1, "Alice", 9800)` | `"#1 [Player] Alice — 9800pts"` |
| `format_leaderboard_entry(2, "Bob", 8500, "VIP")` | `"#2 [VIP] Bob — 8500pts"` |
| `format_leaderboard_entry(3, "지수", 7200, "챌린저")` | `"#3 [챌린저] 지수 — 7200pts"` |

💡 **Hint:** The `—` is an em dash, not a regular hyphen (`-`). Copy it from here!

---

### 📝 Function 4: `repeat_message`

Repeat a message multiple times with a separator between each.

```python
def repeat_message(message: str, times: int = 3, separator: str = " | ") -> str:
```

| Call | Return Value |
|------|-------------|
| `repeat_message("Go!")` | `"Go! \| Go! \| Go!"` |
| `repeat_message("Go!", 2)` | `"Go! \| Go!"` |
| `repeat_message("Go!", 4, " / ")` | `"Go! / Go! / Go! / Go!"` |
| `repeat_message("Hi", 1, "---")` | `"Hi"` |
| `repeat_message("야호", 3, "🎉")` | `"야호🎉야호🎉야호"` |

💡 **Hint:** The separator goes **between** messages, not after the last one!

---

## 🎪 Test Your Code

```python
# Test 1 — greet_user
print(greet_user("Alice"))                       # Hello, Alice!
print(greet_user("Bob", "Hi"))                   # Hi, Bob!
print(greet_user("지수", "안녕하세요"))             # 안녕하세요, 지수!
print(greet_user(greeting="Hey", name="Sam"))    # Hey, Sam!

# Test 2 — calculate_shipping
print(calculate_shipping(10000))                 # 13000.0
print(calculate_shipping(10000, 0.1))            # 12000.0
print(calculate_shipping(10000, 0.1, 0))         # 9000.0
print(calculate_shipping(50000, shipping_fee=0)) # 50000.0
print(calculate_shipping(20000, 0.2, 2500))      # 18500.0

# Test 3 — format_leaderboard_entry
print(format_leaderboard_entry(1, "Alice", 9800))          # #1 [Player] Alice — 9800pts
print(format_leaderboard_entry(2, "Bob", 8500, "VIP"))     # #2 [VIP] Bob — 8500pts
print(format_leaderboard_entry(3, "지수", 7200, "챌린저"))  # #3 [챌린저] 지수 — 7200pts

# Test 4 — repeat_message
print(repeat_message("Go!"))                     # Go! | Go! | Go!
print(repeat_message("Go!", 2))                  # Go! | Go!
print(repeat_message("Go!", 4, " / "))           # Go! / Go! / Go! / Go!
print(repeat_message("Hi", 1, "---"))            # Hi
print(repeat_message("야호", 3, "🎉"))            # 야호🎉야호🎉야호
```

---

## 🤔 Think About It

Before you start, sketch out your approach:

1. When you call `greet_user("Alice")` with only one argument, how does Python decide which parameter it belongs to?
2. What advantage does writing `calculate_shipping(50000, shipping_fee=0)` give you over `calculate_shipping(50000, 0, 0)`?
3. Why does `repeat_message("Hi", 1, "---")` return just `"Hi"` with nothing else?

Drop your questions in the thread if you get stuck! Remember, the goal is to learn, not just to finish. 🌱

Good luck! 🚀
