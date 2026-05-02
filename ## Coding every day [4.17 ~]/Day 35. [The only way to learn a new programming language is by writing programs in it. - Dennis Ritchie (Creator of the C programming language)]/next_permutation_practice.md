# 🏃 Python 연습: 다음 레인 배치 만들기!

여러분, 안녕하세요! 오늘은 진짜 까다로운 챌린지입니다 — 차근차근 가봅시다.

## 🎯 미션

여러분은 **육상 대회 운영팀의 신입 개발자**입니다. 결승전에는 모든 가능한 레인 배치(순열)를 사전순으로 한 번씩 시도하기로 했어요. 코치가 묻습니다:

> "현재 배치가 `[1, 2, 3]`인데, **바로 다음 배치**는 뭐야? 매번 처음부터 모든 순열을 만들지 말고, 지금 배치에서 한 단계만 넘겨줘."

여러분의 임무는 현재 선수 번호 배열을 보고, **사전순으로 바로 다음 배열**로 변환하는 것입니다.

**여기서 중요한 점:** *in-place* 방식으로 해야 합니다 — 새로운 리스트를 만들 수 없어요. 원본 리스트를 직접 수정해야 합니다!

## 📋 규칙

*주어지는 것:*
• `nums`라는 정수 리스트 (선수 번호 배치)
• 길이는 1 이상

*해야 할 일:*
1. 사전순으로 **바로 다음** 순열을 찾기
2. 원본 `nums` 리스트를 그 다음 순열로 직접 수정
3. 다음 순열이 없다면 (예: `[3, 2, 1]`처럼 이미 가장 큰 배치), **가장 작은 배치**(오름차순)로 되돌리기
4. 아무것도 반환하지 않음 (`None`)

*반드시 따라야 할 제약사항:*
• **추가 리스트 사용 금지!** 몇 개의 변수와 인덱스만 사용해야 합니다
• 원본 `nums` 리스트를 직접 수정하세요
• `sorted()`, `sort()`, `reversed()`, `[::-1]` 슬라이싱 **사용 금지** — 직접 구현해야 합니다
• `itertools` 같은 라이브러리도 사용 금지
• `while` 반복문과 인덱스 교환(`a, b = b, a`)을 활용하세요

## 💡 예제

**예제 1:**
```
입력: nums = [1, 2, 3]
출력: nums는 [1, 3, 2]가 됨
```
왜? `[1, 2, 3]` 다음에 오는 사전순 배치는 `[1, 3, 2]`입니다.

**예제 2:**
```
입력: nums = [3, 2, 1]
출력: nums는 [1, 2, 3]가 됨
```
왜? `[3, 2, 1]`은 이미 가장 큰 배치예요. 그러므로 가장 작은 배치(오름차순)로 되돌립니다.

**예제 3:**
```
입력: nums = [1, 1, 5]
출력: nums는 [1, 5, 1]가 됨
```
왜? 중복이 있어도 동일한 규칙이 적용됩니다. 사전순으로 바로 다음 배치는 `[1, 5, 1]`입니다.

## 🎓 알아야 할 것

코딩을 시작하기 전에, 다음을 이해하고 있는지 확인하세요:
• `while` 반복문과 인덱스 사용법
• 두 변수의 값을 교환하는 방법: `a, b = b, a`
• 리스트 인덱싱 (`nums[i]`, `nums[-1]` 등)
• "사전순(lexicographic order)"이 무엇을 의미하는지 — 사전에서 단어 순서처럼, 앞에서부터 차례로 비교하는 순서

## 🔍 직접 발견해봅시다

손으로 `[1, 2, 3, 6, 5, 4]`의 다음 순열을 찾아보세요. 답은 `[1, 2, 4, 3, 5, 6]`입니다. 어떤 패턴이 보이나요?

> 💡 힌트: 오른쪽에서 왼쪽으로 보면, 어디까지가 "이미 가장 큰 상태"인가요? (`[6, 5, 4]` 부분이 그래요!) 그 직전 숫자(`3`)에 무슨 일이 일어났나요?

이 관찰을 바탕으로 알고리즘을 3단계로 나눌 수 있습니다:

1. **피벗 찾기**: 오른쪽부터 보면서, 처음으로 "다음 숫자보다 작은" 위치(`i`)를 찾기
2. **교환 대상 찾기**: 오른쪽부터 보면서, 처음으로 `nums[i]`보다 큰 숫자(`nums[j]`)를 찾아 교환
3. **뒤집기**: `i+1`부터 끝까지를 뒤집기 (오름차순으로 만들기)

