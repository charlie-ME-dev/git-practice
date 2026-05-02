# 🐍 Python 연습: 소수를 찾아라! (에라토스테네스의 체)

여러분, 안녕하세요! 오늘은 2,000년도 더 된 수학자의 아이디어로 소수를 찾아봅시다. 준비됐나요? 🎉

---

## 🧮 에라토스테네스의 체란?

**에라토스테네스(Eratosthenes)** 는 고대 그리스의 수학자입니다. 그는 소수를 찾는 기막힌 방법을 고안했는데, 마치 체(sieve)로 숫자들을 걸러내는 것과 같아서 **"에라토스테네스의 체"** 라고 불립니다.

### 📐 방법은 이렇습니다

1부터 100까지의 숫자가 담긴 리스트를 상상해보세요.

```
단계 1: 1을 제거합니다 — 1은 소수가 아닙니다.

단계 2: 2는 소수입니다! ✅
         그런데 2의 배수(4, 6, 8, ...)는 모두 소수가 아닙니다. ❌ 제거!

단계 3: 3은 소수입니다! ✅
         3의 배수(6, 9, 12, ...)는 모두 소수가 아닙니다. ❌ 제거!

단계 4: 4는 이미 제거됐습니다. 건너뜁니다.

단계 5: 5는 소수입니다! ✅
         5의 배수(10, 15, 20, ...)를 제거합니다. ❌

... 이 과정을 반복하면 ...

남은 숫자들이 바로 소수입니다! 🎯
```

### 💡 핵심 아이디어

리스트를 직접 만들어 숫자가 소수인지 아닌지를 `True` / `False` 로 표시합니다.
처음에는 모두 `True` (소수 후보)로 시작하고, 배수를 발견할 때마다 `False` 로 바꿉니다.
마지막에 `True` 로 남은 인덱스들이 소수입니다!

```
인덱스:  0      1      2     3     4      5     6      ...
값:    False  False  True  True  False  True  False  ...
        (0)    (1)    (2)   (3)   (4)    (5)   (6)
```

---

## 🎯 미션

여러분은 **데이터 분석 인턴**입니다! 팀장이 1부터 100 사이의 모든 소수 목록이 필요하다고 했습니다. 에라토스테네스의 체 방법을 사용해서 소수 리스트를 만들어 제출하세요.

---

## 📋 규칙

*주어지는 것:*
• 찾을 범위: 1 이상 100 이하의 정수

*해야 할 일:*
1. 크기 101짜리 `is_prime` 리스트를 만들고 모두 `True` 로 초기화
2. `is_prime[0]` 과 `is_prime[1]` 을 `False` 로 설정 (0과 1은 소수가 아님)
3. 2부터 시작하여 각 숫자의 배수를 `False` 로 표시
4. 마지막에 `True` 로 남은 인덱스들을 모아 소수 리스트 반환

*반드시 따라야 할 제약사항:*
• 함수 이름과 변수 이름은 **snake_case** 로 작성
• `is_prime` 리스트를 활용할 것
• 외부 라이브러리 사용 금지 (순수 Python만 사용!)

---

## 💡 예제

```
입력: 범위 없음 (항상 1~100)
출력: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, ...]
```

왜? 2는 소수, 3은 소수, 4는 2의 배수라 제거, 5는 소수 ... 이런 식으로 걸러냅니다!

---

## 🎓 알아야 할 것

코딩을 시작하기 전에, 다음을 이해하고 있는지 확인하세요:
• `for` 루프로 범위를 반복하는 방법 (`range()`)
• 리스트에 같은 값을 여러 개 넣는 방법 (`[True] * 101`)
• 리스트 인덱싱 (`is_prime[i]`)
• `if` 조건문으로 값을 확인하는 방법

---

## ✅ 과제

다음 시그니처로 함수를 작성하세요:

```python
def find_primes_up_to_100() -> list[int]:
    # 1단계: is_prime 리스트 초기화 (크기 101, 모두 True)
    # TODO: 여기에 코드 작성

    # 2단계: 0과 1은 소수가 아님
    # TODO: 여기에 코드 작성

    # 3단계: 2부터 100까지 반복하며 배수 제거
    # TODO: 여기에 코드 작성

    # 4단계: True로 남은 인덱스만 모아서 반환
    # TODO: 여기에 코드 작성
    pass
```

*시작하는 데 도움이 될 팁:*
• `[True] * 101` 로 리스트를 한 번에 만들 수 있어요
• 배수를 제거할 때 `i * 2` 부터 시작해서 `i` 씩 건너뛰세요
• `range(start, stop, step)` 의 세 번째 인자를 활용해보세요!

---

## 🎪 코드 테스트

다음 테스트 케이스를 실행해보세요:

```python
primes = find_primes_up_to_100()
print(f"소수의 개수: {len(primes)}")
print(f"소수 목록: {primes}")
# 예상: 소수의 개수: 25
# 예상: 소수 목록: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
#                   43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

# 경계값 확인
print(f"가장 작은 소수: {primes[0]}")   # 예상: 2
print(f"가장 큰 소수: {primes[-1]}")    # 예상: 97
print(f"97은 소수인가? {97 in primes}") # 예상: True
print(f"100은 소수인가? {100 in primes}") # 예상: False
```

