# 🧩 Python 연습: 퍼즐 보드 다루기 (2차원 리스트)!

여러분, 안녕하세요! 이번에는 모바일 퍼즐 게임의 보드를 코드로 다뤄봅니다.

## 🎯 미션

퍼즐 게임 화면을 떠올려보세요. 숫자들이 가로·세로로 격자(grid)처럼 놓여 있죠? 이런 격자는 Python에서 **리스트 안에 리스트**를 넣어서 표현합니다. 이걸 **2차원 리스트**라고 불러요.

이번 미션의 목표는 이 퍼즐 보드를 자유자재로 다루는 것입니다. 특정 칸 읽기, 한 줄 합산하기, 숫자 찾기, 그리고 보드 전체를 펼쳐서 정렬하기까지!

## 🗂️ 우리의 퍼즐 보드

```python
puzzle_board = [
    [13, 18, 33, 20,  2],
    [ 3, 40,  7, 22, 38],
    [10, 27, 31, 14, 43],
    [29,  5,  8, 25, 16],
]
```

이 보드는 **4행(row) × 5열(column)** 입니다.

- 바깥쪽 리스트의 각 원소가 한 **행**입니다.
- 각 행 안의 숫자가 그 행의 **열** 값입니다.
- `puzzle_board[행][열]` 로 칸 하나를 읽습니다. 행과 열 모두 **0번부터** 시작해요!

```python
print(puzzle_board[0][0])   # 13  (맨 위 왼쪽)
print(puzzle_board[2][4])   # 43  (3번째 행, 마지막 열)
print(puzzle_board[3][2])   #  8  (맨 아래 행, 가운데)
```

## 📋 규칙

*주어지는 것:*

- `board`라는 2차원 리스트 (행들의 리스트)
- 모든 행의 길이는 같다고 가정합니다 (직사각형 보드)

*해야 할 일 (핵심 과제):*

1. 행·열 번호로 특정 칸의 값 읽기
2. 한 행, 한 열의 합 구하기
3. 보드 전체 숫자의 합 구하기
4. 특정 숫자가 어느 칸에 있는지 찾기 (행·열 반환)
5. 보드를 1차원으로 펼친 뒤 정렬하기

*제약사항:*

- 함수 이름과 변수 이름은 모두 **snake_case** 로 작성하세요
- `sum()`, `max()` 등 사용 금지 — 직접 반복문으로 더하세요
- 보너스 과제에서만 새로운 개념을 미리 맛봅니다

## 💡 예제

**예제 1 — 칸 읽기:**
```
입력: board = puzzle_board, row = 2, col = 2
출력: 31
```
3번째 행(인덱스 2), 3번째 열(인덱스 2)의 값이 31이기 때문입니다.

**예제 2 — 한 행의 합:**
```
입력: board = puzzle_board, row = 0
출력: 86
```
첫 번째 행 `[13, 18, 33, 20, 2]` 을 모두 더하면 86입니다.

**예제 3 — 숫자 찾기:**
```
입력: board = puzzle_board, target = 43
출력: (2, 4)
```
숫자 43은 3번째 행, 5번째 열(인덱스 2, 4)에 있습니다.

## 🎓 알아야 할 것

코딩을 시작하기 전에, 다음을 이해하고 있는지 확인하세요:

- 리스트 인덱싱 (`my_list[0]`)
- **중첩 반복문** (반복문 안에 반복문)
- `range()` 와 `len()` 을 함께 쓰는 방법
- 함수에서 값 반환하기 (`return`)
- 튜플로 두 값을 한 번에 반환하기 (`return (row, col)`)

> 💬 **핵심 감 잡기:** 2차원 리스트를 다룰 때는 "바깥 반복문은 행, 안쪽 반복문은 열" 이라고 기억하면 헷갈리지 않아요.

## ✅ 과제

다음 함수들을 작성하세요. **모두 snake_case** 입니다.

```python
def get_cell(board, row, col):
    # board의 (row, col) 칸 값을 반환
    pass

def sum_row(board, row):
    # row번째 행의 모든 숫자의 합을 반환
    pass

def sum_column(board, col):
    # col번째 열의 모든 숫자의 합을 반환
    pass

def total_all_pieces(board):
    # 보드 전체 숫자의 합을 반환
    pass

def find_piece(board, target):
    # target이 있는 (row, col)을 반환, 없으면 None
    pass

def sorted_pieces(board):
    # 보드의 모든 숫자를 펼쳐 오름차순 정렬된 새 리스트로 반환
    pass
```

