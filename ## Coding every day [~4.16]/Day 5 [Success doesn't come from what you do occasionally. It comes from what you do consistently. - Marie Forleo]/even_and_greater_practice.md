# 🐍 Python 연습: 두 가지 조건 동시에 확인하기!

여러분, 안녕하세요! 이번엔 조건 하나가 아니라 두 가지를 동시에 확인하는 문제입니다. 핵심은 딱 한 줄이에요!

## 🎯 미션

온라인 쇼핑몰의 VIP 혜택 시스템을 만들고 있어요. 고객의 주문 수량 `n`이 **짝수이면서 동시에 10보다 클 때만** 특별 할인 혜택을 제공합니다. 두 조건을 모두 만족하는지 `True` 또는 `False`로 출력하세요.

## 📋 규칙

*주어지는 것:*
• 정수 `n` — 고객의 주문 수량

*해야 할 일:*
1. `n`이 짝수인지 확인 — 단, 아래 식을 반드시 사용하세요:
   ```
   n // 2 * 2 == n
   ```
2. `n`이 10보다 큰지 확인
3. 두 조건을 **동시에** 만족하면 `True`, 그렇지 않으면 `False` 출력

*반드시 따라야 할 제약사항:*
• 짝수 판별은 반드시 `n // 2 * 2 == n` 식을 사용해야 합니다
• `print()` 함수 **한 줄**로 결과를 출력해야 합니다
• `if` 조건문은 사용하지 않아도 됩니다!
• 입력은 코드 스켈레톤에 이미 제공되어 있습니다 — `input()` 부분은 건드리지 마세요!

## 💡 예제

