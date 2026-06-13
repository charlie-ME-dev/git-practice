# 🧬 Python 연습: 반복되는 DNA 서열 찾기

> "In bioinformatics, the sequence is the message — and repetition is often where the meaning hides."

여러분, 안녕하세요! 이번에는 **문자열 메서드**와 **반복문**, 그리고 **딕셔너리**를 활용해 실제 생물정보학 문제를 풀어봅니다.

---

## 🎯 미션: Helix Genomics 연구실

여러분은 **Helix Genomics** 연구실의 신입 분석가입니다. 환자의 DNA 염기 서열에서 **반복되는 패턴**을 찾는 것이 임무예요. 특정 길이의 서열이 반복되면, 그것은 유전 질환이나 돌연변이의 단서가 될 수 있습니다.

DNA는 네 가지 염기(`A`, `C`, `G`, `T`)로 이루어진 긴 문자열입니다. 예: `"ACGAATTCCG"`. 우리는 그 안에서 **10글자짜리 서열 중 두 번 이상 나타나는 것**을 모두 찾아야 합니다.

---

## 📋 규칙

*주어지는 것:*
- `s`라는 DNA 문자열 (`A`, `C`, `G`, `T`로만 구성)

*해야 할 일:*
1. 길이 10짜리 모든 부분 문자열(서열)을 살펴보기
2. 두 번 이상 등장하는 서열을 모두 찾기
3. 그 서열들을 리스트로 반환하기 (순서는 상관없음)

*제약사항:*
- 길이 10짜리 서열만 봅니다 (더 길거나 짧은 것은 무시)
- 문자열 길이가 10보다 작으면 빈 리스트 `[]` 반환
- 중복 없이, 각 반복 서열은 결과에 **한 번만** 포함

---

## 💡 예제

**예제 1:**
```
입력:  s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
출력:  ["AAAAACCCCC", "CCCCCAAAAA"]
```
왜? `"AAAAACCCCC"`와 `"CCCCCAAAAA"`가 각각 두 번 이상 나타납니다.

**예제 2:**
```
입력:  s = "AAAAAAAAAAAAA"
출력:  ["AAAAAAAAAA"]
```
왜? `"AAAAAAAAAA"`(A 10개)가 겹치면서 여러 번 등장합니다.

**예제 3:**
```
입력:  s = "ACGT"
출력:  []
```
왜? 길이가 10보다 작으므로 만들 수 있는 10글자 서열이 없습니다.

---

## 🎓 알아야 할 것

시작 전에 다음을 떠올려 보세요:
- 문자열 슬라이싱: `s[i:i+10]`은 인덱스 `i`부터 10글자를 잘라냅니다
- `range()`와 `for` 반복문으로 인덱스를 순회하는 법
- 딕셔너리에 등장 횟수를 세는 법 (`if key in dict` 활용)
- "슬라이딩 윈도우": 한 칸씩 옮기며 길이가 고정된 창(window)을 훑는 방법

---

## ✅ 과제

다음 시그니처로 함수를 작성하세요:
```python
def find_repeated_dna(s: str) -> list[str]:
    # 여기에 코드 작성
    pass
```

**시작 팁:**
- 마지막으로 잘라낼 수 있는 시작 위치는 `len(s) - 10`입니다
- 딕셔너리에 각 서열의 등장 횟수를 기록해 보세요
- 횟수가 2가 되는 순간을 활용하면 중복 추가를 피할 수 있어요

---

## 🎪 코드 테스트

```python
# 테스트 1
print(sorted(find_repeated_dna("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")))
# 예상: ['AAAAACCCCC', 'CCCCCAAAAA']

# 테스트 2
print(find_repeated_dna("AAAAAAAAAAAAA"))
# 예상: ['AAAAAAAAAA']

# 테스트 3
print(find_repeated_dna("ACGT"))
# 예상: []
```

---

## 🏆 보너스 도전

- 🥉 **Easy** — 반복 서열을 **등장 횟수와 함께** 반환하세요. 예: `{"AAAAACCCCC": 2}` 형태의 딕셔너리.
- 🥈 **Medium** — 서열 길이를 고정값 10이 아니라 **매개변수 `k`**로 받도록 일반화하세요: `find_repeated_dna(s, k)`.
- 🥇 **Hard** *(다음 단원 미리보기)* — `collections.Counter`를 사용해 한 줄로 카운팅해 보세요. 어떤 서열이 가장 많이 반복되는지도 찾아보세요. (아직 안 배운 도구이니 도전만 해보면 됩니다!)

