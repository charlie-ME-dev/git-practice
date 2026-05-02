# 🐍 Python 연습: 10,001번째 소수를 찾아라!

여러분, 안녕하세요! 오늘은 수학자들도 사랑하는 고전 문제에 도전해봅시다.

## 🎯 미션

여러분은 암호학 연구소의 신입 개발자입니다. 선배 연구원이 다가와 이렇게 말합니다:

> "보안 키 생성 시스템을 테스트해야 하는데, **10,001번째 소수**가 필요해요. 계산해주실 수 있나요?"

처음 여섯 개의 소수를 나열하면 2, 3, 5, 7, 11, 13이고, 6번째 소수는 13입니다. 그렇다면 10,001번째 소수는 무엇일까요?

## 📋 규칙

*주어지는 것:*
• 정수 하나 `n` (몇 번째 소수를 찾을지)

*해야 할 일:*
1. `n`번째 소수를 찾아서 반환
2. 순서는 1부터 시작 (첫 번째 소수는 2)

*반드시 따라야 할 제약사항:*
• **`import` 사용 금지!** 기본 Python만 사용
• 리스트에 소수를 저장할 필요는 없습니다 — 개수만 세어도 충분해요
• `n`은 1 이상의 양의 정수

## 💡 예제

**예제 1:**
```
입력: n = 1
출력: 2
```
왜? 첫 번째 소수는 2입니다.

**예제 2:**
```
입력: n = 6
출력: 13
```
왜? 소수를 순서대로 나열하면 2, 3, 5, 7, 11, 13 → 6번째는 13입니다.

**예제 3 (최종 목표):**
```
입력: n = 10001
출력: ???
```
직접 알아내세요! 🎯

## 🎓 알아야 할 것

코딩을 시작하기 전에, 다음을 이해하고 있는지 확인하세요:
• 소수의 정의 (1과 자기 자신으로만 나누어지는 2 이상의 자연수)
• `while` 반복문으로 조건이 만족될 때까지 반복하는 방법
• `for` 반복문과 `range()` 사용법
• `%` 연산자로 나머지 확인하는 방법
• 함수에서 `return`으로 값 반환하기

## ✅ 과제

다음 시그니처로 두 개의 함수를 작성하세요:

```python
def is_prime(num: int) -> bool:
    """숫자가 소수인지 판별합니다."""
    # 여기에 코드 작성
    pass


def nth_prime(n: int) -> int:
    """n번째 소수를 반환합니다."""
    # 여기에 코드 작성
    pass
```

**시작하는 데 도움이 될 팁:**
• `is_prime` 함수를 먼저 완성하세요 — `nth_prime`의 핵심 부품입니다
• 2보다 작은 수는 소수가 아닙니다
• 2는 유일한 짝수 소수입니다
• 소수를 찾을 때마다 카운터를 증가시키고, 카운터가 `n`이 되면 멈추세요

## 🎪 코드 테스트

다음 테스트 케이스를 실행해보세요:

```python
# 테스트 1: is_prime 함수
print(is_prime(2))   # True
print(is_prime(4))   # False
print(is_prime(17))  # True
print(is_prime(1))   # False
print(is_prime(0))   # False

# 테스트 2: 작은 값의 nth_prime
print(nth_prime(1))   # 2
print(nth_prime(6))   # 13
print(nth_prime(10))  # 29

# 테스트 3: 최종 목표!
print(nth_prime(10001))  # ???
```

## 🤔 생각해보기

코딩을 시작하기 전에, 접근 방법을 스케치해보세요:

1. `is_prime(num)`에서 `num`이 소수인지 확인하려면 몇 개의 숫자로 나누어봐야 할까요?
2. `nth_prime(n)`에서 언제 멈춰야 할지 어떻게 알 수 있을까요?
3. 2는 특별한 경우입니다 — 어떻게 처리할까요?
4. **속도 체크:** 10,001번째 소수는 100,000이 넘습니다. 여러분의 코드는 몇 초 안에 실행되나요?

## 🎁 보너스 챌린지

기본 문제를 끝냈다면, 다음 도전에 뛰어들어 보세요!

### 🟢 Easy: 속도 개선 1단계
`is_prime`에서 2를 제외한 모든 짝수는 소수가 아닙니다. 짝수를 빠르게 걸러내어 속도를 2배로 높여보세요.

### 🟡 Medium: 속도 개선 2단계 (제곱근 최적화)
`num`이 소수인지 확인할 때, `num`의 **제곱근**까지만 확인하면 충분합니다. 왜 그럴까요?
힌트: 만약 `num = a × b`라면, `a`와 `b` 중 하나는 반드시 `√num` 이하입니다.

