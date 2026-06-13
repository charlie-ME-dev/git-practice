# 🐍 Python 연습: 단어의 숫자 값 계산하기!

여러분, 안녕하세요! 오늘은 Dictionary를 활용한 재미있는 연습입니다.

## 🎯 미션

각 알파벳에 숫자 값을 부여한다고 상상해보세요: **A=1, B=2, C=3, ..., Z=26**. 단어를 받아서 모든 글자의 값을 더하면 그 단어의 "총 값"이 나옵니다.

재미있는 사실 하나! 영어에서 어떤 단어들은 정확히 **100점**이 됩니다:
- `attitude` → 100점
- `discipline` → 100점

여러분은 동기부여 포스터를 만드는 스타트업의 인턴이라고 상상해봐요. 디자인 팀에서 **"100점짜리 단어"** 만 골라서 포스터에 넣고 싶어합니다. 여러분의 임무는 단어 값을 계산하는 도구를 만드는 것!

## 📋 규칙

*주어지는 것:*
- 영어 단어 (대소문자 섞여 있을 수 있음)
- 또는 단어들이 들어있는 리스트

*해야 할 일:*
1. A=1, B=2, ..., Z=26 매핑을 dictionary로 만들기
2. 한 글자의 값을 반환하는 함수
3. 단어 전체의 값을 계산하는 함수
4. 리스트에서 특정 값을 가진 단어들을 찾는 함수

*반드시 따라야 할 제약사항:*
- **대소문자 모두 처리해야 합니다** (A와 a는 둘 다 1)
- 알파벳이 아닌 문자는 무시 (공백, 숫자, 기호 등)
- 빈 문자열의 값은 0
- 함수 이름은 모두 `snake_case` (예: `calculate_word_value`)

## 💡 예제

**예제 1: 한 글자**
```
입력: 'A' → 출력: 1
입력: 'z' → 출력: 26
입력: 'h' → 출력: 8
```

**예제 2: 단어 전체**
```
입력: 'knowledge' → 출력: 96
입력: 'hardwork'  → 출력: 98
입력: 'attitude'  → 출력: 100  ⭐
입력: 'DISCIPLINE' → 출력: 100  ⭐
```

> **팁**: knowledge(지식)와 hardwork(노력)도 중요하지만, 100점이 되려면 `attitude`(태도)나 `discipline`(자기관리)가 필요하다는 메시지가 있는 유명한 이야기입니다!

**예제 3: 리스트에서 찾기**
```
입력: words = ['attitude', 'knowledge', 'discipline', 'hope']
       target_value = 100
출력: ['attitude', 'discipline']
```

## 🎓 알아야 할 것

코딩을 시작하기 전에, 다음을 이해하고 있는지 확인하세요:
- Dictionary 생성과 키로 값 접근하기 (`dict[key]`)
- for 루프와 enumerate 함수
- 문자열 메서드: `.upper()`, `.isalpha()`
- `string.ascii_uppercase`로 알파벳 문자열 가져오기

## ✅ 과제

다음 세 가지 함수를 작성하세요:

| 함수 이름 | 매개변수 | 반환 값 | 설명 |
|---|---|---|---|
| `get_letter_value` | `letter: str` | `int` | 한 글자의 값 (대소문자 무관) |
| `calculate_word_value` | `word: str` | `int` | 단어의 총 값 (알파벳 외 문자 무시) |
| `find_words_with_value` | `words: list[str]`, `target_value: int` | `list[str]` | 리스트에서 target_value와 같은 값을 가진 단어들 |

```python
import string

def get_letter_value(letter: str) -> int:
    # 여기에 코드 작성
    pass

def calculate_word_value(word: str) -> int:
    # 여기에 코드 작성
    pass

def find_words_with_value(words: list[str], target_value: int) -> list[str]:
    # 여기에 코드 작성
    pass
```

**시작하는 데 도움이 될 팁:**
- 먼저 알파벳-숫자 매핑 dictionary를 만드세요. `string.ascii_uppercase`는 `'ABCDEFGHIJKLMNOPQRSTUVWXYZ'`를 반환합니다
- `enumerate(string.ascii_uppercase, 1)`을 사용하면 1부터 시작하는 인덱스를 얻을 수 있어요
- 입력을 `.upper()`로 통일하면 대소문자를 한 번에 처리할 수 있습니다
- `calculate_word_value`는 내부에서 `get_letter_value`를 호출하면 깔끔합니다

## 🎪 코드 테스트

다음 테스트 케이스를 실행해보세요:

```python
# 테스트 1: 한 글자
print(get_letter_value('A'))   # 예상: 1
print(get_letter_value('z'))   # 예상: 26
print(get_letter_value('M'))   # 예상: 13

# 테스트 2: 단어 값
print(calculate_word_value('knowledge'))   # 예상: 96
print(calculate_word_value('hardwork'))    # 예상: 98
print(calculate_word_value('attitude'))    # 예상: 100
print(calculate_word_value('DISCIPLINE'))  # 예상: 100

# 테스트 3: 경계값
print(calculate_word_value(''))            # 예상: 0
print(calculate_word_value('Hello World')) # 예상: 124 (공백 무시)

# 테스트 4: 리스트 검색
words = ['attitude', 'knowledge', 'discipline', 'hardwork', 'hope']
print(find_words_with_value(words, 100))  # 예상: ['attitude', 'discipline']
print(find_words_with_value(words, 96))   # 예상: ['knowledge']
print(find_words_with_value(words, 999))  # 예상: []
```

