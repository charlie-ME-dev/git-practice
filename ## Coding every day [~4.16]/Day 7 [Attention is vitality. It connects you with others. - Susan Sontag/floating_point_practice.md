# 🐍 Python 연습: 왜 62.8이 아니라 62.800000000000004일까?

여러분, 안녕하세요! 이번 문제는 계산 결과가 이상하게 나오는 현상을 탐구합니다. 버그가 아니에요 — Python이 숫자를 저장하는 방식 때문에 생기는 현상입니다. 끝까지 읽으면 컴퓨터 과학의 핵심 개념 하나를 이해하게 됩니다! 🧠

## 🎯 미션

반지름이 10.0인 원의 **둘레**와 **면적**을 계산하고 출력하세요. 그런데 아래 코드를 그대로 실행하면 이런 결과가 나옵니다:

```
원의 반지름 10.0
원의 면적 314.0
원의 둘레 62.800000000000004   ← 🤔 이게 뭔가요?
```

왜 `62.8`이 아니라 `62.800000000000004`가 나올까요? 그리고 어떻게 고칠 수 있을까요?

## 📋 주어진 코드

```python
radius = 10.0
print('원의 반지름', radius)
print('원의 면적', 3.14 * radius**2)
print('원의 둘레', 2.0 * 3.14 * radius)
```

## 🔍 왜 이런 일이 생길까요?

컴퓨터는 모든 숫자를 **이진수(0과 1)**로 저장합니다. 그런데 `3.14` 같은 소수는 이진수로 **정확하게** 표현할 수 없어요.

일상에서 비슷한 예를 들어볼게요:
- 1/3을 소수로 쓰면? → 0.333333333... (끝이 없어요!)
- 마찬가지로, 컴퓨터는 `3.14`를 이진수로 저장할 때 아주 긴 근삿값을 씁니다

그래서 `2.0 * 3.14 * 10.0`을 계산하면:
```
정확한 답:  62.8
컴퓨터 계산: 62.800000000000004  ← 이진수 오차가 끝에 붙어요!
```

이것을 **부동소수점 오차(floating point error)**라고 합니다. Python만의 문제가 아니라 Java, C, JavaScript 등 거의 모든 프로그래밍 언어에서 발생합니다!

## 🖥️ 컴퓨터는 소수를 어떻게 저장할까요?

Python의 소수(float)는 **IEEE 754 배정밀도(double precision)** 표준을 따릅니다. 이 표준은 64비트(0과 1 총 64개)를 세 구역으로 나눠 하나의 소수를 표현합니다:

```
 63      62–52        51–0
┌────┬───────────┬──────────────────────────────────────────────────┐
│ 부호│   지수부   │                     가수부                        │
│  1 │   11비트  │                    52비트                         │
└────┴───────────┴──────────────────────────────────────────────────┘
```

• **부호(1비트)** — 양수(0)인지 음수(1)인지 나타냅니다
• **지수부(11비트)** — 소수점의 위치를 나타냅니다 (몇 자리 수인지)
• **가수부(52비트)** — 실제 숫자의 값을 나타냅니다

마치 과학적 표기법과 비슷해요:
```
3.14  →  1.57 × 2¹   (지수: 1, 가수: 1.57)
10.0  →  1.25 × 2³   (지수: 3, 가수: 1.25)
```

**핵심 문제:** 가수부는 52비트로 고정되어 있습니다. 그런데 `3.14`를 이진수로 변환하면 소수점 이하가 끝없이 이어집니다:

```
3.14 (10진수)
= 11.0010001111010111000010100011110101110000101000111101... (2진수, 끝이 없음!)
```

52비트에 맞게 잘라내면 오차가 생깁니다:
```
저장된 실제 값: 3.14000000000000012434497875801753252744674682617187500
```

그 오차가 곱셈을 거치면서 `62.800000000000004`로 나타나는 것입니다.

## 💡 두 가지 해결 방법

### 방법 1: `round()` 함수 사용
`round(숫자, 소수점_자리수)` — 지정한 자리수로 반올림합니다:
```python
print(round(2.0 * 3.14 * 10.0, 1))   # 출력: 62.8
```

### 방법 2: f-string 포맷 사용
`f'{값:.자리수f}'` — 소수점 자리수를 고정해서 출력합니다:
```python
print(f'{2.0 * 3.14 * 10.0:.1f}')    # 출력: 62.8
```

두 방법의 차이:
- `round()` → 값 자체를 반올림한 숫자로 바꿉니다
- f-string `:.1f` → 값은 그대로, 화면에 출력할 때만 자리수를 맞춥니다

## ✅ 과제

주어진 코드를 수정하여, 아래처럼 깔끔하게 출력되도록 만드세요:

```
원의 반지름 10.0
원의 면적 314.0
원의 둘레 62.8
```

**두 가지 버전을 모두 작성해보세요:**
1. `round()`를 사용한 버전
2. f-string `:.1f`를 사용한 버전

## 🤔 생각해보기

