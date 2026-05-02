"""
🏃 Next Permutation Practice — Skeleton
다음 순열 만들기 — 시작 코드

규칙 (Rules):
- nums를 in-place로 수정하세요 (Modify nums in-place)
- sorted(), sort(), reversed(), [::-1] 사용 금지 (Forbidden)
- itertools 등 라이브러리 사용 금지 (No libraries)
- while 반복문과 a, b = b, a 교환을 활용하세요
"""


def next_permutation(nums: list[int]) -> None:
    n = len(nums)

    # ---------------------------------------------------------------
    # TODO 1: 피벗(pivot) 찾기
    # TODO 1: Find the pivot
    # KO: 오른쪽에서 왼쪽으로 보면서, nums[i] < nums[i+1]이 되는 가장 오른쪽 i를 찾으세요.
    # EN: Scan right-to-left and find the largest i such that nums[i] < nums[i+1].
    # 못 찾으면 i는 -1로 끝나야 합니다 (전체가 내림차순이라는 뜻).
    # If not found, i should end as -1 (the whole array is descending).
    # ---------------------------------------------------------------
    i = n - 2
    # 여기에 while 반복문을 작성하세요 (Write your while loop here)
    while i >= 0 and nums[i] >= nums[i+1]:
        i -= 1

    # ---------------------------------------------------------------
    # TODO 2: 교환 대상(swap target) 찾고 교환하기
    # TODO 2: Find the swap target and swap
    # KO: i >= 0인 경우에만, 오른쪽에서 왼쪽으로 보면서 nums[j] > nums[i]인 가장 오른쪽 j를 찾으세요.
    #     그런 다음 nums[i]와 nums[j]를 교환하세요.
    # EN: Only if i >= 0, scan right-to-left to find the largest j with nums[j] > nums[i].
    #     Then swap nums[i] and nums[j].
    # 힌트 (Hint): a, b = b, a 문법으로 교환할 수 있습니다.
    # ---------------------------------------------------------------
    if i >= 0:
        j = n - 1
        # 여기에 while 반복문과 교환 코드를 작성하세요
        # Write your while loop and swap here
        while nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]


    # ---------------------------------------------------------------
    # TODO 3: i+1부터 끝까지 뒤집기 (두 포인터 방식)
    # TODO 3: Reverse the suffix from i+1 to the end (two-pointer style)
    # KO: left = i+1, right = n-1로 시작해서, left < right인 동안 교환하면서 안쪽으로 좁혀오세요.
    # EN: Start with left = i+1, right = n-1. While left < right, swap them and move inward.
    # 주의 (Note): i = -1인 경우에도 left = 0이 되어 전체가 뒤집혀야 합니다.
    # Even when i = -1, left becomes 0, so the entire array gets reversed (correct!).
    # ---------------------------------------------------------------
    left = i + 1
    right = n - 1
    # 여기에 while 반복문을 작성하세요 (Write your while loop here)
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1  


# ============================================================
# ⚠️ 아래 부분은 수정하지 마세요 (DO NOT MODIFY BELOW)
# ============================================================
if __name__ == "__main__":
    # 테스트 1: 일반적인 경우 (Typical case)
    nums1 = [1, 2, 3]
    next_permutation(nums1)
    print(f"테스트 1 (Test 1): {nums1}")
    # 예상 (Expected): [1, 3, 2]

    # 테스트 2: 가장 큰 → 가장 작은 (Largest → smallest)
    nums2 = [3, 2, 1]
    next_permutation(nums2)
    print(f"테스트 2 (Test 2): {nums2}")
    # 예상 (Expected): [1, 2, 3]

    # 테스트 3: 중복 (With duplicates)
    nums3 = [1, 1, 5]
    next_permutation(nums3)
    print(f"테스트 3 (Test 3): {nums3}")
    # 예상 (Expected): [1, 5, 1]

    # 테스트 4: 길이 1 (Length 1)
    nums4 = [1]
    next_permutation(nums4)
    print(f"테스트 4 (Test 4): {nums4}")
    # 예상 (Expected): [1]

    # 테스트 5: 까다로운 경우 (Tricky case)
    nums5 = [1, 3, 2]
    next_permutation(nums5)
    print(f"테스트 5 (Test 5): {nums5}")
    # 예상 (Expected): [2, 1, 3]