```python
# 예: 100 = 2 × 50 = 4 × 25 = 5 × 20 = 10 × 10
# √100 = 10, 10보다 큰 약수가 있다면 반드시 짝꿍 약수가 10 이하에 있음!
```

`num ** 0.5`를 사용해서 제곱근까지만 확인하도록 바꿔보세요.

### 🔴 Hard: 소수 목록 반환하기
`first_n_primes(n)` 함수를 작성하세요 — 처음 `n`개의 소수를 **리스트**로 반환합니다.

```python
print(first_n_primes(6))  # [2, 3, 5, 7, 11, 13]
```

---

막히면 스레드에 질문을 남겨주세요! 수학과 프로그래밍이 만나는 재미있는 문제입니다. 천천히 논리를 따라가 보세요.

행운을 빕니다! 🚀

---
---

# 🐍 Python Practice: Find the 10,001st Prime!

Hey team! Today we're tackling a classic problem that mathematicians have loved for centuries.

## 🎯 Your Mission

You're a junior developer at a cryptography research lab. A senior researcher walks up and says:

> "We need to test our security key generation system, and I need the **10,001st prime number**. Can you calculate it?"

The first six prime numbers are 2, 3, 5, 7, 11, and 13, so the 6th prime is 13. So... what is the 10,001st prime?

## 📋 The Rules

*What you're given:*
• An integer `n` (which prime number to find)

*What you need to do:*
1. Find and return the `n`-th prime number
2. Counting starts at 1 (the 1st prime is 2)

*Constraints you must follow:*
• **No `import` statements!** Pure Python only
• You don't need to store primes in a list — just counting is enough
• `n` will be a positive integer (1 or greater)

## 💡 Example Time

**Example 1:**
```
Input: n = 1
Output: 2
```
Why? The first prime is 2.

**Example 2:**
```
Input: n = 6
Output: 13
```
Why? Primes in order: 2, 3, 5, 7, 11, 13 → the 6th is 13.

**Example 3 (The Final Goal):**
```
Input: n = 10001
Output: ???
```
Figure it out yourself! 🎯

## 🎓 What You Should Know

Before you start coding, make sure you understand:
• The definition of a prime number (integer ≥ 2 divisible only by 1 and itself)
• How `while` loops keep running until a condition is met
• How `for` loops and `range()` work
• How `%` (modulo) checks for remainders
• Returning values from functions with `return`

## ✅ Your Task

Write two functions with these signatures:

```python
def is_prime(num: int) -> bool:
    """Check whether a number is prime."""
    # Your code here
    pass


def nth_prime(n: int) -> int:
    """Return the n-th prime number."""
    # Your code here
    pass
```

**Tips to get you started:**
• Build `is_prime` first — it's the building block for `nth_prime`
• Numbers less than 2 are not prime
• 2 is the only even prime number
• Every time you find a prime, increase a counter — stop when the counter reaches `n`

## 🎪 Test Your Code

Try running these test cases:

```python
# Test 1: is_prime function
print(is_prime(2))   # True
print(is_prime(4))   # False
print(is_prime(17))  # True
print(is_prime(1))   # False
print(is_prime(0))   # False

# Test 2: nth_prime for small values
print(nth_prime(1))   # 2
print(nth_prime(6))   # 13
print(nth_prime(10))  # 29

# Test 3: The final goal!
print(nth_prime(10001))  # ???
```

## 🤔 Think About It

Before you start coding, sketch out your approach:

1. For `is_prime(num)`, how many numbers do you need to try dividing by?
2. For `nth_prime(n)`, how do you know when to stop?
3. 2 is a special case — how will you handle it?
4. **Speed check:** The 10,001st prime is over 100,000. How many seconds does your code take?

## 🎁 Bonus Challenges

Finished the core task? Jump into these!

### 🟢 Easy: Speed Boost 1
In `is_prime`, every even number except 2 is not prime. Filter out evens quickly to double your speed.

### 🟡 Medium: Speed Boost 2 (Square Root Optimization)
When checking if `num` is prime, you only need to check divisors up to the **square root** of `num`. Why?
Hint: If `num = a × b`, then one of `a` or `b` must be ≤ `√num`.

```python
# Example: 100 = 2 × 50 = 4 × 25 = 5 × 20 = 10 × 10
# √100 = 10 — any divisor above 10 must pair with one at or below 10!
```

Try using `num ** 0.5` to only check up to the square root.

### 🔴 Hard: Return the List of Primes
Write a function `first_n_primes(n)` that returns the first `n` primes as a **list**.

```python
print(first_n_primes(6))  # [2, 3, 5, 7, 11, 13]
```

---

Drop your questions in the thread if you get stuck! This is a fun problem where math meets programming. Take your time and follow the logic step by step.

Good luck! 🚀