**시작하는 데 도움이 될 팁:**

- 한 행의 합은 `for number in board[row]:` 로 그 행만 반복하면 됩니다
- 한 열의 합은 행 번호를 바꿔가며 `board[r][col]` 을 더해야 합니다 → `for r in range(len(board)):`
- 숫자를 찾을 때는 행·열 인덱스가 모두 필요하니 `range(len(...))` 를 두 번 중첩하세요
- 펼치기(flatten)는 빈 리스트를 만들고 모든 칸을 `.append()` 하면 됩니다

## 🎪 코드 테스트

```python
puzzle_board = [
    [13, 18, 33, 20,  2],
    [ 3, 40,  7, 22, 38],
    [10, 27, 31, 14, 43],
    [29,  5,  8, 25, 16],
]

print(get_cell(puzzle_board, 2, 2))        # 예상: 31
print(sum_row(puzzle_board, 0))            # 예상: 86
print(sum_column(puzzle_board, 0))         # 예상: 55
print(total_all_pieces(puzzle_board))      # 예상: 404
print(find_piece(puzzle_board, 43))        # 예상: (2, 4)
print(find_piece(puzzle_board, 999))       # 예상: None
print(sorted_pieces(puzzle_board)[:5])     # 예상: [2, 3, 5, 7, 8]
```

## 🌟 보너스 도전 과제

### 🥉 Easy — 가장 큰 조각 찾기
`max()` 를 쓰지 말고, 반복문만으로 보드 전체에서 **가장 큰 숫자**를 반환하는 `find_largest_piece(board)` 를 작성하세요.

### 🥈 Medium — 임계값 넘는 칸 세기
`count_above(board, threshold)` 를 작성하세요. `threshold` 보다 **큰** 숫자가 몇 칸이나 있는지 반환합니다.
예: `count_above(puzzle_board, 30)` → `5` (31, 33, 38, 40, 43)

### 🥇 Hard — 십의 자리별로 묶어 세기 (딕셔너리 미리보기!)
> ⚠️ 이 과제는 다음에 배울 **딕셔너리(dictionary)** 를 미리 맛보는 단계입니다.

`count_by_tens(board)` 를 작성하세요. 각 숫자를 십의 자리 기준으로 묶어(`0, 10, 20, ...`), 각 묶음에 몇 개가 있는지 딕셔너리로 반환합니다.
예: `count_by_tens(puzzle_board)` → `{0: 5, 10: 5, 20: 5, 30: 3, 40: 2}`
힌트: `(number // 10) * 10` 으로 묶음 키를 만들 수 있어요.

## 🤔 생각해보기

1. `board[row][col]` 에서 첫 번째 `[ ]` 와 두 번째 `[ ]` 는 각각 무엇을 고르는 걸까요?
2. 행의 합과 열의 합을 구하는 코드가 왜 서로 다르게 생겼을까요?
3. `find_piece` 에서 숫자를 찾자마자 바로 `return` 하면 어떤 점이 좋을까요?
4. 보드가 직사각형이 아니라 행마다 길이가 다르다면, 어떤 코드가 문제를 일으킬까요?

막히면 스레드에 질문을 남겨주세요! 목표는 끝내는 것이 아니라 배우는 것입니다. 천천히 논리를 이해하면서 진행하세요.

행운을 빕니다! 🚀

---
---

# 🧩 Python Practice: Working With a Puzzle Board (2D Lists)!

Hey team! This time we're taking the board from a mobile puzzle game and handling it in code.

## 🎯 Your Mission

Picture a puzzle game screen. The numbers sit in a grid — rows across, columns down. In Python we represent a grid like that with a **list inside a list**, called a **2D list (two-dimensional list)**.

Your mission is to handle this puzzle board with confidence: read a specific cell, sum a row, find a number, and flatten the whole board out and sort it!

## 🗂️ Our Puzzle Board

```python
puzzle_board = [
    [13, 18, 33, 20,  2],
    [ 3, 40,  7, 22, 38],
    [10, 27, 31, 14, 43],
    [29,  5,  8, 25, 16],
]
```

This board is **4 rows × 5 columns**.

- Each element of the outer list is one **row**.
- Each number inside a row is a **column** value in that row.
- You read one cell with `puzzle_board[row][col]`. Both rows and columns start at **0**!

```python
print(puzzle_board[0][0])   # 13  (top-left)
print(puzzle_board[2][4])   # 43  (3rd row, last column)
print(puzzle_board[3][2])   #  8  (bottom row, middle)
```

## 📋 The Rules

*What you're given:*

