# 🐍 비교 연산자 연습 | Comparison Operators Practice
# -------------------------------------------------------
# 미션: n이 1 이상 100 이하인지 출력하세요
# Mission: Print whether n is between 1 and 100 (inclusive)
# -------------------------------------------------------

# ✅ 입력 처리 (건드리지 마세요! / Don't touch this part!)
# input()은 항상 문자열(str)을 반환하기 때문에 int()로 변환해줍니다
# input() always returns a string, so we convert it to int with int()
n = int(input())

# -------------------------------------------------------

def is_valid_level(n: int) -> None:
    """
    n이 1 이상 100 이하인지 출력합니다.
    Prints whether n is between 1 and 100 inclusive.

    매개변수 | Parameters:
        n (int): 확인할 정수 | the integer to check

    출력 | Output:
        True  → n이 1 이상 100 이하인 경우 | when 1 <= n <= 100
        False → 그 외의 경우              | otherwise
    """

    # TODO 1: n이 1 이상인지 확인하는 식을 작성하세요
    #         Write the expression to check if n is at least 1
    #         힌트(Hint): n __ 1

    # TODO 2: n이 100 이하인지 확인하는 식을 작성하세요
    #         Write the expression to check if n is at most 100
    #         힌트(Hint): n __ 100

    # TODO 3: 두 조건을 연결하여 print() 한 줄로 출력하세요
    #         Connect both conditions and print the result in one print() line
    #         힌트(Hint): print( 식1 ___ 식2 )

    # 🌟 보너스 | Bonus:
    # 기본 풀이가 완성되면, Python의 chaining 문법으로도 작성해보세요!
    # Once your basic solution works, try rewriting it using Python's chaining syntax!
    # 힌트(Hint): print( 1 __ n __ 100 )

    pass  # 이 줄은 삭제하고 코드를 작성하세요 | Delete this line and write your code


# -------------------------------------------------------
# ✅ 함수 호출 (건드리지 마세요! / Don't touch this part!)
is_valid_level(n)
