# 🐍 Python 연습: 시저 암호 만들기!

> *"암호학은 수학에서 시작되었습니다. 카이사르 시대부터 이미, 암호는 정수론과 수학적 원리를 바탕으로 발전해왔습니다."*
> — 제임스 샌본 (CIA 본부의 암호 조각상 *Kryptos*의 작가)

여러분, 안녕하세요! 오늘은 약 2,000년 전 로마 황제 율리우스 카이사르가 군사 메시지를 보호하기 위해 사용했던 암호를 직접 구현해봅니다.

## 🎯 미션

여러분은 한 스타트업의 신입 보안 엔지니어입니다. 회사가 사내 메시지를 간단하게 보호하는 프로토타입을 만들고 있는데, 가장 기본적인 암호화 방식인 **시저 암호(Caesar Cipher)** 를 Python으로 구현하는 임무를 맡았습니다.

**시저 암호란?** 알파벳의 각 글자를 정해진 칸 수만큼 뒤로 밀어서 다른 글자로 바꾸는 방식입니다.

예를 들어, 3칸 밀기(key=3)를 적용하면:
- `a` → `d`
- `b` → `e`
- `c` → `f`
- ...
- `x` → `a` (알파벳 끝에 도달하면 다시 처음으로 돌아옵니다!)
- `y` → `b`
- `z` → `c`

## 📋 규칙

*주어지는 것:*
• `message`: 암호화할 문자열 (영문, 숫자, 공백, 특수문자 포함 가능)
• `key`: 몇 칸 밀지 결정하는 정수 (예: 3, 7, 13, 25)

*해야 할 일:*
1. `message`의 각 글자를 확인
2. 영문자(A-Z, a-z)이면 `key`만큼 밀어서 변환
3. 영문자가 아니면 (숫자, 공백, 특수문자) 그대로 유지
4. 대문자는 대문자로, 소문자는 소문자로 유지
5. 알파벳 끝(z 또는 Z)을 넘어가면 처음(a 또는 A)으로 돌아가기

*반드시 따라야 할 제약사항:*
• `ord()`와 `chr()` 함수를 반드시 사용할 것
• 새로운 문자열을 만들어서 반환 (원본 message는 수정하지 않음)
• `key`가 26보다 크거나 0이어도 정상 동작해야 함 (예: key=27은 key=1과 같은 결과)

## 🔧 도구 소개: `ord()`와 `chr()`

이 문제를 풀기 위해 두 가지 내장 함수를 사용합니다:

**`ord(문자)`** → 문자를 숫자(아스키 코드)로 변환
```python
ord("A")  # 65
ord("a")  # 97
ord("Z")  # 90
ord("z")  # 122
```

**`chr(숫자)`** → 숫자(아스키 코드)를 문자로 변환
```python
chr(65)   # "A"
chr(97)   # "a"
chr(100)  # "d"
```

**핵심 관찰:**
- 알파벳은 연속된 숫자입니다 (A=65, B=66, C=67, ...)
- `ord("c") - ord("a")`는 `c`가 알파벳에서 몇 번째인지 알려줍니다 (0부터 시작)
- 글자를 밀려면? → 숫자로 바꿔서 더하고 → 다시 글자로 바꾸기!

## 💡 예제

**예제 1:**
```
입력: message = "hello", key = 3
출력: "khoor"
```
왜? h→k, e→h, l→o, l→o, o→r (각각 3칸씩 뒤로)

**예제 2:**
```
입력: message = "xyz", key = 3
출력: "abc"
```
왜? x→a, y→b, z→c (알파벳 끝을 넘어가면 다시 처음으로!)

**예제 3:**
```
입력: message = "Hello, World!", key = 5
출력: "Mjqqt, Btwqi!"
```
왜? 대문자는 대문자로, 소문자는 소문자로 유지! 쉼표, 공백, 느낌표는 그대로.

## 🎓 알아야 할 것

코딩을 시작하기 전에, 다음을 이해하고 있는지 확인하세요:
• 문자열을 `for` 루프로 반복하는 방법
• 문자열 비교 (예: `"a" <= char <= "z"`)
• `ord()`와 `chr()`의 사용법
• 모듈로 연산자 `%`로 "순환"을 구현하는 방법
• 함수 정의와 반환값

## ✅ 과제

다음 시그니처로 함수를 작성하세요:
```python
def caesar_encode(message: str, key: int) -> str:
    # 여기에 코드 작성
    pass
```

