# 💱 Python 연습: 환전 계산기 만들기!

여러분, 안녕하세요! 오늘은 여러분이 실제로 여행 중에 겪을 수 있는 상황을 코드로 해결해봅니다.

## 🎯 미션

친구 Chandler가 세계 여행을 계획 중이에요! 그런데 Chandler는 수학이 약해서 환전소에서 바가지를 쓸까봐 걱정하고 있어요. 여러분이 Chandler를 위한 환전 계산기를 만들어주세요. 총 **6개의 함수**를 완성하면 됩니다!

## 💡 핵심 개념: 환율이란?

환율(exchange rate)은 내 나라 돈 1단위가 외국 돈으로 얼마인지를 나타냅니다.

```
환율이 1.20 USD/EUR 라면:
→ 1 EUR을 사려면 1.20 USD가 필요합니다
→ 120 USD로는 120 / 1.20 = 100 EUR을 살 수 있습니다
```

---

## ✅ 함수 1: 환전 후 금액 계산 — `exchange_money()`

```python
def exchange_money(budget, exchange_rate):
```

• `budget` : 환전할 돈의 금액
• `exchange_rate` : 외국 돈 1단위에 해당하는 내 나라 돈의 금액

**반환값:** 환전 후 받게 되는 외국 돈의 금액

```
예시:
exchange_money(127.5, 1.2)  →  106.25
```
✏️ 손으로 확인: 127.5 ÷ 1.2 = 106.25 ✓

---

## ✅ 함수 2: 환전 후 남은 돈 — `get_change()`

```python
def get_change(budget, exchanging_value):
```

• `budget` : 환전 전 총 보유 금액
• `exchanging_value` : 환전에 사용한 금액

**반환값:** 환전 후 내 지갑에 남아있는 원래 화폐 금액

```
예시:
get_change(127.5, 120)  →  7.5
```
✏️ 손으로 확인: 127.5 - 120 = 7.5 ✓

---

## ✅ 함수 3: 지폐 다발의 총 가치 — `get_value_of_bills()`

```python
def get_value_of_bills(denomination, number_of_bills):
```

• `denomination` : 지폐 한 장의 금액 (예: 5달러짜리, 20달러짜리)
• `number_of_bills` : 지폐의 장수

**반환값:** 지폐 다발의 총 가치

```
예시:
get_value_of_bills(5, 128)  →  640
```
✏️ 손으로 확인: 5 × 128 = 640 ✓

---

## ✅ 함수 4: 받을 수 있는 지폐 장수 — `get_number_of_bills()`

```python
def get_number_of_bills(amount, denomination):
```

환전소는 지폐 단위로만 거스름돈을 줍니다. 20달러짜리 지폐만 있다면, 127.5달러어치를 환전해도 6장(120달러)만 받을 수 있어요.

• `amount` : 환전할 총 금액
• `denomination` : 지폐 한 장의 금액

**반환값:** 받을 수 있는 지폐의 장수 (소수점 이하 버림 — *완전한* 지폐만!)

```
예시:
get_number_of_bills(127.5, 5)  →  25
```
✏️ 손으로 확인: 127.5 ÷ 5 = 25.5 → 25장 ✓

---

## ✅ 함수 5: 지폐로 못 받는 나머지 금액 — `get_leftover_of_bills()`

```python
def get_leftover_of_bills(amount, denomination):
```

지폐 단위로 나누고 남은 금액 — 환전소가 가져가는 부분이에요!

• `amount` : 환전할 총 금액
• `denomination` : 지폐 한 장의 금액

**반환값:** 지폐로 받지 못하는 나머지 금액

```
예시:
get_leftover_of_bills(127.5, 20)  →  7.5
```
✏️ 손으로 확인: 127.5 ÷ 20 = 6장 나머지 7.5 ✓

---

## ✅ 함수 6: 수수료 포함 최종 환전 금액 — `exchangeable_value()`

```python
def exchangeable_value(budget, exchange_rate, spread, denomination):
```

현실에서 환전소는 수수료(spread)를 붙입니다. 수수료가 10%라면 실제 환율은 더 불리해져요.

• `budget` : 환전할 금액
• `exchange_rate` : 기본 환율
• `spread` : 수수료 (정수, 퍼센트 단위) — 예: `10`은 10%를 의미
• `denomination` : 지폐 한 장의 금액

**실제 환율 계산법:**
```
실제 환율 = 기본 환율 × (1 + 수수료 / 100)
예: 환율 1.20, 수수료 10% → 1.20 × 1.10 = 1.32
```

