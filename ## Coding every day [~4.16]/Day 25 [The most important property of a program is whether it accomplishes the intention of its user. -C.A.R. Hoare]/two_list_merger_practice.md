# 🔀 Python 연습: 두 리스트 합치기!

여러분, 안녕하세요! 오늘은 실제 데이터 처리 현장에서 자주 쓰이는 알고리즘을 직접 구현해봅니다.

## 🎯 미션

여러분은 금융 데이터 회사의 주니어 개발자입니다! 팀장이 이렇게 요청했어요:

> "두 거래소에서 이미 정렬된 주가 데이터가 들어와요. 이걸 하나의 정렬된 리스트로 합쳐야 하는데, `sort()`는 쓰면 안 돼요. 두 리스트가 이미 정렬되어 있다는 걸 활용해야 합니다!"

두 개의 **이미 정렬된** 리스트를 하나의 정렬된 리스트로 합치는 함수를 만들어봅시다.

## 📋 만들어야 할 함수

### `merge_lists(list_a, list_b)`
두 개의 정렬된 리스트를 받아서 하나의 정렬된 리스트로 합쳐 반환합니다.
• **`sort()` 또는 `sorted()` 사용 금지!** 두 리스트가 이미 정렬되어 있다는 점을 활용하세요.
• 원본 리스트는 수정하지 않습니다.
• 반환값: 합쳐진 정렬된 리스트

## 💡 예제

```
list_a = [1, 3, 5, 7]
list_b = [2, 4, 6, 8]

merge_lists(list_a, list_b)
→ [1, 2, 3, 4, 5, 6, 7, 8]
```

```
list_a = [1, 2, 9]
list_b = [3, 5, 7]

merge_lists(list_a, list_b)
→ [1, 2, 3, 5, 7, 9]
```

## 🧠 핵심 아이디어: 두 포인터 전략

`sort()`를 쓰지 않고도 합칠 수 있는 이유가 있어요.
두 리스트가 **이미 정렬되어 있기 때문**입니다!

이렇게 생각해보세요 — 두 줄의 카드 패가 있고, 각 패는 이미 작은 순서로 정렬되어 있어요:

```
list_a: [1,  3,  5,  7]
         ↑
         i = 0  (현재 list_a에서 볼 카드)

list_b: [2,  4,  6,  8]
         ↑
         j = 0  (현재 list_b에서 볼 카드)

결과:   []
```

매 단계마다 두 포인터가 가리키는 카드를 비교해서, **더 작은 쪽**을 결과 리스트에 추가하고 그 포인터를 한 칸 앞으로 이동합니다:

```
1단계: list_a[0]=1 vs list_b[0]=2  →  1이 더 작으니 결과에 추가, i=1
2단계: list_a[1]=3 vs list_b[0]=2  →  2가 더 작으니 결과에 추가, j=1
3단계: list_a[1]=3 vs list_b[1]=4  →  3이 더 작으니 결과에 추가, i=2
...
```

한 쪽이 끝나면, 남은 쪽의 카드를 전부 결과에 붙여넣으면 됩니다!

## 🎓 알아야 할 것

코딩 시작 전, 다음 개념을 떠올려보세요:
• 인덱스 변수로 리스트 위치 추적하기 (`i = 0`, `j = 0`)
• `while` 반복문으로 두 조건을 동시에 확인하기
• `append()` 로 결과 리스트에 항목 추가하기
• 리스트 슬라이싱으로 나머지 항목 한 번에 붙이기 (`result + list_a[i:]`)

## ✅ 과제

아래 함수 시그니처를 사용해서 코드를 완성하세요:

```python
def merge_lists(list_a: list, list_b: list) -> list:
    # TODO: 여기에 코드 작성
    pass
```

**시작 힌트:**
```python
def merge_lists(list_a: list, list_b: list) -> list:
    result = []
    i = 0   # list_a의 현재 위치 / current position in list_a
    j = 0   # list_b의 현재 위치 / current position in list_b

    # 두 리스트 모두 남은 항목이 있는 동안 반복
    # while both lists still have items remaining
    while i < len(list_a) and j < len(list_b):
        # TODO: 비교하고 더 작은 쪽을 result에 추가하세요
        # TODO: compare and append the smaller one to result
        pass

    # TODO: 남은 항목들을 result에 붙이세요
    # TODO: attach any remaining items to result
    pass
```

## 🎪 코드 테스트

