# 🔀 Two-List Merger - Skeleton Code
# 두 리스트 합치기 - 뼈대 코드

# ============================================================
# 함수를 완성하세요! Complete each function below.
# 각 TODO 주석을 읽고 코드를 채워 넣으세요.
# Read each TODO comment and fill in the code.
# ⚠️  sort() 또는 sorted() 사용 금지! / No sort() or sorted()!
# ============================================================


def merge_lists(list_a: list, list_b: list) -> list:
    """
    두 개의 정렬된 리스트를 하나의 정렬된 리스트로 합칩니다.
    Merges two sorted lists into one sorted list.

    두 리스트가 이미 정렬되어 있다는 점을 활용하세요!
    Use the fact that both lists are already sorted!
    """
    # TODO 1: 결과를 담을 빈 리스트와 두 포인터(인덱스)를 만드세요.
    #         Create an empty result list and two pointer variables.
    #         힌트 / Hint:
    #             result = []
    #             i = 0   ← list_a에서 현재 볼 위치 / current position in list_a
    #             j = 0   ← list_b에서 현재 볼 위치 / current position in list_b

    # TODO 2: 두 리스트 모두 남은 항목이 있는 동안 반복하세요.
    #         Loop while both lists still have remaining items.
    #         힌트 / Hint: while i < len(list_a) and j < len(list_b):

        # TODO 3: list_a[i]와 list_b[j]를 비교하세요.
        #         Compare list_a[i] and list_b[j].

        # TODO 4: 더 작은 쪽을 result에 추가하고, 그 포인터를 1 증가시키세요.
        #         Append the smaller one to result, and move that pointer forward by 1.
        #         힌트 / Hint:
        #             if list_a[i] <= list_b[j]:
        #                 result.append(list_a[i])
        #                 i = i + 1
        #             else:
        #                 ...

    # TODO 5: 반복이 끝난 후, list_a에 남은 항목이 있으면 result에 붙이세요.
    #         After the loop, attach any remaining items from list_a to result.
    #         힌트 / Hint: result = result + list_a[i:]

    # TODO 6: list_b에 남은 항목도 result에 붙이세요.
    #         Do the same for any remaining items from list_b.
    #         힌트 / Hint: result = result + list_b[j:]

    # TODO 7: 완성된 result를 반환하세요.
    #         Return the completed result list.
    pass


# ============================================================
# 🌟 보너스 챌린지 / Bonus Challenges
# 기본 과제를 모두 마친 후 시도해보세요!
# Try these only after finishing the main task!
# ============================================================


def merge_three(list_a: list, list_b: list, list_c: list) -> list:
    """
    🥉 Easy Bonus
    세 개의 정렬된 리스트를 하나로 합칩니다.
    Merges three sorted lists into one sorted list.

    merge_lists()를 두 번 재사용하세요! 새 로직 필요 없어요.
    Reuse merge_lists() twice! No new merge logic needed.
    """
    # TODO 1: merge_lists()를 호출해서 list_a와 list_b를 먼저 합치세요.
    #         Call merge_lists() to merge list_a and list_b first.

    # TODO 2: 그 결과와 list_c를 다시 merge_lists()로 합치세요.
    #         Then merge that result with list_c using merge_lists() again.

    # TODO 3: 최종 결과를 반환하세요.
    #         Return the final result.
    pass


def merge_unique(list_a: list, list_b: list) -> list:
    """
    🥈 Medium Bonus
    두 정렬된 리스트를 합치되, 중복 값은 한 번만 포함합니다.
    Merges two sorted lists, including each value only once.

    sort() / sorted() 사용 금지!
    No sort() / sorted()!
    """
    # TODO 1: merge_lists()와 같은 방식으로 result, i, j를 준비하세요.
    #         Set up result, i, j the same way as in merge_lists().

    # TODO 2: 두 포인터 while 반복문을 작성하세요.
    #         Write the two-pointer while loop.

        # TODO 3: 더 작은 쪽을 고르되, result에 이미 같은 값이 있으면 건너뛰세요.
        #         Pick the smaller value, but skip it if result already ends with that value.
        #         힌트 / Hint: 결과 리스트가 비어 있지 않고 마지막 값과 같으면 건너뛰기
        #                      if len(result) == 0 or result[-1] != value_to_add:
        #                          result.append(value_to_add)

    # TODO 4: 남은 항목들도 같은 방식으로 중복 확인 후 붙이세요.
    #         Handle remaining items the same way — check for duplicates before appending.
    #         힌트 / Hint: 슬라이싱으로 남은 부분을 for 반복문으로 하나씩 확인하세요.
    #                      Use a for loop over the remaining slice to check each one.
    pass


