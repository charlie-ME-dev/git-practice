# 🐍 Python 연습: 여동생의 에세이 편집하기!

여러분, 안녕하세요! 오늘은 Python의 문자열(string) 메서드를 활용해서 실제 편집자처럼 글을 다듬어 볼 거예요.

---

## 🏢 실전 시나리오

여러분은 스타트업의 주니어 개발자입니다. 팀에서 학생들이 제출한 에세이를 자동으로 교정해주는 간단한 도구를 만들어 달라고 요청했어요. 제목 형식 맞추기, 문장 부호 확인, 불필요한 공백 제거, 단어 교체 — 이 네 가지 기능을 함수로 구현해야 합니다!

---

## 🎯 미션

여동생이 학교 에세이를 썼는데 선생님이 **올바른 문장 부호, 문법, 좋은 단어 선택**을 중요하게 보신대요. 다음 네 가지 함수를 만들어 여동생의 에세이를 깔끔하게 다듬어 주세요!

---

## 📋 함수 목록

### ① `capitalize_title(title)`
**제목의 각 단어 첫 글자를 대문자로 만들기**

```
입력: "my hobbies"
출력: "My Hobbies"
```

### ② `check_sentence_ending(sentence)`
**문장이 마침표(`.`)로 끝나는지 확인하기**
- 끝나면 `True`, 아니면 `False` 반환

```
입력: "I like to hike, bake, and read."
출력: True

입력: "This sentence has no period"
출력: False
```

### ③ `clean_up_spacing(sentence)`
**문장 앞뒤의 불필요한 공백 제거하기**

```
입력: "   I like to go on hikes with my dog.  "
출력: "I like to go on hikes with my dog."
```

### ④ `replace_word_choice(sentence, old_word, new_word)`
**문장 안의 특정 단어를 새 단어로 모두 교체하기**

```
입력: "I bake good cakes.", "good", "amazing"
출력: "I bake amazing cakes."

입력: "The big dog saw a big cat.", "big", "tiny"
출력: "The tiny dog saw a tiny cat."
```

---

## 💡 힌트: 이런 문자열 메서드를 활용하세요!

| 메서드 | 하는 일 | 예시 |
|---|---|---|
| `"hello world".title()` | 각 단어 첫 글자 대문자로 | `"Hello World"` |
| `"hello.".endswith(".")` | 특정 문자로 끝나는지 확인 | `True` |
| `"  hi  ".strip()` | 앞뒤 공백 제거 | `"hi"` |
| `"I am good".replace("good", "great")` | 단어 교체 | `"I am great"` |

> 💡 문자열(string)은 **변경 불가능(immutable)**합니다! 위 메서드들은 원본을 바꾸지 않고 **새 문자열을 반환**해요. 반드시 반환값을 `return` 해야 합니다!

---

## ✅ 과제

다음 함수 시그니처를 완성하세요:

```python
def capitalize_title(title):
    pass

def check_sentence_ending(sentence):
    pass

def clean_up_spacing(sentence):
    pass

def replace_word_choice(sentence, old_word, new_word):
    pass
```

---

## 🎪 테스트 케이스

```python
# 테스트 1: capitalize_title
print(capitalize_title("my hobbies"))
# 예상: My Hobbies

print(capitalize_title("a day in the life"))
# 예상: A Day In The Life

# 테스트 2: check_sentence_ending
print(check_sentence_ending("I like to hike, bake, and read."))
# 예상: True

print(check_sentence_ending("This is great"))
# 예상: False

# 테스트 3: clean_up_spacing
print(clean_up_spacing("   I like to go on hikes with my dog.  "))
# 예상: I like to go on hikes with my dog.

# 테스트 4: replace_word_choice
print(replace_word_choice("I bake good cakes.", "good", "amazing"))
# 예상: I bake amazing cakes.

print(replace_word_choice("The big dog saw a big cat.", "big", "tiny"))
# 예상: The tiny dog saw a tiny cat.
```

---

## 🤔 생각해보기