## ✅ 과제

다음 시그니처로 함수를 작성하세요:
```python
def next_permutation(nums: list[int]) -> None:
    # 여기에 코드 작성
    pass
```

**시작하는 데 도움이 될 팁:**
• 위의 3단계를 그대로 코드로 옮기세요
• 1단계에서 피벗을 못 찾으면(`i = -1`), 전체가 내림차순이라는 뜻 → 2단계는 건너뛰고 3단계로
• 3단계의 "뒤집기"는 두 포인터(`left`, `right`)로 양쪽 끝에서 안쪽으로 좁혀오면서 교환합니다
• 간단한 예제로 손으로 따라가보세요!

## 🎪 코드 테스트

다음 테스트 케이스를 실행해보세요:

```python
# 테스트 1: 일반적인 경우
nums1 = [1, 2, 3]
next_permutation(nums1)
print(f"테스트 1: {nums1}")
# 예상: [1, 3, 2]

# 테스트 2: 가장 큰 배치 → 가장 작은 배치
nums2 = [3, 2, 1]
next_permutation(nums2)
print(f"테스트 2: {nums2}")
# 예상: [1, 2, 3]

# 테스트 3: 중복이 있는 경우
nums3 = [1, 1, 5]
next_permutation(nums3)
print(f"테스트 3: {nums3}")
# 예상: [1, 5, 1]

# 테스트 4: 길이 1
nums4 = [1]
next_permutation(nums4)
print(f"테스트 4: {nums4}")
# 예상: [1]

# 테스트 5: 까다로운 경우
nums5 = [1, 3, 2]
next_permutation(nums5)
print(f"테스트 5: {nums5}")
# 예상: [2, 1, 3]
```

## 🤔 생각해보기

코딩을 시작하기 전에, 접근 방법을 스케치해보세요:
1. 왜 "오른쪽에서 왼쪽으로" 피벗을 찾을까요?
2. 피벗을 찾은 후, 왜 또다시 오른쪽에서 왼쪽으로 교환 대상을 찾을까요?
3. 마지막에 왜 뒤집어야 할까요? (힌트: 교환 후 오른쪽 부분이 어떤 상태인가요?)

## 🎁 보너스 도전

기본 문제를 끝냈다면, 도전해보세요!

**🟢 Easy:** `previous_permutation(nums)` — 사전순으로 **이전** 순열을 만드는 함수를 작성하세요. (예: `[1, 3, 2]` → `[1, 2, 3]`, `[1, 2, 3]` → `[3, 2, 1]`)

**🟡 Medium:** `kth_next_permutation(nums, k)` — `next_permutation`을 `k`번 적용한 결과를 만드는 함수를 작성하세요. (단순히 `for` 반복문으로 호출해도 OK!)

**🔴 Hard:** `is_last_permutation(nums)` — 현재 배치가 사전순으로 가장 마지막 순열인지 판단하는 함수를 작성하세요. (다음 순열이 더 작아진다면 → 현재가 마지막입니다.)

막히면 스레드에 질문을 남겨주세요! 목표는 끝내는 것이 아니라 배우는 것입니다. 천천히 논리를 이해하면서 진행하세요.

행운을 빕니다! 🚀

---
---

# 🏃 Python Practice: Generate the Next Lane Arrangement!

Hey team! Today's challenge is genuinely tricky — let's take it step by step.

## 🎯 Your Mission

You're a **junior developer on a track meet operations team**. The committee decided to run the final by trying every possible lane arrangement (permutation) in lexicographic order, one by one. The coach asks:

> "The current arrangement is `[1, 2, 3]` — what's the **very next** one? Don't generate all permutations from scratch every time. Just give me the next one from where we are now."

Your job is to take an array of runner numbers and transform it into the **next lexicographic arrangement**.

**Here's the twist:** You need to do this *in-place* — you can't create a new list. You have to modify the original one!

## 📋 The Rules

*What you're given:*
• A list `nums` of integers (the current lane arrangement)
• Length is at least 1

*What you need to do:*
1. Find the **immediately next** permutation in lexicographic order
2. Modify the original `nums` list in-place to that next permutation
3. If there's no next permutation (e.g., `[3, 2, 1]` is already the largest), reset it to the **smallest** arrangement (ascending order)
4. Return nothing (`None`)

