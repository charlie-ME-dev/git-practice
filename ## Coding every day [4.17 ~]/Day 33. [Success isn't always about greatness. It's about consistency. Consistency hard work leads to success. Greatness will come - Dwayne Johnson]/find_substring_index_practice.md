# 🔍 Python 연습: 문자열 속 숨은 단어 찾기!

여러분, 안녕하세요! 오늘은 문자열 검색 기능의 내부 동작을 직접 구현해보는 시간입니다.

## 🎯 미션

여러분은 사이버보안 회사의 신입 개발자입니다. 팀장님이 **로그 분석 도구**를 만들고 있는데, 특정 오류 코드가 로그 메시지 안에서 **처음 나타나는 위치**를 찾아야 한대요.

Python의 편리한 `.find()` 메서드를 쓰고 싶겠지만... 팀장님의 말씀:
> "라이브러리에 의존하지 말고, 문자열 검색이 **내부적으로 어떻게 동작하는지** 직접 구현해보세요. 그래야 알고리즘 감각이 생깁니다!"

여러분의 임무는 **큰 문자열(haystack) 안에서 작은 문자열(needle)이 처음 나타나는 인덱스**를 찾는 함수를 만드는 것입니다.

> 💡 **참고:** Python에는 이 작업을 해주는 문자열 메서드 `.find()`가 이미 존재합니다. 하지만 오늘은 그 내부 동작을 직접 만들어보는 것이 목표예요. 메서드 호출은 마지막 보너스에서 만날 수 있어요!

## 📋 규칙

*주어지는 것:*
• `haystack`: 검색 대상 문자열 (건초더미 🌾)
• `needle`: 찾고자 하는 부분 문자열 (바늘 🪡)

*해야 할 일:*
1. `haystack` 안에서 `needle`이 처음 나타나는 **시작 인덱스**를 반환
2. `needle`이 `haystack` 안에 없으면 `-1`을 반환
3. `needle`이 빈 문자열(`""`)이면 `0`을 반환

*제약사항:*
• `.find()`, `.index()`, `in` 연산자 **사용 금지!** (내부 동작 구현이 목적)
• 슬라이싱 `s[a:b]`과 반복문(`for`, `while`)을 활용하세요
• `haystack`과 `needle`은 빈 문자열일 수 있습니다

## 💡 예제

**예제 1: 오류 코드 찾기**
```
입력: haystack = "sadbutsad", needle = "sad"
출력: 0
```
`"sad"`가 인덱스 `0`에서 시작해요. (인덱스 `6`에도 또 있지만 **처음** 나타나는 위치를 원합니다!)

**예제 2: 존재하지 않는 패턴**
```
입력: haystack = "leetcode", needle = "leeto"
출력: -1
```
`"leeto"`는 `"leetcode"` 안에 없으므로 `-1`을 반환합니다.

**예제 3: 로그 메시지 속 오류 코드**
```
입력: haystack = "ERROR_404 not found in server", needle = "404"
출력: 6
```
`"404"`가 인덱스 `6`에서 시작합니다.

## 🎓 알아야 할 것

코딩을 시작하기 전에, 다음을 이해하고 있는지 확인하세요:
• 문자열 인덱싱과 슬라이싱 (`s[i]`, `s[a:b]`)
• `len()` 함수로 문자열 길이 얻기
• `for` 반복문과 `range()` 사용법
• `while` 반복문과 조건
• 문자 단위 비교 (`==`)

## ✅ 과제

다음 시그니처로 함수를 작성하세요:
```python
def find_substring_index(haystack: str, needle: str) -> int:
    # 여기에 코드 작성
    pass
```

**시작하는 데 도움이 될 팁:**
• `haystack`의 각 위치 `i`에서 시작하여, `needle`과 길이만큼 비교해보세요
• 슬라이싱을 쓰면 `haystack[i:i+len(needle)] == needle`로 한 번에 비교할 수 있어요
• 반복 범위는 어디까지여야 할까요? `needle`이 들어갈 공간이 있어야 합니다!