1. `capitalize_title("the man in the hat")`의 출력은 무엇일까요? 왜 그럴까요?
2. `check_sentence_ending("Hello!")` — 느낌표로 끝나면 `True`일까요 `False`일까요?
3. `"  spaces  ".strip()`은 중간 공백도 제거할까요, 아니면 앞뒤만 제거할까요?
4. `replace_word_choice("Happy happy day.", "happy", "great")`의 출력은? (대소문자 주의!)

막히면 스레드에 질문을 남겨주세요! 목표는 빨리 끝내는 것이 아니라 제대로 이해하는 것입니다. 🚀

---
---

# 🐍 Python Practice: Edit Your Little Sister's Essay!

Hey team! Today we're going to use Python's built-in string methods to clean up text — just like a real editor would.

---

## 🏢 Real-World Scenario

You're a junior developer at a startup. Your team needs a simple tool that automatically proofreads essays submitted by students. Your job: implement four helper functions that handle formatting, punctuation checking, whitespace cleanup, and word replacement!

---

## 🎯 Your Mission

Your little sister wrote a school essay, and her teacher cares about **proper punctuation, grammar, and excellent word choice**. Build four functions to polish the essay!

---

## 📋 Function List

### ① `capitalize_title(title)`
**Capitalize the first letter of each word in the title**

```
Input:  "my hobbies"
Output: "My Hobbies"
```

### ② `check_sentence_ending(sentence)`
**Check if a sentence ends with a period (`.`)**
- Return `True` if it does, `False` if it doesn't

```
Input:  "I like to hike, bake, and read."
Output: True

Input:  "This sentence has no period"
Output: False
```

### ③ `clean_up_spacing(sentence)`
**Remove unnecessary whitespace from both ends of the sentence**

```
Input:  "   I like to go on hikes with my dog.  "
Output: "I like to go on hikes with my dog."
```

### ④ `replace_word_choice(sentence, old_word, new_word)`
**Replace every occurrence of `old_word` with `new_word` in the sentence**

```
Input:  "I bake good cakes.", "good", "amazing"
Output: "I bake amazing cakes."

Input:  "The big dog saw a big cat.", "big", "tiny"
Output: "The tiny dog saw a tiny cat."
```

---

## 💡 Hint: Useful String Methods

| Method | What it does | Example |
|---|---|---|
| `"hello world".title()` | Capitalizes first letter of each word | `"Hello World"` |
| `"hello.".endswith(".")` | Checks if string ends with a given suffix | `True` |
| `"  hi  ".strip()` | Removes leading and trailing whitespace | `"hi"` |
| `"I am good".replace("good", "great")` | Replaces all matching words | `"I am great"` |

> 💡 Strings are **immutable** in Python — methods like these don't modify the original; they **return a new string**. Always `return` the result!

---

## ✅ Your Task

Complete these function signatures:

```python
def capitalize_title(title):
    pass

def check_sentence_ending(sentence):
    pass

def clean_up_spacing(sentence):
    pass

def replace_word_choice(sentence, old_word, new_word):
    pass
```

---

## 🎪 Test Your Code

```python
# Test 1: capitalize_title
print(capitalize_title("my hobbies"))
# Expected: My Hobbies

print(capitalize_title("a day in the life"))
# Expected: A Day In The Life

# Test 2: check_sentence_ending
print(check_sentence_ending("I like to hike, bake, and read."))
# Expected: True

print(check_sentence_ending("This is great"))
# Expected: False

# Test 3: clean_up_spacing
print(clean_up_spacing("   I like to go on hikes with my dog.  "))
# Expected: I like to go on hikes with my dog.

# Test 4: replace_word_choice
print(replace_word_choice("I bake good cakes.", "good", "amazing"))
# Expected: I bake amazing cakes.

print(replace_word_choice("The big dog saw a big cat.", "big", "tiny"))
# Expected: The tiny dog saw a tiny cat.
```

---

## 🤔 Think About It

1. What does `capitalize_title("the man in the hat")` output? Why?
2. `check_sentence_ending("Hello!")` — does an exclamation mark count as a period?
3. Does `.strip()` remove spaces in the *middle* of a string, or only at the ends?
4. What does `replace_word_choice("Happy happy day.", "happy", "great")` return? (Watch the case!)

Drop your questions in the thread if you get stuck! The goal is to truly understand the logic, not just to finish fast. Good luck! 🚀