---

## 🤔 생각해보기

1. 같은 서열을 두 번 발견했을 때, 결과에 중복으로 넣지 않으려면 어떻게 할까요?
2. 슬라이딩 윈도우의 시작 인덱스는 어디서 멈춰야 할까요? (`len(s)`? `len(s)-10`?)
3. 딕셔너리 대신 집합(set)을 두 개 쓰면 더 간단해질까요?

막히면 언제든 질문하세요. 목표는 끝내는 게 아니라 **논리를 이해하는 것**입니다! 🚀

---
---

# 🧬 Python Practice: Find Repeated DNA Sequences

> "In bioinformatics, the sequence is the message — and repetition is often where the meaning hides."

Hey team! This time we'll use **string methods**, **loops**, and **dictionaries** to solve a real bioinformatics problem.

---

## 🎯 Your Mission: Helix Genomics Lab

You're a new analyst at the **Helix Genomics** lab. Your job is to find **repeated patterns** in a patient's DNA sequence. When a sequence of a certain length repeats, it can be a clue to genetic conditions or mutations.

DNA is a long string made of four bases (`A`, `C`, `G`, `T`). For example: `"ACGAATTCCG"`. We need to find all **10-letter sequences that appear more than once**.

---

## 📋 The Rules

*What you're given:*
- A DNA string `s` (only `A`, `C`, `G`, `T`)

*What you need to do:*
1. Look at every length-10 substring (sequence)
2. Find all that appear more than once
3. Return them as a list (order doesn't matter)

*Constraints:*
- Only length-10 sequences (ignore anything longer or shorter)
- If the string is shorter than 10, return an empty list `[]`
- Each repeated sequence appears in the result **only once** (no duplicates)

---

## 💡 Examples

**Example 1:**
```
Input:  s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC", "CCCCCAAAAA"]
```
Why? Both `"AAAAACCCCC"` and `"CCCCCAAAAA"` appear more than once.

**Example 2:**
```
Input:  s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]
```
Why? `"AAAAAAAAAA"` (ten A's) appears multiple times in overlapping fashion.

**Example 3:**
```
Input:  s = "ACGT"
Output: []
```
Why? The string is shorter than 10, so no 10-letter sequence exists.

---

## 🎓 What You Should Know

Before you start, recall:
- String slicing: `s[i:i+10]` takes 10 characters starting at index `i`
- Looping over indices with `range()` and `for`
- Counting occurrences in a dictionary (using `if key in dict`)
- "Sliding window": scanning a fixed-length window one step at a time

---

## ✅ Your Task

Write a function with this signature:
```python
def find_repeated_dna(s: str) -> list[str]:
    # Your code here
    pass
```

**Tips to get started:**
- The last valid start position is `len(s) - 10`
- Record each sequence's count in a dictionary
- The moment a count hits 2 is a handy way to avoid adding duplicates

---

## 🎪 Test Your Code

```python
# Test 1
print(sorted(find_repeated_dna("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")))
# Expected: ['AAAAACCCCC', 'CCCCCAAAAA']

# Test 2
print(find_repeated_dna("AAAAAAAAAAAAA"))
# Expected: ['AAAAAAAAAA']

# Test 3
print(find_repeated_dna("ACGT"))
# Expected: []
```

---

## 🏆 Bonus Challenges

- 🥉 **Easy** — Return the repeated sequences **with their counts**, e.g. a dictionary like `{"AAAAACCCCC": 2}`.
- 🥈 **Medium** — Generalize the sequence length from the fixed `10` to a **parameter `k`**: `find_repeated_dna(s, k)`.
- 🥇 **Hard** *(preview of the next unit)* — Use `collections.Counter` to count in a single line. Also find which sequence repeats the most. (You haven't learned this tool yet — just give it a try!)

---

## 🤔 Think About It

1. When you find the same sequence twice, how do you avoid adding it to the result twice?
2. Where should the sliding window's start index stop? (`len(s)`? `len(s)-10`?)
3. Would two sets be simpler than one dictionary here?

Drop your questions anytime. The goal isn't to finish — it's to **understand the logic**! 🚀
