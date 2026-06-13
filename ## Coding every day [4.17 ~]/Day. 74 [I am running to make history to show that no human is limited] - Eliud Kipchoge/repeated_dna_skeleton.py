# 🧬 반복되는 DNA 서열 찾기 — 스켈레톤 / Skeleton
# =====================================================
# 빈칸 ___ 을 채워 함수를 완성하세요.
# Fill in the numbered blanks ___ to complete the function.
# =====================================================


def find_repeated_dna(s: str) -> list[str]:
    # 길이가 10보다 작으면 만들 수 있는 서열이 없습니다.
    # If shorter than 10, there are no length-10 sequences.
    if len(s) < ___:          # (1) 비교할 기준 길이 / the threshold length
        return ___            # (2) 무엇을 반환할까요? / what do we return?

    # 각 서열의 등장 횟수를 기록할 딕셔너리
    # A dictionary to record how many times each sequence appears
    counts = {}
    result = []

    # 슬라이딩 윈도우: 시작 인덱스 i 를 0부터 끝까지 옮깁니다.
    # Sliding window: move start index i from 0 to the end.
    for i in range(len(s) - ___):   # (3) 마지막 시작 위치를 만들려면? / to reach the last start
        window = s[i:i + ___]       # (4) 윈도우 길이 / window length

        # 이미 본 서열인지 확인하고 횟수를 갱신
        # Check if seen before, then update the count
        if window ___ counts:       # (5) 키 존재 여부 확인 연산자 / membership operator
            counts[window] = counts[window] + 1
        else:
            counts[window] = ___    # (6) 처음 봤을 때의 초기값 / initial count

    # 두 번 이상 등장한 서열만 결과에 담기
    # Collect only the sequences that appeared more than once
    for seq in counts:
        if counts[seq] ___ 1:       # (7) "두 번 이상"을 뜻하는 비교 / "more than once"
            result.append(seq)

    return result


# =====================================================
# 🔒 테스트 블록 (수정하지 마세요) / TEST BLOCK (do not modify)
# =====================================================
passed = 0
total = 0

# 테스트 1
total = total + 1
out1 = sorted(find_repeated_dna("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
if out1 == ["AAAAACCCCC", "CCCCCAAAAA"]:
    passed = passed + 1
    print("테스트 1 통과 / Test 1 PASS")
else:
    print("테스트 1 실패 / Test 1 FAIL -> 받은 값 / got:", out1)

# 테스트 2
total = total + 1
out2 = find_repeated_dna("AAAAAAAAAAAAA")
if out2 == ["AAAAAAAAAA"]:
    passed = passed + 1
    print("테스트 2 통과 / Test 2 PASS")
else:
    print("테스트 2 실패 / Test 2 FAIL -> 받은 값 / got:", out2)

# 테스트 3
total = total + 1
out3 = find_repeated_dna("ACGT")
if out3 == []:
    passed = passed + 1
    print("테스트 3 통과 / Test 3 PASS")
else:
    print("테스트 3 실패 / Test 3 FAIL -> 받은 값 / got:", out3)

# 테스트 4 (정확히 길이 10, 반복 없음 / exactly length 10, no repeat)
total = total + 1
out4 = find_repeated_dna("ACGTACGTAC")
if out4 == []:
    passed = passed + 1
    print("테스트 4 통과 / Test 4 PASS")
else:
    print("테스트 4 실패 / Test 4 FAIL -> 받은 값 / got:", out4)

print("=====================================")
print(f"결과 / Score: {passed}/{total}")
