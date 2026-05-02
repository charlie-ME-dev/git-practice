# 🐍 Python 연습: 정렬된 배열에서 중복 제거하기!

여러분, 안녕하세요! 오늘은 실전에서 자주 마주치는 데이터 정리 문제를 풀어봅시다. 📚

## 🏢 실전 시나리오

여러분은 대학교 도서관에서 **주니어 개발자 인턴**으로 일하고 있습니다. 매일 밤, 시스템이 대출 기록을 학생 ID 순서대로 정렬된 리스트로 출력합니다. 하지만 같은 학생이 여러 번 책을 빌린 경우가 많아서, 리스트에는 **중복된 학생 ID가 가득**합니다!

선배 개발자가 여러분에게 이 미션을 맡겼습니다:

> "이 정렬된 리스트에서 고유한 학생 ID만 앞쪽에 모아주세요. 서버 메모리가 부족해서 **새 리스트를 만들면 안 됩니다** — 원본을 직접 수정해야 해요!"

## 🎯 미션

정렬된 숫자 리스트에서 중복을 제거하고, 각 숫자가 한 번만 나타나도록 정리하세요. 그리고 고유한 숫자가 몇 개인지 반환하세요.

**여기서 중요한 점:** *in-place* 방식으로 해야 합니다 — 새로운 리스트를 만들 수 없어요!

## 📋 규칙

*주어지는 것:*
• `nums`라는 이미 정렬된 리스트 (작은 것부터 큰 순서)
• 리스트에 중복된 값들이 포함되어 있음

*해야 할 일:*
1. 리스트를 재배열하여 중복 제거
2. 모든 고유한 숫자를 앞쪽에 배치
3. 정렬된 순서 유지
4. 고유한 숫자의 개수 반환

*반드시 따라야 할 제약사항:*
• **추가 리스트 사용 금지!** 몇 개의 변수만 사용해야 합니다
• 배열은 이미 정렬되어 있습니다 (이 점을 활용하세요!)
• 원본 `nums` 리스트를 직접 수정하세요
• 함수 실행 후, 처음 `k`개의 요소가 고유한 값이 되어야 합니다
• `k` 위치 이후는 신경 쓰지 않아도 됩니다 — 아무 값이나 남겨도 괜찮아요

## 💡 예제

**예제 1:**
```
입력: nums = [1, 1, 2]
출력: 2, nums는 [1, 2, _]가 됨
```
왜? 고유한 숫자가 2개 (1과 2)이므로, 2를 반환합니다. 처음 두 자리에는 [1, 2]가 들어갑니다.

**예제 2:**
```
입력: nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
출력: 5, nums는 [0, 1, 2, 3, 4, _, _, _, _, _]가 됨
```
왜? 고유한 숫자가 5개이므로, 5를 반환합니다.

## 📐 함수 명세

| 항목 | 내용 |
|------|------|
| 함수 이름 | `remove_duplicates` |
| 매개변수 | `nums: list[int]` — 정렬된 정수 리스트 |
| 반환값 | `int` — 고유한 값의 개수 (`k`) |
| 부작용 | `nums`의 처음 `k`개 위치에 고유값이 정렬된 순서로 저장됨 |

## 🎓 알아야 할 것

코딩을 시작하기 전에, 다음을 이해하고 있는지 확인하세요:
• 리스트를 반복하는 방법 (`for`, `while`)
• 인접한 요소들을 비교하는 방법 (`nums[i]` vs `nums[i-1]`)
• Python에서 리스트 인덱싱이 작동하는 방식
• "in-place" 수정이 무엇을 의미하는지
• `len()` 함수 사용법

## ✅ 과제

다음 시그니처로 함수를 작성하세요:
```python
def remove_duplicates(nums: list[int]) -> int:
    # 여기에 코드 작성
    pass
```

**시작하는 데 도움이 될 팁:**
• 리스트가 정렬되어 있으므로, 중복은 항상 서로 옆에 있습니다
• 두 개의 "포인터" 사용을 생각해보세요: 하나는 리스트를 읽고, 하나는 고유한 값을 쓸 위치를 추적
• 첫 번째 요소는 항상 고유합니다 (그 앞에는 아무것도 없으니까요!)

## 🎪 코드 테스트

다음 테스트 케이스를 실행해보세요:

