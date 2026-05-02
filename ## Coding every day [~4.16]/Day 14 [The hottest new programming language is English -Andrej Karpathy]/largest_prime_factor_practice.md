# 🐍 Python 연습: 가장 큰 소인수를 찾아라!

여러분, 안녕하세요! 오늘은 수학과 코딩이 만나는 흥미로운 챌린지입니다. 숫자를 분해해서 그 안에 숨어있는 가장 큰 소수를 찾아봅시다!

## 🔢 소인수분해란?

코딩을 시작하기 전에, 핵심 개념을 먼저 이해해봅시다.

**소수(Prime Number)** 란 1과 자기 자신으로만 나누어지는 1보다 큰 자연수입니다.
예: 2, 3, 5, 7, 11, 13 ...

**소인수분해(Prime Factorization)** 란 어떤 정수를 소수들의 곱으로 나타내는 것입니다.
산술의 기본 정리(Fundamental Theorem of Arithmetic)에 따르면, 1보다 큰 모든 정수는 소수들의 곱으로 *유일하게* 표현됩니다.

예를 들어:
```
12  = 2 × 2 × 3        → 소인수: 2, 3  (최대 소인수: 3)
100 = 2 × 2 × 5 × 5   → 소인수: 2, 5  (최대 소인수: 5)
13  = 13               → 13 자체가 소수! (최대 소인수: 13)
```

**어떻게 소인수를 찾을까요?**
가장 작은 소수인 2부터 시작해서, 나누어 떨어지면 계속 나눠줍니다. 더 이상 나눠지지 않으면 다음 수로 넘어갑니다. 이 과정을 반복하면 됩니다!

```
36을 분해해봅시다:
36 ÷ 2 = 18  → 2 발견!
18 ÷ 2 = 9   → 2 발견!
9  ÷ 2 = ?   → 나누어 떨어지지 않음, 다음으로!
9  ÷ 3 = 3   → 3 발견!
3  ÷ 3 = 1   → 3 발견!
결과: 36 = 2 × 2 × 3 × 3, 최대 소인수 = 3
```

## 🎯 미션

여러분은 보안 소프트웨어 회사의 주니어 개발자입니다! 암호화 알고리즘 팀에서 특정 숫자의 **최대 소인수(largest prime factor)** 를 빠르게 구하는 함수가 필요합니다. 이 함수를 작성하는 것이 여러분의 임무입니다.

## 📋 규칙

*주어지는 것:*
• 1보다 큰 정수 `n`

*해야 할 일:*
• `n`의 최대 소인수를 반환하세요

*반드시 따라야 할 제약사항:*
• **추가 리스트 사용 금지!** 몇 개의 변수만 사용하세요
• 루프를 사용해서 소인수를 하나씩 찾아나가세요
• `n`이 소수라면, `n` 자체가 최대 소인수입니다

## 💡 예제

**예제 1:**
```
입력: n = 12
출력: 3
```
왜? 12 = 2 × 2 × 3, 소인수는 2와 3이고, 그 중 가장 큰 것은 3입니다.

**예제 2:**
```
입력: n = 100
출력: 5
```
왜? 100 = 2 × 2 × 5 × 5, 소인수는 2와 5이고, 가장 큰 것은 5입니다.

**예제 3:**
```
입력: n = 13
출력: 13
```
왜? 13은 소수이므로, 13 자체가 최대 소인수입니다.

**예제 4:**
```
입력: n = 13195
출력: 29
```
왜? 13195 = 5 × 7 × 13 × 29, 가장 큰 소인수는 29입니다.

## 🎓 알아야 할 것

코딩을 시작하기 전에, 다음을 이해하고 있는지 확인하세요:
• `while` 루프 사용법
• 나머지 연산자 `%` 사용법 (나누어 떨어지는지 확인할 때!)
• 정수 나눗셈 `//` 사용법
• 변수에 값을 저장하고 업데이트하는 방법

## ✅ 과제

다음 시그니처로 함수를 작성하세요:
```python
def find_largest_prime_factor(n: int) -> int:
    # 여기에 코드 작성
    pass
```

