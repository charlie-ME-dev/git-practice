# 🧬 Python 연습: 서열 속 애너그램 찾기 (변형)

> "I am running to make history, to show that no human is limited."
> 나는 역사를 만들기 위해 달립니다. 인간에게 한계가 없다는 것을 보여주기 위해.
> — Eliud Kipchoge (엘리우드 킵초게), 마라톤 2시간 벽 최초 돌파

여러분, 안녕하세요! 어제 **반복되는 DNA 서열**을 찾았던 그 기술 — **고정 길이 윈도우 + 딕셔너리 빈도 세기** — 을 오늘 살짝 다른 문제에 다시 써봅니다. 어제 흐름이 손에 익었다면, 오늘은 그걸 *전이*하는 연습이에요. 어렵지 않으니 자신감을 가지고 가봅시다!

---

## 🎯 미션: Helix Genomics 연구실 — 패턴 정렬 분석

어제는 **반복되는** 서열을 찾았죠. 오늘 연구실의 새 과제는 조금 다릅니다. 짧은 **기준 패턴 `p`** 가 주어지고, 긴 서열 `s` 안에서 **그 패턴과 똑같은 글자들을 (순서만 다르게) 가진 구간**이 어디서 시작하는지 모두 찾아야 합니다.

예를 들어 패턴이 `"abc"`라면, `"cba"`나 `"bac"`도 같은 글자 묶음이므로 애너그램(anagram)입니다. DNA 분석에서는 염기 구성은 같지만 배열 순서가 다른 구간을 찾는 것에 해당해요.

---

## 📋 규칙

*주어지는 것:*
- 긴 문자열 `s`
- 짧은 기준 패턴 `p`

*해야 할 일:*
1. `s` 안에서 길이가 `len(p)`인 모든 구간을 살펴보기
2. 그 구간이 `p`의 **애너그램**인지 확인 (= 글자 종류와 개수가 똑같은지)
3. 애너그램인 구간의 **시작 인덱스**를 모두 리스트로 반환 (순서는 상관없음)

*제약사항:*
- 구간 길이는 항상 `len(p)`로 고정입니다
- `s`가 `p`보다 짧으면 빈 리스트 `[]` 반환
- "애너그램"은 순서가 달라도 글자 구성이 같으면 됩니다 (`"ab"`와 `"ba"`는 애너그램)

---

## 💡 예제

**예제 1:**
```
입력:  s = "cbaebabacd", p = "abc"
출력:  [0, 6]
```
왜? 인덱스 0의 `"cba"`와 인덱스 6의 `"bac"`가 `"abc"`의 애너그램입니다.

**예제 2:**
```
입력:  s = "abab", p = "ab"
출력:  [0, 1, 2]
```
왜? `"ab"`(0), `"ba"`(1), `"ab"`(2) 모두 `"ab"`의 애너그램입니다.

**예제 3:**
```
입력:  s = "abc", p = "xyz"
출력:  []
```
왜? 글자 구성이 전혀 다르므로 애너그램이 없습니다.

---

## 🎓 알아야 할 것 (어제와 똑같아요!)

- 문자열 슬라이싱: `s[i:i+n]`은 인덱스 `i`부터 `n`글자를 잘라냅니다
- `range()`와 `for` 반복문으로 시작 인덱스를 순회하는 법
- 딕셔너리로 **글자별 등장 횟수**를 세는 법 (`if ch in count`)
- 두 딕셔너리가 같은지 비교하는 법: `dict_a == dict_b` (Python은 키·값이 모두 같으면 `True`)

> 💬 **핵심 전이 포인트:** 어제는 "윈도우 문자열 자체"를 딕셔너리 키로 셌어요. 오늘은 "윈도우 *안의 글자들*"을 세서 패턴의 글자 빈도와 비교합니다. 윈도우를 훑는 뼈대는 똑같습니다!

---

## ✅ 과제

다음 시그니처로 함수를 작성하세요:
```python
def find_anagrams(s: str, p: str) -> list[int]:
    # 여기에 코드 작성
    pass
```

**시작 팁:**
- 먼저 패턴 `p`의 글자 빈도를 딕셔너리 `p_count`로 만들어 두세요
- 마지막 윈도우 시작 위치는 `len(s) - len(p)`이므로 `range(len(s) - len(p) + 1)`로 순회합니다
- 각 윈도우마다 글자 빈도 딕셔너리를 만들고, `p_count`와 `==`로 비교하세요
- 같으면 그 시작 인덱스 `i`를 결과에 추가!

---

## 🎪 코드 테스트

```python
# 테스트 1
print(find_anagrams("cbaebabacd", "abc"))
# 예상: [0, 6]

# 테스트 2
print(find_anagrams("abab", "ab"))
# 예상: [0, 1, 2]

# 테스트 3
print(find_anagrams("abc", "xyz"))
# 예상: []
```

---

## 🏆 보너스 도전