```python
# 테스트 1: 기본 케이스
nums1 = [1, 1, 2]
k1 = remove_duplicates(nums1)
print(f"길이: {k1}, 처음 {k1}개 요소: {nums1[:k1]}")
# 예상: 길이: 2, 처음 2개 요소: [1, 2]

# 테스트 2: 여러 중복
nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
k2 = remove_duplicates(nums2)
print(f"길이: {k2}, 처음 {k2}개 요소: {nums2[:k2]}")
# 예상: 길이: 5, 처음 5개 요소: [0, 1, 2, 3, 4]

# 테스트 3: 요소 하나 (경계 케이스)
nums3 = [7]
k3 = remove_duplicates(nums3)
print(f"길이: {k3}, 처음 {k3}개 요소: {nums3[:k3]}")
# 예상: 길이: 1, 처음 1개 요소: [7]

# 테스트 4: 전부 같은 값 (경계 케이스)
nums4 = [5, 5, 5, 5, 5]
k4 = remove_duplicates(nums4)
print(f"길이: {k4}, 처음 {k4}개 요소: {nums4[:k4]}")
# 예상: 길이: 1, 처음 1개 요소: [5]

# 테스트 5: 중복 없음 (경계 케이스)
nums5 = [1, 2, 3, 4, 5]
k5 = remove_duplicates(nums5)
print(f"길이: {k5}, 처음 {k5}개 요소: {nums5[:k5]}")
# 예상: 길이: 5, 처음 5개 요소: [1, 2, 3, 4, 5]

# 테스트 6: 음수 포함
nums6 = [-3, -3, -1, 0, 0, 2]
k6 = remove_duplicates(nums6)
print(f"길이: {k6}, 처음 {k6}개 요소: {nums6[:k6]}")
# 예상: 길이: 4, 처음 4개 요소: [-3, -1, 0, 2]
```

## 🤔 생각해보기

코딩을 시작하기 전에, 접근 방법을 스케치해보세요:
1. 고유한 숫자를 찾았는지 어떻게 알 수 있을까요?
2. 그것을 어디에 배치할까요?
3. 리스트의 "정리된" 부분이 어디서 끝나는지 어떻게 추적할까요?
4. 빈 리스트가 들어오면 어떻게 될까요?

## 🌟 보너스 챌린지

기본 과제를 끝냈다면, 도전해보세요!

### 🟢 Easy 보너스: `count_duplicates(nums)`
리스트를 수정하지 않고 **중복된 요소의 개수**만 세서 반환하는 함수를 작성하세요.
```python
count_duplicates([1, 1, 2, 2, 2, 3])  # 3 반환 (중복 3개: 1 한 번, 2 두 번)
count_duplicates([1, 2, 3])           # 0 반환
```

### 🟡 Medium 보너스: `remove_duplicates_twice(nums)`
이번에는 각 숫자가 **최대 2번까지** 나타나도록 허용하세요. 나머지 규칙은 동일합니다.
```python
nums = [1, 1, 1, 2, 2, 3]
k = remove_duplicates_twice(nums)
# k = 5, nums의 처음 5개: [1, 1, 2, 2, 3]
```

### 🔴 Hard 보너스: `remove_duplicates_with_counts(nums)`
중복을 제거하면서, 각 고유값이 몇 번 나타났는지도 기록하세요. 튜플 `(counts_dict, k)`를 반환합니다.
```python
nums = [1, 1, 2, 3, 3, 3]
counts, k = remove_duplicates_with_counts(nums)
# counts = {1: 2, 2: 1, 3: 3}, k = 3, nums의 처음 3개: [1, 2, 3]
```
💡 *이 문제는 딕셔너리(dictionary)라는 새로운 자료구조를 미리 맛보는 것입니다! 다음 수업에서 자세히 배워요.*

---

막히면 스레드에 질문을 남겨주세요! 목표는 끝내는 것이 아니라 배우는 것입니다. 천천히 논리를 이해하면서 진행하세요.

행운을 빕니다! 🚀

---
---

# 🐍 Python Practice: Remove Duplicates from Sorted Array!

Hey team! Today we're tackling a data-cleanup problem you'll meet often in real work. 📚

## 🏢 Real-World Scenario

You're working as a **junior developer intern** at your university library. Every night, the system outputs borrowing records as a list sorted by student ID. But since the same student often borrows multiple books, the list is **packed with duplicate student IDs**!

A senior developer hands you this mission:

> "Take this sorted list and pack only the unique student IDs at the front. Our server is low on memory, so you **can't create a new list** — you need to modify the original directly!"

## 🎯 Your Mission

Remove duplicates from a sorted list of numbers so each value appears only once, and return how many unique numbers you found.

**Here's the twist:** You need to do this *in-place* — meaning you can't create a new list!

## 📋 The Rules

*What you're given:*
• A list called `nums` that's already sorted (smallest to largest)
• The list has duplicates in it

*What you need to do:*
1. Remove the duplicates by rearranging the list
2. Put all the unique numbers at the front
3. Keep them in sorted order
4. Return the count of unique numbers

*Constraints you must follow:*
• **No extra lists!** You can only use just a few variables
• The array is already sorted (use this to your advantage!)
• Modify the original `nums` list directly
• After your function runs, the first `k` elements should be the unique values
• We don't care what comes after position `k`