---

## 🤔 생각해보기

코딩을 시작하기 전에, 접근 방법을 스케치해보세요:
1. `is_prime` 리스트의 인덱스와 실제 숫자가 어떻게 대응되나요?
2. 숫자 `i` 의 배수는 어디서부터 시작해서 어떻게 건너뛰어야 할까요?
3. 최종적으로 소수 목록을 어떻게 모을 수 있을까요?

막히면 스레드에 질문을 남겨주세요! 목표는 끝내는 것이 아니라 배우는 것입니다. 천천히 논리를 이해하면서 진행하세요.

행운을 빕니다! 🚀

---
---

# 🐍 Python Practice: Hunt for Prime Numbers! (Sieve of Eratosthenes)

Hey team! Today we're using a 2,000-year-old mathematician's trick to find prime numbers. Let's go! 🎉

---

## 🧮 What Is the Sieve of Eratosthenes?

**Eratosthenes** was an ancient Greek mathematician. He invented a brilliant method for finding prime numbers — it works like a sieve (a strainer), filtering out non-primes until only the primes remain. That's why it's called the **"Sieve of Eratosthenes."**

### 📐 Here's How It Works

Imagine a list of numbers from 1 to 100.

```
Step 1: Remove 1 — it is NOT a prime number.

Step 2: 2 is prime! ✅
         All multiples of 2 (4, 6, 8, ...) are NOT prime. ❌ Remove them!

Step 3: 3 is prime! ✅
         All multiples of 3 (6, 9, 12, ...) are NOT prime. ❌ Remove them!

Step 4: 4 is already removed. Skip it.

Step 5: 5 is prime! ✅
         All multiples of 5 (10, 15, 20, ...) are NOT prime. ❌ Remove them!

... repeat this process ...

Whatever numbers are left — those are your primes! 🎯
```

### 💡 The Core Idea

We create a list and mark each number as `True` (prime candidate) or `False` (not prime).
We start with everything as `True`, and flip multiples to `False` as we go.
At the end, the indices still marked `True` are the primes!

```
Index:  0      1      2     3     4      5     6      ...
Value: False  False  True  True  False  True  False  ...
        (0)    (1)    (2)   (3)   (4)    (5)   (6)
```

---

## 🎯 Your Mission

You're a **data analysis intern**! Your team lead needs a list of all prime numbers between 1 and 100. Use the Sieve of Eratosthenes to build and return that list.

---

## 📋 The Rules

*What you're given:*
• A fixed range: integers from 1 to 100

*What you need to do:*
1. Create an `is_prime` list of size 101 and initialize everything to `True`
2. Set `is_prime[0]` and `is_prime[1]` to `False` (0 and 1 are not primes)
3. Starting from 2, mark all multiples of each number as `False`
4. Collect all indices still marked `True` and return them as the prime list

*Constraints you must follow:*
• All function and variable names in **snake_case**
• Use the `is_prime` list as your core data structure
• No external libraries — pure Python only!

---

## 💡 Example

```
Input: none (always searches 1–100)
Output: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, ...]
```

Why? 2 is prime, 3 is prime, 4 gets removed as a multiple of 2, 5 is prime... and so on!

---

## 🎓 What You Should Know

Before you start coding, make sure you're comfortable with:
• Using `for` loops with a range (`range()`)
• Creating a list with repeated values (`[True] * 101`)
• List indexing (`is_prime[i]`)
• Using `if` statements to check values

---

## ✅ Your Task

Write a function with this signature:

```python
def find_primes_up_to_100() -> list[int]:
    # Step 1: Initialize is_prime list (size 101, all True)
    # TODO: Your code here

    # Step 2: 0 and 1 are not primes
    # TODO: Your code here

    # Step 3: Loop from 2 to 100, marking multiples as False
    # TODO: Your code here

    # Step 4: Collect and return all indices still marked True
    # TODO: Your code here
    pass
```

*Tips to get you started:*
• `[True] * 101` creates a list of 101 `True` values all at once
• When marking multiples of `i`, start at `i * 2` and step by `i`
• Try the third argument of `range(start, stop, step)` — it's perfect here!

---

## 🎪 Test Your Code

Try running these test cases:

```python
primes = find_primes_up_to_100()
print(f"Number of primes: {len(primes)}")
print(f"Prime list: {primes}")
# Expected: Number of primes: 25
# Expected: Prime list: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
#                        43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

# Boundary checks
print(f"Smallest prime: {primes[0]}")      # Expected: 2
print(f"Largest prime: {primes[-1]}")      # Expected: 97
print(f"Is 97 prime? {97 in primes}")      # Expected: True
print(f"Is 100 prime? {100 in primes}")    # Expected: False
```

---

## 🤔 Think About It

Before you start coding, sketch out your approach:
1. How does the index of `is_prime` correspond to the actual number?
2. For a number `i`, where do its multiples start, and how do you skip through them?
3. How will you collect the final list of primes at the end?

Drop your questions in the thread if you get stuck! Remember, the goal is to learn, not just to finish. Take your time and understand the logic.

Good luck! 🚀