```python
# 테스트 1: 기본 케이스 — 번갈아가며 섞임
list_a = [1, 3, 5, 7]
list_b = [2, 4, 6, 8]
print(merge_lists(list_a, list_b))
# 예상: [1, 2, 3, 4, 5, 6, 7, 8]

# 테스트 2: 한쪽이 먼저 끝남
list_a = [1, 2, 3]
list_b = [10, 20, 30]
print(merge_lists(list_a, list_b))
# 예상: [1, 2, 3, 10, 20, 30]

# 테스트 3: 길이가 다른 리스트
list_a = [1, 2, 9]
list_b = [3, 5, 7]
print(merge_lists(list_a, list_b))
# 예상: [1, 2, 3, 5, 7, 9]

# 테스트 4: 한쪽이 빈 리스트
list_a = []
list_b = [1, 2, 3]
print(merge_lists(list_a, list_b))
# 예상: [1, 2, 3]

# 테스트 5: 중복 값이 있을 때
list_a = [1, 3, 3, 5]
list_b = [2, 3, 4]
print(merge_lists(list_a, list_b))
# 예상: [1, 2, 3, 3, 3, 4, 5]

# 테스트 6: 원본 리스트가 수정되지 않았는지 확인
list_a = [1, 3, 5]
list_b = [2, 4, 6]
result = merge_lists(list_a, list_b)
print(list_a)   # 예상: [1, 3, 5]  ← 변경되지 않아야 함!
print(list_b)   # 예상: [2, 4, 6]  ← 변경되지 않아야 함!
```

## 🌟 보너스 챌린지

기본 과제를 다 끝냈나요? 단계별로 도전해봅시다!

---

### 🥉 Easy: `merge_three(list_a, list_b, list_c)`

세 개의 정렬된 리스트를 하나로 합치는 함수를 만드세요.
`merge_lists()`를 **두 번** 재사용해서 구현하세요 — 새로운 병합 로직을 작성하지 않아도 됩니다!

```python
list_a = [1, 4, 7]
list_b = [2, 5, 8]
list_c = [3, 6, 9]

merge_three(list_a, list_b, list_c)
→ [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

힌트: `merge_lists(merge_lists(list_a, list_b), list_c)` 처럼 생각해보세요!

---

### 🥈 Medium: `merge_unique(list_a, list_b)`

두 정렬된 리스트를 합치되, **중복 값은 한 번만** 포함하는 함수를 만드세요.
역시 `sort()` / `sorted()` 사용 금지!

```python
list_a = [1, 2, 3, 5]
list_b = [2, 3, 4, 5, 6]

merge_unique(list_a, list_b)
→ [1, 2, 3, 4, 5, 6]
```

힌트: `merge_lists()`의 로직을 기반으로, 결과에 추가하기 전에 중복인지 확인하세요.
이미 결과 리스트의 마지막 항목과 같다면 건너뛰면 됩니다!

---

### 🥇 Hard: `merge_all(lists)`

정렬된 리스트들의 리스트를 받아서 하나로 합치는 함수를 만드세요.
리스트가 몇 개든 상관없이 작동해야 합니다.

```python
all_lists = [[1, 5, 9], [2, 6], [3, 7, 10], [4, 8]]

