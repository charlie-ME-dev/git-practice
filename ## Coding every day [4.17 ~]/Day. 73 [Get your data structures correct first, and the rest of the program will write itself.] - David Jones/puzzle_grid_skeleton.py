# 🧩 퍼즐 보드 다루기 (2차원 리스트) — 스켈레톤 파일
# Puzzle Board (2D Lists) — Skeleton File
#
# 빈칸(___)과 TODO를 채워 함수를 완성하세요.
# Fill in the blanks (___) and TODOs to complete each function.
# 모든 이름은 snake_case 입니다. / All names are snake_case.


# 우리의 퍼즐 보드 (수정하지 마세요)
# Our puzzle board (do not modify)
puzzle_board = [
    [13, 18, 33, 20,  2],
    [ 3, 40,  7, 22, 38],
    [10, 27, 31, 14, 43],
    [29,  5,  8, 25, 16],
]


def get_cell(board, row, col):
    # TODO 1: (row, col) 칸의 값을 반환하세요.
    # TODO 1: Return the value at cell (row, col).
    return board[___][___]


def sum_row(board, row):
    # TODO 2: row번째 행의 모든 숫자를 더해 반환하세요.
    # TODO 2: Add up every number in the given row and return it.
    total = 0
    for number in board[___]:
        total = total + ___
    return total


def sum_column(board, col):
    # TODO 3: col번째 열의 모든 숫자를 더해 반환하세요.
    # TODO 3: Add up every number in the given column and return it.
    # 힌트: 행 번호를 바꿔가며 board[r][col]을 더합니다.
    # Hint: change the row number while keeping the column.
    total = 0
    for r in range(len(board)):
        total = total + board[r][___]
    return total


def total_all_pieces(board):
    # TODO 4: 보드 전체 숫자의 합을 반환하세요. (중첩 반복문)
    # TODO 4: Return the sum of every number on the board. (nested loop)
    total = 0
    for row in board:
        for number in ___:
            total = total + ___
    return total


def find_piece(board, target):
    # TODO 5: target이 있는 (row, col)을 반환하세요. 없으면 None.
    # TODO 5: Return (row, col) where target sits, or None if not found.
    for r in range(len(board)):
        for c in range(len(board[r])):
            if board[r][c] == ___:
                return (___, ___)
    return ___


def sorted_pieces(board):
    # TODO 6: 모든 숫자를 한 리스트로 펼친 뒤 오름차순 정렬하여 반환하세요.
    # TODO 6: Flatten all numbers into one list, sort ascending, and return.
    flat = []
    for row in board:
        for number in row:
            flat.append(___)
    flat.sort()
    return ___


# ─────────────────────────────────────────────
# 테스트 블록 — 수정하지 마세요
# Test block — do not modify
# ─────────────────────────────────────────────
passed = 0

if get_cell(puzzle_board, 2, 2) == 31:
    passed = passed + 1
    print("✅ 테스트 1 통과 / Test 1 passed")
else:
    print("❌ 테스트 1 실패 / Test 1 failed")

if sum_row(puzzle_board, 0) == 86:
    passed = passed + 1
    print("✅ 테스트 2 통과 / Test 2 passed")
else:
    print("❌ 테스트 2 실패 / Test 2 failed")

if sum_column(puzzle_board, 0) == 55:
    passed = passed + 1
    print("✅ 테스트 3 통과 / Test 3 passed")
else:
    print("❌ 테스트 3 실패 / Test 3 failed")

if total_all_pieces(puzzle_board) == 404:
    passed = passed + 1
    print("✅ 테스트 4 통과 / Test 4 passed")
else:
    print("❌ 테스트 4 실패 / Test 4 failed")

if find_piece(puzzle_board, 43) == (2, 4) and find_piece(puzzle_board, 999) is None:
    passed = passed + 1
    print("✅ 테스트 5 통과 / Test 5 passed")
else:
    print("❌ 테스트 5 실패 / Test 5 failed")

if sorted_pieces(puzzle_board)[:5] == [2, 3, 5, 7, 8]:
    passed = passed + 1
    print("✅ 테스트 6 통과 / Test 6 passed")
else:
    print("❌ 테스트 6 실패 / Test 6 failed")

print("결과 / Result:", passed, "/ 6")
