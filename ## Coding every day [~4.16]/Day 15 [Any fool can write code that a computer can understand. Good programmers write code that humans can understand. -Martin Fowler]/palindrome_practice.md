# 🐍 Python 연습: 회문(palindrome) 감지기 만들기!

여러분, 안녕하세요! 오늘은 문자열을 앞에서 읽어도, 뒤에서 읽어도 똑같은지 확인하는 프로그램을 만들어 봅시다.

## 🎯 미션

보안 시스템 회사에서 인턴으로 일하고 있다고 상상해보세요! 사용자가 입력한 단어가 *회문(palindrome)* 인지 확인하는 함수를 만들어야 합니다. 회문이란 앞에서 읽어도, 뒤에서 읽어도 같은 단어나 문장입니다.

예를 들어, `"racecar"`는 거꾸로 읽어도 `"racecar"`이므로 회문입니다. `"hello"`는 거꾸로 하면 `"olleh"`이므로 회문이 아니에요.

## 📋 규칙

*주어지는 것:*
• `word`라는 문자열 (영문자로만 구성)
• 대문자나 소문자가 섞여 있을 수 있음

*해야 할 일:*
1. 대소문자를 무시하고 비교 (예: `"Racecar"` → 회문으로 처리)
2. 단어가 회문이면 `True`, 아니면 `False` 반환

*제약사항:*
• `[::-1]` 같은 슬라이싱은 아직 배우지 않았으니 사용하지 마세요
• `reversed()` 내장 함수도 아직 사용하지 마세요
• 직접 인덱싱과 반복문으로 해결하세요
• 몇 개의 변수만 사용하세요

## 💡 예제

**예제 1:**
```
입력: word = "racecar"
출력: True
```
왜? r-a-c-e-c-a-r → 거꾸로 해도 r-a-c-e-c-a-r → 똑같아요!

**예제 2:**
```
입력: word = "hello"
출력: False
```
왜? h-e-l-l-o → 거꾸로 하면 o-l-l-e-h → 달라요!

**예제 3:**
```
입력: word = "Racecar"
출력: True
```
왜? 대소문자를 무시하면 "racecar" → 회문입니다!

**예제 4:**
```
입력: word = "madam"
출력: True
```

**예제 5:**
```
입력: word = "python"
출력: False
```

## 🎓 알아야 할 것

코딩을 시작하기 전에, 다음을 이해하고 있는지 확인하세요:
• 문자열을 인덱싱하는 방법 (`word[0]`, `word[-1]` 등)
• `len()` 함수 사용법
• `.lower()` 메서드 — 문자를 소문자로 바꾸기
• `while` 반복문 사용법

## ✅ 과제

다음 시그니처로 함수를 작성하세요:
```python
def is_palindrome(word: str) -> bool:
    # 여기에 코드 작성
    pass
```

**시작하는 데 도움이 될 팁:**
• 먼저 `word`를 전부 소문자로 바꾸세요 (`.lower()` 사용)
• 두 개의 변수를 사용해보세요: 하나는 왼쪽에서, 하나는 오른쪽에서 시작
• 왼쪽과 오른쪽을 비교하면서 가운데를 향해 이동하세요
• 중간에 다른 문자를 발견하면? → 회문이 아닙니다!
• 가운데까지 다 통과하면? → 회문입니다!

## 🎪 코드 테스트

다음 테스트 케이스를 실행해보세요:

```python
# 테스트 1
print(is_palindrome("racecar"))
# 예상: True

# 테스트 2
print(is_palindrome("hello"))
# 예상: False

# 테스트 3
print(is_palindrome("madam"))
# 예상: True

# 테스트 4
print(is_palindrome("Racecar"))
# 예상: True

# 테스트 5 (경계값: 글자가 하나)
print(is_palindrome("a"))
# 예상: True

# 테스트 6
print(is_palindrome("level"))
# 예상: True

# 테스트 7
print(is_palindrome("python"))
# 예상: False
```

## 🌍 실제 세계에서는?

회문 감지는 생각보다 여러 곳에서 쓰입니다:
• DNA 염기서열 분석 (생물정보학)
• 문자열 압축 알고리즘
• 코딩 인터뷰에서 가장 자주 나오는 문제 중 하나!