## 🎪 코드 테스트

다음 테스트 케이스를 실행해보세요:

```python
# 테스트 1: 기본 찾기
print(find_substring_index("sadbutsad", "sad"))
# 예상: 0

# 테스트 2: 찾을 수 없음
print(find_substring_index("leetcode", "leeto"))
# 예상: -1

# 테스트 3: 로그 분석
print(find_substring_index("ERROR_404 not found", "404"))
# 예상: 6

# 테스트 4: 빈 needle
print(find_substring_index("hello", ""))
# 예상: 0

# 테스트 5: needle이 더 긴 경우
print(find_substring_index("abc", "abcd"))
# 예상: -1
```

## 🤔 생각해보기

코딩을 시작하기 전에, 접근 방법을 스케치해보세요:
1. `haystack`의 어느 위치까지 검사하면 될까요? (끝까지 갈 필요가 있을까요?)
2. 각 위치에서 `needle`과 어떻게 비교할 건가요?
3. `needle`이 빈 문자열이면 왜 `0`을 반환해야 할까요?

## 🎁 보너스 챌린지

기본 과제를 끝냈다면, 실력을 더 키워보세요!

### 🟢 Easy: 마지막 위치 찾기
`find_last_substring_index(haystack, needle)` 함수를 만들어 **마지막** 출현 위치를 반환하세요.
```python
find_last_substring_index("sadbutsad", "sad")  # 예상: 6
```

### 🟡 Medium: 모든 위치 찾기
`find_all_occurrences(haystack, needle)` 함수를 만들어 **모든** 출현 위치의 리스트를 반환하세요.
```python
find_all_occurrences("ababab", "ab")  # 예상: [0, 2, 4]
find_all_occurrences("aaaa", "aa")    # 예상: [0, 1, 2]  (겹치는 경우 포함!)
```

### 🔴 Hard: 똑똑한 건너뛰기 (KMP 알고리즘 맛보기)
현재 방식은 `"aaaaaaaab"`에서 `"aaab"`를 찾을 때 매번 처음부터 다시 비교합니다. 비효율적이죠!

실제 프로그래밍 언어의 `.find()`는 **KMP 알고리즘** 같은 똑똑한 방법을 씁니다. 이미 비교한 정보를 활용해서 불필요한 비교를 건너뛰는 거예요.

KMP 알고리즘을 조사해보고, 왜 이런 알고리즘이 필요한지 짧은 설명을 써보세요. (코드 구현까지는 하지 않아도 괜찮습니다 — **개념 이해가 목표**입니다!)

힌트 질문:
- "부분 일치"가 실패했을 때, 얼마나 뒤로 돌아가야 할까요?
- `"ABCABD"`에서 앞쪽의 `"ABC"`를 이미 봤다면, 다음엔 어디서부터 비교하면 될까요?

---

막히면 스레드에 질문을 남겨주세요! 목표는 끝내는 것이 아니라 **문자열 검색이 어떻게 작동하는지 이해하는 것**입니다. 천천히 논리를 이해하면서 진행하세요.

행운을 빕니다! 🚀

---
---

# 🔍 Python Practice: Find the Hidden Word in a String!

Hey team! Today we're implementing one of the most common string operations from scratch.

## 🎯 Your Mission

You're a junior developer at a cybersecurity firm. Your team lead is building a **log analysis tool** and needs to find where a specific error code **first appears** inside a log message.

You'd love to just use Python's convenient `.find()` method, but your lead says:
> "Don't rely on the library — implement it yourself so you understand **how string search actually works under the hood**. That's how you build algorithmic intuition!"

Your mission: write a function that finds **the index where a small string (needle) first appears inside a larger string (haystack)**.

> 💡 **Note:** Python already has a string method called `.find()` that does this job. But today's goal is to build it yourself. You'll meet the method itself in the final bonus!

## 📋 The Rules

