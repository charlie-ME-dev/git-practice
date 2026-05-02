# ☕ Python 연습: 카페 주문 시스템 만들기!

여러분, 안녕하세요! 오늘은 Python의 중요한 개념인 **변수의 범위(Scope)** 를 카페 주문 시스템을 만들면서 익혀볼 거예요.

---

## 🏢 실전 시나리오

여러분은 작은 카페의 주니어 개발자입니다! 사장님이 주문 관리 시스템을 만들어 달라고 했어요. 메뉴 가격 조회, 할인 계산, 주문 접수, 하루 마감 초기화까지 — 네 가지 기능을 함수로 구현해야 합니다.

그런데 이 시스템을 잘 만들려면 **어떤 데이터를 함수 안에서만 쓰고, 어떤 데이터를 함수 밖에서 공유할지** 이해해야 합니다. 바로 이게 오늘의 핵심 개념인 **스코프(Scope)** 입니다!

---

## 📚 핵심 개념: 스코프(Scope)란?

스코프란 **변수가 어디서 보이고 어디서 안 보이는지**를 결정하는 규칙이에요.

### 🏠 지역 변수 (Local Variable)
함수 **안에서** 만들어진 변수입니다. 함수가 끝나면 사라져요.

```python
def make_coffee():
    temperature = 90   # 👈 지역 변수 — 이 함수 안에서만 존재
    print(temperature)

make_coffee()       # 90 출력
print(temperature)  # ❌ NameError! 함수 밖에서는 보이지 않아요
```

### 🌍 전역 변수 (Global Variable)
함수 **밖에서** 만들어진 변수입니다. 프로그램 어디서든 읽을 수 있어요.

```python
cafe_name = "파이썬 카페"   # 👈 전역 변수

def greet_customer():
    print(f"어서오세요, {cafe_name}입니다!")  # ✅ 읽기는 OK

greet_customer()   # 어서오세요, 파이썬 카페입니다!
```

### 🔑 global 키워드
함수 안에서 전역 변수의 값을 **변경**하려면 `global` 키워드가 필요해요.

```python
visitor_count = 0   # 전역 변수

def welcome_customer():
    global visitor_count        # 👈 "나는 전역 변수를 수정할 거야!"
    visitor_count += 1
    print(f"손님 {visitor_count}번째 방문!")

welcome_customer()   # 손님 1번째 방문!
welcome_customer()   # 손님 2번째 방문!
print(visitor_count) # 2
```

> ⚠️ **중요한 규칙:** `global` 없이 함수 안에서 전역 변수에 값을 대입하면, Python은 새로운 **지역 변수**를 만들어버려요! 전역 변수는 그대로입니다.

```python
score = 100

def try_to_change():
    score = 999      # ❌ global 없음 → 지역 변수 score가 새로 생긴 것!
    print(score)     # 999 (지역 변수)

try_to_change()
print(score)         # 100 (전역 변수는 그대로!)
```

---

## 🗂️ 시스템 전역 변수

이 시스템에서는 다음 전역 변수들을 미리 준비해드립니다. 절대 수정하지 마세요!

```python
MENU = {
    "아메리카노": 4500,
    "카페라떼": 5000,
    "카푸치노": 5500,
    "녹차라떼": 5500,
    "초코라떼": 6000,
}
daily_revenue = 0   # 오늘 하루 총 매출 (원)
total_orders = 0    # 오늘 하루 총 주문 수량
```

---

## ✅ 과제: 네 가지 함수 구현하기

---

### ① `get_item_price(item_name)`

**메뉴판에서 가격 조회하기**

전역 변수 `MENU`에서 `item_name`에 해당하는 가격을 찾아 반환하세요.

```
입력: "아메리카노"
출력: 4500

입력: "초코라떼"
출력: 6000
```

> 💡 힌트: 이 함수는 전역 변수를 **읽기만** 합니다. `global` 키워드가 필요할까요?

---

### ② `calculate_discounted_price(price, discount_rate)`

**할인된 가격 계산하기**

원래 가격(`price`)에서 할인율(`discount_rate`)만큼 할인된 최종 가격을 반환하세요. 모든 계산은 **함수 안에서만** 이루어집니다.

```
입력: price=5000, discount_rate=0.1    (10% 할인)
출력: 4500

입력: price=6000, discount_rate=0.2    (20% 할인)
출력: 4800

입력: price=4500, discount_rate=0.0    (할인 없음)
출력: 4500
```

> 💡 힌트: 이 함수는 전역 변수를 전혀 사용하지 않아요. 모든 변수가 지역 변수입니다. 결과를 `int()`로 변환해서 반환하세요.

---