*Constraints you must follow:*
• **No extra lists!** You can only use a few variables and indices
• Modify the original `nums` list directly
• **Forbidden:** `sorted()`, `sort()`, `reversed()`, `[::-1]` slicing — implement it yourself
• No libraries like `itertools`
• Use `while` loops and index swapping (`a, b = b, a`)

## 💡 Example Time

**Example 1:**
```
Input: nums = [1, 2, 3]
Output: nums becomes [1, 3, 2]
```
Why? The next lexicographic arrangement after `[1, 2, 3]` is `[1, 3, 2]`.

**Example 2:**
```
Input: nums = [3, 2, 1]
Output: nums becomes [1, 2, 3]
```
Why? `[3, 2, 1]` is already the largest. So we reset to the smallest (ascending order).

**Example 3:**
```
Input: nums = [1, 1, 5]
Output: nums becomes [1, 5, 1]
```
Why? The same rule applies even with duplicates. The next arrangement is `[1, 5, 1]`.

## 🎓 What You Should Know

Before you start coding, make sure you understand:
• How to use `while` loops with indices
• How to swap two variables: `a, b = b, a`
• List indexing (`nums[i]`, `nums[-1]`, etc.)
• What "lexicographic order" means — like word order in a dictionary, comparing position by position from the front

## 🔍 Discover It Yourself

By hand, find the next permutation of `[1, 2, 3, 6, 5, 4]`. The answer is `[1, 2, 4, 3, 5, 6]`. Do you see a pattern?

> 💡 Hint: Looking from right to left, how far back is the array "already at its biggest possible state"? (The `[6, 5, 4]` part is!) What happened to the number just before it (`3`)?

This observation lets us split the algorithm into 3 steps:

1. **Find the pivot**: Scan from the right and find the first position (`i`) that's "smaller than the next number"
2. **Find the swap target**: Scan from the right and find the first number (`nums[j]`) bigger than `nums[i]`, then swap them
3. **Reverse**: Reverse everything from `i+1` to the end (making it ascending)

## ✅ Your Task

Write a function with this signature:
```python
def next_permutation(nums: list[int]) -> None:
    # Your code here
    pass
```

**Tips to get you started:**
• Translate the 3 steps above directly into code
• In step 1, if you don't find a pivot (`i = -1`), the whole list is descending → skip step 2 and go straight to step 3
• The "reverse" in step 3 uses two pointers (`left`, `right`) closing in from both ends, swapping as you go
• Walk through a small example by hand!

## 🎪 Test Your Code

Try running these test cases:

```python
# Test 1: typical case
nums1 = [1, 2, 3]
next_permutation(nums1)
print(f"Test 1: {nums1}")
# Expected: [1, 3, 2]

# Test 2: largest → smallest
nums2 = [3, 2, 1]
next_permutation(nums2)
print(f"Test 2: {nums2}")
# Expected: [1, 2, 3]

# Test 3: with duplicates
nums3 = [1, 1, 5]
next_permutation(nums3)
print(f"Test 3: {nums3}")
# Expected: [1, 5, 1]

# Test 4: length 1
nums4 = [1]
next_permutation(nums4)
print(f"Test 4: {nums4}")
# Expected: [1]

# Test 5: tricky case
nums5 = [1, 3, 2]
next_permutation(nums5)
print(f"Test 5: {nums5}")
# Expected: [2, 1, 3]
```

## 🤔 Think About It

Before you start coding, sketch out your approach:
1. Why scan from "right to left" to find the pivot?
2. After finding the pivot, why scan from right to left again to find the swap target?
3. Why do we need to reverse at the end? (Hint: what state is the right part in after the swap?)

## 🎁 Bonus Challenges

Once you've finished the main problem, try these!

**🟢 Easy:** `previous_permutation(nums)` — Write a function that produces the **previous** permutation in lexicographic order. (e.g., `[1, 3, 2]` → `[1, 2, 3]`, `[1, 2, 3]` → `[3, 2, 1]`)

**🟡 Medium:** `kth_next_permutation(nums, k)` — Write a function that applies `next_permutation` `k` times. (Just calling it in a `for` loop is fine!)

**🔴 Hard:** `is_last_permutation(nums)` — Write a function that decides whether the current arrangement is the very last permutation in lexicographic order. (If the next permutation would be smaller → the current one is last.)

Drop your questions in the thread if you get stuck! Remember, the goal is to learn, not just to finish. Take your time and understand the logic.

Good luck! 🚀
