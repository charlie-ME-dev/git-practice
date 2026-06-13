# =============================================================
#  Python 연습: enumerate() — 출석부에 번호 매기기
#  Python Practice: enumerate() — Numbering an Attendance Roster
# =============================================================
#  규칙 / Rules:
#   - 모든 이름은 snake_case / Use snake_case for everything
#   - 직접 세는 변수 만들지 말기 / Don't make your own counter
#   - enumerate() 사용 / Use enumerate(), not range(len(...))
# =============================================================


# -------------------------------------------------------------
# 과제 1 / Task 1: make_numbered_roster(names)
#   1번부터 번호가 붙은 출석부 문자열 리스트 반환
#   Return roster strings numbered from 1
#   예 / e.g. ["김민준", "이서연"] -> ["1. 김민준", "2. 이서연"]
# -------------------------------------------------------------
def make_numbered_roster(names):
    result = []
    # TODO 1-1: enumerate()로 번호와 이름을 함께 받으세요. 번호는 1부터!
    #           Loop with enumerate() to get number + name. Start at 1!
    for ___, ___ in enumerate(names, start=___):
        # TODO 1-2: "번호. 이름" 형태의 문자열을 만들어 result에 추가
        #           Append a "number. name" string to result
        result.append(___)
    return result


# -------------------------------------------------------------
# 과제 2 / Task 2: find_position(names, target)
#   target이 몇 번째(1부터)인지 반환. 없으면 0.
#   Return target's 1-based position. Return 0 if not found.
# -------------------------------------------------------------
def find_position(names, target):
    # TODO 2-1: enumerate()로 번호와 이름을 함께 받으세요 (1부터)
    #           Loop with enumerate() to get position + name (from 1)
    for ___, ___ in enumerate(names, start=___):
        # TODO 2-2: 이름이 target과 같으면 그 번호를 반환
        #           If the name equals target, return that position
        if ___ == ___:
            return ___
    # TODO 2-3: 끝까지 못 찾았다면 무엇을 반환할까요?
    #           What do you return if it was never found?
    return ___


# -------------------------------------------------------------
# 과제 3 / Task 3: make_attendance_report(names, present_flags)
#   "이름: 출석" 또는 "이름: 결석" 문자열 리스트 반환
#   Return strings like "name: 출석" / "name: 결석"
#   present_flags[i]가 True면 출석, False면 결석
#   present_flags[i] True -> 출석(present), False -> 결석(absent)
# -------------------------------------------------------------
def make_attendance_report(names, present_flags):
    report = []
    # TODO 3-1: 번호 i와 이름 name을 함께 받으세요 (여기선 0부터가 편해요)
    #           Get the index i AND the name (0-based is handy here)
    for ___, ___ in enumerate(names):
        # TODO 3-2: 같은 자리의 출석 여부 present_flags[i]를 확인
        #           Check the matching flag present_flags[i]
        if ___:
            report.append(f"{name}: 출석")
        else:
            report.append(f"{name}: 결석")
    return report


# =============================================================
# 🌟 보너스 / BONUS (선택 / optional)
# =============================================================

# 🥉 Easy: make_seating_chart(names, seat_start)
#   번호를 seat_start부터 시작 / numbering starts at seat_start
def make_seating_chart(names, seat_start):
    result = []
    for ___, ___ in enumerate(names, start=___):
        result.append(___)
    return result


# 🥈 Medium: find_all_positions(names, letter)
#   letter로 시작하는 모든 학생의 번호(1부터)를 리스트로
#   1-based positions of every name starting with letter
def find_all_positions(names, letter):
    positions = []
    for ___, ___ in enumerate(names, start=___):
        if ___.startswith(___):
            positions.append(___)
    return positions


# 🥇 Hard: label_positions(names)
#   "맨 앞" / "중간" / "맨 뒤", 한 명이면 "혼자", 빈 리스트도 처리
#   "맨 앞"/"중간"/"맨 뒤"; "혼자" if only one; handle empty list
def label_positions(names):
    result = []
    n = len(names)
    for ___, ___ in enumerate(names):
        # TODO: 한 명인 경우를 먼저! 그다음 맨 앞(i==0), 맨 뒤(i==n-1), 나머지
        #       Handle one-student case first, then first / last / middle
        if ___:
            label = "혼자"
        elif ___:
            label = "맨 앞"
        elif ___:
            label = "맨 뒤"
        else:
            label = "중간"
        result.append(f"{name}: {label}")
    return result


# =============================================================
# 🎪 테스트 / TESTS  (이 아래는 수정하지 마세요 / Do not edit below)
# =============================================================
if __name__ == "__main__":
    passed = 0
    total = 0

    # --- 과제 1 / Task 1 ---
    total = total + 1
    if make_numbered_roster(["김민준", "이서연", "박도윤"]) == ["1. 김민준", "2. 이서연", "3. 박도윤"]:
        passed = passed + 1
        print("과제 1 기본 통과 / Task 1 basic OK")
    else:
        print("과제 1 기본 실패 / Task 1 basic FAILED")

    total = total + 1
    if make_numbered_roster([]) == []:
        passed = passed + 1
        print("과제 1 빈 리스트 통과 / Task 1 empty OK")
    else:
        print("과제 1 빈 리스트 실패 / Task 1 empty FAILED")

    # --- 과제 2 / Task 2 ---
    total = total + 1
    if find_position(["김민준", "이서연", "박도윤"], "박도윤") == 3:
        passed = passed + 1
        print("과제 2 찾기 통과 / Task 2 found OK")
    else:
        print("과제 2 찾기 실패 / Task 2 found FAILED")

    total = total + 1
    if find_position(["김민준", "이서연", "박도윤"], "홍길동") == 0:
        passed = passed + 1
        print("과제 2 없음 통과 / Task 2 not-found OK")
    else:
        print("과제 2 없음 실패 / Task 2 not-found FAILED")

    # --- 과제 3 / Task 3 ---
    total = total + 1
    if make_attendance_report(["김민준", "이서연"], [True, False]) == ["김민준: 출석", "이서연: 결석"]:
        passed = passed + 1
        print("과제 3 통과 / Task 3 OK")
    else:
        print("과제 3 실패 / Task 3 FAILED")

    print("=================================")
    print(f"통과 / passed: {passed} / {total}")
