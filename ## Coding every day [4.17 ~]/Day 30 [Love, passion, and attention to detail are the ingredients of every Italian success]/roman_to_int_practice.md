# 🏛️ Python 연습: 로마 숫자를 정수로 바꾸기!

안녕하세요, 주니어 개발자 여러분! 오늘 여러분은 박물관 큐레이터를 돕는 임무를 맡았습니다. 박물관에는 로마 숫자로 연도가 새겨진 유물이 수천 개 있는데, 큐레이터는 이것을 현대 숫자로 변환해서 데이터베이스에 정리하고 싶어합니다. 여러분의 프로그램이 바로 그 변환기입니다! 🏺

## 🎯 미션

로마 숫자 문자열을 받아서 해당하는 정수로 변환하는 함수를 작성하세요.

## 📜 로마 숫자 기본 규칙

로마 숫자는 7개의 기호로 구성됩니다:

```
기호  값
 I    1
 V    5
 X    10
 L    50
 C    100
 D    500
 M    1000
```

**규칙 1 — 보통은 더하기 (왼쪽부터 큰 순서):**
• `III` = 1 + 1 + 1 = **3**
• `XII` = 10 + 1 + 1 = **12**
• `XXVII` = 10 + 10 + 5 + 1 + 1 = **27**

**규칙 2 — 작은 숫자가 큰 숫자 앞에 있으면 빼기:**
4는 `IIII`가 아니라 `IV`로 씁니다 (5에서 1을 뺀 값).
9는 `IX`로 씁니다 (10에서 1을 뺀 값).

뺄셈이 적용되는 경우는 딱 6가지뿐입니다:
• `IV` = 4, `IX` = 9
• `XL` = 40, `XC` = 90
• `CD` = 400, `CM` = 900

## 📋 규칙

*주어지는 것:*
• `s`라는 문자열 (유효한 로마 숫자)
• 길이: 1 ~ 15자
• 값의 범위: 1 ~ 3999
• 사용되는 문자: `I`, `V`, `X`, `L`, `C`, `D`, `M`만 포함

*해야 할 일:*
1. 문자열을 왼쪽부터 오른쪽으로 하나씩 읽기
2. 현재 문자의 값과 다음 문자의 값을 비교
3. 현재 값이 다음 값보다 작으면 → **빼기**
4. 그렇지 않으면 → **더하기**
5. 최종 합계를 반환

## 💡 예제

**예제 1:**
```
입력: s = "III"
출력: 3
설명: I + I + I = 1 + 1 + 1 = 3
```

**예제 2:**
```
입력: s = "LVIII"
출력: 58
설명: L + V + I + I + I = 50 + 5 + 1 + 1 + 1 = 58
```

**예제 3:**
```
입력: s = "MCMXCIV"
출력: 1994
설명: M + CM + XC + IV = 1000 + 900 + 90 + 4 = 1994
```

마지막 예제를 잘 보세요! `CM`, `XC`, `IV`는 각각 뺄셈 쌍입니다.

## 🎓 알아야 할 것

코딩을 시작하기 전에, 다음을 이해하고 있는지 확인하세요:
• 문자열을 인덱스로 접근하는 방법 (`s[i]`)
• `for` 반복문 또는 `while` 반복문
• `if` / `elif` / `else` 조건문
• 문자열의 길이를 구하는 방법 (`len(s)`)
• 변수에 값을 누적하는 방법 (`total = total + value`)

## ✅ 과제

다음 시그니처로 함수를 작성하세요:

```python
def roman_to_int(s: str) -> int:
    # 여기에 코드 작성
    pass
```

**시작하는 데 도움이 될 팁:**
• 각 로마 기호의 값을 먼저 알아내는 함수를 만들어보세요 (`if`/`elif` 체인)
• 문자열을 왼쪽에서 오른쪽으로 순회하세요
• 각 위치에서 "현재 문자의 값이 다음 문자의 값보다 작은가?"를 확인하세요
• 작다면 빼고, 아니면 더하세요
• ⚠️ 마지막 문자는 "다음 문자"가 없으니 조심하세요!

## 🎪 코드 테스트

다음 테스트 케이스를 실행해보세요:

```python
# 테스트 1: 기본 더하기
print(roman_to_int("III"))       # 예상: 3

# 테스트 2: 뺄셈 쌍
print(roman_to_int("IV"))        # 예상: 4
print(roman_to_int("IX"))        # 예상: 9

# 테스트 3: 혼합
print(roman_to_int("LVIII"))     # 예상: 58

# 테스트 4: 복잡한 혼합
print(roman_to_int("MCMXCIV"))   # 예상: 1994

# 테스트 5: 경계값 (가장 작은 값)
print(roman_to_int("I"))         # 예상: 1

# 테스트 6: 경계값 (가장 큰 값)
print(roman_to_int("MMMCMXCIX")) # 예상: 3999
```

## 🤔 생각해보기

코딩을 시작하기 전에, 접근 방법을 스케치해보세요:
1. 문자열의 각 문자에 대응하는 숫자 값을 어떻게 얻을 수 있을까요?
2. "다음 문자가 현재 문자보다 크다"는 것을 어떻게 코드로 표현할까요?
3. 문자열의 **마지막 문자**를 처리할 때 주의할 점은 무엇일까요? (다음 문자가 없어요!)
4. 왜 "작은 값이 큰 값 앞에 있으면 빼기" 규칙이 왼쪽부터 스캔하는 방식에서 자연스럽게 작동할까요?

## 🎁 보너스 도전

기본 과제를 완료했다면, 다음 도전도 시도해보세요:

**🟢 Easy:** 각 문자를 값으로 바꿔주는 헬퍼 함수 `get_value(ch)`를 따로 만들어서, 메인 함수에서 호출하도록 리팩토링해보세요.

