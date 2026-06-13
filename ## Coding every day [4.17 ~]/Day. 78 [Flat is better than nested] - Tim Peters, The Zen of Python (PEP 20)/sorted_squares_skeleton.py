# =============================================================
# Wonder Pay — 정렬된 손익을 위험도로 변환하기
# Wonder Pay — Turn Sorted P&L into Risk Scores
# =============================================================
# 빈칸(___)을 채워서 함수를 완성하세요.
# Fill in the blanks (___) to complete each function.
# 함수명과 변수명은 snake_case를 지킵니다.
# Keep all function and variable names in snake_case.
# =============================================================


def sorted_squares(nums: list[int]) -> list[int]:
    # TODO 1: 리스트 컴프리헨션으로 각 숫자를 제곱한 새 리스트를 만드세요.
    # TODO 1: Build a new list of each number squared using a list comprehension.
    #         힌트 / hint:  [ ___ for n in nums ]
    squared = ___

    # TODO 2: 제곱된 리스트를 작은 값부터 큰 값 순으로 정렬해서 반환하세요.
    # TODO 2: Return the squared list sorted from smallest to largest.
    #         힌트 / hint:  내장 함수 sorted() 를 사용하세요 / use the built-in sorted()
    return ___


# -------------------------------------------------------------
# 🎁 보너스 / BONUS
# -------------------------------------------------------------

def biggest_risk(nums: list[int]) -> int:
    # 🥉 TODO 3: 가장 큰 위험도 점수 하나를 반환하세요.
    # 🥉 TODO 3: Return the single largest risk score.
    #            힌트 / hint:  max(...) 와 컴프리헨션을 함께 / combine max(...) with a comprehension
    return ___


def total_risk(nums: list[int]) -> int:
    # 🥈 TODO 4: 모든 위험도 점수의 총합을 반환하세요.
    # 🥈 TODO 4: Return the sum of all risk scores.
    #            힌트 / hint:  sum(...) 와 컴프리헨션을 함께 / combine sum(...) with a comprehension
    return ___


def sorted_squares_no_sort(nums: list[int]) -> list[int]:
    # 🥇 TODO 5 (도전): sorted() 없이 정렬된 결과를 만드세요. (투 포인터)
    # 🥇 TODO 5 (challenge): Build the sorted result WITHOUT sorted(). (two pointers)
    n = len(nums)
    result = [0] * n
    left = 0
    right = n - 1
    pos = n - 1
    while left <= right:
        left_sq = nums[left] * nums[left]
        right_sq = nums[right] * nums[right]
        # TODO 5a: 절댓값이 큰 쪽의 제곱을 result[pos]에 넣고, 해당 포인터를 옮기세요.
        # TODO 5a: Put the larger square into result[pos], then move that pointer.
        if left_sq > right_sq:
            result[pos] = ___
            left = ___
        else:
            result[pos] = ___
            right = ___
        pos = pos - 1
    return result


# =============================================================
# 🎪 테스트 블록 / TEST BLOCK
# (배운 문법만 사용 — 직접 if/else로 채점합니다)
# (Only taught constructs — graded with plain if/else)
# =============================================================
if __name__ == "__main__":
    passed = 0
    total = 0

    # ---- Test 1 ----
    total = total + 1
    if sorted_squares([-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100]:
        passed = passed + 1
        print("Test 1 통과 / passed")
    else:
        print("Test 1 실패 / failed:", sorted_squares([-4, -1, 0, 3, 10]))

    # ---- Test 2 ----
    total = total + 1
    if sorted_squares([-7, -3, 2, 3, 11]) == [4, 9, 9, 49, 121]:
        passed = passed + 1
        print("Test 2 통과 / passed")
    else:
        print("Test 2 실패 / failed:", sorted_squares([-7, -3, 2, 3, 11]))

    # ---- Test 3 ----
    total = total + 1
    if sorted_squares([-5, -2, 0, 1, 4]) == [0, 1, 4, 16, 25]:
        passed = passed + 1
        print("Test 3 통과 / passed")
    else:
        print("Test 3 실패 / failed:", sorted_squares([-5, -2, 0, 1, 4]))

    print("결과 / score:", passed, "/", total)