**시작하는 데 도움이 될 팁:**
• 2부터 나누기를 시작하세요 — 가장 작은 소수니까요!
• `n % divisor == 0` 이면 나누어 떨어진다는 뜻입니다
• 나누어 떨어질 때마다 `n = n // divisor` 로 n을 줄여가세요
• 소인수를 발견할 때마다 `largest_factor` 를 업데이트하세요
• `divisor * divisor > n` 이 되면 루프를 멈춰도 됩니다 — 왜일까요? 🤔
• 루프가 끝난 후 `n > 1` 이라면, 그 `n`은 소수입니다!

## 🎪 코드 테스트

다음 테스트 케이스를 실행해보세요:

```python
# 테스트 1: 합성수
print(find_largest_prime_factor(12))
# 예상: 3  (12 = 2 × 2 × 3)

# 테스트 2: 완전 제곱수
print(find_largest_prime_factor(100))
# 예상: 5  (100 = 2 × 2 × 5 × 5)

# 테스트 3: 소수 입력
print(find_largest_prime_factor(13))
# 예상: 13  (13은 소수)

# 테스트 4: 큰 수
print(find_largest_prime_factor(13195))
# 예상: 29  (13195 = 5 × 7 × 13 × 29)

# 테스트 5: 경계값
print(find_largest_prime_factor(2))
# 예상: 2  (2는 소수)
```

## 🤔 생각해보기

코딩을 시작하기 전에, 접근 방법을 스케치해보세요:
1. `n`을 어떤 수로 나누기 시작할까요? 왜 그 수부터 시작하나요?
2. 같은 소인수가 여러 번 나올 수 있을까요? (예: 12 = 2 × 2 × 3에서 2가 두 번!)
3. 루프가 끝난 후 `n`이 1보다 크면 어떤 의미일까요?
4. `divisor * divisor <= n` 까지만 확인하면 충분한 이유가 뭘까요?

막히면 스레드에 질문을 남겨주세요! 목표는 끝내는 것이 아니라 배우는 것입니다. 천천히 논리를 이해하면서 진행하세요.

행운을 빕니다! 🚀

## 🌟 보너스 챌린지

기본 문제를 풀었다면 도전해보세요!

**Easy:** 모든 소인수를 리스트로 반환하는 함수 `get_all_prime_factors(n)` 를 작성해보세요. (중복 포함)
```
get_all_prime_factors(12) → [2, 2, 3]
get_all_prime_factors(100) → [2, 2, 5, 5]
```

**Medium:** 짝수를 먼저 처리하고, 그 다음에는 홀수만 확인하도록 최적화해보세요. 왜 홀수만 확인해도 될까요?

**Hard:** `n = 600851475143` 의 최대 소인수를 구해보세요. (힌트: Project Euler Problem 3!) 기본 풀이와 최적화 풀이의 속도 차이가 느껴지나요?

---
---

# 🐍 Python Practice: Find the Largest Prime Factor!

Hey team! Today's challenge is where math meets coding. We're going to break numbers apart and find the largest prime hiding inside them!

## 🔢 What is Prime Factorization?

Before we start coding, let's understand the key concept.

A **prime number** is any number greater than 1 that can only be divided evenly by 1 and itself.
Examples: 2, 3, 5, 7, 11, 13 ...

**Prime factorization** means expressing an integer as a product of prime numbers.
According to the Fundamental Theorem of Arithmetic, every integer greater than 1 can be *uniquely* expressed as a product of primes.

For example:
```
12  = 2 × 2 × 3        → prime factors: 2, 3  (largest: 3)
100 = 2 × 2 × 5 × 5   → prime factors: 2, 5  (largest: 5)
13  = 13               → 13 is prime itself! (largest: 13)
```

**How do we find prime factors?**
Start from the smallest prime, 2. If it divides evenly, keep dividing. When it no longer divides, move to the next number. Repeat until done!

