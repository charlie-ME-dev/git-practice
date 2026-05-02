"""
🔍 Find Substring Index — 부분 문자열 인덱스 찾기
==================================================

시나리오 / Scenario:
  사이버보안 로그 분석 도구의 일부로, 로그 메시지 안에서
  오류 코드가 처음 나타나는 위치를 찾는 함수를 구현합니다.

  Implement a function that finds the first occurrence of a
  substring inside a string — part of a cybersecurity log tool.

규칙 / Rules:
  ⚠️ .find(), .index(), `in` 연산자 사용 금지!
  ⚠️ Do NOT use .find(), .index(), or the `in` operator!
  슬라이싱과 반복문으로 직접 구현하세요.
  Implement it yourself using slicing and loops.
"""


def find_substring_index(haystack: str, needle: str) -> int:
    """
    haystack 안에서 needle이 처음 나타나는 인덱스를 반환합니다.
    needle이 없으면 -1을 반환합니다.

    Return the index of the first occurrence of needle in haystack.
    Return -1 if needle is not found.
    """

    # TODO 1 (KO): needle이 빈 문자열("")이면 0을 반환하세요.
    # TODO 1 (EN): If needle is an empty string (""), return 0.
    if needle == "":
        return 0

    # TODO 2 (KO): haystack과 needle의 길이를 변수에 저장하세요.
    # TODO 2 (EN): Store the lengths of haystack and needle in variables.
    haystack_length = len(haystack)  # ← 바꾸세요 / change this
    needle_length = len(needle)    # ← 바꾸세요 / change this


    # TODO 3 (KO): needle이 haystack보다 길면 찾을 수 없으니 -1을 반환하세요.
    # TODO 3 (EN): If needle is longer than haystack, return -1.
    if needle_length > haystack_length:
        return -1



    # TODO 4 (KO): haystack의 시작 위치 i를 0부터 (haystack_length - needle_length)까지 반복하세요.
    #              각 위치에서 haystack[i : i + needle_length]가 needle과 같은지 확인하고,
    #              같으면 i를 반환하세요.
    # TODO 4 (EN): Loop i from 0 to (haystack_length - needle_length) inclusive.
    #              At each position, check if haystack[i : i + needle_length] equals needle.
    #              If so, return i.
    #
    # 힌트 / Hint: range(haystack_length - needle_length + 1)
    for i in range(haystack_length - needle_length + 1):
        if haystack[i : i + needle_length] == needle:
            return i




    # TODO 5 (KO): 반복이 끝나도 못 찾았으면 -1을 반환하세요.
    # TODO 5 (EN): If the loop finishes without finding needle, return -1.


    return -1  # ← 필요하면 바꾸세요 / change if needed


# ==========================================================================
# 🚫 아래 코드는 수정하지 마세요! (채점용 테스트 코드)
# 🚫 DO NOT MODIFY below this line (test harness for grading)
# ==========================================================================
if __name__ == "__main__":
    print("=" * 50)
    print("🧪 Testing find_substring_index")
    print("=" * 50)

    # 테스트 케이스 / Test cases: (haystack, needle, expected)
    test_cases = [
        ("sadbutsad", "sad", 0),
        ("leetcode", "leeto", -1),
        ("ERROR_404 not found in server", "404", 6),
        ("hello", "", 0),
        ("abc", "abcd", -1),
        ("mississippi", "issip", 4),
        ("banana", "nan", 2),
        ("python is fun", "fun", 10),
    ]

    passed = 0
    for haystack, needle, expected in test_cases:
        result = find_substring_index(haystack, needle)
        status = "✅" if result == expected else "❌"
        if result == expected:
            passed += 1
        print(f"{status} find_substring_index({haystack!r}, {needle!r})")
        print(f"   → got {result}, expected {expected}")

    print("=" * 50)
    print(f"결과 / Result: {passed}/{len(test_cases)} tests passed")
    print("=" * 50)
