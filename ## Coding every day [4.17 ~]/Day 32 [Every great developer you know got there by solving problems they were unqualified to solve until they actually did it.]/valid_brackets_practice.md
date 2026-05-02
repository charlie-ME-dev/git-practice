# 🐍 Python 연습: 괄호 매칭 검사기 만들기!

여러분, 안녕하세요! 오늘은 코드 에디터(VS Code 같은 것!)에서 매일 보는 기능을 직접 만들어봅니다.

## 🎯 미션

여러분은 신생 코드 에디터 스타트업의 주니어 개발자예요. 시니어 개발자가 이런 요청을 했습니다:

> "사용자가 코드를 작성할 때 괄호 `()`, 대괄호 `[]`, 중괄호 `{}`가 올바르게 짝지어져 있는지 실시간으로 검사하는 기능이 필요해요. 함수 하나 만들어줄래요?"

올바른 괄호 문자열을 판별하는 함수를 작성하세요!

## 📋 규칙

*주어지는 것:*
• `s`라는 문자열 — `()`, `[]`, `{}` 6가지 문자만 포함
• 빈 문자열도 입력될 수 있음

*해야 할 일:*
1. 문자열을 한 글자씩 검사
2. 모든 여는 괄호는 같은 종류의 닫는 괄호로 닫혀야 함
3. 올바른 순서로 닫혀야 함 (가장 최근에 열린 괄호가 먼저 닫혀야 함)
4. 유효하면 `True`, 아니면 `False` 반환

*"올바르다"는 것의 의미:*
• `()` ✅ — 같은 종류로 닫힘
• `()[]{}` ✅ — 각자 자기 짝과 매칭
• `{[]}` ✅ — 안쪽이 먼저 닫힘
• `(]` ❌ — 다른 종류로 닫힘
• `([)]` ❌ — 순서가 꼬임 (가장 최근에 연 `[`가 먼저 닫혀야 함)

## 💡 예제

**예제 1:**
```
입력: s = "()"
출력: True
```
왜? `(`가 열리고 바로 `)`로 닫혔어요. 완벽한 짝!

**예제 2:**
```
입력: s = "()[]{}"
출력: True
```
왜? 세 쌍의 괄호가 각자 자기 짝과 잘 매칭되어 있어요.

**예제 3:**
```
입력: s = "([)]"
출력: False
```
왜? `(` 다음에 `[`가 열렸으면, `]`가 먼저 닫혀야 해요. 순서가 꼬였습니다!

**예제 4:**
```
입력: s = "{[]}"
출력: True
```
왜? `{`가 열리고 → `[`가 열리고 → `]`로 안쪽이 먼저 닫히고 → `}`로 바깥이 닫힘. 완벽!

## 🎓 알아야 할 것

코딩을 시작하기 전에, 다음을 이해하고 있는지 확인하세요:
• 문자열을 한 글자씩 반복하는 방법 (`for char in s:`)
• 리스트의 `append()`와 `pop()` 메서드
• `if` / `elif` / `else` 조건문
• 리스트의 길이 확인하기 (`len()`)

## ✅ 과제

다음 시그니처로 함수를 작성하세요:
```python
def is_valid_brackets(s: str) -> bool:
    # 여기에 코드 작성
    pass
```

**시작하는 데 도움이 될 팁:**
• 리스트를 "쌓아두는 공간(stack)"처럼 사용하세요
• 여는 괄호를 만나면 → 리스트에 `append`
• 닫는 괄호를 만나면 → 리스트의 마지막 요소를 `pop`해서 짝이 맞는지 확인
• 다 끝났을 때 리스트가 비어있어야 유효함

## 🎪 코드 테스트

다음 테스트 케이스를 실행해보세요:

```python
# 테스트 1
print(is_valid_brackets("()"))        # 예상: True
print(is_valid_brackets("()[]{}"))    # 예상: True
print(is_valid_brackets("(]"))        # 예상: False
print(is_valid_brackets("([)]"))      # 예상: False
print(is_valid_brackets("{[]}"))      # 예상: True

# 엣지 케이스도 잊지 마세요!
print(is_valid_brackets(""))          # 예상: True (빈 문자열)
print(is_valid_brackets("("))         # 예상: False (안 닫힘)
print(is_valid_brackets(")"))         # 예상: False (열린 적 없음)
```

## 🤔 생각해보기

코딩을 시작하기 전에, 접근 방법을 스케치해보세요:
1. `(`를 만났을 때, 무엇을 기억해두어야 할까요?
2. `)`를 만났을 때, 어떤 정보가 필요할까요?
3. `"(("` 처럼 여는 괄호만 있고 끝나면 어떻게 처리할까요?
4. `"))"` 처럼 닫는 괄호부터 시작하면 어떻게 처리할까요?

## 🎁 보너스 챌린지

기본 문제를 끝냈다면, 다음에 도전해보세요!