**시작하는 데 도움이 될 팁:**
• 빈 문자열 `result = ""`로 시작하고, 한 글자씩 추가해나가세요
• 글자를 밀 때 공식을 유도해보세요:
  - 소문자의 경우: `chr((ord(char) - ord("a") + key) % 26 + ord("a"))`
  - 왜 `% 26`을 쓸까요? (힌트: 알파벳이 26글자!)
• `if-elif-else` 구조로 대문자, 소문자, 그 외를 구분하세요

## 🎪 코드 테스트

다음 테스트 케이스를 실행해보세요:

```python
# 테스트 1: 기본 소문자
print(caesar_encode("hello", 3))
# 예상: khoor

# 테스트 2: 대문자
print(caesar_encode("HELLO", 3))
# 예상: KHOOR

# 테스트 3: 알파벳 끝 넘기기
print(caesar_encode("xyz", 3))
# 예상: abc

# 테스트 4: 혼합 (대소문자, 특수문자, 공백)
print(caesar_encode("Hello, World!", 5))
# 예상: Mjqqt, Btwqi!

# 테스트 5: 숫자와 특수문자 유지
print(caesar_encode("Python 3.10", 13))
# 예상: Clguba 3.10

# 테스트 6: key가 26 (한 바퀴 도는 경우)
print(caesar_encode("zebra", 26))
# 예상: zebra (변화 없음!)

# 테스트 7: key가 26보다 큰 경우
print(caesar_encode("abc", 27))
# 예상: bcd (key=1과 같은 결과)
```

## 🤔 생각해보기

코딩을 시작하기 전에, 접근 방법을 스케치해보세요:
1. 글자가 알파벳인지 어떻게 판단할 수 있을까요?
2. `a`를 0으로, `b`를 1로 만들려면 어떻게 해야 할까요?
3. `z` 다음에 다시 `a`로 돌아가게 하려면 어떤 연산자가 필요할까요?
4. 대문자와 소문자를 어떻게 다르게 처리할 수 있을까요?

## 🌟 보너스 도전 (선택)

기본 함수를 완성했다면, 다음 도전을 시도해보세요:

**🟢 Easy:** `caesar_decode(message, key)` 함수 만들기
- 암호화된 메시지를 원래대로 복호화하는 함수입니다
- 힌트: `caesar_encode(message, -key)`로 간단히 만들 수 있을까요?

**🟡 Medium:** 한글이나 다른 문자가 섞여 있어도 영문자만 암호화하고 나머지는 그대로 두기
- 예: `caesar_encode("안녕 hello!", 3)` → `"안녕 khoor!"`
- 이미 우리 코드가 이렇게 동작할까요? 확인해보세요!

**🔴 Hard:** 음수 key도 처리할 수 있도록 만들기
- 예: `caesar_encode("def", -3)` → `"abc"`
- 힌트: Python의 `%` 연산자는 음수에서 어떻게 동작하나요? 직접 실험해보세요!
- `(-1) % 26`의 결과가 무엇인가요?

---

막히면 스레드에 질문을 남겨주세요! 목표는 끝내는 것이 아니라 배우는 것입니다. 천천히 논리를 이해하면서 진행하세요.

행운을 빕니다! 🚀

---
---

# 🐍 Python Practice: Build a Caesar Cipher!

> *"Cryptography began in mathematics. Codes were developed, even from Caesar's time, based on number theory and mathematical principles."*
> — James Sanborn (sculptor of *Kryptos*, the encoded sculpture at CIA headquarters)

Hey team! Today we're implementing a cipher that Roman emperor Julius Caesar used about 2,000 years ago to protect his military messages.

## 🎯 Your Mission

You're a junior security engineer at a startup. The company is building a prototype to lightly protect internal messages, and you've been assigned to implement the most basic encryption method — the **Caesar Cipher** — in Python.

**What's a Caesar Cipher?** It shifts each letter of the alphabet forward by a fixed number of positions to produce a different letter.

For example, with a shift of 3 (key=3):
- `a` → `d`
- `b` → `e`
- `c` → `f`
- ...
- `x` → `a` (when you hit the end of the alphabet, you wrap back to the start!)
- `y` → `b`
- `z` → `c`

## 📋 The Rules

*What you're given:*
• `message`: a string to encrypt (may contain letters, numbers, spaces, special characters)
• `key`: an integer that decides how many positions to shift (e.g., 3, 7, 13, 25)

*What you need to do:*
1. Check each character in `message`
2. If it's a letter (A-Z, a-z), shift it by `key` positions
3. If it's not a letter (number, space, special character), keep it as-is
4. Keep uppercase as uppercase, lowercase as lowercase
5. Wrap around when you go past z (or Z) — back to a (or A)