### ③ `place_order(item_name, quantity)`

**주문 접수하고 매출 기록하기**

주문을 받아서 전역 변수 `daily_revenue`와 `total_orders`를 업데이트하고, 주문 내역 문자열을 반환하세요.

계산 방법:
- `order_total` = `MENU[item_name]` × `quantity`
- `daily_revenue` += `order_total`
- `total_orders` += `quantity`

```
입력: item_name="아메리카노", quantity=2
출력: "아메리카노 x2 = 9000원"
전역 변수 변화: daily_revenue=9000, total_orders=2

이어서 입력: item_name="카페라떼", quantity=1
출력: "카페라떼 x1 = 5000원"
전역 변수 변화: daily_revenue=14000, total_orders=3
```

> 💡 힌트: 이 함수는 전역 변수를 **수정**합니다. `global` 키워드가 필요해요!

---

### ④ `reset_daily_sales()`

**하루 마감 — 매출 초기화하기**

영업이 끝났어요! `daily_revenue`와 `total_orders`를 모두 `0`으로 초기화하고, 완료 메시지를 반환하세요.

```
실행 후:
daily_revenue = 0
total_orders = 0
반환값: "하루 매출이 초기화되었습니다."
```

> 💡 힌트: 두 개의 전역 변수를 동시에 수정해야 해요. `global` 선언에 변수를 어떻게 나열할까요?

---

## 🎪 테스트 코드

```python
# 테스트 1: 가격 조회
print(get_item_price("아메리카노"))   # 예상: 4500
print(get_item_price("카페라떼"))     # 예상: 5000
print(get_item_price("초코라떼"))     # 예상: 6000

# 테스트 2: 할인 계산
print(calculate_discounted_price(5000, 0.1))  # 예상: 4500
print(calculate_discounted_price(6000, 0.2))  # 예상: 4800
print(calculate_discounted_price(4500, 0.0))  # 예상: 4500

# 테스트 3: 주문 접수
print(place_order("아메리카노", 2))   # 예상: 아메리카노 x2 = 9000원
print(place_order("카페라떼", 1))     # 예상: 카페라떼 x1 = 5000원
print(f"오늘 매출: {daily_revenue}원, 총 주문: {total_orders}잔")
# 예상: 오늘 매출: 14000원, 총 주문: 3잔

# 테스트 4: 하루 마감
print(reset_daily_sales())            # 예상: 하루 매출이 초기화되었습니다.
print(f"초기화 후 매출: {daily_revenue}원, 주문: {total_orders}잔")
# 예상: 초기화 후 매출: 0원, 주문: 0잔
```

---

## 🤔 생각해보기

1. `get_item_price()`에서는 `global MENU`를 쓰지 않아도 `MENU`를 읽을 수 있어요. 왜 그럴까요?
2. `calculate_discounted_price()`의 `discount_amount`는 함수가 끝나면 어떻게 될까요?
3. `place_order()`에서 `global`을 깜빡하면 어떤 일이 생길까요? 직접 지워보고 실행해보세요!
4. 전역 변수를 함수에서 자유롭게 바꿀 수 있다면 편리할 것 같은데, 왜 `global`을 명시적으로 써야 할까요?

막히면 스레드에 질문을 남겨주세요! 목표는 빨리 끝내는 것이 아니라 스코프를 제대로 이해하는 것입니다. ☕🚀

---
---

# ☕ Python Practice: Build a Café Order System!

Hey team! Today we're learning one of Python's most important concepts — **variable scope** — by building a café order management system.

---

## 🏢 Real-World Scenario

You're a junior developer at a small café! The owner wants an order management system. You need to build four functions: look up menu prices, calculate discounts, record orders, and reset daily sales at closing time.

To build this well, you need to understand **which data lives only inside a function, and which data is shared across the whole program**. That's exactly what **scope** is about!

---

## 📚 Core Concept: What Is Scope?

Scope is the rule that determines **where a variable can be seen and used**.

### 🏠 Local Variable
Created **inside** a function. It disappears when the function ends.

```python
def make_coffee():
    temperature = 90   # 👈 local variable — lives only inside this function
    print(temperature)

make_coffee()       # prints 90
print(temperature)  # ❌ NameError! can't see it outside the function
```

### 🌍 Global Variable
Created **outside** any function. Can be read from anywhere in the program.

```python
cafe_name = "Python Café"   # 👈 global variable

def greet_customer():
    print(f"Welcome to {cafe_name}!")  # ✅ reading is fine

greet_customer()   # Welcome to Python Café!
```

### 🔑 The global Keyword
To **change** a global variable from inside a function, you need the `global` keyword.

