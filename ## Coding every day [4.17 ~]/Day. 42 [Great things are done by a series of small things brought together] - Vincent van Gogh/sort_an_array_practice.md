# 🐍 Python 연습: 배열 정렬하기!

여러분, 안녕하세요! 오늘은 컴퓨터 과학의 가장 유명한 문제 중 하나에 도전합니다 — **정렬(sorting)**!

## 🎯 미션

여러분은 음악 스트리밍 스타트업의 인턴이 되었습니다. 사용자들이 플레이리스트의 곡 길이를 짧은 순서대로 보고 싶다고 요청했어요. 하지만 한 가지 함정이 있습니다 — 매니저가 `sorted()`나 `.sort()` 같은 내장 함수를 사용하지 말라고 했어요. 정렬이 어떻게 동작하는지 직접 이해해야 한다는 거죠!

정수가 들어있는 리스트를 받아서, **오름차순**으로 정렬된 리스트를 반환하는 함수를 작성해야 합니다.

## 📋 규칙

**주어지는 것:**
- `nums`라는 정수 리스트 (정렬되어 있지 않음)
- 리스트에는 음수, 0, 양수가 모두 들어갈 수 있음
- 중복된 값이 있을 수 있음

**해야 할 일:**
1. 리스트를 오름차순(작은 값 → 큰 값)으로 정렬
2. 정렬된 리스트를 반환

**반드시 따라야 할 제약사항:**
- ❌ `sorted()`, `nums.sort()` 같은 내장 정렬 함수 사용 **금지**
- ❌ `min()`, `max()` 사용 **금지** (직접 비교해야 합니다)
- ✅ 중첩 반복문(nested loops)과 변수 교환(swapping)만 사용
- ✅ 직접 비교하고, 직접 위치를 바꿔야 합니다

## 💡 예제

**예제 1:**
```
입력: nums = [5, 2, 3, 1]
출력: [1, 2, 3, 5]
```

**예제 2:**
```
입력: nums = [5, 1, 1, 2, 0, 0]
출력: [0, 0, 1, 1, 2, 5]
```
> 값이 중복되어도 괜찮습니다 — 그대로 정렬된 위치에 두면 돼요.

**예제 3:**
```
입력: nums = [-3, -1, -2]
출력: [-3, -2, -1]
```
> 음수도 처리할 수 있어야 합니다!

## 🎓 알아야 할 것

코딩을 시작하기 전에, 다음을 이해하고 있는지 확인하세요:
- `for` 반복문과 `range()`를 사용하는 방법
- 중첩 반복문(반복문 안의 반복문)
- `if`로 두 값을 비교하는 방법
- Python의 변수 교환: `a, b = b, a`
- 리스트 인덱싱(`nums[i]`)과 `len()`

## ✅ 과제

다음 시그니처로 함수를 작성하세요:

```python
def sort_array(nums: list[int]) -> list[int]:
    # 여기에 코드 작성
    pass
```

**힌트 (선택 정렬, Selection Sort 접근법):**
- 리스트의 가장 앞부터 시작합니다
- 나머지 부분에서 **가장 작은 값의 인덱스**를 찾습니다
- 그 값을 현재 위치와 교환합니다
- 다음 위치로 이동해서 같은 작업을 반복합니다
- 끝까지 가면 정렬이 완료됩니다!

## 📊 함수 명세

| 항목 | 설명 |
|------|------|
| 함수 이름 | `sort_array` |
| 매개변수 | `nums: list[int]` — 정렬할 정수 리스트 |
| 반환값 | `list[int]` — 오름차순으로 정렬된 리스트 |
| 부작용 | 원본 리스트를 직접 수정해도 됨 (in-place) |

## 🎪 코드 테스트

다음 테스트 케이스를 실행해보세요:

```python
# 테스트 1: 기본 케이스
print(sort_array([5, 2, 3, 1]))
# 예상: [1, 2, 3, 5]

# 테스트 2: 중복이 있는 경우
print(sort_array([5, 1, 1, 2, 0, 0]))
# 예상: [0, 0, 1, 1, 2, 5]

# 테스트 3: 요소가 하나뿐인 경우 (경계값)
print(sort_array([1]))
# 예상: [1]

# 테스트 4: 이미 정렬된 경우
print(sort_array([1, 2, 3, 4, 5]))
# 예상: [1, 2, 3, 4, 5]

# 테스트 5: 역순으로 정렬된 경우
print(sort_array([5, 4, 3, 2, 1]))
# 예상: [1, 2, 3, 4, 5]

# 테스트 6: 음수가 섞인 경우
print(sort_array([-5, 3, -1, 0, 2]))
# 예상: [-5, -1, 0, 2, 3]
```

