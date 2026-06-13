# =============================================================
# 짝꿍 찾기 — 딕셔너리 연습 / Find the Pair — Dictionary Practice
# =============================================================
# 이름 / Name: ____________________
# 학번 / Student ID: ____________________
# =============================================================


def find_pair(free_hours: list[int], target_hours: int) -> list[int]:
    # 1. 지금까지 본 멤버를 저장할 빈 딕셔너리를 만드세요. {시간: 인덱스} 형태입니다.
    #    Create an empty dictionary to store members seen so far, as {hours: index}.
    seen = ___

    # 2. 인덱스를 사용해 리스트를 한 번 훑으세요.
    #    Loop through the list once, using the index.
    for index in range(___):

        # 3. 현재 멤버의 자유 시간을 변수에 저장하세요.
        #    Store the current member's free hours in a variable.
        hours = free_hours[___]

        # 4. 우리가 찾는 짝(보수)을 계산하세요: 목표 시간 - 현재 시간
        #    Compute the complement we are looking for: target hours - current hours.
        complement = ___ - ___

        # 5. 그 보수가 이미 딕셔너리(seen)에 있는지 확인하세요.
        #    Check whether that complement is already in the dictionary (seen).
        if ___ in ___:
            # 6. 있다면! 보수의 인덱스와 현재 인덱스를 리스트로 반환하세요.
            #    If it is! Return the complement's index and the current index as a list.
            return [seen[___], ___]

        # 7. 없다면, 현재 멤버의 시간과 인덱스를 딕셔너리에 저장하세요.
        #    If not, store the current member's hours and index in the dictionary.
        seen[___] = ___


# =============================================================
# 테스트 블록 — 이 부분은 수정하지 마세요!
# TEST BLOCK — Do NOT modify this part!
# =============================================================
passed = 0
total = 0

# 테스트 1 / Test 1
total = total + 1
answer1 = find_pair([2, 7, 11, 15], 9)
if answer1 == [0, 1] or answer1 == [1, 0]:
    passed = passed + 1
    print("테스트 1 통과 / Test 1 PASSED")
else:
    print("테스트 1 실패 / Test 1 FAILED ->", answer1)

# 테스트 2 / Test 2
total = total + 1
answer2 = find_pair([3, 2, 4], 6)
if answer2 == [1, 2] or answer2 == [2, 1]:
    passed = passed + 1
    print("테스트 2 통과 / Test 2 PASSED")
else:
    print("테스트 2 실패 / Test 2 FAILED ->", answer2)

# 테스트 3 / Test 3
total = total + 1
answer3 = find_pair([3, 3], 6)
if answer3 == [0, 1] or answer3 == [1, 0]:
    passed = passed + 1
    print("테스트 3 통과 / Test 3 PASSED")
else:
    print("테스트 3 실패 / Test 3 FAILED ->", answer3)

print("-----")
print("결과 / Result:", passed, "/", total)