## 🤔 생각해보기

코딩을 시작하기 전에, 접근 방법을 스케치해보세요:
1. Dictionary를 어떻게 만들 건가요? for 루프? enumerate?
2. 대소문자를 어떻게 한 번에 처리할까요?
3. `'Hello World'`의 공백은 어떻게 무시하나요?
4. 단어 안에 숫자가 들어있다면? (예: `'abc123'`)

막히면 스레드에 질문을 남겨주세요! 목표는 끝내는 것이 아니라 배우는 것입니다.

행운을 빕니다! 🚀

---
---

# 🐍 Python Practice: Calculate Word Values!

Hey team! Today's exercise is a fun one using Dictionaries.

## 🎯 Your Mission

Imagine each letter has a numeric value: **A=1, B=2, C=3, ..., Z=26**. When you take a word and add up all its letter values, you get the word's "total value".

Here's a fun fact! Some English words add up to exactly **100 points**:
- `attitude` → 100 points
- `discipline` → 100 points

Imagine you're an intern at a startup that makes motivational posters. The design team wants to feature only **"100-point words"** on their posters. Your job is to build the tools that calculate word values!

## 📋 The Rules

*What you're given:*
- An English word (could be mixed case)
- Or a list of words

*What you need to do:*
1. Build a dictionary mapping A=1, B=2, ..., Z=26
2. A function that returns the value of a single letter
3. A function that calculates a whole word's value
4. A function that finds words from a list with a specific value

*Constraints you must follow:*
- **Handle both upper and lower case** (A and a are both 1)
- Ignore non-alphabetic characters (spaces, digits, symbols, etc.)
- Empty string has a value of 0
- All function names must be `snake_case` (e.g., `calculate_word_value`)

## 💡 Example Time

**Example 1: Single letter**
```
Input: 'A' → Output: 1
Input: 'z' → Output: 26
Input: 'h' → Output: 8
```

**Example 2: Whole word**
```
Input: 'knowledge'  → Output: 96
Input: 'hardwork'   → Output: 98
Input: 'attitude'   → Output: 100  ⭐
Input: 'DISCIPLINE' → Output: 100  ⭐
```

> **Note**: There's a famous saying that knowledge and hardwork are important, but to reach 100, you need `attitude` or `discipline`!

**Example 3: Search a list**
```
Input: words = ['attitude', 'knowledge', 'discipline', 'hope']
       target_value = 100
Output: ['attitude', 'discipline']
```

## 🎓 What You Should Know

Before you start coding, make sure you understand:
- Creating dictionaries and accessing values by key (`dict[key]`)
- for loops and the enumerate function
- String methods: `.upper()`, `.isalpha()`
- Using `string.ascii_uppercase` to get the alphabet

## ✅ Your Task

Write these three functions:

| Function Name | Parameters | Returns | Description |
|---|---|---|---|
| `get_letter_value` | `letter: str` | `int` | Value of one letter (case-insensitive) |
| `calculate_word_value` | `word: str` | `int` | Total value of a word (ignore non-letters) |
| `find_words_with_value` | `words: list[str]`, `target_value: int` | `list[str]` | Words from list whose value equals target_value |

```python
import string

def get_letter_value(letter: str) -> int:
    # Your code here
    pass

def calculate_word_value(word: str) -> int:
    # Your code here
    pass

def find_words_with_value(words: list[str], target_value: int) -> list[str]:
    # Your code here
    pass
```

**Tips to get you started:**
- First, build the letter-to-number dictionary. `string.ascii_uppercase` returns `'ABCDEFGHIJKLMNOPQRSTUVWXYZ'`
- `enumerate(string.ascii_uppercase, 1)` gives you indices starting at 1
- Convert input with `.upper()` to handle case in one shot
- `calculate_word_value` can call `get_letter_value` internally — that's clean code!

## 🎪 Test Your Code

Try running these test cases:

```python
# Test 1: Single letters
print(get_letter_value('A'))   # Expected: 1
print(get_letter_value('z'))   # Expected: 26
print(get_letter_value('M'))   # Expected: 13

# Test 2: Word values
print(calculate_word_value('knowledge'))   # Expected: 96
print(calculate_word_value('hardwork'))    # Expected: 98
print(calculate_word_value('attitude'))    # Expected: 100
print(calculate_word_value('DISCIPLINE'))  # Expected: 100

# Test 3: Boundary values
print(calculate_word_value(''))            # Expected: 0
print(calculate_word_value('Hello World')) # Expected: 124 (spaces ignored)

# Test 4: List search
words = ['attitude', 'knowledge', 'discipline', 'hardwork', 'hope']
print(find_words_with_value(words, 100))  # Expected: ['attitude', 'discipline']
print(find_words_with_value(words, 96))   # Expected: ['knowledge']
print(find_words_with_value(words, 999))  # Expected: []
```

## 🤔 Think About It

Before you start coding, sketch out your approach:
1. How will you build the dictionary? for loop? enumerate?
2. How will you handle both cases at once?
3. How do you ignore the space in `'Hello World'`?
4. What if a word has numbers in it? (e.g., `'abc123'`)

Drop your questions in the thread if you get stuck! Remember, the goal is to learn, not just to finish.

Good luck! 🚀
