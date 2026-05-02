# 🐍 Python 연습: 가장 큰 대칭수를 찾아라!

여러분, 안녕하세요! 오늘은 수비학(numerology)의 세계로 빠져볼 실전 챌린지입니다. 숫자의 아름다운 대칭을 Python으로 탐험해봐요!

## 🎯 미션

여러분은 신생 핀테크(FinTech) 스타트업의 주니어 개발자입니다. 팀장이 흥미로운 과제를 던져줬어요:

> *"세 자리 수 두 개를 곱해서 만들 수 있는 가장 큰 대칭수(palindrome)를 찾아주세요. 이 패턴 분석이 우리 암호화 알고리즘의 기초가 될 거예요!"*

## 📖 대칭수(palindrome)란?

대칭수는 앞에서 읽으나 뒤에서 읽으나 똑같은 수입니다.

```
9009  → "9009"를 뒤집으면 "9009" ✅ 대칭수!
12321 → "12321"을 뒤집으면 "12321" ✅ 대칭수!
12345 → "12345"를 뒤집으면 "54321" ❌ 대칭수 아님
```

힌트: 두 자리 수 두 개를 곱해서 만들 수 있는 가장 큰 대칭수는 `9009 = 91 × 99`입니다. 세 자리 수로는?

## 📋 규칙

*입력:* 없음 — 세 자리 수의 범위(100~999)를 직접 탐색합니다

*해야 할 일:*
1. 어떤 수가 대칭수인지 판별하는 함수 작성
2. 세 자리 수 두 개의 모든 곱 중 가장 큰 대칭수 탐색
3. 그 대칭수를 반환

*제약사항:*
• **세 자리 수**는 100 이상 999 이하입니다
• 같은 수를 두 번 곱해도 됩니다 (예: 111 × 111)
• 두 함수를 작성해야 합니다 — 각각의 역할을 분리하세요!

## 💡 예제

```
두 자리 수 예시:
91 × 99 = 9009  → 대칭수 ✅
99 × 99 = 9801  → 대칭수 아님 ❌
91 × 91 = 8281  → 대칭수 아님 ❌

세 자리 수 예시 (직접 찾아보세요!):
100 × 100 = 10000 → ?
111 × 111 = 12321 → ?
```

## 🎓 알아야 할 것

코딩을 시작하기 전에, 다음을 이해하고 있는지 확인하세요:
• 문자열(string)로 변환하는 방법 — `str()`
• 문자열 슬라이싱으로 뒤집기 — `[::-1]`
• 중첩 반복문(nested loop)으로 모든 조합 탐색하기
• 최댓값을 추적하는 변수 사용법

## ✅ 과제

두 함수를 작성하세요:

```python
def is_palindrome_number(n: int) -> bool:
    # n이 대칭수이면 True, 아니면 False 반환
    pass


def find_largest_palindrome_product() -> int:
    # 세 자리 수 두 개의 곱 중 가장 큰 대칭수 반환
    pass
```

**시작하는 데 도움이 될 팁:**
• 숫자를 문자열로 바꾸면 뒤집기가 쉬워요: `str(9009)` → `"9009"`
• 문자열 슬라이싱 `[::-1]`으로 문자열을 뒤집을 수 있어요
• 중첩 반복문으로 세 자리 수의 모든 쌍을 확인하세요
• `largest` 변수를 0으로 시작해서, 더 큰 대칭수를 찾을 때마다 업데이트하세요

## 🎪 코드 테스트

```python
# 테스트 1: is_palindrome_number 확인
print(is_palindrome_number(9009))   # 예상: True
print(is_palindrome_number(12321))  # 예상: True
print(is_palindrome_number(12345))  # 예상: False
print(is_palindrome_number(11))     # 예상: True
print(is_palindrome_number(10))     # 예상: False

# 테스트 2: 최종 답
result = find_largest_palindrome_product()
print(f"가장 큰 대칭수: {result}")
print(f"대칭수 확인: {is_palindrome_number(result)}")
# 예상: 6자리 숫자가 출력되어야 합니다!
```

## 🤔 생각해보기