*What you're given:*
• `haystack`: the string to search inside (the haystack 🌾)
• `needle`: the substring you're looking for (the needle 🪡)

*What you need to do:*
1. Return the **starting index** where `needle` first appears in `haystack`
2. Return `-1` if `needle` is not found
3. Return `0` if `needle` is an empty string (`""`)

*Constraints:*
• **No `.find()`, `.index()`, or `in` operator!** (the whole point is to implement it)
• Use slicing `s[a:b]` and loops (`for`, `while`)
• Both `haystack` and `needle` can be empty strings

## 💡 Example Time

**Example 1: Finding an error code**
```
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
```
`"sad"` starts at index `0`. (It also appears at index `6`, but we want the **first** occurrence!)

**Example 2: Pattern not present**
```
Input: haystack = "leetcode", needle = "leeto"
Output: -1
```
`"leeto"` is not inside `"leetcode"`, so we return `-1`.

**Example 3: Error code in a log message**
```
Input: haystack = "ERROR_404 not found in server", needle = "404"
Output: 6
```
`"404"` starts at index `6`.

## 🎓 What You Should Know

Before you start coding, make sure you understand:
• String indexing and slicing (`s[i]`, `s[a:b]`)
• Getting string length with `len()`
• `for` loops with `range()`
• `while` loops with conditions
• Character-by-character comparison (`==`)

## ✅ Your Task

Write a function with this signature:
```python
def find_substring_index(haystack: str, needle: str) -> int:
    # Your code here
    pass
```

**Tips to get you started:**
• At each position `i` in `haystack`, compare `needle`-many characters
• With slicing, you can compare a whole chunk at once: `haystack[i:i+len(needle)] == needle`
• How far should your loop go? You need room for `needle` to fit!

## 🎪 Test Your Code

Try running these test cases:

```python
# Test 1: Basic find
print(find_substring_index("sadbutsad", "sad"))
# Expected: 0

# Test 2: Not found
print(find_substring_index("leetcode", "leeto"))
# Expected: -1

# Test 3: Log analysis
print(find_substring_index("ERROR_404 not found", "404"))
# Expected: 6

# Test 4: Empty needle
print(find_substring_index("hello", ""))
# Expected: 0

# Test 5: needle longer than haystack
print(find_substring_index("abc", "abcd"))
# Expected: -1
```

## 🤔 Think About It

Before you start coding, sketch out your approach:
1. How far should you check in `haystack`? (Do you really need to go all the way to the end?)
2. How will you compare at each position?
3. Why should an empty `needle` return `0`?

## 🎁 Bonus Challenges

Finished the core task? Level up!

### 🟢 Easy: Find the Last Occurrence
Write `find_last_substring_index(haystack, needle)` that returns the **last** index instead.
```python
find_last_substring_index("sadbutsad", "sad")  # Expected: 6
```

### 🟡 Medium: Find All Occurrences
Write `find_all_occurrences(haystack, needle)` that returns a list of **all** starting indices.
```python
find_all_occurrences("ababab", "ab")  # Expected: [0, 2, 4]
find_all_occurrences("aaaa", "aa")    # Expected: [0, 1, 2]  (overlaps count!)
```

### 🔴 Hard: Smart Skipping (A Taste of KMP)
Our current approach is wasteful: searching for `"aaab"` in `"aaaaaaaab"` re-compares from scratch at every position. That's slow!

Real-world `.find()` implementations use clever algorithms like **KMP (Knuth–Morris–Pratt)** that reuse information from previous comparisons to **skip ahead** instead of restarting.

Research KMP and write a short explanation of why such algorithms exist. (You don't have to implement it — **understanding the concept is the goal**!)

Guiding questions:
- When a partial match fails, how far back do you *really* need to go?
- In `"ABCABD"`, if you already matched `"ABC"` at the front, where can comparison resume next?

---

Drop your questions in the thread if you get stuck! The goal isn't just to finish — it's to understand **how string search actually works**. Take your time and enjoy the logic.

Good luck! 🚀
