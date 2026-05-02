# 📦 Python 연습: 창고 재고 관리 시스템 만들기!

여러분, 안녕하세요! 오늘은 실제 물류 회사에서 사용하는 재고 관리 프로그램을 만들어볼 거예요.

## 🎯 미션

여러분은 온라인 쇼핑몰의 주니어 백엔드 개발자입니다! 물류 팀장이 이렇게 요청했어요:

> "창고 재고 시스템이 필요해요. 새 물건이 들어오면 앞에 쌓고, 오래된 물건부터 먼저 출고해야 해요. 재고가 3개 미만이면 경고도 띄워줘야 하고요!"

리스트(list)의 `insert()`와 `pop()`을 활용해서 이 시스템을 구현해봅시다.

## 📋 만들어야 할 함수들

### 1️⃣ `restock(inventory, item)`
새 물건을 재고 리스트의 **맨 앞**에 추가합니다.
• 추가 후: `"[item] 입고 완료! 현재 재고: [inventory]"` 출력

### 2️⃣ `ship(inventory)`
재고 리스트의 **맨 뒤** 물건을 꺼내서 출고합니다.
• 재고가 있으면: 꺼낸 물건 이름을 반환하고 `"[item] 출고 완료!"` 출력
• 재고가 없으면: `"출고 실패: 재고가 없습니다."` 출력 후 `None` 반환

### 3️⃣ `check_stock(inventory, threshold)`
재고 수량을 확인하고 부족하면 경고를 출력합니다.
• `threshold`의 기본값은 `3`
• 재고가 `threshold`보다 적으면: `"⚠️ 재고 부족 경고! 현재 [n]개 남음 (기준: [threshold]개)"` 출력
• 재고가 충분하면: `"✅ 재고 양호. 현재 [n]개 보유 중"` 출력

### 4️⃣ `get_oldest(inventory)`
가장 오래된 물건(리스트 **맨 뒤** 항목)의 이름을 반환합니다.
• 재고가 있으면: 맨 뒤 항목 반환
• 재고가 없으면: `"재고가 없습니다."` 출력 후 `None` 반환

## 💡 예제

```python
inventory = []

restock(inventory, "사과")
restock(inventory, "바나나")
restock(inventory, "딸기")

# 현재 재고: ["딸기", "바나나", "사과"]
# 새 물건이 앞에 쌓이므로 "사과"가 가장 오래된 물건

print(get_oldest(inventory))    # 사과
print(ship(inventory))          # 사과 출고 완료! / 반환: "사과"
check_stock(inventory, 3)       # ⚠️ 재고 부족 경고! 현재 2개 남음 (기준: 3개)
```

## 🎓 알아야 할 것

코딩 시작 전, 다음 개념을 떠올려보세요:
• `insert(0, item)` — 리스트 맨 앞에 항목 추가
• `pop()` — 리스트 맨 뒤 항목을 꺼내서 반환 (리스트에서 제거됨)
• `len()` — 리스트 길이 확인
• 인덱싱 — `inventory[-1]`은 마지막 항목

## ✅ 과제

아래 함수 시그니처를 사용해서 코드를 완성하세요:

```python
def restock(inventory: list, item: str) -> None:
    # TODO: 여기에 코드 작성
    pass

def ship(inventory: list) -> str:
    # TODO: 여기에 코드 작성
    pass

def check_stock(inventory: list, threshold: int = 3) -> None:
    # TODO: 여기에 코드 작성
    pass

def get_oldest(inventory: list) -> str:
    # TODO: 여기에 코드 작성
    pass
```

## 🎪 코드 테스트

```python
# 테스트 1: 입고 및 재고 확인
inventory = []
restock(inventory, "사과")
restock(inventory, "바나나")
restock(inventory, "딸기")
restock(inventory, "포도")
restock(inventory, "수박")
check_stock(inventory, 3)
# 예상: ✅ 재고 양호. 현재 5개 보유 중

# 테스트 2: 가장 오래된 물건 확인
print(get_oldest(inventory))
# 예상: 사과  (가장 먼저 들어온 물건)

# 테스트 3: 출고
print(ship(inventory))
print(ship(inventory))
# 예상: 사과 출고 완료! / 반환: "사과"
# 예상: 바나나 출고 완료! / 반환: "바나나"

# 테스트 4: 재고 부족 경고
check_stock(inventory, 3)
# 예상: ⚠️ 재고 부족 경고! 현재 3개 남음 (기준: 3개) 아니면 양호?
# 🤔 threshold가 3이고 재고가 3개면 어떻게 될까요?

# 테스트 5: 빈 창고
empty = []
print(ship(empty))
print(get_oldest(empty))
# 예상: 출고 실패: 재고가 없습니다. / None
# 예상: 재고가 없습니다. / None
```