def merge_all(lists: list) -> list:
    """
    🥇 Hard Bonus
    정렬된 리스트들의 리스트를 받아 하나로 합칩니다.
    Takes a list of sorted lists and merges them all into one.

    merge_lists()를 재사용하세요!
    Reuse merge_lists()!
    """
    # TODO 1: lists가 비어 있으면 빈 리스트를 반환하세요.
    #         If lists is empty, return an empty list.

    # TODO 2: 결과를 누적할 변수를 만드세요. 첫 번째 리스트로 시작하세요.
    #         Create a variable to accumulate the result. Start with the first list.
    #         힌트 / Hint: result = lists[0]

    # TODO 3: 나머지 리스트들을 반복문으로 하나씩 merge_lists()로 합치세요.
    #         Loop through the remaining lists and merge each one using merge_lists().
    #         힌트 / Hint: for i in range(1, len(lists)):
    #                          result = merge_lists(result, lists[i])

    # TODO 4: 최종 결과를 반환하세요.
    #         Return the final result.
    pass


# ============================================================
# 🎪 테스트 코드 / Test Code
# 아래 코드를 실행해서 함수가 잘 작동하는지 확인하세요!
# Run the code below to check if your functions work!
# ============================================================

if __name__ == "__main__":
    print("=" * 45)
    print("테스트 1: 기본 케이스 / Test 1: Basic case")
    print("=" * 45)
    print(merge_lists([1, 3, 5, 7], [2, 4, 6, 8]))
    # 예상 / Expected: [1, 2, 3, 4, 5, 6, 7, 8]

    print()
    print("=" * 45)
    print("테스트 2: 한쪽이 먼저 끝남 / Test 2: One side finishes first")
    print("=" * 45)
    print(merge_lists([1, 2, 3], [10, 20, 30]))
    # 예상 / Expected: [1, 2, 3, 10, 20, 30]

    print()
    print("=" * 45)
    print("테스트 3: 길이 다름 / Test 3: Different lengths")
    print("=" * 45)
    print(merge_lists([1, 2, 9], [3, 5, 7]))
    # 예상 / Expected: [1, 2, 3, 5, 7, 9]

    print()
    print("=" * 45)
    print("테스트 4: 빈 리스트 / Test 4: Empty list")
    print("=" * 45)
    print(merge_lists([], [1, 2, 3]))
    # 예상 / Expected: [1, 2, 3]

    print()
    print("=" * 45)
    print("테스트 5: 중복 값 / Test 5: Duplicate values")
    print("=" * 45)
    print(merge_lists([1, 3, 3, 5], [2, 3, 4]))
    # 예상 / Expected: [1, 2, 3, 3, 3, 4, 5]

    print()
    print("=" * 45)
    print("테스트 6: 원본 변경 없음 / Test 6: Originals unchanged")
    print("=" * 45)
    a = [1, 3, 5]
    b = [2, 4, 6]
    merge_lists(a, b)
    print(a)   # 예상 / Expected: [1, 3, 5]
    print(b)   # 예상 / Expected: [2, 4, 6]

    print()
    print("=" * 45)
    print("🥉 보너스 Easy / Bonus Easy")
    print("=" * 45)
    print(merge_three([1, 4, 7], [2, 5, 8], [3, 6, 9]))
    # 예상 / Expected: [1, 2, 3, 4, 5, 6, 7, 8, 9]

    print()
    print("=" * 45)
    print("🥈 보너스 Medium / Bonus Medium")
    print("=" * 45)
    print(merge_unique([1, 2, 3, 5], [2, 3, 4, 5, 6]))
    # 예상 / Expected: [1, 2, 3, 4, 5, 6]

    print()
    print("=" * 45)
    print("🥇 보너스 Hard / Bonus Hard")
    print("=" * 45)
    print(merge_all([[1, 5, 9], [2, 6], [3, 7, 10], [4, 8]]))
    # 예상 / Expected: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(merge_all([]))
    # 예상 / Expected: []
