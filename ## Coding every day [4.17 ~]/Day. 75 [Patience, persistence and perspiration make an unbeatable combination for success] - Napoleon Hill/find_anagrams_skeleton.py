# 🧬 서열 속 애너그램 찾기 — 스켈레톤 / Skeleton
# =====================================================
# 빈칸 ___ 을 채워 함수를 완성하세요.
# Fill in the numbered blanks ___ to complete the function.
# (어제의 윈도우 순회 + 딕셔너리 빈도 세기를 그대로 활용!)
# (Reuse yesterday's window loop + dictionary frequency counting!)
# =====================================================


def find_anagrams(s: str, p: str) -> list[int]:
    n = len(p)
    result = []

    # s가 패턴보다 짧으면 애너그램이 있을 수 없습니다.
    # If s is shorter than the pattern, no anagram can exist.
    if len(s) < n:
        return ___                # (1) 무엇을 반환할까요? / what do we return?

    # 1) 패턴 p의 글자 빈도를 먼저 셉니다.
    #    First, count the letter frequencies of pattern p.
    p_count = {}
    for ch in p:
        if ch in p_count:
            p_count[ch] = p_count[ch] + 1
        else:
            p_count[ch] = ___     # (2) 처음 본 글자의 초기 횟수 / initial count

    # 2) 길이 n짜리 윈도우를 한 칸씩 옮기며 훑습니다.
    #    Slide a window of length n across s.
    for i in range(len(s) - n + ___):   # (3) 마지막 시작 위치까지 도달하려면? / reach the last start
        window = s[i:i + ___]           # (4) 윈도우 길이 / window length

        # 3) 이번 윈도우의 글자 빈도를 셉니다.
        #    Count the letter frequencies of this window.
        w_count = {}
        for ch in window:
            if ch in w_count:
                w_count[ch] = w_count[ch] + 1
            else:
                w_count[ch] = 1

        # 4) 두 빈도 딕셔너리가 같으면 애너그램입니다.
        #    If the two frequency dicts are equal, it's an anagram.
        if w_count ___ p_count:         # (5) 두 딕셔너리가 "같은지" 비교 / compare for equality
            result.append(___)          # (6) 무엇을 결과에 담을까요? / what do we record?

    return result


# =====================================================
# 🔒 테스트 블록 (수정하지 마세요) / TEST BLOCK (do not modify)
# =====================================================
passed = 0
total = 0

# 테스트 1
total = total + 1
out1 = find_anagrams("cbaebabacd", "abc")
if out1 == [0, 6]:
    passed = passed + 1
    print("테스트 1 통과 / Test 1 PASS")
else:
    print("테스트 1 실패 / Test 1 FAIL -> 받은 값 / got:", out1)

# 테스트 2
total = total + 1
out2 = find_anagrams("abab", "ab")
if out2 == [0, 1, 2]:
    passed = passed + 1
    print("테스트 2 통과 / Test 2 PASS")
else:
    print("테스트 2 실패 / Test 2 FAIL -> 받은 값 / got:", out2)

# 테스트 3 (애너그램 없음 / no anagram)
total = total + 1
out3 = find_anagrams("abc", "xyz")
if out3 == []:
    passed = passed + 1
    print("테스트 3 통과 / Test 3 PASS")
else:
    print("테스트 3 실패 / Test 3 FAIL -> 받은 값 / got:", out3)

# 테스트 4 (s가 p보다 짧음 / s shorter than p)
total = total + 1
out4 = find_anagrams("a", "aa")
if out4 == []:
    passed = passed + 1
    print("테스트 4 통과 / Test 4 PASS")
else:
    print("테스트 4 실패 / Test 4 FAIL -> 받은 값 / got:", out4)

# 테스트 5 (반복 글자 패턴 / repeated-letter pattern)
total = total + 1
out5 = find_anagrams("baa", "aa")
if out5 == [1]:
    passed = passed + 1
    print("테스트 5 통과 / Test 5 PASS")
else:
    print("테스트 5 실패 / Test 5 FAIL -> 받은 값 / got:", out5)

print("=====================================")
print(f"결과 / Score: {passed}/{total}")