## 🤔 생각해보기

코딩을 시작하기 전에, 접근 방법을 스케치해보세요:

1. 어떤 인덱스부터 어떤 인덱스까지 "정렬되지 않은 부분"인지 어떻게 추적할까요?
2. 가장 작은 값을 찾을 때, **값** 자체를 저장해야 할까요, 아니면 **인덱스**를 저장해야 할까요? 왜 그럴까요?
3. 두 위치의 값을 바꿀 때, 임시 변수가 필요할까요? Python에서는 어떻게 더 간단하게 할 수 있을까요?
4. 리스트의 길이가 `n`일 때, 바깥쪽 반복문은 몇 번 돌아야 할까요?

막히면 스레드에 질문을 남겨주세요! 목표는 **끝내는 것이 아니라 배우는 것**입니다.

행운을 빕니다! 🚀

---
---

# 🐍 Python Practice: Sort an Array!

Hey team! Today we're tackling one of the most famous problems in computer science — **sorting**!

## 🎯 Your Mission

You're an intern at a music streaming startup. Users are asking to see the songs in their playlists ordered by length (shortest first). But here's the catch — your manager said no using built-in functions like `sorted()` or `.sort()`. You need to actually understand how sorting works!

Write a function that takes a list of integers and returns the same list sorted in **ascending order**.

## 📋 The Rules

**What you're given:**
- A list called `nums` containing integers (not sorted)
- The list may contain negative numbers, zero, and positive numbers
- Duplicate values may exist

**What you need to do:**
1. Sort the list in ascending order (smallest → largest)
2. Return the sorted list

**Constraints you must follow:**
- ❌ **No** built-in sort functions like `sorted()` or `nums.sort()`
- ❌ **No** `min()` or `max()` (you must compare values yourself)
- ✅ Use only nested loops and variable swapping
- ✅ Do the comparisons and position changes yourself

## 💡 Examples

**Example 1:**
```
Input: nums = [5, 2, 3, 1]
Output: [1, 2, 3, 5]
```

**Example 2:**
```
Input: nums = [5, 1, 1, 2, 0, 0]
Output: [0, 0, 1, 1, 2, 5]
```
> Duplicate values are fine — just leave them in their sorted positions.

**Example 3:**
```
Input: nums = [-3, -1, -2]
Output: [-3, -2, -1]
```
> Your function should handle negative numbers too!

## 🎓 What You Should Know

Before you start coding, make sure you understand:
- How to use `for` loops with `range()`
- Nested loops (a loop inside a loop)
- How to compare two values with `if`
- Python's variable swap: `a, b = b, a`
- List indexing (`nums[i]`) and `len()`

## ✅ Your Task

Write a function with this signature:

```python
def sort_array(nums: list[int]) -> list[int]:
    # Your code here
    pass
```

**Hint (Selection Sort approach):**
- Start at the front of the list
- Find the **index of the smallest value** in the remaining part
- Swap that value with the current position
- Move to the next position and repeat
- When you reach the end, the list is sorted!

## 📊 Function Specification

| Item | Description |
|------|-------------|
| Function name | `sort_array` |
| Parameter | `nums: list[int]` — the list of integers to sort |
| Return value | `list[int]` — the list sorted in ascending order |
| Side effects | You may modify the original list directly (in-place) |

## 🎪 Test Your Code

Try running these test cases:

```python
# Test 1: Basic case
print(sort_array([5, 2, 3, 1]))
# Expected: [1, 2, 3, 5]

# Test 2: With duplicates
print(sort_array([5, 1, 1, 2, 0, 0]))
# Expected: [0, 0, 1, 1, 2, 5]

# Test 3: Single element (boundary)
print(sort_array([1]))
# Expected: [1]

# Test 4: Already sorted
print(sort_array([1, 2, 3, 4, 5]))
# Expected: [1, 2, 3, 4, 5]

# Test 5: Reverse sorted
print(sort_array([5, 4, 3, 2, 1]))
# Expected: [1, 2, 3, 4, 5]

# Test 6: Negative numbers mixed in
print(sort_array([-5, 3, -1, 0, 2]))
# Expected: [-5, -1, 0, 2, 3]
```

## 🤔 Think About It

Before you start coding, sketch out your approach:

1. How will you keep track of which part of the list is the "unsorted part"?
2. When finding the smallest value, should you store the **value itself** or the **index**? Why?
3. When you swap two positions, do you need a temporary variable? How can Python make it simpler?
4. If the list has length `n`, how many times should the outer loop run?

Drop your questions in the thread if you get stuck! Remember, the goal is **to learn, not just to finish**.

Good luck! 🚀
