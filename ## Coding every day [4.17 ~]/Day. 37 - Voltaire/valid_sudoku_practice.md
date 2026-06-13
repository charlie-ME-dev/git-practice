# 🐍 Python 연습: 스도쿠 검증기 만들기!

여러분, 좋은 아침입니다! ☀️ 오늘은 진짜 게임 회사에서 일하는 것처럼 코딩해볼 거예요.

## 🎯 미션

여러분은 모바일 퍼즐 게임 회사의 신입 개발자입니다. 사용자가 스도쿠 퍼즐을 풀고 있을 때, 입력한 값이 규칙에 맞는지 실시간으로 확인해야 해요. 여러분의 임무는 **현재 보드 상태가 유효한지** 검사하는 함수를 만드는 것입니다.

**중요한 점:** 보드를 *완성*시킬 필요는 없어요. 지금까지 채워진 숫자들이 스도쿠 규칙을 어기지 않았는지만 확인하면 됩니다!

## 📋 규칙

*주어지는 것:*
• 9 x 9 크기의 2차원 리스트 `board` (리스트 안에 리스트)
• 각 칸에는 1~9 사이의 정수 또는 빈 칸을 의미하는 `0`이 들어있음

*해야 할 일:*
보드가 다음 세 가지 규칙을 모두 만족하면 `True`, 하나라도 어기면 `False`를 반환:
1. **각 행(row)**에 1~9 숫자가 중복 없이 나타나야 함
2. **각 열(column)**에 1~9 숫자가 중복 없이 나타나야 함
3. **9개의 3x3 박스** 각각에 1~9 숫자가 중복 없이 나타나야 함

*반드시 지켜야 할 것:*
• `0`은 빈 칸이므로 검사에서 제외하세요
• 보드가 꽉 차 있을 필요는 없습니다
• `set`을 사용해서 중복을 추적하세요 (이미 배운 자료구조 활용!)

## 💡 예제

**예제 1 — 유효한 보드:**
```
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]
```
출력: `True` — 모든 행, 열, 박스에 중복이 없습니다!

**예제 2 — 행 중복:**
첫 번째 행이 `[8, 3, 0, 0, 7, 0, 0, 0, 8]`이라면? 8이 두 번 나타나므로 `False`!

**예제 3 — 박스 중복:**
좌상단 3x3 박스 안에 5가 두 번 들어있다면? 행과 열은 멀쩡해도 `False`!

## 🎓 알아야 할 것

코딩을 시작하기 전에, 다음을 이해하고 있는지 확인하세요:
• 2차원 리스트 인덱싱: `board[행][열]`
• `set` 자료구조와 `add()`, `in` 연산자 사용법
• 중첩 반복문 (`for` 안에 `for`)
• 정수 나눗셈 `//`의 의미

## ✅ 과제

다음 시그니처로 함수를 작성하세요:
```python
def is_valid_sudoku(board: list[list[str]]) -> bool:
    # 여기에 코드 작성
    pass
```

> 💬 **타입 힌트 설명:** `list[list[str]]`는 "리스트 안에 또 리스트가 들어있다"는 뜻입니다. 우리는 정수를 사용하지만 LeetCode 원본 문제와 일관성을 위해 이 시그니처를 사용해요. 실제로는 `int`가 들어옵니다!

**시작하는 데 도움이 될 팁:**
• 행, 열, 박스를 따로따로 검사하면 코드가 깔끔해집니다
• 9개 박스 중 어느 박스에 속하는지 알려면? `(행 // 3, 열 // 3)`을 생각해보세요
• 빈 칸(`0`)을 만나면 `continue`로 건너뛰세요

## 🎪 코드 테스트

다음 테스트 케이스를 실행해보세요:

```python
# 테스트 1: 유효한 보드
valid_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]
print(is_valid_sudoku(valid_board))  # 예상: True

# 테스트 2: 빈 보드
empty_board = [[0] * 9 for _ in range(9)]
print(is_valid_sudoku(empty_board))  # 예상: True

# 테스트 3: 박스 중복 (좌상단 박스에 5가 두 번)
invalid_box = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 5, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]
print(is_valid_sudoku(invalid_box))  # 예상: False
```

## 🤔 생각해보기

코딩을 시작하기 전에, 접근 방법을 스케치해보세요:
1. 한 행에 중복이 있는지 어떻게 확인할까요? (힌트: `set`과 길이 비교)
2. 한 열을 어떻게 순회할까요? 행과는 인덱싱이 어떻게 다를까요?
3. 좌표 `(행, 열)`이 주어졌을 때, 그 칸이 9개 박스 중 어느 박스인지 어떻게 계산할까요?

## 🌟 보너스 도전

기본 함수를 완성했나요? 더 도전해보세요!

**🟢 Easy — 보너스 1:**
유효하지 않은 보드를 받았을 때, 어느 규칙(행/열/박스)을 어겼는지 출력하는 함수를 만들어보세요.
```python
def explain_invalid(board: list[list[str]]) -> str:
    # "Row 2 has duplicate" 같은 메시지 반환
    pass
```

