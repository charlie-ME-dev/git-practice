# 🏦 Python 연습: 가장 부유한 고객 찾기 (map / filter / lambda)

안녕하세요 여러분! 이번에는 여러분이 방금 배운 **고차 함수** — `map()`, `filter()`, `lambda` — 를 실전에서 써볼 차례입니다.

## 🎯 미션

여러분은 디지털 은행의 **주니어 개발자**입니다. 분석 대시보드 팀이 여러분에게 작은 작업을 맡겼어요: "고객들 중 **가장 부유한 사람의 총 자산**이 얼마인지 알려줘."

각 고객은 여러 개의 은행 계좌를 가질 수 있습니다. 한 고객의 **총 자산**은 그 사람의 모든 계좌 잔액을 합한 값입니다. 가장 부유한 고객은 총 자산이 가장 큰 사람이고요.

## 📋 규칙

*주어지는 것:*
- `accounts`라는 2차원 리스트 — `accounts[i]`는 `i`번째 고객의 계좌 잔액 리스트입니다
- 예: `accounts[i][j]` = `i`번째 고객의 `j`번째 계좌 잔액

*해야 할 일:*
1. 각 고객의 총 자산(모든 계좌의 합)을 계산
2. 그중 가장 큰 값을 반환

*제약사항:*
- 잔액은 0 이상의 정수입니다
- 고객은 최소 1명, 각 고객은 최소 1개의 계좌를 가집니다

## 💡 예제

**예제 1:**
```
입력: accounts = [[1, 2, 3], [3, 2, 1]]
출력: 6
```
왜? 1번 고객 = 1+2+3 = 6, 2번 고객 = 3+2+1 = 6. 둘 다 6이므로 가장 부유한 자산은 6.

**예제 2:**
```
입력: accounts = [[1, 5], [7, 3], [3, 5]]
출력: 10
```
왜? 자산은 각각 6, 10, 8. 가장 큰 값은 10.

## 🎓 알아야 할 것

- 리스트의 합을 구하는 `sum()`
- 가장 큰 값을 찾는 `max()`
- `map(함수, 반복가능객체)` — 모든 요소에 함수를 적용
- `filter(함수, 반복가능객체)` — 조건을 만족하는 요소만 남김
- `lambda 인자: 식` — 이름 없는 짧은 함수

## ✅ 과제

다음 시그니처로 함수를 작성하세요:
```python
def find_richest_wealth(accounts: list[list[int]]) -> int:
    # 여기에 코드 작성
    pass
```

**힌트:**
- 각 고객의 자산은 그 고객의 계좌 리스트를 `sum()`하면 됩니다
- 모든 고객의 자산을 한 번에 구하고 싶다면? → `map(sum, accounts)`를 떠올려보세요
- 그중 최댓값은? → `max(...)`

## 🎁 보너스 도전 과제

### 🥉 Easy — 모든 고객의 자산 목록
모든 고객의 총 자산을 **리스트로** 반환하세요. `map()`을 사용해보세요.
```python
def list_all_wealth(accounts: list[list[int]]) -> list[int]:
    pass
# list_all_wealth([[1, 5], [7, 3], [3, 5]]) -> [6, 10, 8]
```

### 🥈 Medium — 우량 고객 수 세기
기준 금액 `threshold`를 **초과하는**(`>`) 자산을 가진 고객이 몇 명인지 반환하세요. `filter()`와 `lambda`를 사용해보세요.
```python
def count_high_value_customers(accounts: list[list[int]], threshold: int) -> int:
    pass
# count_high_value_customers([[1, 5], [7, 3], [3, 5]], 7) -> 2  (자산 10, 8 > 7)
```

### 🥇 Hard 🔮 — 은행 전체 자산 (아직 안 배운 도구 미리보기)
> ⚠️ 이 보너스는 **아직 수업에서 다루지 않은** `functools.reduce`를 미리 맛보는 과제입니다. 몰라도 괜찮으니, 도전하고 싶은 사람만 시도해보세요!

`reduce`는 `map`/`filter`에 이어지는 세 번째 함수형 도구로, 여러 값을 **하나의 값으로 누적**합니다. 은행에 보관된 **모든 고객의 자산을 전부 합한 총액**을 반환하세요.
```python
from functools import reduce

def total_bank_wealth(accounts: list[list[int]]) -> int:
    pass
# total_bank_wealth([[1, 2, 3], [3, 2, 1]]) -> 12
```

## 🎪 코드 테스트

```python
print(find_richest_wealth([[1, 2, 3], [3, 2, 1]]))            # 예상: 6
print(find_richest_wealth([[1, 5], [7, 3], [3, 5]]))          # 예상: 10
print(find_richest_wealth([[2, 8, 7], [7, 1, 3], [1, 9, 5]])) # 예상: 17
```

## 🤔 생각해보기

1. `map(sum, accounts)`는 무엇을 돌려줄까요? 바로 `print` 하면 왜 이상하게 보일까요? (힌트: `list()`로 감싸보세요)
2. `filter`의 조건 함수는 무엇을 반환해야 할까요? (참/거짓)
3. `lambda`가 너무 길고 복잡해지면, 차라리 이름 있는 함수로 빼는 게 읽기 좋을 때가 있습니다. 언제 그럴까요?