1. `원의 면적`은 왜 `314.0`으로 깔끔하게 나왔을까요? `2.0 * 3.14 * 10.0`은 오차가 생겼는데, `3.14 * 10.0**2`는 왜 괜찮았을까요?
2. `round(62.800000000000004, 2)`의 결과는 무엇일까요? 직접 실행해보세요!
3. 부동소수점 오차가 은행 시스템에서 발생하면 어떤 문제가 생길까요? 🏦

   > 예를 들어, 1원을 1000번 더하면 정확히 1000원이 나와야 할까요? Python에서 직접 확인해보세요:
   > ```python
   > total = 0.0
   > for i in range(1000):
   >     total += 0.001
   > print(total)
   > ```
   > 결과가 정확히 `1.0`인가요? 만약 은행이 수백만 건의 거래를 이런 방식으로 계산한다면, 작은 오차들이 쌓여서 실제 돈 계산이 틀려질 수 있습니다. 실제 금융 시스템에서는 이 문제를 피하기 위해 소수 대신 정수(예: 원 단위 정수)나 `decimal` 모듈 같은 특별한 도구를 사용합니다.

막히면 스레드에 질문을 남겨주세요! 목표는 끝내는 것이 아니라 배우는 것입니다.

행운을 빕니다! 🚀

---
---

# 🐍 Python Practice: Why 62.800000000000004 Instead of 62.8?

Hey team! This problem is about a strange-looking calculation result. It's not a bug — it's a consequence of how Python stores numbers internally. By the end, you'll understand one of the most important concepts in computer science! 🧠

## 🎯 Your Mission

Calculate and print the **circumference** and **area** of a circle with radius 10.0. But if you run the code below as-is, you get this:

```
원의 반지름 10.0
원의 면적 314.0
원의 둘레 62.800000000000004   ← 🤔 What is that?
```

Why does Python print `62.800000000000004` instead of `62.8`? And how can we fix it?

## 📋 The Starting Code

```python
radius = 10.0
print('원의 반지름', radius)
print('원의 면적', 3.14 * radius**2)
print('원의 둘레', 2.0 * 3.14 * radius)
```

## 🔍 Why Does This Happen?

Computers store all numbers in **binary (0s and 1s)**. But decimal numbers like `3.14` cannot be represented **exactly** in binary.

Here's a familiar analogy:
- What's 1/3 as a decimal? → 0.333333333... (it never ends!)
- Similarly, when a computer stores `3.14` in binary, it uses a very long approximation

So when Python calculates `2.0 * 3.14 * 10.0`:
```
Exact answer:        62.8
Computer calculates: 62.800000000000004  ← binary rounding error sneaks in!
```

This is called a **floating point error**. It's not a Python problem — it happens in Java, C, JavaScript, and almost every programming language!

## 🖥️ How Does a Computer Actually Store Decimals?

Python's decimal numbers (floats) follow the **IEEE 754 double precision** standard. This standard uses 64 bits (64 zeros and ones) split into three zones to represent a single decimal number:

```
 63      62–52        51–0
┌────┬───────────┬──────────────────────────────────────────────────┐
│Sign│  Exponent │                    Mantissa                      │
│ 1  │  11 bits  │                    52 bits                       │
└────┴───────────┴──────────────────────────────────────────────────┘
```

• **Sign (1 bit)** — is the number positive (0) or negative (1)?
• **Exponent (11 bits)** — where is the decimal point? (the scale of the number)
• **Mantissa (52 bits)** — what is the actual value?

It works similarly to scientific notation:
```
3.14  →  1.57 × 2¹   (exponent: 1, mantissa: 1.57)
10.0  →  1.25 × 2³   (exponent: 3, mantissa: 1.25)
```

**The core problem:** the mantissa is fixed at 52 bits. But when you convert `3.14` to binary, the digits after the decimal point go on forever:

```
3.14 (decimal)
= 11.0010001111010111000010100011110101110000101000111101... (binary, never ends!)
```

Cutting it off to fit in 52 bits introduces an error:
```
Actual stored value: 3.14000000000000012434497875801753252744674682617187500
```

That tiny error then gets amplified through multiplication, producing `62.800000000000004`.

## 💡 Two Ways to Fix It

### Method 1: `round()` function
`round(number, decimal_places)` — rounds to the specified number of decimal places:
```python
print(round(2.0 * 3.14 * 10.0, 1))   # Output: 62.8
```

### Method 2: f-string formatting
`f'{value:.decimal_placesf}'` — fixes the number of decimal places on output:
```python
print(f'{2.0 * 3.14 * 10.0:.1f}')    # Output: 62.8
```

The difference between the two:
- `round()` → actually changes the number itself by rounding it
- f-string `:.1f` → leaves the number unchanged, only controls how it's displayed

## ✅ Your Task

Modify the given code so the output looks clean like this:

```
원의 반지름 10.0
원의 면적 314.0
원의 둘레 62.8
```

**Write both versions:**
1. A version using `round()`
2. A version using f-string `:.1f`

## 🤔 Think About It

1. Why did `원의 면적` print cleanly as `314.0`? `2.0 * 3.14 * 10.0` had an error, but why didn't `3.14 * 10.0**2`?
2. What does `round(62.800000000000004, 2)` return? Try it and see!
3. If floating point errors happened in a banking system, what problems could that cause? 🏦

   > For example, if you add 0.001 won a thousand times, should you get exactly 1.0 won? Try it in Python:
   > ```python
   > total = 0.0
   > for i in range(1000):
   >     total += 0.001
   > print(total)
   > ```
   > Is the result exactly `1.0`? If a bank calculates millions of transactions this way, tiny errors can accumulate and make the actual money totals wrong. Real financial systems avoid this by working with integers (e.g. amounts in whole won) or using a special tool like Python's `decimal` module instead of regular floats.

Drop your questions in the thread if you get stuck! Remember, the goal is to learn, not just to finish.

Good luck! 🚀
