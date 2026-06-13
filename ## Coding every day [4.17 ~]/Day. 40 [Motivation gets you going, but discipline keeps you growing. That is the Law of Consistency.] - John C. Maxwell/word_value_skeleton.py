"""
단어의 숫자 값 계산하기 / Word Value Calculator
==============================================

A=1, B=2, ..., Z=26 매핑을 사용해서 단어의 총 값을 계산하는 연습.
Practice calculating word values using A=1, B=2, ..., Z=26 mapping.

학습 목표 / Learning Goals:
- Dictionary 생성과 활용 / Build and use dictionaries
- 문자열 메서드 활용 / Use string methods
- 함수가 다른 함수를 호출하는 패턴 / Function composition pattern
"""

import string


# ============================================================
# 함수 1: 한 글자의 값 구하기 / Function 1: Get a single letter's value
# ============================================================

def get_letter_value(letter: str) -> int:
    """
    한 글자의 숫자 값을 반환합니다 (A=1, B=2, ..., Z=26).
    Returns the numeric value of a single letter (A=1, B=2, ..., Z=26).

    예 / Examples:
        get_letter_value('A') -> 1
        get_letter_value('z') -> 26
    """
    # TODO (KO): A=1, B=2, ..., Z=26 매핑을 dictionary로 만드세요.
    # TODO (EN): Build a dictionary mapping A=1, B=2, ..., Z=26.
    #   힌트 / Hint: string.ascii_uppercase + enumerate(..., 1)
    letter_value = {}

    # TODO (KO): 입력받은 letter를 대문자로 바꾸고, dictionary에서 값을 꺼내세요.
    # TODO (EN): Convert the input letter to uppercase, then look it up in the dictionary.
    result = 0

    return result


# ============================================================
# 함수 2: 단어의 총 값 계산하기 / Function 2: Calculate total word value
# ============================================================

def calculate_word_value(word: str) -> int:
    """
    단어를 구성하는 모든 글자의 값을 더한 합을 반환합니다.
    알파벳이 아닌 문자(공백, 숫자, 기호)는 무시합니다.
    Returns the sum of all letter values in the word.
    Non-alphabetic characters (spaces, digits, symbols) are ignored.

    예 / Examples:
        calculate_word_value('attitude') -> 100
        calculate_word_value('Hello World') -> 124  # 공백 무시 / space ignored
        calculate_word_value('') -> 0
    """
    # TODO (KO): 합계를 누적할 변수를 0으로 초기화하세요.
    # TODO (EN): Initialize an accumulator variable to 0.
    total = 0

    # TODO (KO): word의 각 글자를 순회하면서, 알파벳이면 값을 더하세요.
    # TODO (EN): Loop through each character in word; if it's a letter, add its value.
    #   힌트 / Hint: char.isalpha() 로 알파벳인지 확인 / use char.isalpha() to check
    #   힌트 / Hint: get_letter_value(char) 를 재사용하세요 / reuse get_letter_value(char)

    return total


# ============================================================
# 함수 3: 특정 값의 단어 찾기 / Function 3: Find words with a target value
# ============================================================

def find_words_with_value(words: list[str], target_value: int) -> list[str]:
    """
    리스트에서 값이 target_value와 같은 단어들만 골라서 반환합니다.
    Returns only the words from the list whose value equals target_value.

    예 / Examples:
        find_words_with_value(['attitude', 'knowledge', 'discipline'], 100)
            -> ['attitude', 'discipline']
        find_words_with_value(['hope'], 999) -> []
    """
    # TODO (KO): 결과를 담을 빈 리스트를 만드세요.
    # TODO (EN): Create an empty list to hold results.
    result = []

    # TODO (KO): words의 각 단어에 대해 calculate_word_value를 호출하고,
    #            target_value와 같으면 result에 append 하세요.
    # TODO (EN): For each word in words, call calculate_word_value;
    #            if it equals target_value, append it to result.

    return result


# ============================================================
# 테스트 / Tests
# ============================================================

if __name__ == "__main__":
    print("=" * 50)
    print("Test 1: get_letter_value")
    print("=" * 50)
    print(f"get_letter_value('A')  = {get_letter_value('A')}   (예상/expected: 1)")
    print(f"get_letter_value('z')  = {get_letter_value('z')}  (예상/expected: 26)")
    print(f"get_letter_value('M')  = {get_letter_value('M')}  (예상/expected: 13)")

    print("\n" + "=" * 50)
    print("Test 2: calculate_word_value")
    print("=" * 50)
    print(f"'knowledge'  = {calculate_word_value('knowledge')}   (예상/expected: 96)")
    print(f"'hardwork'   = {calculate_word_value('hardwork')}   (예상/expected: 98)")
    print(f"'attitude'   = {calculate_word_value('attitude')}  (예상/expected: 100)")
    print(f"'DISCIPLINE' = {calculate_word_value('DISCIPLINE')}  (예상/expected: 100)")

    print("\n" + "=" * 50)
    print("Test 3: 경계값 / Boundary values")
    print("=" * 50)
    print(f"''            = {calculate_word_value('')}    (예상/expected: 0)")
    print(f"'Hello World' = {calculate_word_value('Hello World')}  (예상/expected: 124)")

    print("\n" + "=" * 50)
    print("Test 4: find_words_with_value")
    print("=" * 50)
    words = ['attitude', 'knowledge', 'discipline', 'hardwork', 'hope']
    print(f"target=100 -> {find_words_with_value(words, 100)}")
    print(f"  예상/expected: ['attitude', 'discipline']")
    print(f"target=96  -> {find_words_with_value(words, 96)}")
    print(f"  예상/expected: ['knowledge']")
    print(f"target=999 -> {find_words_with_value(words, 999)}")
    print(f"  예상/expected: []")