> 💬 **읽기 좋은 코드에 대하여**
> *"프로그램은 사람이 읽을 수 있도록 작성되어야 하며, 기계가 실행하는 것은 부차적인 일일 뿐이다."*
> — Harold Abelson, 『Structure and Interpretation of Computer Programs』 (1985) 서문
> *(출처 신뢰도: 높음 — 출판된 교재 서문에 명시됨)*

막히면 스레드에 질문 남겨주세요. 목표는 끝내는 게 아니라 **왜 그렇게 되는지 이해하는 것**입니다! 🚀

---
---

# 🏦 Python Practice: Find the Richest Customer (map / filter / lambda)

Hey team! Time to put the **higher-order functions** you just learned — `map()`, `filter()`, and `lambda` — to work on something real.

## 🎯 Your Mission

You're a **junior developer** at a digital bank. The analytics dashboard team handed you a small task: *"Tell me the total wealth of our richest customer."*

Each customer can have several bank accounts. A customer's **total wealth** is the sum of all their account balances. The richest customer is the one with the largest total wealth.

## 📋 The Rules

*What you're given:*
- A 2D list called `accounts`, where `accounts[i]` is the list of account balances for customer `i`
- So `accounts[i][j]` = balance in customer `i`'s `j`-th account

*What you need to do:*
1. Compute each customer's total wealth (sum of all their accounts)
2. Return the largest one

*Constraints:*
- Balances are non-negative integers
- There's at least 1 customer, and each customer has at least 1 account

## 💡 Example Time

**Example 1:**
```
Input: accounts = [[1, 2, 3], [3, 2, 1]]
Output: 6
```
Why? Customer 1 = 1+2+3 = 6, Customer 2 = 3+2+1 = 6. Both are 6, so the richest wealth is 6.

**Example 2:**
```
Input: accounts = [[1, 5], [7, 3], [3, 5]]
Output: 10
```
Why? The wealths are 6, 10, and 8. The largest is 10.

## 🎓 What You Should Know

- `sum()` to total a list
- `max()` to find the largest value
- `map(function, iterable)` — applies a function to every element
- `filter(function, iterable)` — keeps only the elements that pass a test
- `lambda arg: expression` — a short, unnamed function

## ✅ Your Task

Write a function with this signature:
```python
def find_richest_wealth(accounts: list[list[int]]) -> int:
    # Your code here
    pass
```

**Hints:**
- A customer's wealth is just `sum()` of their account list
- Want every customer's wealth at once? → think `map(sum, accounts)`
- The largest of those? → `max(...)`

## 🎁 Bonus Challenges

### 🥉 Easy — List Every Customer's Wealth
Return a **list** of every customer's total wealth. Use `map()`.
```python
def list_all_wealth(accounts: list[list[int]]) -> list[int]:
    pass
# list_all_wealth([[1, 5], [7, 3], [3, 5]]) -> [6, 10, 8]
```

### 🥈 Medium — Count High-Value Customers
Return how many customers have wealth **strictly greater than** (`>`) a given `threshold`. Use `filter()` with `lambda`.
```python
def count_high_value_customers(accounts: list[list[int]], threshold: int) -> int:
    pass
# count_high_value_customers([[1, 5], [7, 3], [3, 5]], 7) -> 2  (wealth 10, 8 > 7)
```

### 🥇 Hard 🔮 — Total Bank Wealth (preview of a tool you haven't learned yet)
> ⚠️ This bonus previews `functools.reduce`, which we **haven't covered in class yet**. Totally fine if it's unfamiliar — only try it if you want a stretch!

`reduce` is the third functional tool alongside `map`/`filter`: it **accumulates many values into one**. Return the **grand total of every customer's wealth** held at the bank.
```python
from functools import reduce

def total_bank_wealth(accounts: list[list[int]]) -> int:
    pass
# total_bank_wealth([[1, 2, 3], [3, 2, 1]]) -> 12
```

## 🎪 Test Your Code

```python
print(find_richest_wealth([[1, 2, 3], [3, 2, 1]]))            # Expected: 6
print(find_richest_wealth([[1, 5], [7, 3], [3, 5]]))          # Expected: 10
print(find_richest_wealth([[2, 8, 7], [7, 1, 3], [1, 9, 5]])) # Expected: 17
```

## 🤔 Think About It

1. What does `map(sum, accounts)` give back? Why does it look strange if you `print` it directly? (Hint: wrap it in `list()`.)
2. What must a `filter` test function return? (True/False)
3. When a `lambda` gets long and complex, pulling it out into a named function often reads better. When would you make that call?

> 💬 **On readable code**
> *"Programs must be written for people to read, and only incidentally for machines to execute."*
> — Harold Abelson, *Structure and Interpretation of Computer Programs* (1985), preface
> *(Attribution confidence: high — stated in the preface of the published textbook.)*

Drop questions in the thread if you get stuck. The goal isn't to finish — it's to **understand why it works**! 🚀
