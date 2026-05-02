# 🐍 Python 연습: 나이에 따라 요금이 달라져요!

여러분, 안녕하세요! 이번에는 조건문을 본격적으로 활용합니다. 조건이 여러 개일 때는 `if` 하나로는 부족해요 — `elif`가 등장할 차례입니다! 🎟️

## 🎯 미션

지하철 요금 계산 시스템을 만들고 있어요. 승객의 나이 `age`를 받아서, 아래 기준에 맞는 요금을 출력하세요:

| 나이 조건 | 요금 |
|-----------|------|
| 8세 미만 | 무료 |
| 8세 이상 ~ 19세 이하 | 1000원 |
| 20세 이상 ~ 64세 이하 | 2000원 |
| 65세 이상 | 1000원 |

## 📋 규칙

*주어지는 것:*
• 정수 `age` — 승객의 나이

*해야 할 일:*
1. `age`에 맞는 조건을 판별
2. 해당하는 요금을 출력

*반드시 따라야 할 제약사항:*
• `if` / `elif` / `else` 구조를 사용해야 합니다
• 입력은 코드 스켈레톤에 이미 제공되어 있습니다 — `input()` 부분은 건드리지 마세요!

## 💡 예제

**예제 1:**
```
입력: age = 5
출력: 무료
```
왜? 5세는 8세 미만이에요.

**예제 2:**
```
입력: age = 13
출력: 1000원
```
왜? 13세는 8세 이상 19세 이하에 해당해요.

**예제 3:**
```
입력: age = 30
출력: 2000원
```
왜? 30세는 20세 이상 64세 이하에 해당해요.

**예제 4:**
```
입력: age = 70
출력: 1000원
```
왜? 70세는 65세 이상 노인 할인 대상이에요.

## 🎓 알아야 할 것

코딩을 시작하기 전에, 다음을 이해하고 있는지 확인하세요:
• `if` 조건문이 어떻게 작동하는지
• `elif`가 무엇인지, `if`와 어떻게 다른지
• `else`가 언제 실행되는지
• 조건이 위에서부터 순서대로 확인된다는 것

## 🆕 새로운 개념: elif

지금까지는 조건이 하나였지만, 이번에는 조건이 네 가지입니다. 이럴 때 `elif`를 사용합니다:

```python
if 첫 번째 조건:
    # 첫 번째 조건이 True일 때 실행
elif 두 번째 조건:
    # 첫 번째는 False, 두 번째 조건이 True일 때 실행
elif 세 번째 조건:
    # 앞의 조건들이 모두 False, 세 번째가 True일 때 실행
else:
    # 위의 모든 조건이 False일 때 실행
```

**핵심:** Python은 조건을 **위에서 아래로** 확인합니다. 하나가 `True`가 되는 순간, 나머지 조건은 확인하지 않고 건너뜁니다!

```python
age = 13
if age < 8:        # False → 건너뜀
    print("무료")
elif age <= 19:    # True  → 실행! 여기서 멈춤
    print("1000원")
elif age < 65:     # 확인조차 안 함
    print("2000원")
else:              # 확인조차 안 함
    print("1000원")
```

## ✅ 과제

다음 시그니처로 함수를 작성하세요:
```python
def calculate_fare(age: int) -> None:
    # 여기에 코드 작성
    pass
```

**시작하는 데 도움이 될 팁:**
• 조건의 순서가 중요합니다 — 어떤 조건을 먼저 확인해야 할까요?
• 경계값을 주의하세요: 8세는 "무료"일까요, "1000원"일까요?
• 65세 이상과 8~19세는 요금이 같지만, 두 그룹이 섞이면 안 됩니다!

## 🎪 코드 테스트

다음 테스트 케이스를 실행해보세요:

```python
# 테스트 1: 8세 미만
calculate_fare(5)
# 예상 출력: 무료

# 테스트 2: 정확히 8세 (경계값!)
calculate_fare(8)
# 예상 출력: 1000원

# 테스트 3: 청소년
calculate_fare(13)
# 예상 출력: 1000원

# 테스트 4: 정확히 19세 (경계값!)
calculate_fare(19)
# 예상 출력: 1000원

# 테스트 5: 정확히 20세 (경계값!)
calculate_fare(20)
# 예상 출력: 2000원

# 테스트 6: 성인
calculate_fare(30)
# 예상 출력: 2000원

# 테스트 7: 정확히 64세 (경계값!)
calculate_fare(64)
# 예상 출력: 2000원

# 테스트 8: 정확히 65세 (경계값!)
calculate_fare(65)
# 예상 출력: 1000원

# 테스트 9: 노인
calculate_fare(70)
# 예상 출력: 1000원
```