**예제 1:**
```
입력: n = 12
출력: True
```
왜? 12는 짝수(12 // 2 * 2 == 12 ✅)이고, 10보다 큽니다(12 > 10 ✅). 두 조건 모두 만족!

**예제 2:**
```
입력: n = 8
출력: False
```
왜? 8은 짝수지만(8 // 2 * 2 == 8 ✅), 10보다 크지 않습니다(8 > 10 ❌). 한 조건만 만족!

**예제 3:**
```
입력: n = 11
출력: False
```
왜? 11은 10보다 크지만(11 > 10 ✅), 홀수입니다(11 // 2 * 2 == 10 ≠ 11 ❌). 한 조건만 만족!

**예제 4:**
```
입력: n = 10
출력: False
```
왜? 10은 짝수지만(10 // 2 * 2 == 10 ✅), 10보다 **크지 않습니다** — 10은 10과 같아요!(10 > 10 ❌)

## 🎓 알아야 할 것

코딩을 시작하기 전에, 다음을 이해하고 있는지 확인하세요:
• `//` 연산자(정수 나눗셈)가 무엇인지
• `==` 연산자가 무엇인지
• `>` 연산자가 무엇인지
• 두 개의 조건을 하나로 합치는 방법 🤔

## 💡 힌트: 짝수 판별식이 어떻게 작동할까요?

`n // 2 * 2 == n` 이 왜 짝수를 판별할 수 있을까요?

```
n = 12 → 12 // 2 = 6 → 6 * 2 = 12 → 12 == 12 → True  ✅ (짝수!)
n = 7  →  7 // 2 = 3 → 3 * 2 = 6  →  6 == 7  → False ❌ (홀수!)
```

`//`는 소수점을 버리는 나눗셈입니다. 홀수를 2로 나누면 소수점이 잘리기 때문에, 다시 2를 곱해도 원래 숫자로 돌아오지 않아요!

## ✅ 과제

다음 시그니처로 함수를 작성하세요:
```python
def check_vip_condition(n: int) -> None:
    # 여기에 코드 작성 (딱 한 줄이면 충분해요!)
    pass
```

**시작하는 데 도움이 될 팁:**
• 지난번처럼 `print()` 안에 비교식을 바로 넣을 수 있어요
• 두 조건을 동시에 만족해야 한다면, 두 식을 어떻게 연결할 수 있을까요?
• Python에는 두 조건을 한 번에 확인하는 키워드가 있습니다 — 영어 단어 그대로예요! 🔍

## 🎪 코드 테스트

다음 테스트 케이스를 실행해보세요:

```python
# 테스트 1: 두 조건 모두 만족
check_vip_condition(12)
# 예상 출력: True

# 테스트 2: 짝수지만 10 이하
check_vip_condition(8)
# 예상 출력: False

# 테스트 3: 10보다 크지만 홀수
check_vip_condition(11)
# 예상 출력: False

# 테스트 4: 정확히 10
check_vip_condition(10)
# 예상 출력: False

# 테스트 5: 큰 홀수
check_vip_condition(101)
# 예상 출력: False

# 테스트 6: 큰 짝수
check_vip_condition(100)
# 예상 출력: True
```

## 🤔 생각해보기

코딩을 시작하기 전에, 스스로에게 물어보세요:
1. `n // 2 * 2 == n` 은 어떤 값을 반환할까요?
2. `n > 10` 은 어떤 값을 반환할까요?
3. 두 결과가 **모두** `True`여야 한다면, 두 식을 어떻게 연결할 수 있을까요?

막히면 스레드에 질문을 남겨주세요! 목표는 끝내는 것이 아니라 배우는 것입니다. 천천히 논리를 이해하면서 진행하세요.

행운을 빕니다! 🚀

---
---

# 🐍 Python Practice: Checking Two Conditions at Once!

Hey team! This time we're checking not just one condition, but two at the same time. The secret? It still fits in one line!

## 🎯 Your Mission

You're building a VIP discount system for an online shop. A customer qualifies for a special deal only when their order quantity `n` is **both even AND greater than 10**. Print `True` or `False` depending on whether both conditions are met.

## 📋 The Rules

*What you're given:*
• An integer `n` — the customer's order quantity

*What you need to do:*
1. Check whether `n` is even — you **must** use this exact expression:
   ```
   n // 2 * 2 == n
   ```
2. Check whether `n` is greater than 10
3. Print `True` if **both** conditions are satisfied, `False` otherwise

*Constraints you must follow:*
• You must use `n // 2 * 2 == n` to check for even numbers
• Print the result using **just one** `print()` call
• You do NOT need an `if` statement!
• The input section is already provided in the skeleton — don't touch the `input()` lines!

## 💡 Example Time

**Example 1:**
```
Input: n = 12
Output: True
```
Why? 12 is even (12 // 2 * 2 == 12 ✅) and greater than 10 (12 > 10 ✅). Both conditions met!

**Example 2:**
```
Input: n = 8
Output: False
```
Why? 8 is even (8 // 2 * 2 == 8 ✅), but not greater than 10 (8 > 10 ❌). Only one condition met!

**Example 3:**
```
Input: n = 11
Output: False
```
Why? 11 is greater than 10 (11 > 10 ✅), but it's odd (11 // 2 * 2 == 10 ≠ 11 ❌). Only one condition met!

**Example 4:**
```
Input: n = 10
Output: False
```
Why? 10 is even (10 // 2 * 2 == 10 ✅), but 10 is NOT greater than 10 — it's equal! (10 > 10 ❌)

## 🎓 What You Should Know

Before you start coding, make sure you understand:
• What the `//` operator (integer division) does
• What the `==` operator does
• What the `>` operator does
• How to combine two conditions into one 🤔

## 💡 Hint: How does the even-number check work?

Why does `n // 2 * 2 == n` detect even numbers?

```
n = 12 → 12 // 2 = 6 → 6 * 2 = 12 → 12 == 12 → True  ✅ (even!)
n = 7  →  7 // 2 = 3 → 3 * 2 = 6  →  6 == 7  → False ❌ (odd!)
```

`//` is division that throws away the decimal. When you divide an odd number by 2, the decimal gets cut off — so multiplying back by 2 doesn't give you the original number!

## ✅ Your Task

Write a function with this signature:
```python
def check_vip_condition(n: int) -> None:
    # Your code here (just one line is enough!)
    pass
```

**Tips to get you started:**
• Just like last time, you can put expressions directly inside `print()`
• If both conditions must be true at the same time, how can you connect two expressions?
• Python has a keyword for checking two conditions at once — it's a plain English word! 🔍

## 🎪 Test Your Code

Try running these test cases:

```python
# Test 1: both conditions met
check_vip_condition(12)
# Expected output: True

# Test 2: even but not greater than 10
check_vip_condition(8)
# Expected output: False

# Test 3: greater than 10 but odd
check_vip_condition(11)
# Expected output: False

# Test 4: exactly 10
check_vip_condition(10)
# Expected output: False

# Test 5: large odd number
check_vip_condition(101)
# Expected output: False

# Test 6: large even number
check_vip_condition(100)
# Expected output: True
```

## 🤔 Think About It

Before you start coding, ask yourself:
1. What does `n // 2 * 2 == n` return on its own?
2. What does `n > 10` return on its own?
3. If **both** need to be `True`, how can you connect the two expressions?

Drop your questions in the thread if you get stuck! Remember, the goal is to learn, not just to finish. Take your time and understand the logic.

Good luck! 🚀