**반환값:** 수수료 포함 후 받을 수 있는 최대 금액 (`int` 타입)

```
예시:
exchangeable_value(127.25, 1.20, 10, 20)  →  80
exchangeable_value(127.25, 1.20, 10, 5)   →  95
```

---

## 🎪 테스트 케이스

```python
# 함수 1
print(exchange_money(127.5, 1.2))            # 예상: 106.25
print(exchange_money(100, 2.0))              # 예상: 50.0
print(exchange_money(0, 1.5))               # 예상: 0.0

# 함수 2
print(get_change(127.5, 120))               # 예상: 7.5
print(get_change(500, 500))                 # 예상: 0

# 함수 3
print(get_value_of_bills(5, 128))           # 예상: 640
print(get_value_of_bills(20, 0))            # 예상: 0

# 함수 4
print(get_number_of_bills(127.5, 5))        # 예상: 25
print(get_number_of_bills(19.99, 20))       # 예상: 0
print(get_number_of_bills(100, 20))         # 예상: 5

# 함수 5
print(get_leftover_of_bills(127.5, 20))     # 예상: 7.5
print(get_leftover_of_bills(100, 20))       # 예상: 0

# 함수 6
print(exchangeable_value(127.25, 1.20, 10, 20))  # 예상: 80
print(exchangeable_value(127.25, 1.20, 10, 5))   # 예상: 95
print(exchangeable_value(100, 1.0, 0, 10))        # 예상: 100
```

---

## 🎁 보너스 챌린지

🟢 **Easy:** `exchange_money()`를 사용해서, 200달러를 환율 1.35로 환전하면 얼마인지 출력해보세요.

🟡 **Medium:** 여행 예산이 500달러입니다. 환율 1.25, 수수료 8%일 때, 20달러짜리 지폐로 얼마나 받을 수 있나요? 그리고 환전소가 가져가는 금액은 얼마인가요?

🔴 **Hard:** (함수를 모두 완성한 후) 위의 함수들을 조합해서, 사용자가 예산과 환율과 수수료를 입력하면 전체 환전 결과를 요약해서 출력하는 코드를 작성해보세요.

---

## 🤔 생각해보기

1. `//` 와 `/` 는 어떻게 다른가요? 함수 4에서 왜 `//`를 사용하나요?
2. `%` 연산자는 무엇을 계산하나요? 함수 5에서 어떻게 활용되나요?
3. 함수 6의 반환값이 `int`여야 하는 이유가 무엇일까요?

막히면 스레드에 질문 남겨주세요! 목표는 끝내는 것이 아니라 배우는 것입니다. 천천히 논리를 이해하면서 진행하세요.

행운을 빕니다! 🚀

---
---

# 💱 Python Practice: Build a Currency Exchange Calculator!

Hey team! Today's challenge is something you might actually use someday — real-world currency conversion!

## 🎯 Your Mission

Your friend Chandler is planning a trip around the world! But Chandler's not great at math and is worried about getting ripped off at currency exchange booths. Your job is to build a currency calculator for him. You'll write **6 functions** — one at a time, step by step.

## 💡 Key Concept: What is an Exchange Rate?

An exchange rate tells you how much of your home currency you need to buy one unit of foreign currency.

```
If the exchange rate is 1.20 USD/EUR:
→ You need 1.20 USD to buy 1 EUR
→ With 120 USD, you can get 120 / 1.20 = 100 EUR
```

---

## ✅ Function 1: Value after exchange — `exchange_money()`

```python
def exchange_money(budget, exchange_rate):
```

• `budget` : How much money you want to exchange
• `exchange_rate` : How much home currency equals one unit of foreign currency

**Returns:** The amount of foreign currency you receive

```
Example:
exchange_money(127.5, 1.2)  →  106.25
```
✏️ Check by hand: 127.5 ÷ 1.2 = 106.25 ✓

---

## ✅ Function 2: Money left after exchanging — `get_change()`

```python
def get_change(budget, exchanging_value):
```

• `budget` : Total money you have before exchanging
• `exchanging_value` : The amount you're handing over to exchange

**Returns:** How much of your original currency is left in your wallet

```
Example:
get_change(127.5, 120)  →  7.5
```
✏️ Check by hand: 127.5 - 120 = 7.5 ✓

---

## ✅ Function 3: Total value of a stack of bills — `get_value_of_bills()`

