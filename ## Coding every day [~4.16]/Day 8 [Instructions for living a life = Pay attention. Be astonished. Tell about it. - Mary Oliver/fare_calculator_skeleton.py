# 🐍 조건문 연습 | Conditional Statement Practice
# -------------------------------------------------------
# 미션: 나이에 따라 지하철 요금을 출력하세요
# Mission: Print the subway fare based on passenger age
#
# 8세 미만         → 무료
# 8세 이상 19세 이하 → 1000원
# 20세 이상 64세 이하 → 2000원
# 65세 이상         → 1000원
# -------------------------------------------------------

# ✅ 입력 처리 (건드리지 마세요! / Don't touch this part!)
# input()은 항상 문자열(str)을 반환하기 때문에 int()로 변환해줍니다
# input() always returns a string, so we convert it to int with int()
age = int(input())

# -------------------------------------------------------

def calculate_fare(age: int) -> None:
    """
    나이에 따른 지하철 요금을 출력합니다.
    Prints the subway fare based on the passenger's age.

    매개변수 | Parameters:
        age (int): 승객의 나이 | passenger's age

    출력 | Output:
        무료   → 8세 미만        | under 8
        1000원 → 8세 이상 19세 이하 | 8 to 19 inclusive
        2000원 → 20세 이상 64세 이하 | 20 to 64 inclusive
        1000원 → 65세 이상       | 65 and above
    """

    # TODO 1: 첫 번째 조건 — 8세 미만이면 "무료"를 출력하세요
    #         First condition — if under 8, print "무료"
    #         힌트(Hint): if age ___ 8:

    # TODO 2: 두 번째 조건 — 19세 이하이면 "1000원"을 출력하세요
    #         Second condition — if 19 or under, print "1000원"
    #         힌트(Hint): elif age ___ 19:
    #         (앞에서 이미 8세 미만은 걸러졌으니, 여기선 하한을 다시 쓸 필요가 없어요!)
    #         (ages under 8 are already handled above, so no need to re-check the lower bound!)

    # TODO 3: 세 번째 조건 — 64세 이하이면 "2000원"을 출력하세요
    #         Third condition — if 64 or under, print "2000원"
    #         힌트(Hint): elif age ___ 64:

    # TODO 4: 나머지 경우 — "1000원"을 출력하세요 (65세 이상)
    #         Remaining case — print "1000원" (65 and above)
    #         힌트(Hint): else:

    pass  # 이 줄은 삭제하고 코드를 작성하세요 | Delete this line and write your code


# -------------------------------------------------------
# ✅ 함수 호출 (건드리지 마세요! / Don't touch this part!)
calculate_fare(age)