**Easy** — 한 종류만 있는 버전:
괄호가 `(`, `)`만 있다면, 리스트(스택) 없이 정수 카운터 하나만으로 풀 수 있을까요?

**Medium** — 코드 안의 괄호:
실제 코드 문자열 `"if (x > 0) { y[0] = 1; }"`처럼 알파벳, 숫자, 공백이 섞여 있을 때, **괄호만** 검사하는 함수를 만들어보세요.

**Hard** — 딕셔너리(dict)로 더 깔끔하게:
Python에는 "키-값"을 저장하는 `dict` 자료형이 있어요. 예: `{')': '(', ']': '[', '}': '{'}`. 이걸 쓰면 if/elif가 줄어들어요. 다음 주에 배울 내용을 미리 맛보세요!

막히면 스레드에 질문을 남겨주세요! 목표는 끝내는 것이 아니라 배우는 것입니다. 천천히 논리를 이해하면서 진행하세요.

행운을 빕니다! 🚀

---
---

# 🐍 Python Practice: Build a Bracket Matcher!

Hey team! Today we're building something you see every day in your code editor (like VS Code!).

## 🎯 Your Mission

You're a junior developer at a code editor startup. Your senior dev sends you this request:

> "We need a function that checks in real-time whether parentheses `()`, brackets `[]`, and braces `{}` are properly matched when users type code. Can you build it?"

Write a function that determines if a bracket string is valid!

## 📋 The Rules

*What you're given:*
• A string `s` containing only these 6 characters: `()`, `[]`, `{}`
• Empty strings are also possible inputs

*What you need to do:*
1. Scan the string character by character
2. Every opening bracket must close with the same type of bracket
3. They must close in the correct order (most recently opened closes first)
4. Return `True` if valid, `False` otherwise

*What "valid" means:*
• `()` ✅ — closed with matching type
• `()[]{}` ✅ — each matches its own pair
• `{[]}` ✅ — inner closes first
• `(]` ❌ — closed with wrong type
• `([)]` ❌ — wrong order (the most recent `[` should close first)

## 💡 Example Time

**Example 1:**
```
Input: s = "()"
Output: True
```
Why? `(` opens, then `)` closes it immediately. Perfect pair!

**Example 2:**
```
Input: s = "()[]{}"
Output: True
```
Why? Three pairs of brackets, each matched with its own partner.

**Example 3:**
```
Input: s = "([)]"
Output: False
```
Why? After `(` opens, then `[` opens — the `]` should close first, not `)`. The order is broken!

**Example 4:**
```
Input: s = "{[]}"
Output: True
```
Why? `{` opens → `[` opens → `]` closes the inner one → `}` closes the outer one. 

## 🎓 What You Should Know

Before you start coding, make sure you understand:
• How to loop through a string character by character (`for char in s:`)
• List methods `append()` and `pop()`
• `if` / `elif` / `else` statements
• How to check list length (`len()`)

## ✅ Your Task

Write a function with this signature:
```python
def is_valid_brackets(s: str) -> bool:
    # Your code here
    pass
```

**Tips to get you started:**
• Use a list as a "stacking space" (a stack)
• When you see an opening bracket → `append` it to the list
• When you see a closing bracket → `pop` the last item and check if it matches
• When you're done, the list should be empty for the string to be valid

## 🎪 Test Your Code

Try running these test cases:

```python
# Test 1
print(is_valid_brackets("()"))        # Expected: True
print(is_valid_brackets("()[]{}"))    # Expected: True
print(is_valid_brackets("(]"))        # Expected: False
print(is_valid_brackets("([)]"))      # Expected: False
print(is_valid_brackets("{[]}"))      # Expected: True

# Don't forget edge cases!
print(is_valid_brackets(""))          # Expected: True (empty string)
print(is_valid_brackets("("))         # Expected: False (never closed)
print(is_valid_brackets(")"))         # Expected: False (never opened)
```

## 🤔 Think About It

Before you start coding, sketch out your approach:
1. When you see `(`, what do you need to remember?
2. When you see `)`, what information do you need?
3. How do you handle a string like `"(("` that only has openers?
4. How do you handle a string like `"))"` that starts with closers?

## 🎁 Bonus Challenges

Done with the main problem? Try these!

**Easy** — Single bracket type:
If the string only contains `(` and `)`, can you solve it with just an integer counter (no list/stack needed)?

**Medium** — Brackets in real code:
Real code like `"if (x > 0) { y[0] = 1; }"` has letters, numbers, and spaces mixed in. Write a version that checks **only the brackets** and ignores everything else.

**Hard** — Cleaner with a dictionary (dict):
Python has a `dict` type that stores "key-value" pairs. Example: `{')': '(', ']': '[', '}': '{'}`. Using this, you can shrink all those if/elif statements. Get a sneak peek at next week's topic!

Drop your questions in the thread if you get stuck! Remember, the goal is to learn, not just to finish. Take your time and understand the logic.

Good luck! 🚀
