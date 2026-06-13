"""
연습 문제: 최고 평균 구간 찾기 (Maximum Average Subarray)
Practice: Maximum Average Subarray

길이가 k인 연속된 부분 리스트 중 평균이 가장 큰 것의 평균값을 반환하세요.
Return the maximum average value among all contiguous subarrays of length k.
"""


def find_max_average(nums: list[int], k: int) -> float:
    # KO: TODO 1 — 첫 번째 윈도우의 합을 계산하세요 (인덱스 0부터 k-1까지).
    # EN: TODO 1 — Compute the sum of the first window (indices 0 to k-1).
    # 힌트 / Hint: sum()과 슬라이싱을 활용하세요. / Use sum() with slicing.
    window_sum = 0

    # KO: TODO 2 — 지금까지 본 최댓값을 추적할 변수를 초기화하세요.
    # EN: TODO 2 — Initialize a variable to track the maximum sum seen so far.
    # 주의 / Caution: 0으로 시작하면 음수 입력에서 틀립니다!
    #                 Starting at 0 fails on all-negative inputs!
    max_sum = 0

    # KO: TODO 3 — 윈도우를 한 칸씩 오른쪽으로 옮기며 합을 갱신하세요.
    # EN: TODO 3 — Slide the window one step right, updating the sum each time.
    # 힌트 / Hint: 들어오는 값(nums[i])을 더하고, 나가는 값(nums[i - k])을 빼세요.
    #              Add the entering value (nums[i]) and subtract the leaving one (nums[i - k]).
    for i in range(k, len(nums)):
        # KO: 윈도우 합 갱신 / EN: Update the window sum
        pass

        # KO: 최댓값 갱신 / EN: Update the maximum
        pass

    # KO: TODO 4 — 합이 아닌 "평균"을 반환해야 합니다. k로 나누세요.
    # EN: TODO 4 — Return the "average," not the sum. Divide by k.
    return 0.0


if __name__ == "__main__":
    # KO: 기본 테스트 케이스 / EN: Basic test cases
    print("Test 1:", find_max_average([1, 12, -5, -6, 50, 3], 4))
    # 예상 / Expected: 12.75

    print("Test 2:", find_max_average([5], 1))
    # 예상 / Expected: 5.0

    print("Test 3:", find_max_average([-1, -2, -3, -4, -5], 2))
    # 예상 / Expected: -1.5

    print("Test 4:", find_max_average([1, 2, 3, 4, 5], 5))
    # 예상 / Expected: 3.0

    print("Test 5:", find_max_average([1, 1, 1, 1, 1], 3))
    # 예상 / Expected: 1.0

    print("Test 6:", find_max_average([10, -10, 10, -10, 10], 1))
    # 예상 / Expected: 10.0