*Constraints you must follow:*
• You **must use** `ord()` and `chr()` functions
• Return a **new** string (don't modify the original message)
• Must work correctly even if `key` is greater than 26 or equal to 0 (e.g., key=27 should give the same result as key=1)

## 🔧 Tool Introduction: `ord()` and `chr()`

To solve this problem, you'll use two built-in functions:

**`ord(character)`** → converts a character to its number (ASCII code)
```python
ord("A")  # 65
ord("a")  # 97
ord("Z")  # 90
ord("z")  # 122
```

**`chr(number)`** → converts a number (ASCII code) to a character
```python
chr(65)   # "A"
chr(97)   # "a"
chr(100)  # "d"
```

**Key observation:**
- Letters are consecutive numbers (A=65, B=66, C=67, ...)
- `ord("c") - ord("a")` tells you what position `c` is in the alphabet (starting from 0)
- To shift a letter? → convert to number → add → convert back to letter!

## 💡 Examples

**Example 1:**
```
Input: message = "hello", key = 3
Output: "khoor"
```
Why? h→k, e→h, l→o, l→o, o→r (each shifted 3 positions back)

**Example 2:**
```
Input: message = "xyz", key = 3
Output: "abc"
```
Why? x→a, y→b, z→c (when you hit the end of the alphabet, wrap back to start!)

**Example 3:**
```
Input: message = "Hello, World!", key = 5
Output: "Mjqqt, Btwqi!"
```
Why? Uppercase stays uppercase, lowercase stays lowercase! Comma, space, and exclamation mark are kept as-is.

## 🎓 What You Should Know

Before you start coding, make sure you understand:
• How to loop through a string with `for`
• String comparison (e.g., `"a" <= char <= "z"`)
• How to use `ord()` and `chr()`
• How to use the modulo operator `%` for "wrapping around"
• Function definition and return values

## ✅ Your Task

Write a function with this signature:
```python
def caesar_encode(message: str, key: int) -> str:
    # Your code here
    pass
```

**Tips to get you started:**
• Start with an empty string `result = ""` and add one character at a time
• Try to derive the formula for shifting a letter:
  - For lowercase: `chr((ord(char) - ord("a") + key) % 26 + ord("a"))`
  - Why `% 26`? (Hint: there are 26 letters in the alphabet!)
• Use `if-elif-else` to handle uppercase, lowercase, and other cases

## 🎪 Test Your Code

Try running these test cases:

```python
# Test 1: Basic lowercase
print(caesar_encode("hello", 3))
# Expected: khoor

# Test 2: Uppercase
print(caesar_encode("HELLO", 3))
# Expected: KHOOR

# Test 3: Wrapping past the alphabet
print(caesar_encode("xyz", 3))
# Expected: abc

# Test 4: Mixed (upper/lower, special chars, spaces)
print(caesar_encode("Hello, World!", 5))
# Expected: Mjqqt, Btwqi!

# Test 5: Numbers and special chars unchanged
print(caesar_encode("Python 3.10", 13))
# Expected: Clguba 3.10

# Test 6: key of 26 (full rotation)
print(caesar_encode("zebra", 26))
# Expected: zebra (no change!)

# Test 7: key greater than 26
print(caesar_encode("abc", 27))
# Expected: bcd (same as key=1)
```

## 🤔 Think About It

Before you start coding, sketch out your approach:
1. How can you check whether a character is a letter?
2. How would you turn `a` into 0, `b` into 1, etc.?
3. What operator do you need to make `z` wrap back to `a`?
4. How do you handle uppercase and lowercase differently?

## 🌟 Bonus Challenges (Optional)

Once you've completed the main function, try these:

**🟢 Easy:** Build a `caesar_decode(message, key)` function
- A function that decrypts an encrypted message back to its original form
- Hint: Could you simply do `caesar_encode(message, -key)`?

**🟡 Medium:** Handle Korean or other characters mixed in — only encrypt English letters, leave the rest alone
- Example: `caesar_encode("안녕 hello!", 3)` → `"안녕 khoor!"`
- Does our code already do this? Check it out!

**🔴 Hard:** Handle negative keys
- Example: `caesar_encode("def", -3)` → `"abc"`
- Hint: How does Python's `%` operator behave with negative numbers? Experiment!
- What's the result of `(-1) % 26`?

---

Drop your questions in the thread if you get stuck! Remember, the goal is to learn, not just to finish. Take your time and understand the logic.

Good luck! 🚀