```
Let's factor 36:
36 ÷ 2 = 18  → found 2!
18 ÷ 2 = 9   → found 2!
9  ÷ 2 = ?   → doesn't divide evenly, move on!
9  ÷ 3 = 3   → found 3!
3  ÷ 3 = 1   → found 3!
Result: 36 = 2 × 2 × 3 × 3, largest prime factor = 3
```

## 🎯 Your Mission

You're a junior developer at a cybersecurity software company! The encryption team needs a function that quickly finds the **largest prime factor** of a given number. That function is yours to write.

## 📋 The Rules

*What you're given:*
• An integer `n` greater than 1

*What you need to do:*
• Return the largest prime factor of `n`

*Constraints you must follow:*
• **No extra lists!** Use only a few variables
• Use a loop to find prime factors one by one
• If `n` is prime, then `n` itself is the largest prime factor

## 💡 Example Time

**Example 1:**
```
Input: n = 12
Output: 3
```
Why? 12 = 2 × 2 × 3, the prime factors are 2 and 3, and the largest is 3.

**Example 2:**
```
Input: n = 100
Output: 5
```
Why? 100 = 2 × 2 × 5 × 5, the prime factors are 2 and 5, and the largest is 5.

**Example 3:**
```
Input: n = 13
Output: 13
```
Why? 13 is a prime number, so 13 itself is the largest prime factor.

**Example 4:**
```
Input: n = 13195
Output: 29
```
Why? 13195 = 5 × 7 × 13 × 29, so the largest prime factor is 29.

## 🎓 What You Should Know

Before you start coding, make sure you understand:
• How to use a `while` loop
• How to use the modulo operator `%` (to check if something divides evenly!)
• How to use integer division `//`
• How to store and update a value in a variable

## ✅ Your Task

Write a function with this signature:
```python
def find_largest_prime_factor(n: int) -> int:
    # Your code here
    pass
```

**Tips to get you started:**
• Start dividing from 2 — it's the smallest prime!
• `n % divisor == 0` means it divides evenly
• Each time it divides evenly, shrink n with `n = n // divisor`
• Every time you find a prime factor, update `largest_factor`
• You can stop when `divisor * divisor > n` — can you figure out why? 🤔
• After the loop, if `n > 1`, then that remaining `n` is itself a prime!

## 🎪 Test Your Code

Try running these test cases:

```python
# Test 1: composite number
print(find_largest_prime_factor(12))
# Expected: 3  (12 = 2 × 2 × 3)

# Test 2: perfect square
print(find_largest_prime_factor(100))
# Expected: 5  (100 = 2 × 2 × 5 × 5)

# Test 3: prime input
print(find_largest_prime_factor(13))
# Expected: 13  (13 is prime)

# Test 4: larger number
print(find_largest_prime_factor(13195))
# Expected: 29  (13195 = 5 × 7 × 13 × 29)

# Test 5: boundary value
print(find_largest_prime_factor(2))
# Expected: 2  (2 is prime)
```

## 🤔 Think About It

Before you start coding, sketch out your approach:
1. What number should you start dividing by? Why that one?
2. Can the same prime factor appear more than once? (e.g., 12 = 2 × 2 × 3, where 2 appears twice!)
3. After the loop ends, what does it mean if `n` is still greater than 1?
4. Why is it enough to only check up to `divisor * divisor <= n`?

Drop your questions in the thread if you get stuck! Remember, the goal is to learn, not just to finish. Take your time and understand the logic.

Good luck! 🚀

## 🌟 Bonus Challenges

Finished the main problem? Give these a try!

**Easy:** Write a function `get_all_prime_factors(n)` that returns all prime factors as a list (including duplicates).
```
get_all_prime_factors(12) → [2, 2, 3]
get_all_prime_factors(100) → [2, 2, 5, 5]
```

**Medium:** Optimize your solution by handling even numbers first, then checking only odd divisors. Why is it safe to skip even numbers after handling 2?

**Hard:** Find the largest prime factor of `n = 600851475143`. (Hint: this is Project Euler Problem 3!) Can you feel the speed difference between the basic and optimized solutions?
