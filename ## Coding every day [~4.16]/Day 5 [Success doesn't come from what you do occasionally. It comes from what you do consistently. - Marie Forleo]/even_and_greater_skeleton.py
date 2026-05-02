# 🐍 비교 연산자 연습 | Comparison Operators Practice
# -------------------------------------------------------
# 미션: n이 짝수이면서 10보다 크면 True를 출력하세요
# Mission: Print True if n is even AND greater than 10
# -------------------------------------------------------

# ✅ 입력 처리 (건드리지 마세요! / Don't touch this part!)
# input()은 항상 문자열(str)을 반환하기 때문에 int()로 변환해줍니다
# input() always returns a string, so we convert it to int with int()
n = int(input())

# -------------------------------------------------------

def check_vip_condition(n: int) -> None:
    """
    n이 짝수이면서 10보다 큰지 출력합니다.
    Prints whether n is even and greater than 10.

    매개변수 | Parameters:
        n (int): 확인할 정수 | the integer to check

    출력 | Output:
        True  → n이 짝수이면서 10보다 큰 경우 | when n is even AND greater than 10
        False → 그 외의 경우                  | otherwise

    주의 | Note:
        짝수 판별은 반드시 n // 2 * 2 == n 을 사용하세요!
        You must use n // 2 * 2 == n to check for even numbers!
    """

    # TODO 1: n이 짝수인지 확인하는 식을 작성하세요 (주어진 식을 사용하세요!)
    #         Write the expression to check if n is even (use the given formula!)
    #         힌트(Hint): n // 2 * 2 __ n

    # TODO 2: n이 10보다 큰지 확인하는 식을 작성하세요
    #         Write the expression to check if n is greater than 10
    #         힌트(Hint): n __ 10

    # TODO 3: 두 조건을 연결하여 print() 한 줄로 출력하세요
    #         Connect both conditions and print the result in one print() line
    #         힌트(Hint): print( ___ 식1 ___ 식2 ___ )

    pass  # 이 줄은 삭제하고 코드를 작성하세요 | Delete this line and write your code


# -------------------------------------------------------
# ✅ 함수 호출 (건드리지 마세요! / Don't touch this part!)
check_vip_condition(n)