## 💡 Example Time

**Example 1:**
```
Input: nums = [1, 1, 2]
Output: 2, and nums becomes [1, 2, _]
```
Why? There are 2 unique numbers, so return 2. First two spots have [1, 2].

**Example 2:**
```
Input: nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
Output: 5, and nums becomes [0, 1, 2, 3, 4, _, _, _, _, _]
```
Why? There are 5 unique numbers, so return 5.

## 📐 Function Spec

| Item | Details |
|------|---------|
| Function name | `remove_duplicates` |
| Parameter | `nums: list[int]` — sorted list of integers |
| Returns | `int` — count of unique values (`k`) |
| Side effect | First `k` positions of `nums` hold unique values in sorted order |

## 🎓 What You Should Know

Before you start coding, make sure you understand:
• How to loop through a list (`for`, `while`)
• How to compare adjacent elements (`nums[i]` vs `nums[i-1]`)
• How list indexing works in Python
• What "in-place" modification means
• How to use `len()`

## ✅ Your Task

Write a function with this signature:
```python
def remove_duplicates(nums: list[int]) -> int:
    # Your code here
    pass
```

**Tips to get you started:**
• Since the list is sorted, duplicates are always next to each other
• Think about using two "pointers": one to read, one to track where to write unique values
• The first element is always unique (nothing comes before it!)

## 🎪 Test Your Code

Try running these test cases:

```python
# Test 1: Basic case
nums1 = [1, 1, 2]
k1 = remove_duplicates(nums1)
print(f"Length: {k1}, First {k1} elements: {nums1[:k1]}")
# Expected: Length: 2, First 2 elements: [1, 2]

# Test 2: Multiple duplicates
nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
k2 = remove_duplicates(nums2)
print(f"Length: {k2}, First {k2} elements: {nums2[:k2]}")
# Expected: Length: 5, First 5 elements: [0, 1, 2, 3, 4]

# Test 3: Single element (boundary)
nums3 = [7]
k3 = remove_duplicates(nums3)
print(f"Length: {k3}, First {k3} elements: {nums3[:k3]}")
# Expected: Length: 1, First 1 elements: [7]

# Test 4: All same values (boundary)
nums4 = [5, 5, 5, 5, 5]
k4 = remove_duplicates(nums4)
print(f"Length: {k4}, First {k4} elements: {nums4[:k4]}")
# Expected: Length: 1, First 1 elements: [5]

# Test 5: No duplicates (boundary)
nums5 = [1, 2, 3, 4, 5]
k5 = remove_duplicates(nums5)
print(f"Length: {k5}, First {k5} elements: {nums5[:k5]}")
# Expected: Length: 5, First 5 elements: [1, 2, 3, 4, 5]

# Test 6: Negative numbers
nums6 = [-3, -3, -1, 0, 0, 2]
k6 = remove_duplicates(nums6)
print(f"Length: {k6}, First {k6} elements: {nums6[:k6]}")
# Expected: Length: 4, First 4 elements: [-3, -1, 0, 2]
```

## 🤔 Think About It

Before you start coding, sketch out your approach:
1. How will you know when you've found a unique number?
2. Where will you place it?
3. How do you keep track of where the "clean" part of your list ends?
4. What happens if an empty list comes in?

## 🌟 Bonus Challenges

Done with the core task? Try these!

### 🟢 Easy Bonus: `count_duplicates(nums)`
Without modifying the list, write a function that **counts how many duplicate elements** there are.
```python
count_duplicates([1, 1, 2, 2, 2, 3])  # returns 3 (three duplicates: one extra 1, two extra 2s)
count_duplicates([1, 2, 3])           # returns 0
```

### 🟡 Medium Bonus: `remove_duplicates_twice(nums)`
This time, allow each number to appear **at most twice**. Same rules otherwise.
```python
nums = [1, 1, 1, 2, 2, 3]
k = remove_duplicates_twice(nums)
# k = 5, first 5 of nums: [1, 1, 2, 2, 3]
```

### 🔴 Hard Bonus: `remove_duplicates_with_counts(nums)`
Remove duplicates AND record how many times each unique value appeared. Return a tuple `(counts_dict, k)`.
```python
nums = [1, 1, 2, 3, 3, 3]
counts, k = remove_duplicates_with_counts(nums)
# counts = {1: 2, 2: 1, 3: 3}, k = 3, first 3 of nums: [1, 2, 3]
```
💡 *This is a sneak peek at dictionaries — a new data structure you'll learn about next!*

---

Drop your questions in the thread if you get stuck! Remember, the goal is to learn, not just to finish. Take your time and understand the logic.

Good luck! 🚀
