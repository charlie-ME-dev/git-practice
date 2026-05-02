"""
🏛️ 로마 숫자를 정수로 변환하기 / Roman to Integer
==================================================

박물관 큐레이터를 위한 로마 숫자 → 정수 변환기를 만들어봅시다!
Let's build a Roman numeral to integer converter for a museum curator!

기호 값 / Symbol values:
  I=1, V=5, X=10, L=50, C=100, D=500, M=1000

뺄셈 쌍 / Subtraction pairs:
  IV=4, IX=9, XL=40, XC=90, CD=400, CM=900
"""


def roman_to_int(s: str) -> int:
    # TODO 1: 합계를 저장할 변수를 0으로 초기화하세요.
    # TODO 1: Initialize a variable to hold the running total, starting at 0.
    total = 0

    # TODO 2: 문자열의 각 위치(인덱스)를 순회하는 반복문을 작성하세요.
    #          힌트: range(len(s)) 를 사용해보세요.
    # TODO 2: Loop over each position (index) in the string.
    #          Hint: try range(len(s)).
    for i in range(len(s)):

        # TODO 3: 현재 문자 s[i]의 값(정수)을 구하세요.
        #          if / elif 체인을 사용해서 7가지 기호를 각각 처리하세요.
        # TODO 3: Get the integer value of the current character s[i].
        #          Use an if / elif chain to handle each of the 7 symbols.
        current_value = 0
        # if s[i] == "I":
        #     current_value = 1
        # elif ...

        # TODO 4: 다음 문자가 존재하고(마지막 문자가 아니고)
        #          다음 문자의 값이 현재 값보다 크면 → 현재 값을 빼기.
        #          그렇지 않으면 → 현재 값을 더하기.
        #          힌트: i < len(s) - 1 로 "다음 문자가 있는지" 확인할 수 있어요.
        # TODO 4: If there IS a next character (not the last one)
        #          AND the next character's value is bigger than current → subtract.
        #          Otherwise → add.
        #          Hint: check "is there a next char?" with  i < len(s) - 1.

        pass  # 이 줄을 지우고 위 로직을 완성하세요 / Remove this line once done

    # TODO 5: 최종 합계를 반환하세요.
    # TODO 5: Return the final total.
    return total


# ============================================================
# 🚫 아래 코드는 수정하지 마세요! / Do NOT modify below this line
# ============================================================
if __name__ == "__main__":
    test_cases = [
        ("III", 3),
        ("IV", 4),
        ("IX", 9),
        ("LVIII", 58),
        ("MCMXCIV", 1994),
        ("I", 1),
        ("MMMCMXCIX", 3999),
    ]

    print("🧪 테스트 시작 / Running tests...\n")
    passed = 0
    for roman, expected in test_cases:
        result = roman_to_int(roman)
        status = "✅" if result == expected else "❌"
        print(f"{status} roman_to_int({roman!r}) = {result}  (예상 / expected: {expected})")
        if result == expected:
            passed += 1

    print(f"\n결과 / Result: {passed} / {len(test_cases)} 통과 / passed")
