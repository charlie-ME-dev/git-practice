# =============================================================
# 오늘의 카페 투표 집계 — 딕셔너리 개수 세기
# Café of the Day Vote Tally — Dictionary Frequency Counting
# =============================================================
# 이름 / Name: ____________________
# 학번 / Student ID: ____________________
# =============================================================


def find_winning_cafe(votes: list[str]) -> str:
    # 1. 각 카페의 표 수를 저장할 빈 딕셔너리를 만드세요. {카페이름: 표수} 형태입니다.
    #    Create an empty dictionary to store each cafe's vote count, as {cafe: count}.
    counts = ___

    # 2. 투표 리스트를 하나씩 훑으세요.
    #    Loop through the votes one by one.
    for cafe in ___:

        # 3. 이 카페가 이미 딕셔너리에 있나요?
        #    Is this cafe already in the dictionary?
        if cafe in ___:
            # 4. 있다면, 표 수에 1을 더하세요.
            #    If so, add 1 to its count.
            counts[cafe] = counts[cafe] + ___
        else:
            # 5. 없다면, 표 수를 1로 시작하세요.
            #    If not, start its count at 1.
            counts[cafe] = ___

    # 6. 과반 기준을 계산하세요: 전체 투표 수의 절반.
    #    Compute the majority threshold: half of the total votes.
    threshold = len(votes) / ___

    # 7. 딕셔너리를 훑으며, 표 수가 기준을 "초과"하는 카페를 찾으세요.
    #    Scan the dictionary for the cafe whose count is GREATER THAN the threshold.
    for cafe in counts:
        if counts[cafe] > ___:
            # 8. 찾았다면 그 카페 이름을 반환하세요.
            #    If found, return that cafe's name.
            return ___


# =============================================================
# 테스트 블록 — 이 부분은 수정하지 마세요!
# TEST BLOCK — Do NOT modify this part!
# =============================================================
passed = 0
total = 0

# 테스트 1 / Test 1
total = total + 1
answer1 = find_winning_cafe(["Blue Bottle", "Blue Bottle", "Green Bean"])
if answer1 == "Blue Bottle":
    passed = passed + 1
    print("테스트 1 통과 / Test 1 PASSED")
else:
    print("테스트 1 실패 / Test 1 FAILED ->", answer1)

# 테스트 2 / Test 2
total = total + 1
answer2 = find_winning_cafe(["A", "B", "A", "C", "A", "A"])
if answer2 == "A":
    passed = passed + 1
    print("테스트 2 통과 / Test 2 PASSED")
else:
    print("테스트 2 실패 / Test 2 FAILED ->", answer2)

# 테스트 3 / Test 3
total = total + 1
answer3 = find_winning_cafe(["W Collection"])
if answer3 == "W Collection":
    passed = passed + 1
    print("테스트 3 통과 / Test 3 PASSED")
else:
    print("테스트 3 실패 / Test 3 FAILED ->", answer3)

print("-----")
print("결과 / Result:", passed, "/", total)