## 🌟 보너스 챌린지

기본 과제를 다 끝냈나요? 단계별로 도전해봅시다!

---

### 🥉 Easy: `show_inventory(inventory)`

현재 재고를 앞에서부터 번호와 함께 출력하는 함수를 만드세요.
입고 순서(최신 → 오래된 순)로 보여줘야 합니다.

```
예상 출력 (inventory = ["수박", "포도", "딸기", "바나나", "사과"]):

===== 현재 재고 현황 =====
1. 수박  (최신)
2. 포도
3. 딸기
4. 바나나
5. 사과  (가장 오래됨)
총 5개 보유 중
=========================
```

---

### 🥈 Medium: `bulk_restock(inventory, items)`

물건 리스트를 한 번에 입고하는 함수를 만드세요.
`items` 리스트의 **순서대로** 하나씩 `restock()`을 호출해야 합니다.

```python
bulk_restock(inventory, ["키위", "망고", "파인애플"])
# "키위"를 먼저 입고, 그 다음 "망고", 마지막으로 "파인애플"
# 결과: ["파인애플", "망고", "키위", ...기존재고...]
```

그 다음, 입고 후 자동으로 `check_stock()`이 실행되도록 만드세요.

---

### 🥇 Hard: `ship_until_low(inventory, threshold)`

재고가 `threshold`개가 될 때까지 계속 출고하는 함수를 만드세요.

```python
inventory = ["수박", "포도", "딸기", "바나나", "사과"]
ship_until_low(inventory, 2)
# 출고: 사과, 바나나, 딸기
# 결과: inventory = ["수박", "포도"]
# 출력: "총 3개 출고. 남은 재고: 2개"

# 이미 threshold 이하라면?
ship_until_low(inventory, 5)
# 출력: "이미 재고가 기준(5개) 이하입니다. 현재 2개 보유 중."
```

힌트:
• `while` 반복문을 활용해보세요
• `ship()`을 재사용하면 출고 로직을 다시 구현하지 않아도 됩니다
• 몇 개나 출고했는지 카운터 변수로 추적하세요

## 🤔 생각해보기

1. 왜 새 물건은 앞에 넣고, 오래된 물건은 뒤에서 꺼낼까요? 실제 창고에서 이 방식이 왜 중요할까요?
2. `pop()`은 항목을 꺼내면서 리스트에서도 제거합니다. `inventory[-1]`로 읽는 것과 어떻게 다른가요?
3. `check_stock`에서 재고가 정확히 `threshold`개일 때 경고를 띄워야 할까요, 말아야 할까요? 왜 그렇게 생각하나요?

막히면 스레드에 질문 남겨주세요! 완성보다 이해가 목표입니다. 천천히, 하나씩! 💪

행운을 빕니다! 🚀

---
---

# 📦 Python Practice: Build a Warehouse Inventory System!

Hey team! Today we're building something that powers real e-commerce — a warehouse inventory manager.

## 🎯 Your Mission

You're a junior backend developer at an online shopping company! Your logistics lead just said:

> "We need a warehouse inventory system. New stock gets stacked at the front, and the oldest items ship out first. We also need a low-stock warning when things get thin!"

Let's build this using Python list operations — specifically `insert()` and `pop()`.

## 📋 Functions to Build

### 1️⃣ `restock(inventory, item)`
Adds a new item to the **front** of the inventory list.
• After adding: print `"[item] restocked! Current inventory: [inventory]"`

### 2️⃣ `ship(inventory)`
Removes and returns the item at the **back** of the inventory list.
• If stock exists: return the item name and print `"[item] shipped!"`
• If empty: print `"Shipment failed: no stock available."` and return `None`

### 3️⃣ `check_stock(inventory, threshold)`
Checks stock level and prints a warning if low.
• `threshold` defaults to `3`
• If stock is below `threshold`: print `"⚠️ Low stock warning! [n] item(s) left (threshold: [threshold])"`
• If stock is sufficient: print `"✅ Stock OK. Currently holding [n] item(s)"`

### 4️⃣ `get_oldest(inventory)`
Returns the name of the oldest item (the **last** item in the list).
• If stock exists: return the last item
• If empty: print `"No items in inventory."` and return `None`

