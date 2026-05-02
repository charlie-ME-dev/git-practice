# 🐍 비교 연산자 연습 | Comparison Operators Practice
# -------------------------------------------------------
# 미션: a가 b보다 큰지 출력하세요
# Mission: Print whether a is greater than b
# -------------------------------------------------------

# ✅ 입력 처리 (건드리지 마세요! / Don't touch this part!)
# input()은 항상 문자열(str)을 반환하기 때문에 int()로 변환해줍니다
# input() always returns a string, so we convert it to int with int()
a = int(input())
b = int(input())

# -------------------------------------------------------

def is_a_greater(a: int, b: int) -> None:
    """
    두 정수를 비교하여 a가 b보다 큰지 출력합니다.
    Prints whether a is greater than b.

    매개변수 | Parameters:
        a (int): 첫 번째 정수 | first integer
        b (int): 두 번째 정수 | second integer

    출력 | Output:
        True  → a가 b보다 큰 경우 | when a is greater than b
        False → 그 외의 경우      | otherwise
    """

    # TODO: print() 함수 안에 비교 연산자 >를 사용하여 결과를 출력하세요
    #       Use the comparison operator > inside print() to output the result
    #       힌트(Hint): print(a __ b)

    pass  # 이 줄은 삭제하고 코드를 작성하세요 | Delete this line and write your code


# -------------------------------------------------------
# ✅ 함수 호출 (건드리지 마세요! / Don't touch this part!)
is_a_greater(a, b)
