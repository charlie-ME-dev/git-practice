"""
🕵️ 4Sum 연습 — 수상한 거래 조합 찾기
🕵️ 4Sum Practice — Find Suspicious Transaction Combos

⚠️ 사용 금지 / FORBIDDEN:
   - set, tuple, itertools, dict, collections
   - 재귀 / recursion
   - 리스트 컴프리헨션 / list comprehensions

✅ 사용 가능 / ALLOWED:
   - list, .sort(), .append(), 인덱싱 / indexing
   - for, while, if, continue
"""


def four_sum(nums: list[int], target: int) -> list[list[int]]:
    """
    합이 target이 되는 4개 숫자의 모든 고유한 조합을 반환합니다.
    Return all unique combinations of 4 numbers that sum to target.
    """
    # TODO 1: 결과를 담을 빈 리스트를 만드세요.
    # TODO 1: Create an empty list to store results.
    result = ___

    # TODO 2: 리스트의 길이를 구하세요.
    # TODO 2: Get the length of the list.
    n = ___

    # TODO 3: 리스트 길이가 4보다 작으면 빈 결과를 바로 반환하세요.
    # TODO 3: If the list has fewer than 4 elements, return empty result immediately.
    if ___ < ___:
        return ___

    # TODO 4: nums를 오름차순으로 정렬하세요. (투 포인터의 핵심!)
    # TODO 4: Sort nums in ascending order. (The KEY to two pointers!)
    nums.___()

    # ===== 바깥쪽 반복문: 첫 번째 숫자 선택 =====
    # ===== Outer loop: pick the first number =====
    # TODO 5: i를 0부터 n-3까지 반복하세요. (뒤에 3개는 남겨둬야 함)
    # TODO 5: Loop i from 0 to n-3. (Leave room for 3 more numbers.)
    for i in range(___, ___):

        # TODO 6: i > 0이고 nums[i]가 이전 값과 같으면 건너뛰세요 (중복 방지).
        # TODO 6: Skip duplicate: if i > 0 and nums[i] equals the previous value.
        if ___ > 0 and nums[___] == nums[___]:
            continue

        # ===== 안쪽 반복문: 두 번째 숫자 선택 =====
        # ===== Inner loop: pick the second number =====
        # TODO 7: j를 i+1부터 n-2까지 반복하세요.
        # TODO 7: Loop j from i+1 to n-2.
        for j in range(___, ___):

            # TODO 8: j > i+1이고 nums[j]가 이전 값과 같으면 건너뛰세요.
            # TODO 8: Skip duplicate: if j > i+1 and nums[j] equals the previous value.
            if ___ > i + 1 and nums[___] == nums[___]:
                continue

            # ===== 투 포인터: 나머지 두 숫자 찾기 =====
            # ===== Two pointers: find the remaining two numbers =====
            # TODO 9: left는 j 바로 다음, right는 리스트 맨 끝을 가리키도록 설정하세요.
            # TODO 9: Set left to just after j, and right to the last index.
            left = ___
            right = ___

            # TODO 10: left가 right보다 작은 동안 반복하세요.
            # TODO 10: Loop while left is less than right.
            while ___ < ___:

                # TODO 11: 4개 숫자의 합을 계산하세요.
                # TODO 11: Compute the sum of the 4 numbers.
                total = nums[i] + nums[j] + nums[___] + nums[___]

                # TODO 12: 합이 target과 같으면…
                # TODO 12: If the sum equals target…
                if total == ___:
                    # TODO 13: 조합 [nums[i], nums[j], nums[left], nums[right]]를 결과에 추가하세요.
                    # TODO 13: Append [nums[i], nums[j], nums[left], nums[right]] to result.
                    result.___([nums[i], nums[j], nums[___], nums[___]])

                    # TODO 14: left 쪽 중복 건너뛰기 — nums[left]가 다음 값과 같은 동안 left를 증가시키세요.
                    # TODO 14: Skip left duplicates — while nums[left] equals the next value, increment left.
                    while left < right and nums[left] == nums[___ + 1]:
                        left = ___ + 1

                    # TODO 15: right 쪽 중복 건너뛰기 — nums[right]가 이전 값과 같은 동안 right를 감소시키세요.
                    # TODO 15: Skip right duplicates — while nums[right] equals the previous value, decrement right.
                    while left < right and nums[right] == nums[___ - 1]:
                        right = ___ - 1

                    # TODO 16: 두 포인터를 각각 한 칸씩 안쪽으로 이동시키세요.
                    # TODO 16: Move both pointers one step inward.
                    left = ___ + 1
                    right = ___ - 1

                # TODO 17: 합이 target보다 작으면 left를 증가시키세요 (더 큰 수 필요).
                # TODO 17: If the sum is less than target, increment left (need bigger).
                elif total < ___:
                    left = ___ + 1

                # TODO 18: 그렇지 않으면 (합이 target보다 큼) right를 감소시키세요.
                # TODO 18: Otherwise (sum is greater than target), decrement right.
                else:
                    right = ___ - 1

    # TODO 19: 결과를 반환하세요.
    # TODO 19: Return the result.
    return ___


# ==========================================================================
# ⛔ 아래 테스트 블록은 수정하지 마세요! / DO NOT MODIFY THE TEST BLOCK BELOW!
# ==========================================================================
if __name__ == "__main__":

    def normalize(quads):
        """비교를 위해 정규화 / Normalize for comparison"""
        return sorted([sorted(q) for q in quads])

    tests = [
        ([1, 0, -1, 0, -2, 2], 0, [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]),
        ([2, 2, 2, 2, 2], 8, [[2, 2, 2, 2]]),
        ([1, 2, 3, 4], 100, []),
        ([0, 0, 0, 0], 0, [[0, 0, 0, 0]]),
        ([1, 2, 3], 6, []),
        ([], 0, []),
        ([-3, -1, 0, 2, 4, 5], 2, [[-3, -1, 2, 4]]),
        ([1000, 1000, 1000, 1000], 4000, [[1000, 1000, 1000, 1000]]),
    ]

    passed = 0
    for idx, (nums, target, expected) in enumerate(tests, 1):
        got = four_sum(list(nums), target)
        if normalize(got) == normalize(expected):
            print(f"✅ Test {idx} passed")
            passed = passed + 1
        else:
            print(f"❌ Test {idx} FAILED")
            print(f"   입력 / Input:    nums={nums}, target={target}")
            print(f"   기대 / Expected: {expected}")
            print(f"   결과 / Got:      {got}")

    print(f"\n총 {passed}/{len(tests)}개 테스트 통과 / {passed}/{len(tests)} tests passed")
