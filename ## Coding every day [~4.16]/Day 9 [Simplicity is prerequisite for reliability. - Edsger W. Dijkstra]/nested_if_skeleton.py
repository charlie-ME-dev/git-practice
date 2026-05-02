# 🐍 중첩 if 연습 | Nested if Practice
# -------------------------------------------------------
# 미션: HP와 레벨에 따라 캐릭터 스탯을 출력하세요
# Mission: Print character stats based on HP and level
#
# HP ≥ 50 + 레벨 ≥ 50  →  ATK: 200 / DEF: 100
# HP ≥ 50 + 레벨 < 50  →  ATK: 100 / DEF: 50
# HP < 50 + 레벨 ≥ 50  →  ATK: 100 / DEF: 50
# HP < 50 + 레벨 < 50  →  ATK: 50  / DEF: 25
# -------------------------------------------------------

# ✅ 입력 처리 (건드리지 마세요! / Don't touch this part!)
# input()은 항상 문자열(str)을 반환하기 때문에 int()로 변환해줍니다
# input() always returns a string, so we convert it to int with int()
hp = int(input())
level = int(input())

# -------------------------------------------------------

def calculate_stats(hp: int, level: int) -> None:
    """
    HP와 레벨에 따른 캐릭터 스탯을 출력합니다.
    Prints character stats based on HP and level.

    매개변수 | Parameters:
        hp    (int): 캐릭터의 현재 체력 | character's current HP
        level (int): 캐릭터의 현재 레벨 | character's current level

    출력 | Output:
        ATK: {공격력}
        DEF: {방어력}
    """

    # TODO 1: 바깥 조건 — HP가 50 이상인지 확인하세요
    #         Outer condition — check if HP is 50 or above
    #         힌트(Hint): if hp ___ 50:

        # TODO 2: 안쪽 조건 (건강할 때) — 레벨이 50 이상인지 확인하세요
        #         Inner condition (when healthy) — check if level is 50 or above
        #         힌트(Hint): if level ___ 50:
        #         ⚠️  들여쓰기 주의! 이 if는 TODO 1의 if 안에 있어야 합니다
        #         ⚠️  Watch indentation! This if must be inside TODO 1's if block

            # TODO 3: 건강 + 고레벨 스탯을 출력하세요
            #         Print stats for healthy + high level
            #         ATK: 200, DEF: 100

        # TODO 4: 건강하지만 저레벨일 때 스탯을 출력하세요
        #         Print stats for healthy + low level
        #         ATK: 100, DEF: 50

    # TODO 5: 바깥 else — HP가 50 미만일 때
    #         Outer else — when HP is below 50
    #         힌트(Hint): else:

        # TODO 6: 안쪽 조건 (부상일 때) — 레벨이 50 이상인지 확인하세요
        #         Inner condition (when injured) — check if level is 50 or above
        #         ⚠️  들여쓰기 주의! 이 if는 else 블록 안에 있어야 합니다
        #         ⚠️  Watch indentation! This if must be inside the else block

            # TODO 7: 부상 + 고레벨 스탯을 출력하세요
            #         Print stats for injured + high level
            #         ATK: 100, DEF: 50

        # TODO 8: 부상 + 저레벨일 때 스탯을 출력하세요
        #         Print stats for injured + low level
        #         ATK: 50, DEF: 25

    pass  # 이 줄은 삭제하고 코드를 작성하세요 | Delete this line and write your code


# -------------------------------------------------------
# ✅ 함수 호출 (건드리지 마세요! / Don't touch this part!)
calculate_stats(hp, level)