- A 2D list called `board` (a list of rows)
- Assume every row has the same length (a rectangular board)

*What you need to do (core tasks):*

1. Read a specific cell by its row and column number
2. Sum one row and one column
3. Sum every number on the board
4. Find which cell holds a given number (return its row and column)
5. Flatten the board into one list and sort it

*Constraints:*

- All function and variable names must use **snake_case**
- Don't use syntax you haven't learned yet in the core tasks (no `sum()`, `max()`, etc. — add with a loop instead)
- New concepts appear only in the bonus tiers as a preview

## 💡 Examples

**Example 1 — read a cell:**
```
Input: board = puzzle_board, row = 2, col = 2
Output: 31
```
The value at row index 2, column index 2 is 31.

**Example 2 — sum a row:**
```
Input: board = puzzle_board, row = 0
Output: 86
```
Adding up the first row `[13, 18, 33, 20, 2]` gives 86.

**Example 3 — find a number:**
```
Input: board = puzzle_board, target = 43
Output: (2, 4)
```
The number 43 sits at row index 2, column index 4.

## 🎓 What You Should Know

Before you start coding, make sure you understand:

- List indexing (`my_list[0]`)
- **Nested loops** (a loop inside a loop)
- Using `range()` together with `len()`
- Returning a value from a function (`return`)
- Returning two values at once with a tuple (`return (row, col)`)

> 💬 **Key intuition:** When working with a 2D list, remember "outer loop = rows, inner loop = columns" and you won't get lost.

## ✅ Your Task

Write these functions. They're **all snake_case**.

```python
def get_cell(board, row, col):
    # Return the value at (row, col) of board
    pass

def sum_row(board, row):
    # Return the sum of all numbers in the given row
    pass

def sum_column(board, col):
    # Return the sum of all numbers in the given column
    pass

def total_all_pieces(board):
    # Return the sum of every number on the board
    pass

def find_piece(board, target):
    # Return (row, col) where target sits, or None if not found
    pass

def sorted_pieces(board):
    # Return a new list of all numbers, flattened and sorted ascending
    pass
```

**Tips to get you started:**

- A row sum just loops over that one row: `for number in board[row]:`
- A column sum changes the row number while keeping the column: `for r in range(len(board)):` then add `board[r][col]`
- To find a number you need both indices, so nest `range(len(...))` twice
- To flatten, make an empty list and `.append()` every cell into it

## 🎪 Test Your Code

```python
puzzle_board = [
    [13, 18, 33, 20,  2],
    [ 3, 40,  7, 22, 38],
    [10, 27, 31, 14, 43],
    [29,  5,  8, 25, 16],
]

print(get_cell(puzzle_board, 2, 2))        # Expected: 31
print(sum_row(puzzle_board, 0))            # Expected: 86
print(sum_column(puzzle_board, 0))         # Expected: 55
print(total_all_pieces(puzzle_board))      # Expected: 404
print(find_piece(puzzle_board, 43))        # Expected: (2, 4)
print(find_piece(puzzle_board, 999))       # Expected: None
print(sorted_pieces(puzzle_board)[:5])     # Expected: [2, 3, 5, 7, 8]
```

## 🌟 Bonus Challenges

### 🥉 Easy — Find the Biggest Piece
Without using `max()`, write `find_largest_piece(board)` that returns the **largest number** on the whole board using only loops.

### 🥈 Medium — Count Cells Above a Threshold
Write `count_above(board, threshold)` that returns how many cells hold a number **greater than** `threshold`.
Example: `count_above(puzzle_board, 30)` → `5` (31, 33, 38, 40, 43)

### 🥇 Hard — Group and Count by Tens (Dictionary Preview!)
> ⚠️ This task previews **dictionaries**, which you'll learn next.

Write `count_by_tens(board)` that groups each number by its tens place (`0, 10, 20, ...`) and returns a dictionary of how many numbers fall in each group.
Example: `count_by_tens(puzzle_board)` → `{0: 5, 10: 5, 20: 5, 30: 3, 40: 2}`
Hint: `(number // 10) * 10` gives you the group key.

## 🤔 Think About It

1. In `board[row][col]`, what does the first `[ ]` pick, and what does the second `[ ]` pick?
2. Why does the code for summing a row look different from summing a column?
3. In `find_piece`, what's the benefit of returning as soon as you find the number?
4. If the board were *not* rectangular (rows of different lengths), which piece of code might break?

Drop your questions in the thread if you get stuck! Remember, the goal is to learn, not just to finish. Take your time and understand the logic.

Good luck! 🚀