- 🥉 **Easy** — 시작 인덱스 대신 **애너그램 구간 문자열 자체**를 반환하세요. 예: `["cba", "bac"]`.
- 🥈 **Medium** — 애너그램이 **몇 개** 발견됐는지 개수만 반환하는 `count_anagrams(s, p)`를 만들어 보세요.
- 🥇 **Hard** *(다음 단원 미리보기)* — 매 윈도우마다 빈도를 처음부터 다시 세지 말고, **한 칸 옮길 때 왼쪽 글자 하나 빼고 오른쪽 글자 하나 더하는** 방식으로 최적화해 보세요. (진짜 슬라이딩 윈도우! 아직 안 배운 기법이니 도전만 해보세요.)

---

## 🤔 생각해보기

1. 어제 DNA 문제의 윈도우 순회 코드와 오늘 코드는 어디가 같고 어디가 다른가요?
2. 두 딕셔너리를 비교할 때 `==` 하나면 충분할까요? 왜 그럴까요?
3. 패턴에 같은 글자가 여러 번 나오면(예: `p = "aab"`) 빈도 세기가 왜 중요해질까요?

막히면 언제든 질문하세요. 어제 한 걸 떠올리면 분명히 풀 수 있어요! 🚀

---
---

# 🧬 Python Practice: Find Anagrams in a Sequence (Variation)

> "I am running to make history, to show that no human is limited."
> — Eliud Kipchoge, first to break the 2-hour marathon barrier

Hey team! Today we reuse yesterday's technique — **a fixed-length window + counting frequencies with a dictionary** — on a slightly different problem. If yesterday's flow clicked for you, today is about *transferring* that skill. It's not hard, so go in with confidence!

---

## 🎯 Your Mission: Helix Genomics Lab — Pattern Alignment

Yesterday you found **repeated** sequences. Today's new lab task is a bit different. You're given a short **reference pattern `p`**, and inside a longer sequence `s` you must find every position where a window has **the exact same letters as `p`, just in a different order**.

For example, if the pattern is `"abc"`, then `"cba"` and `"bac"` count too — they're anagrams. In DNA analysis, this is like finding regions with the same base composition but a different arrangement.

---

## 📋 The Rules

*What you're given:*
- A long string `s`
- A short reference pattern `p`

*What you need to do:*
1. Look at every length-`len(p)` window in `s`
2. Check if that window is an **anagram** of `p` (same letters, same counts)
3. Return the **start indices** of all anagram windows as a list (order doesn't matter)

*Constraints:*
- The window length is always fixed at `len(p)`
- If `s` is shorter than `p`, return an empty list `[]`
- An "anagram" just needs the same letter composition regardless of order (`"ab"` and `"ba"` are anagrams)

---

## 💡 Examples

**Example 1:**
```
Input:  s = "cbaebabacd", p = "abc"
Output: [0, 6]
```
Why? `"cba"` at index 0 and `"bac"` at index 6 are anagrams of `"abc"`.

**Example 2:**
```
Input:  s = "abab", p = "ab"
Output: [0, 1, 2]
```
Why? `"ab"`(0), `"ba"`(1), `"ab"`(2) are all anagrams of `"ab"`.

**Example 3:**
```
Input:  s = "abc", p = "xyz"
Output: []
```
Why? Completely different letters, so no anagram exists.

---

## 🎓 What You Should Know (same as yesterday!)

- String slicing: `s[i:i+n]` takes `n` characters starting at index `i`
- Looping over start indices with `range()` and `for`
- Counting **per-character occurrences** in a dictionary (`if ch in count`)
- Comparing two dictionaries: `dict_a == dict_b` (Python returns `True` if all keys and values match)

> 💬 **Key transfer point:** Yesterday you counted "the window string itself" as a dictionary key. Today you count "the *letters inside* the window" and compare to the pattern's letter frequencies. The window-scanning skeleton is identical!

---

## ✅ Your Task

Write a function with this signature:
```python
def find_anagrams(s: str, p: str) -> list[int]:
    # Your code here
    pass
```

**Tips to get started:**
- First build the pattern's letter frequency into a dictionary `p_count`
- The last valid window start is `len(s) - len(p)`, so loop with `range(len(s) - len(p) + 1)`
- For each window, build a letter frequency dict and compare to `p_count` with `==`
- If equal, add the start index `i` to your result!

---

## 🎪 Test Your Code

```python
# Test 1
print(find_anagrams("cbaebabacd", "abc"))
# Expected: [0, 6]

# Test 2
print(find_anagrams("abab", "ab"))
# Expected: [0, 1, 2]

# Test 3
print(find_anagrams("abc", "xyz"))
# Expected: []
```

---

## 🏆 Bonus Challenges

- 🥉 **Easy** — Return the **anagram substrings themselves** instead of start indices, e.g. `["cba", "bac"]`.
- 🥈 **Medium** — Write `count_anagrams(s, p)` that returns just **how many** anagrams were found.
- 🥇 **Hard** *(preview of the next unit)* — Instead of rebuilding the frequency from scratch each window, optimize by **removing the leftmost letter and adding the new rightmost letter** as you slide. (A true sliding window! You haven't learned this yet — just give it a try.)

---

## 🤔 Think About It

1. Where is your code today the same as yesterday's DNA window loop, and where is it different?
2. Is a single `==` enough to compare two dictionaries? Why?
3. If the pattern has repeated letters (e.g. `p = "aab"`), why does counting frequencies matter?

Drop your questions anytime. Recall what you did yesterday and you've got this! 🚀