**🟡 Medium:** 오른쪽에서 왼쪽으로 스캔하는 버전으로도 풀어보세요. (힌트: 지금까지 본 최댓값보다 작으면 빼고, 아니면 더하기.)

**🔴 Hard (미리보기):** 아직 배우지 않은 **딕셔너리(dictionary)** 를 활용한 더 우아한 풀이에 도전해보세요. 다음과 같이 시작할 수 있어요:
```python
roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
# roman_values['X'] 는 10 을 반환합니다!
```
이 기능을 사용하면 `if`/`elif` 체인을 한 줄로 바꿀 수 있습니다. 곧 수업에서 배울 개념이에요!

막히면 스레드에 질문을 남겨주세요! 목표는 끝내는 것이 아니라 **왜 그렇게 작동하는지** 이해하는 것입니다. 천천히 논리를 따라가보세요.

행운을 빕니다! 🏛️⚔️

---
---

# 🏛️ Python Practice: Roman Numerals to Integers!

Hey there, junior developers! Today you're helping a museum curator. The museum has thousands of artifacts with years carved in Roman numerals, and the curator wants to convert them to modern numbers to organize the database. Your program is the converter! 🏺

## 🎯 Your Mission

Write a function that takes a Roman numeral string and returns its integer value.

## 📜 Roman Numeral Basics

Roman numerals use 7 symbols:

```
Symbol  Value
  I     1
  V     5
  X     10
  L     50
  C     100
  D     500
  M     1000
```

**Rule 1 — Usually just add them up (left to right, big to small):**
• `III` = 1 + 1 + 1 = **3**
• `XII` = 10 + 1 + 1 = **12**
• `XXVII` = 10 + 10 + 5 + 1 + 1 = **27**

**Rule 2 — If a smaller numeral comes BEFORE a bigger one, subtract it:**
4 is not written as `IIII` but as `IV` (5 minus 1).
9 is written as `IX` (10 minus 1).

Only 6 subtraction cases exist:
• `IV` = 4, `IX` = 9
• `XL` = 40, `XC` = 90
• `CD` = 400, `CM` = 900

## 📋 The Rules

*What you're given:*
• A string `s` (a valid Roman numeral)
• Length: 1 to 15 characters
• Value range: 1 to 3999
• Characters used: only `I`, `V`, `X`, `L`, `C`, `D`, `M`

*What you need to do:*
1. Read the string character by character (left to right)
2. Compare each character's value with the NEXT one's value
3. If current < next → **subtract** it
4. Otherwise → **add** it
5. Return the total

## 💡 Examples

**Example 1:**
```
Input: s = "III"
Output: 3
Explanation: I + I + I = 1 + 1 + 1 = 3
```

**Example 2:**
```
Input: s = "LVIII"
Output: 58
Explanation: L + V + I + I + I = 50 + 5 + 1 + 1 + 1 = 58
```

**Example 3:**
```
Input: s = "MCMXCIV"
Output: 1994
Explanation: M + CM + XC + IV = 1000 + 900 + 90 + 4 = 1994
```

Look carefully at the last example! `CM`, `XC`, and `IV` are subtraction pairs.

## 🎓 What You Should Know

Before you start coding, make sure you understand:
• How to access a string by index (`s[i]`)
• `for` loops or `while` loops
• `if` / `elif` / `else` statements
• How to get the length of a string (`len(s)`)
• How to accumulate a running total (`total = total + value`)

## ✅ Your Task

Write a function with this signature:

```python
def roman_to_int(s: str) -> int:
    # Your code here
    pass
```

**Tips to get you started:**
• First, build a way to get the value of a single Roman symbol (using `if`/`elif`)
• Loop through the string from left to right
• At each position, ask: "Is the current value LESS than the next value?"
• If yes, subtract. If no, add.
• ⚠️ Watch out for the LAST character — it has no "next character"!

## 🎪 Test Your Code

Try running these test cases:

```python
# Test 1: Simple addition
print(roman_to_int("III"))       # Expected: 3

# Test 2: Subtraction pairs
print(roman_to_int("IV"))        # Expected: 4
print(roman_to_int("IX"))        # Expected: 9

# Test 3: Mixed
print(roman_to_int("LVIII"))     # Expected: 58

# Test 4: Complex mix
print(roman_to_int("MCMXCIV"))   # Expected: 1994

# Test 5: Edge case (smallest value)
print(roman_to_int("I"))         # Expected: 1

# Test 6: Edge case (largest value)
print(roman_to_int("MMMCMXCIX")) # Expected: 3999
```

## 🤔 Think About It

Before you start coding, sketch out your approach:
1. How will you get the integer value for each character?
2. How do you express "the next character is bigger than this one" in code?
3. What's special about the **last character** in the string? (No next character!)
4. Why does the "subtract if smaller comes before bigger" rule work naturally when scanning left to right?

## 🎁 Bonus Challenges

Once you've finished the core task, try these:

**🟢 Easy:** Refactor your code by pulling the character-to-value logic into a helper function `get_value(ch)`, and have your main function call it.

**🟡 Medium:** Try solving it by scanning from **right to left** instead. (Hint: keep track of the largest value seen so far. If the current value is smaller, subtract. Otherwise, add.)

**🔴 Hard (preview):** Try an elegant solution using a **dictionary** — a concept you haven't learned yet! You can start like this:
```python
roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
# roman_values['X'] returns 10!
```
With this, your `if`/`elif` chain becomes a single line. We'll cover this concept soon in class!

Drop your questions in the thread if you get stuck! Remember, the goal isn't to finish — it's to understand **why** your solution works. Take your time.

Good luck! 🏛️⚔️