```python
visitor_count = 0   # global variable

def welcome_customer():
    global visitor_count        # 👈 "I'm going to modify the global one!"
    visitor_count += 1
    print(f"Customer #{visitor_count}!")

welcome_customer()   # Customer #1!
welcome_customer()   # Customer #2!
print(visitor_count) # 2
```

> ⚠️ **Key rule:** Without `global`, assigning a value inside a function creates a **new local variable** — the global one is left untouched.

```python
score = 100

def try_to_change():
    score = 999      # ❌ no global → this creates a brand new LOCAL variable
    print(score)     # 999 (the local one)

try_to_change()
print(score)         # 100 (the global is unchanged!)
```

---

## 🗂️ System Global Variables

These globals are provided for you. Do not rename or delete them!

```python
MENU = {
    "아메리카노": 4500,
    "카페라떼": 5000,
    "카푸치노": 5500,
    "녹차라떼": 5500,
    "초코라떼": 6000,
}
daily_revenue = 0   # today's total revenue (won)
total_orders = 0    # today's total number of drinks ordered
```

---

## ✅ Your Tasks: Four Functions

---

### ① `get_item_price(item_name)`

**Look up a price from the menu**

Find and return the price of `item_name` from the global `MENU` dictionary.

```
Input:  "아메리카노"
Output: 4500

Input:  "초코라떼"
Output: 6000
```

> 💡 Hint: This function only **reads** a global variable. Does it need the `global` keyword?

---

### ② `calculate_discounted_price(price, discount_rate)`

**Calculate a discounted price**

Return the final price after applying `discount_rate` to the original `price`. All work stays inside this function.

```
Input:  price=5000, discount_rate=0.1    (10% off)
Output: 4500

Input:  price=6000, discount_rate=0.2    (20% off)
Output: 4800

Input:  price=4500, discount_rate=0.0    (no discount)
Output: 4500
```

> 💡 Hint: This function uses no global variables at all — everything is local. Return the result as `int()`.

---

### ③ `place_order(item_name, quantity)`

**Record an order and update the running totals**

Accept an order, update `daily_revenue` and `total_orders`, and return an order summary string.

How to calculate:
- `order_total` = `MENU[item_name]` × `quantity`
- `daily_revenue` += `order_total`
- `total_orders` += `quantity`

```
Input:  item_name="아메리카노", quantity=2
Output: "아메리카노 x2 = 9000원"
Globals updated: daily_revenue=9000, total_orders=2

Next input: item_name="카페라떼", quantity=1
Output: "카페라떼 x1 = 5000원"
Globals updated: daily_revenue=14000, total_orders=3
```

> 💡 Hint: This function **modifies** global variables. You'll need the `global` keyword!

---

### ④ `reset_daily_sales()`

**End of day — reset everything**

Closing time! Reset both `daily_revenue` and `total_orders` to `0`, and return a completion message.

```
After calling this function:
daily_revenue = 0
total_orders = 0
Return value: "하루 매출이 초기화되었습니다."
```

> 💡 Hint: You need to modify two global variables at once. How do you list multiple variables in one `global` statement?

---

## 🎪 Test Your Code

```python
# Test 1: price lookup
print(get_item_price("아메리카노"))   # Expected: 4500
print(get_item_price("카페라떼"))     # Expected: 5000
print(get_item_price("초코라떼"))     # Expected: 6000

# Test 2: discount calculation
print(calculate_discounted_price(5000, 0.1))  # Expected: 4500
print(calculate_discounted_price(6000, 0.2))  # Expected: 4800
print(calculate_discounted_price(4500, 0.0))  # Expected: 4500

# Test 3: placing orders
print(place_order("아메리카노", 2))   # Expected: 아메리카노 x2 = 9000원
print(place_order("카페라떼", 1))     # Expected: 카페라떼 x1 = 5000원
print(f"Today's revenue: {daily_revenue}원, Total drinks: {total_orders}")
# Expected: Today's revenue: 14000원, Total drinks: 3

# Test 4: end of day reset
print(reset_daily_sales())            # Expected: 하루 매출이 초기화되었습니다.
print(f"After reset: {daily_revenue}원, {total_orders} drinks")
# Expected: After reset: 0원, 0 drinks
```

---

## 🤔 Think About It

1. `get_item_price()` can read `MENU` without writing `global MENU`. Why does that work?
2. What happens to the `discount_amount` variable in `calculate_discounted_price()` after the function returns?
3. What happens if you forget `global` in `place_order()`? Try removing it and running the code!
4. If Python could freely modify global variables from functions without any keyword, what problems might that cause?

Drop your questions in the thread if you get stuck! The goal is to genuinely understand scope, not just pass the tests. ☕🚀