## 💡 Example

```python
inventory = []

restock(inventory, "Apples")
restock(inventory, "Bananas")
restock(inventory, "Strawberries")

# Current inventory: ["Strawberries", "Bananas", "Apples"]
# New items stack at the front, so "Apples" is the oldest

print(get_oldest(inventory))    # Apples
print(ship(inventory))          # Apples shipped! / returns: "Apples"
check_stock(inventory, 3)       # ⚠️ Low stock warning! 2 item(s) left (threshold: 3)
```

## 🎓 What You Should Know

Before you start, make sure you're comfortable with:
• `insert(0, item)` — adds an item to the front of a list
• `pop()` — removes and returns the last item (it's gone from the list!)
• `len()` — gets the length of a list
• Indexing — `inventory[-1]` is the last item

## ✅ Your Task

Complete the functions using these signatures:

```python
def restock(inventory: list, item: str) -> None:
    # TODO: your code here
    pass

def ship(inventory: list) -> str:
    # TODO: your code here
    pass

def check_stock(inventory: list, threshold: int = 3) -> None:
    # TODO: your code here
    pass

def get_oldest(inventory: list) -> str:
    # TODO: your code here
    pass
```

## 🎪 Test Your Code

```python
# Test 1: Restocking and stock check
inventory = []
restock(inventory, "Apples")
restock(inventory, "Bananas")
restock(inventory, "Strawberries")
restock(inventory, "Grapes")
restock(inventory, "Watermelon")
check_stock(inventory, 3)
# Expected: ✅ Stock OK. Currently holding 5 item(s)

# Test 2: Oldest item
print(get_oldest(inventory))
# Expected: Apples  (first item restocked)

# Test 3: Shipping
print(ship(inventory))
print(ship(inventory))
# Expected: Apples shipped! / returns: "Apples"
# Expected: Bananas shipped! / returns: "Bananas"

# Test 4: Low stock threshold
check_stock(inventory, 3)
# Expected: ⚠️ or ✅? 🤔 3 items left, threshold is 3 — what happens?

# Test 5: Empty inventory
empty = []
print(ship(empty))
print(get_oldest(empty))
# Expected: Shipment failed: no stock available. / None
# Expected: No items in inventory. / None
```

## 🌟 Bonus Challenges

Finished the main tasks? Take it further — one tier at a time!

---

### 🥉 Easy: `show_inventory(inventory)`

Build a function that prints the current inventory with numbers, from newest to oldest.

```
Expected output (inventory = ["Watermelon", "Grapes", "Strawberries", "Bananas", "Apples"]):

===== Current Inventory =====
1. Watermelon  (newest)
2. Grapes
3. Strawberries
4. Bananas
5. Apples  (oldest)
Total: 5 item(s)
=============================
```

---

### 🥈 Medium: `bulk_restock(inventory, items)`

Build a function that restocks a whole list of items at once.
It should call `restock()` **once per item**, in the order they appear in `items`.

```python
bulk_restock(inventory, ["Kiwi", "Mango", "Pineapple"])
# Restocks "Kiwi" first, then "Mango", then "Pineapple"
# Result: ["Pineapple", "Mango", "Kiwi", ...existing stock...]
```

After restocking, automatically run `check_stock()` to report the new level.

---

### 🥇 Hard: `ship_until_low(inventory, threshold)`

Build a function that keeps shipping items until the stock count reaches `threshold`.

```python
inventory = ["Watermelon", "Grapes", "Strawberries", "Bananas", "Apples"]
ship_until_low(inventory, 2)
# Ships: Apples, Bananas, Strawberries
# Result: inventory = ["Watermelon", "Grapes"]
# Prints: "3 item(s) shipped. Remaining stock: 2"

# What if already at or below threshold?
ship_until_low(inventory, 5)
# Prints: "Already at or below threshold (5). Currently holding 2 item(s)."
```

Hints:
• Use a `while` loop
• Reuse `ship()` so you don't rewrite the shipping logic
• Track how many items were shipped with a counter variable

## 🤔 Think About It

1. Why do we add new items at the front and ship from the back? Why does this matter in a real warehouse?
2. `pop()` removes an item AND returns it. How is that different from just reading `inventory[-1]`?
3. Should `check_stock` warn when stock is *exactly* equal to `threshold`? Why or why not?

Drop questions in the thread if you get stuck! The goal is understanding, not just finishing. One step at a time! 💪

Good luck! 🚀