merge_all(all_lists)
→ [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

제약사항:
• `merge_lists()`를 재사용하세요
• 빈 `lists`가 들어오면 빈 리스트 `[]`를 반환하세요
• `lists` 안에 빈 리스트가 섞여 있어도 처리되어야 합니다

힌트: 반복문으로 리스트를 하나씩 누적하면서 합쳐가면 됩니다!

## 🤔 생각해보기

1. 두 리스트가 **이미 정렬되어 있다**는 사실이 왜 중요한가요? 정렬이 안 된 리스트라면 이 방법이 통할까요?
2. `while` 반복문이 끝난 후에 왜 남은 항목들을 따로 처리해야 할까요?
3. 두 리스트의 길이가 매우 다를 때 (예: 1개 vs 1000개) 이 방법은 잘 작동할까요?

막히면 스레드에 질문 남겨주세요! 완성보다 이해가 목표입니다. 천천히, 하나씩! 💪

행운을 빕니다! 🚀

---
---

# 🔀 Python Practice: Merge Two Sorted Lists!

Hey team! Today we're implementing an algorithm used constantly in real data pipelines.

## 🎯 Your Mission

You're a junior developer at a financial data company! Your team lead just said:

> "We get sorted stock price data from two exchanges. We need to merge them into one sorted list — but we can't use `sort()`. We need to take advantage of the fact that both lists are already sorted!"

Let's build a function that merges two **already sorted** lists into one sorted list.

## 📋 Function to Build

### `merge_lists(list_a, list_b)`
Takes two sorted lists and returns a single merged sorted list.
• **No `sort()` or `sorted()`!** Use the fact that both lists are already sorted.
• Do not modify the original lists.
• Returns: the merged sorted list

## 💡 Example

```
list_a = [1, 3, 5, 7]
list_b = [2, 4, 6, 8]

merge_lists(list_a, list_b)
→ [1, 2, 3, 4, 5, 6, 7, 8]
```

```
list_a = [1, 2, 9]
list_b = [3, 5, 7]

merge_lists(list_a, list_b)
→ [1, 2, 3, 5, 7, 9]
```

## 🧠 The Key Idea: Two-Pointer Strategy

We can merge without `sort()` because both lists are **already sorted**!

Think of it like two hands of cards, each already in order:

```
list_a: [1,  3,  5,  7]
         ↑
         i = 0  (current card to look at in list_a)

list_b: [2,  4,  6,  8]
         ↑
         j = 0  (current card to look at in list_b)

result: []
```

At each step, compare the two cards the pointers are pointing at, add the **smaller one** to the result, and move that pointer forward one step:

```
Step 1: list_a[0]=1 vs list_b[0]=2  →  1 is smaller, add to result, i=1
Step 2: list_a[1]=3 vs list_b[0]=2  →  2 is smaller, add to result, j=1
Step 3: list_a[1]=3 vs list_b[1]=4  →  3 is smaller, add to result, i=2
...
```

When one side runs out, just attach all the remaining cards from the other side!

## 🎓 What You Should Know

Before you start, make sure you're comfortable with:
• Tracking list positions with index variables (`i = 0`, `j = 0`)
• Using `while` loops to check two conditions at once
• Adding items to a result list with `append()`
• Attaching remaining items with slicing (`result + list_a[i:]`)

## ✅ Your Task

Complete the function using this signature:

```python
def merge_lists(list_a: list, list_b: list) -> list:
    # TODO: your code here
    pass
```

**Starter scaffold:**
```python
def merge_lists(list_a: list, list_b: list) -> list:
    result = []
    i = 0   # current position in list_a
    j = 0   # current position in list_b

    # keep going while both lists still have items
    while i < len(list_a) and j < len(list_b):
        # TODO: compare and append the smaller one to result
        pass

    # TODO: attach any remaining items to result
    pass
```

## 🎪 Test Your Code

```python
# Test 1: Basic case — items interleave evenly
list_a = [1, 3, 5, 7]
list_b = [2, 4, 6, 8]
print(merge_lists(list_a, list_b))
# Expected: [1, 2, 3, 4, 5, 6, 7, 8]

# Test 2: One side finishes first
list_a = [1, 2, 3]
list_b = [10, 20, 30]
print(merge_lists(list_a, list_b))
# Expected: [1, 2, 3, 10, 20, 30]

# Test 3: Different lengths, values interleave
list_a = [1, 2, 9]
list_b = [3, 5, 7]
print(merge_lists(list_a, list_b))
# Expected: [1, 2, 3, 5, 7, 9]

# Test 4: One empty list
list_a = []
list_b = [1, 2, 3]
print(merge_lists(list_a, list_b))
# Expected: [1, 2, 3]

# Test 5: Duplicate values
list_a = [1, 3, 3, 5]
list_b = [2, 3, 4]
print(merge_lists(list_a, list_b))
# Expected: [1, 2, 3, 3, 3, 4, 5]

# Test 6: Originals unchanged
list_a = [1, 3, 5]
list_b = [2, 4, 6]
result = merge_lists(list_a, list_b)
print(list_a)   # Expected: [1, 3, 5]  ← must not change!
print(list_b)   # Expected: [2, 4, 6]  ← must not change!
```

## 🌟 Bonus Challenges

Finished the main task? Take it further — one tier at a time!

---

### 🥉 Easy: `merge_three(list_a, list_b, list_c)`

Merge three sorted lists into one. Reuse `merge_lists()` **twice** — no new merge logic needed!

```python
list_a = [1, 4, 7]
list_b = [2, 5, 8]
list_c = [3, 6, 9]

merge_three(list_a, list_b, list_c)
→ [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

Hint: think of it like `merge_lists(merge_lists(list_a, list_b), list_c)`!

---

### 🥈 Medium: `merge_unique(list_a, list_b)`

Merge two sorted lists but include **each value only once**, even if it appears in both.
No `sort()` / `sorted()` allowed!

```python
list_a = [1, 2, 3, 5]
list_b = [2, 3, 4, 5, 6]

merge_unique(list_a, list_b)
→ [1, 2, 3, 4, 5, 6]
```

Hint: Build on the `merge_lists` logic, but before appending, check if the value is already the last item in result. If it is, skip it!

---

### 🥇 Hard: `merge_all(lists)`

Write a function that takes a **list of sorted lists** and merges them all into one.
It must work no matter how many lists are passed in.

```python
all_lists = [[1, 5, 9], [2, 6], [3, 7, 10], [4, 8]]

merge_all(all_lists)
→ [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

Constraints:
• Reuse `merge_lists()`
• Return `[]` if `lists` is empty
• Handle empty sublists gracefully

Hint: loop through the lists and keep merging into a running result one by one!

## 🤔 Think About It

1. Why does it matter that both input lists are **already sorted**? Would this approach work on unsorted lists?
2. After the `while` loop ends, why do we need to handle the leftover items separately?
3. What happens when the two lists have very different lengths (e.g., 1 item vs 1000 items)? Does this approach still work well?

Drop questions in the thread if you get stuck! The goal is understanding, not just finishing. One step at a time! 💪

Good luck! 🚀