## 🤔 생각해보기

1. 조건의 순서를 바꾸면 어떻게 될까요? 예를 들어 `elif age >= 65`를 맨 위로 올리면?
2. `elif age <= 19` 대신 `elif age < 20`으로 써도 같은 결과가 나올까요?
3. 65세 이상과 8~19세의 요금이 같으니 조건을 합쳐도 될까요? 합친다면 코드가 더 좋아질까요, 나빠질까요?

막히면 스레드에 질문을 남겨주세요! 목표는 끝내는 것이 아니라 배우는 것입니다. 천천히 논리를 이해하면서 진행하세요.

행운을 빕니다! 🚀

---
---

# 🐍 Python Practice: Different Fares for Different Ages!

Hey team! This time we're putting conditionals to real use. When there are multiple conditions to check, one `if` isn't enough — it's time for `elif` to shine! 🎟️

## 🎯 Your Mission

You're building a subway fare calculation system. Given a passenger's age `age`, print the correct fare based on these rules:

| Age Condition | Fare |
|---------------|------|
| Under 8 | Free |
| 8 to 19 (inclusive) | 1000원 |
| 20 to 64 (inclusive) | 2000원 |
| 65 and above | 1000원 |

## 📋 The Rules

*What you're given:*
• An integer `age` — the passenger's age

*What you need to do:*
1. Determine which condition `age` falls into
2. Print the corresponding fare

*Constraints you must follow:*
• You must use an `if` / `elif` / `else` structure
• The input section is already provided in the skeleton — don't touch the `input()` lines!

## 💡 Example Time

**Example 1:**
```
Input: age = 5
Output: 무료
```
Why? 5 is under 8.

**Example 2:**
```
Input: age = 13
Output: 1000원
```
Why? 13 is between 8 and 19 (inclusive).

**Example 3:**
```
Input: age = 30
Output: 2000원
```
Why? 30 is between 20 and 64 (inclusive).

**Example 4:**
```
Input: age = 70
Output: 1000원
```
Why? 70 is 65 or above — senior discount applies!

## 🎓 What You Should Know

Before you start coding, make sure you understand:
• How `if` conditional statements work
• What `elif` is and how it differs from `if`
• When `else` executes
• That conditions are checked from top to bottom, in order

## 🆕 New Concept: elif

So far, you've worked with one condition at a time. This problem has four. That's where `elif` comes in:

```python
if first_condition:
    # runs when first condition is True
elif second_condition:
    # runs when first is False AND second is True
elif third_condition:
    # runs when all above are False AND third is True
else:
    # runs when ALL conditions above are False
```

**Key point:** Python checks conditions **top to bottom**. The moment one is `True`, it runs that block and skips all the rest!

```python
age = 13
if age < 8:        # False → skipped
    print("무료")
elif age <= 19:    # True  → runs! stops here
    print("1000원")
elif age < 65:     # never even checked
    print("2000원")
else:              # never even checked
    print("1000원")
```

## ✅ Your Task

Write a function with this signature:
```python
def calculate_fare(age: int) -> None:
    # Your code here
    pass
```

**Tips to get you started:**
• The order of your conditions matters — which one should you check first?
• Watch the boundary values carefully: is age 8 "무료" or "1000원"?
• Ages 65+ and 8–19 have the same fare, but don't mix the two groups!

## 🎪 Test Your Code

Try running these test cases:

```python
# Test 1: under 8
calculate_fare(5)
# Expected output: 무료

# Test 2: exactly 8 (boundary!)
calculate_fare(8)
# Expected output: 1000원

# Test 3: teenager
calculate_fare(13)
# Expected output: 1000원

# Test 4: exactly 19 (boundary!)
calculate_fare(19)
# Expected output: 1000원

# Test 5: exactly 20 (boundary!)
calculate_fare(20)
# Expected output: 2000원

# Test 6: adult
calculate_fare(30)
# Expected output: 2000원

# Test 7: exactly 64 (boundary!)
calculate_fare(64)
# Expected output: 2000원

# Test 8: exactly 65 (boundary!)
calculate_fare(65)
# Expected output: 1000원

# Test 9: senior
calculate_fare(70)
# Expected output: 1000원
```

## 🤔 Think About It

1. What would happen if you swapped the order of conditions? For example, what if you moved `elif age >= 65` to the very top?
2. Is `elif age <= 19` the same as `elif age < 20`? Would it produce the same results?
3. Ages 65+ and 8–19 have the same fare — could you combine them into one condition? Would that make the code better or worse?

Drop your questions in the thread if you get stuck! Remember, the goal is to learn, not just to finish. Take your time and understand the logic.

Good luck! 🚀