## 🤔 생각해보기

코딩을 시작하기 전에, 접근 방법을 스케치해보세요:
1. `"racecar"`를 손으로 거꾸로 비교한다면 어떻게 할까요? 왼쪽 끝과 오른쪽 끝부터 비교하겠죠?
2. 몇 번 비교하면 확인이 끝날까요? (힌트: `len(word) // 2` 번!)
3. 대소문자가 섞여도 올바르게 처리하려면 언제 `.lower()`를 쓰는 게 좋을까요?

막히면 스레드에 질문을 남겨주세요! 목표는 끝내는 것이 아니라 배우는 것입니다. 천천히 논리를 이해하면서 진행하세요.

행운을 빕니다! 🚀

---
---

# 🐍 Python Practice: Build a Palindrome Detector!

Hey team! Today we're building something used in real coding interviews and even in biology labs — a palindrome checker!

## 🎯 Your Mission

Imagine you're interning at a tech company and your team needs a utility function: given a word, check whether it's a *palindrome* — a word that reads the same forwards and backwards.

For example, `"racecar"` reversed is still `"racecar"` — palindrome! But `"hello"` reversed becomes `"olleh"` — not a palindrome.

## 📋 The Rules

*What you're given:*
• A string called `word` (letters only)
• It may have a mix of uppercase and lowercase letters

*What you need to do:*
1. Ignore case when comparing (e.g. `"Racecar"` counts as a palindrome)
2. Return `True` if it's a palindrome, `False` if it isn't

*Constraints:*
• No string slicing like `[::-1]` — we haven't learned that yet
• No `reversed()` built-in either
• Solve it with indexing and loops directly
• Use only a few variables

## 💡 Example Time

**Example 1:**
```
Input: word = "racecar"
Output: True
```
Why? r-a-c-e-c-a-r → same forwards and backwards!

**Example 2:**
```
Input: word = "hello"
Output: False
```
Why? h-e-l-l-o → reversed is o-l-l-e-h → different!

**Example 3:**
```
Input: word = "Racecar"
Output: True
```
Why? Ignoring case → "racecar" → still a palindrome!

**Example 4:**
```
Input: word = "madam"
Output: True
```

**Example 5:**
```
Input: word = "python"
Output: False
```

## 🎓 What You Should Know

Before you start coding, make sure you understand:
• String indexing (`word[0]`, `word[-1]`, etc.)
• The `len()` function
• The `.lower()` method — converts a character to lowercase
• How `while` loops work

## ✅ Your Task

Write a function with this signature:
```python
def is_palindrome(word: str) -> bool:
    # Your code here
    pass
```

**Tips to get you started:**
• First, convert the whole word to lowercase using `.lower()`
• Use two variables: one starting from the left, one from the right
• Move them toward the middle, comparing as you go
• If you find a mismatch? → Not a palindrome!
• Made it to the middle without a mismatch? → Palindrome!

## 🎪 Test Your Code

Try running these test cases:

```python
# Test 1
print(is_palindrome("racecar"))
# Expected: True

# Test 2
print(is_palindrome("hello"))
# Expected: False

# Test 3
print(is_palindrome("madam"))
# Expected: True

# Test 4
print(is_palindrome("Racecar"))
# Expected: True

# Test 5 (edge case: single character)
print(is_palindrome("a"))
# Expected: True

# Test 6
print(is_palindrome("level"))
# Expected: True

# Test 7
print(is_palindrome("python"))
# Expected: False
```

## 🌍 Real-World Connection

Palindrome detection shows up in surprising places:
• Analyzing DNA sequences in bioinformatics
• String compression algorithms
• One of the most common questions in coding interviews!

## 🤔 Think About It

Before you start coding, sketch out your approach:
1. If you were checking `"racecar"` by hand, you'd compare the leftmost and rightmost letters first, right?
2. How many comparisons do you actually need? (Hint: `len(word) // 2` times!)
3. When is the best moment to apply `.lower()` — before the loop, or inside it?

Drop your questions in the thread if you get stuck! Remember, the goal is to learn, not just to finish. Take your time and understand the logic.

Good luck! 🚀