**🟡 Medium — 보너스 2:**
보드를 받아서 각 숫자(1~9)가 몇 번씩 나타나는지 `dict`로 반환하는 함수를 만들어보세요.
```python
def count_digits(board: list[list[str]]) -> dict:
    # 예: {1: 5, 2: 3, ..., 9: 4}
    pass
```

**🔴 Hard — 보너스 3:**
유효한 보드일 때, 비어있는 칸 중 한 곳을 골라 그 칸에 들어갈 수 있는 후보 숫자들의 집합을 반환하세요.
```python
def find_candidates(board: list[list[str]], row: int, col: int) -> set:
    # 예: {2, 4, 7} — 이 칸에 들어갈 수 있는 숫자들
    pass
```

---

막히면 스레드에 질문을 남겨주세요! 목표는 끝내는 것이 아니라 **2차원 리스트와 set을 자유자재로 다루는 감각**을 익히는 것입니다. 천천히 가세요!

행운을 빕니다! 🚀

---
---

# 🐍 Python Practice: Build a Sudoku Validator!

Good morning, team! ☀️ Today we're coding like real game studio devs.

## 🎯 Your Mission

You're a junior developer at a mobile puzzle game company. While users solve Sudoku puzzles, you need to check in real-time whether their input follows the rules. Your job is to write a function that determines whether **the current board state is valid**.

**Important:** You don't need to *solve* the board. Just check whether the numbers placed so far break any Sudoku rules!

## 📋 The Rules

*What you're given:*
• A 9 x 9 2D list called `board` (a list of lists)
• Each cell contains an integer from 1~9, or `0` representing an empty cell

*What you need to do:*
Return `True` if the board satisfies all three rules, `False` if any rule is broken:
1. **Each row** must contain digits 1~9 with no duplicates
2. **Each column** must contain digits 1~9 with no duplicates
3. **Each of the nine 3x3 boxes** must contain digits 1~9 with no duplicates

*Constraints you must follow:*
• `0` represents empty cells — exclude them from validation
• The board doesn't need to be complete
• Use `set` to track duplicates (apply what you've learned!)

## 💡 Example Time

**Example 1 — Valid board:**
```
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]
```
Output: `True` — no duplicates in any row, column, or box!

**Example 2 — Row duplicate:**
What if row 1 is `[8, 3, 0, 0, 7, 0, 0, 0, 8]`? 8 appears twice → `False`!

**Example 3 — Box duplicate:**
What if the top-left 3x3 box has two 5s in it? Even if rows and columns are fine → `False`!

## 🎓 What You Should Know

Before you start coding, make sure you understand:
• 2D list indexing: `board[row][col]`
• The `set` data structure with `add()` and the `in` operator
• Nested loops (`for` inside `for`)
• What integer division `//` means

## ✅ Your Task

Write a function with this signature:
```python
def is_valid_sudoku(board: list[list[str]]) -> bool:
    # Your code here
    pass
```

> 💬 **About the type hint:** `list[list[str]]` means "a list containing more lists." We're using integers, but we keep this signature for consistency with the original LeetCode problem. In practice, `int` values come in!

**Tips to get you started:**
• Checking rows, columns, and boxes separately keeps your code clean
• To find which of the 9 boxes a cell belongs to, think about `(row // 3, col // 3)`
• When you hit an empty cell (`0`), use `continue` to skip it

## 🎪 Test Your Code

Try running these test cases:

```python
# Test 1: Valid board
valid_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]
print(is_valid_sudoku(valid_board))  # Expected: True

# Test 2: Empty board
empty_board = [[0] * 9 for _ in range(9)]
print(is_valid_sudoku(empty_board))  # Expected: True

# Test 3: Box duplicate (top-left box has two 5s)
invalid_box = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 5, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]
print(is_valid_sudoku(invalid_box))  # Expected: False
```

## 🤔 Think About It

Before you start coding, sketch out your approach:
1. How will you check if a row has duplicates? (Hint: `set` and length comparison)
2. How do you iterate through a column? How is indexing different from a row?
3. Given coordinates `(row, col)`, how do you compute which of the 9 boxes that cell belongs to?

## 🌟 Bonus Challenges

Finished the main function? Try going further!

**🟢 Easy — Bonus 1:**
When given an invalid board, write a function that prints which rule (row/column/box) was broken.
```python
def explain_invalid(board: list[list[str]]) -> str:
    # Return a message like "Row 2 has duplicate"
    pass
```

**🟡 Medium — Bonus 2:**
Given a board, return a `dict` showing how many times each digit (1~9) appears.
```python
def count_digits(board: list[list[str]]) -> dict:
    # Example: {1: 5, 2: 3, ..., 9: 4}
    pass
```

**🔴 Hard — Bonus 3:**
For a valid board, given an empty cell, return the set of candidate digits that could go in that cell.
```python
def find_candidates(board: list[list[str]], row: int, col: int) -> set:
    # Example: {2, 4, 7} — digits that could legally fit
    pass
```

---

Drop your questions in the thread if you get stuck! Remember, the goal isn't just to finish — it's to build **fluency with 2D lists and sets**. Take your time!

Good luck! 🚀
