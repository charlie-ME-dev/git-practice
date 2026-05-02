"""
Python 연습: 괄호 매칭 검사기 / Python Practice: Bracket Matcher
=================================================================

문제: 문자열 s가 올바르게 짝지어진 괄호로 이루어져 있는지 검사하세요.
Problem: Check if a string s contains properly matched brackets.

규칙 / Rules:
- 입력은 '(', ')', '[', ']', '{', '}' 만 포함합니다
- Input contains only '(', ')', '[', ']', '{', '}'
- 빈 문자열은 True 입니다 / Empty string returns True
"""


def is_valid_brackets(s: str) -> bool:
    """
    괄호 문자열이 유효한지 판별합니다.
    Determines if a bracket string is valid.

    매개변수 / Parameters:
        s (str): 괄호 문자만 포함된 문자열
                 A string containing only bracket characters

    반환값 / Returns:
        bool: 유효하면 True, 아니면 False
              True if valid, False otherwise
    """
    # TODO 1: 빈 리스트(스택)를 만드세요. 여는 괄호를 여기에 쌓아둘 거예요.
    # TODO 1: Create an empty list (stack). You'll push opening brackets here.
    stack = []

    # TODO 2: 문자열 s의 각 문자(char)를 순회하는 for문을 작성하세요.
    # TODO 2: Write a for-loop that iterates over each character (char) in s.
    for char in s:

        # TODO 3: 만약 char가 여는 괄호('(', '[', '{') 중 하나라면,
        #         스택에 append 하세요.
        # TODO 3: If char is one of the opening brackets ('(', '[', '{'),
        #         append it to the stack.
        if char in '([{':
            stack.append(char)

        # TODO 4: 그렇지 않으면 (닫는 괄호인 경우), 다음을 처리하세요:
        # TODO 4: Otherwise (it's a closing bracket), handle these cases:
        else:
            # TODO 4-1: 스택이 비어있다면, 짝이 없으므로 False를 반환하세요.
            # TODO 4-1: If the stack is empty, there's no match — return False.
            if not stack:
                return False


            # TODO 4-2: 스택에서 마지막 요소를 pop 하세요. (변수명: top 추천)
            # TODO 4-2: Pop the last element from the stack. (suggested name: top)
            top = stack.pop()


            # TODO 4-3: char가 ')'인데 top이 '('가 아니면, False를 반환하세요.
            #           char가 ']'인데 top이 '['가 아니면, False를 반환하세요.
            #           char가 '}'인데 top이 '{'가 아니면, False를 반환하세요.
            # TODO 4-3: If char is ')' but top is not '(', return False.
            #           If char is ']' but top is not '[', return False.
            #           If char is '}' but top is not '{', return False.
            if char == ')' and top != '(':
                return False
            if char == ']' and top != '[':
                return False
            if char == '}' and top != '{':
                return False



    # TODO 5: 반복이 끝났을 때, 스택이 비어있어야 모든 괄호가 닫힌 것입니다.
    #         스택의 길이가 0이면 True, 아니면 False를 반환하세요.
    # TODO 5: When the loop ends, the stack must be empty for all brackets
    #         to be closed. Return True if the stack length is 0, else False.
    return len(stack) == 0

# ============================================================
# ⚠️  아래 코드는 수정하지 마세요! / DO NOT MODIFY BELOW! ⚠️
# ============================================================
if __name__ == "__main__":
    test_cases = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
        ("", True),
        ("(", False),
        (")", False),
        ("(((", False),
        (")))", False),
        ("({[]})", True),
        ("({[}])", False),
        ("()()", True),
        ("(()", False),
    ]

    print("=" * 50)
    print("테스트 결과 / Test Results")
    print("=" * 50)

    passed = 0
    for s, expected in test_cases:
        try:
            result = is_valid_brackets(s)
            mark = "✅" if result == expected else "❌"
            if result == expected:
                passed += 1
            print(f"{mark} is_valid_brackets({s!r:12}) → {result} (expected {expected})")
        except Exception as e:
            print(f"❌ is_valid_brackets({s!r:12}) → ERROR: {e}")

    print("=" * 50)
    print(f"통과 / Passed: {passed} / {len(test_cases)}")
    print("=" * 50)