```python
def get_value_of_bills(denomination, number_of_bills):
```

• `denomination` : The value of one bill (e.g. a $5 bill, a $20 bill)
• `number_of_bills` : How many bills you have

**Returns:** Total value of all those bills combined

```
Example:
get_value_of_bills(5, 128)  →  640
```
✏️ Check by hand: 5 × 128 = 640 ✓

---

## ✅ Function 4: Number of bills you can receive — `get_number_of_bills()`

```python
def get_number_of_bills(amount, denomination):
```

Exchange booths only hand out whole bills. If they only have $20 bills, you can't get $127.50 — you'd only get 6 bills ($120).

• `amount` : Total amount to exchange
• `denomination` : Value of one bill

**Returns:** How many *whole* bills you can receive (no partial bills!)

```
Example:
get_number_of_bills(127.5, 5)  →  25
```
✏️ Check by hand: 127.5 ÷ 5 = 25.5 → 25 whole bills ✓

---

## ✅ Function 5: Leftover that the booth keeps — `get_leftover_of_bills()`

```python
def get_leftover_of_bills(amount, denomination):
```

After handing out whole bills, whatever's left over stays with the booth!

• `amount` : Total amount being exchanged
• `denomination` : Value of one bill

**Returns:** The leftover amount that can't be returned as bills

```
Example:
get_leftover_of_bills(127.5, 20)  →  7.5
```
✏️ Check by hand: 127.5 ÷ 20 = 6 bills remainder 7.5 ✓

---

## ✅ Function 6: Final exchangeable amount with fees — `exchangeable_value()`

```python
def exchangeable_value(budget, exchange_rate, spread, denomination):
```

In real life, exchange booths charge a fee called a *spread*. This makes the effective exchange rate slightly worse for you.

• `budget` : How much money you're exchanging
• `exchange_rate` : The base exchange rate
• `spread` : The fee percentage as a whole integer — e.g. `10` means 10%
• `denomination` : Value of one bill

**How to calculate the actual rate:**
```
actual_rate = exchange_rate × (1 + spread / 100)
Example: rate 1.20, spread 10% → 1.20 × 1.10 = 1.32
```

**Returns:** The maximum amount you can receive in whole bills, as an `int`

```
Examples:
exchangeable_value(127.25, 1.20, 10, 20)  →  80
exchangeable_value(127.25, 1.20, 10, 5)   →  95
```

---

## 🎪 Test Your Code

```python
# Function 1
print(exchange_money(127.5, 1.2))            # Expected: 106.25
print(exchange_money(100, 2.0))              # Expected: 50.0
print(exchange_money(0, 1.5))               # Expected: 0.0

# Function 2
print(get_change(127.5, 120))               # Expected: 7.5
print(get_change(500, 500))                 # Expected: 0

# Function 3
print(get_value_of_bills(5, 128))           # Expected: 640
print(get_value_of_bills(20, 0))            # Expected: 0

# Function 4
print(get_number_of_bills(127.5, 5))        # Expected: 25
print(get_number_of_bills(19.99, 20))       # Expected: 0
print(get_number_of_bills(100, 20))         # Expected: 5

# Function 5
print(get_leftover_of_bills(127.5, 20))     # Expected: 7.5
print(get_leftover_of_bills(100, 20))       # Expected: 0

# Function 6
print(exchangeable_value(127.25, 1.20, 10, 20))  # Expected: 80
print(exchangeable_value(127.25, 1.20, 10, 5))   # Expected: 95
print(exchangeable_value(100, 1.0, 0, 10))        # Expected: 100
```

---

## 🎁 Bonus Challenges

🟢 **Easy:** Using `exchange_money()`, how much would you get if you exchanged $200 at a rate of 1.35?

🟡 **Medium:** You have a $500 travel budget. With a rate of 1.25 and a 8% spread, how many $20 bills can you get? And how much does the booth keep?

🔴 **Hard:** (After finishing all 6 functions) Combine your functions to write a program that prints a full exchange summary — given a budget, rate, spread, and denomination, show the user everything: exchanged amount, bills received, leftover, and the booth's cut.

---

## 🤔 Think About It

1. What's the difference between `/` and `//`? Why do we use `//` in Function 4?
2. What does the `%` operator calculate? How is it used in Function 5?
3. Why does Function 6 need to return an `int` instead of a `float`?

Drop your questions in the thread if you get stuck! Remember, the goal is to learn, not just to finish. Take your time and understand the logic.

Good luck! 🚀