코딩을 시작하기 전에, 접근 방법을 스케치해보세요:
1. 숫자가 대칭수인지 확인하려면 어떻게 해야 할까요? (힌트: 문자열로 바꿔보세요)
2. 세 자리 수의 범위는 정확히 어디서부터 어디까지인가요?
3. 모든 쌍을 확인하면서 "지금까지 찾은 가장 큰 값"을 어떻게 기억할까요?
4. 이미 찾은 값보다 작은 수의 조합은 건너뛸 수 있을까요? (보너스 생각!)

막히면 스레드에 질문을 남겨주세요! 목표는 끝내는 것이 아니라 배우는 것입니다. 천천히 논리를 이해하면서 진행하세요.

행운을 빕니다! 🚀

---
---

# 🐍 Python Practice: Find the Largest Palindrome Product!

Hey team! Today we're diving into the elegant world of numeric symmetry. Let's explore palindromes with Python!

## 🎯 Your Mission

You're a junior developer at a growing FinTech startup. Your team lead just dropped an interesting task on your desk:

> *"Find the largest palindrome made from the product of two 3-digit numbers. This pattern analysis will be the foundation of our new encryption algorithm!"*

## 📖 What's a Palindrome Number?

A palindrome number reads the same forwards and backwards.

```
9009  → reversed: "9009" ✅ palindrome!
12321 → reversed: "12321" ✅ palindrome!
12345 → reversed: "54321" ❌ not a palindrome
```

Hint: The largest palindrome made from two 2-digit numbers is `9009 = 91 × 99`. Can you find the one for 3-digit numbers?

## 📋 The Rules

*Input:* None — you'll explore the range of 3-digit numbers (100–999) yourself

*What you need to do:*
1. Write a function to check if a number is a palindrome
2. Search through all products of two 3-digit numbers to find the largest palindrome
3. Return that palindrome

*Constraints:*
• **3-digit numbers** range from 100 to 999 (inclusive)
• A number can be multiplied by itself (e.g., 111 × 111 is valid)
• Write two functions — keep each responsibility separate!

## 💡 Example Time

```
2-digit example:
91 × 99 = 9009  → palindrome ✅
99 × 99 = 9801  → not a palindrome ❌
91 × 91 = 8281  → not a palindrome ❌

3-digit examples (find the pattern yourself!):
100 × 100 = 10000 → ?
111 × 111 = 12321 → ?
```

## 🎓 What You Should Know

Before you start coding, make sure you understand:
• How to convert a number to a string — `str()`
• How to reverse a string using slicing — `[::-1]`
• How nested loops explore all combinations
• How to track a running maximum with a variable

## ✅ Your Task

Write two functions:

```python
def is_palindrome_number(n: int) -> bool:
    # Return True if n is a palindrome, False otherwise
    pass


def find_largest_palindrome_product() -> int:
    # Return the largest palindrome made from two 3-digit numbers
    pass
```

**Tips to get you started:**
• Converting a number to a string makes reversing easy: `str(9009)` → `"9009"`
• String slicing `[::-1]` reverses a string
• Use a nested loop to check all pairs of 3-digit numbers
• Start `largest` at 0 and update it whenever you find a bigger palindrome

## 🎪 Test Your Code

```python
# Test 1: Check is_palindrome_number
print(is_palindrome_number(9009))   # Expected: True
print(is_palindrome_number(12321))  # Expected: True
print(is_palindrome_number(12345))  # Expected: False
print(is_palindrome_number(11))     # Expected: True
print(is_palindrome_number(10))     # Expected: False

# Test 2: Final answer
result = find_largest_palindrome_product()
print(f"Largest palindrome: {result}")
print(f"Palindrome check: {is_palindrome_number(result)}")
# Expected: a 6-digit number!
```

## 🤔 Think About It

Before you start coding, sketch out your approach:
1. How can you check if a number is a palindrome? (Hint: convert it to a string)
2. What is the exact range of 3-digit numbers?
3. How do you remember the "largest found so far" as you loop through all pairs?
4. Can you skip pairs whose product is already smaller than your current best? (Bonus thought!)

Drop your questions in the thread if you get stuck! Remember, the goal is to learn, not just to finish. Take your time and understand the logic.

Good luck! 🚀
