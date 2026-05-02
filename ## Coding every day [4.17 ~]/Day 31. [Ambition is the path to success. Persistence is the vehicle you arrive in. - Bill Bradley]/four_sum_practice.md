# 🕵️ Python 연습: 수상한 거래 조합 찾기!

여러분, 안녕하세요! 핀테크 스타트업 신입 개발자로서 진짜 문제를 풀어볼 시간이에요.

## 🎯 미션

여러분은 사기 탐지팀의 주니어 개발자입니다. 시니어 분석가가 이렇게 말합니다:

> "오늘 거래 내역에서 **정확히 4건의 거래 금액을 합쳐서** 특정 목표 금액이 나오는 조합을 모두 찾아줘. 돈세탁 패턴일 수 있어!"

거래 금액 리스트와 목표 금액이 주어지면, **합이 정확히 목표 금액이 되는 4개 숫자의 모든 고유한 조합**을 찾아야 합니다.

**중요:** 같은 조합을 두 번 반환하면 안 됩니다! `[1, 2, 3, 4]`와 `[4, 3, 2, 1]`은 같은 조합이에요.

## 📋 규칙

*주어지는 것:*
• `nums`: 정수 리스트 (거래 금액, 음수도 가능 — 환불 거래!)
• `target`: 목표 합계 (정수)

*해야 할 일:*
1. 합이 정확히 `target`이 되는 4개 숫자의 조합을 모두 찾기
2. 각 조합은 **오름차순으로 정렬된 리스트**로 표현
3. 결과 리스트에 **중복된 조합이 없어야 함**
4. 모든 조합을 담은 리스트를 반환

*반드시 따라야 할 제약사항:*
• **`set` 사용 금지** (아직 안 배웠어요!)
• **`itertools` 사용 금지** (아직 안 배웠어요!)
• **`tuple` 사용 금지** (아직 안 배웠어요!)
• 4개의 숫자는 서로 **다른 인덱스**에서 가져와야 함 (값은 같을 수 있음)
• 정렬, 중첩 반복문, while문, `.append()`만 사용하세요

## 💡 예제

**예제 1:**
```
입력: nums = [1, 0, -1, 0, -2, 2], target = 0
출력: [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
```
왜? 합이 0이 되는 4개 숫자의 조합이 3가지 있습니다.
• -2 + -1 + 1 + 2 = 0 ✅
• -2 + 0 + 0 + 2 = 0 ✅ (0이 두 개 있어서 가능!)
• -1 + 0 + 0 + 1 = 0 ✅

**예제 2:**
```
입력: nums = [2, 2, 2, 2, 2], target = 8
출력: [[2, 2, 2, 2]]
```
왜? 2가 다섯 개지만, 4개를 뽑는 방법은 값으로 보면 한 가지뿐입니다 (모두 2).

**예제 3:**
```
입력: nums = [1, 2, 3, 4], target = 100
출력: []
```
왜? 합이 100이 되는 조합이 없으므로 빈 리스트를 반환합니다.

## 🎓 알아야 할 것

코딩을 시작하기 전에, 다음을 이해하고 있는지 확인하세요:
• `list.sort()`로 리스트를 정렬하는 방법
• 중첩된 `for` 반복문 작성 방법
• `while` 반복문과 조건 업데이트
• `list.append()`로 리스트에 값 추가하는 방법
• 인덱스로 리스트 요소에 접근하는 방법

## ✅ 과제

다음 시그니처로 함수를 작성하세요:
```python
def four_sum(nums: list[int], target: int) -> list[list[int]]:
    # 여기에 코드 작성
    pass
```

**🧠 핵심 아이디어 (이대로 따라오세요!):**

1. **먼저 리스트를 정렬하세요.** 이게 전부의 핵심입니다!
2. 바깥쪽 `for` 반복문으로 **첫 번째 숫자** `nums[i]` 선택
3. 그 안쪽 `for` 반복문으로 **두 번째 숫자** `nums[j]` 선택 (단, `j > i`)
4. 이제 **투 포인터** 사용: `left = j + 1`, `right = n - 1`
5. 나머지 두 숫자를 `while left < right`로 찾기:
   • 합 = `nums[i] + nums[j] + nums[left] + nums[right]`
   • 합 == target → 결과에 추가, 양쪽 포인터 이동
   • 합 < target → `left` 증가 (더 큰 수 필요)
   • 합 > target → `right` 감소 (더 작은 수 필요)

**🚨 중복 제거 트릭 (매우 중요!):**

정렬된 리스트에서 중복 조합을 피하는 방법:
• **같은 값을 두 번 선택하지 마세요.** 예: `nums = [1, 1, 2, 2]`에서 `i=0`(값 1)로 한 번 찾았으면, `i=1`(또 값 1)은 건너뛰기
• 패턴: `if i > 0 and nums[i] == nums[i-1]: continue`
• `j`, `left`, `right`에도 같은 트릭을 적용해야 합니다!

## 🎪 코드 테스트

다음 테스트 케이스를 실행해보세요:

```python
# 테스트 1: 기본 케이스
nums1 = [1, 0, -1, 0, -2, 2]
print(four_sum(nums1, 0))
# 예상: [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]

# 테스트 2: 모두 같은 값
nums2 = [2, 2, 2, 2, 2]
print(four_sum(nums2, 8))
# 예상: [[2, 2, 2, 2]]

# 테스트 3: 답이 없음
nums3 = [1, 2, 3, 4]
print(four_sum(nums3, 100))
# 예상: []

# 테스트 4: 모두 0
nums4 = [0, 0, 0, 0]
print(four_sum(nums4, 0))
# 예상: [[0, 0, 0, 0]]

# 테스트 5: 요소가 4개 미만
nums5 = [1, 2, 3]
print(four_sum(nums5, 6))
# 예상: []

# 테스트 6: 빈 리스트
nums6 = []
print(four_sum(nums6, 0))
# 예상: []
```

## 🤔 생각해보기

코딩을 시작하기 전에, 접근 방법을 스케치해보세요:
1. 왜 리스트를 **먼저 정렬**해야 할까요?
2. 투 포인터가 왜 작동할까요? (합이 너무 작으면 왜 left를 증가시킬까요?)
3. 중복을 건너뛰는 `continue` 문이 없으면 어떤 조합이 중복으로 나올까요?

## 🌶️ 보너스 도전 (선택)

**🟢 쉬움:** 찾은 조합의 **개수**만 반환하는 `count_four_sum(nums, target)` 함수를 작성하세요.

**🟡 보통:** `target`에 가장 **가까운** 4개 숫자의 합을 반환하는 `closest_four_sum(nums, target)` 함수를 작성하세요.

**🔴 어려움:** `k_sum(nums, target, k)` 함수를 작성하세요 — `k`개의 숫자로 일반화! (힌트: 재귀는 아직이니, `k=3`, `k=5` 버전을 분리해서 작성해도 OK)

막히면 스레드에 질문을 남겨주세요! 목표는 끝내는 것이 아니라 **왜** 작동하는지 이해하는 것입니다.

행운을 빕니다! 🚀

---
---

# 🕵️ Python Practice: Find Suspicious Transaction Combos!

Hey team! Time to solve a real problem as a junior developer at a FinTech startup.

## 🎯 Your Mission

You're a junior developer on the fraud detection team. Your senior analyst tells you:

> "Find me every combination of **exactly 4 transaction amounts** from today's log that sum to a specific target. Could be a money laundering pattern!"

Given a list of transaction amounts and a target amount, find **all unique combinations of 4 numbers whose sum equals the target**.

**Important:** Don't return the same combination twice! `[1, 2, 3, 4]` and `[4, 3, 2, 1]` are the same combination.

## 📋 The Rules

*What you're given:*
• `nums`: a list of integers (transaction amounts, negatives allowed — refunds!)
• `target`: the target sum (integer)

*What you need to do:*
1. Find all combinations of 4 numbers whose sum is exactly `target`
2. Each combination should be a **list in ascending order**
3. The result list must have **no duplicate combinations**
4. Return a list containing all combinations

*Constraints you must follow:*
• **No `set`** (you haven't learned it yet!)
• **No `itertools`** (you haven't learned it yet!)
• **No `tuple`** (you haven't learned it yet!)
• The 4 numbers must come from **different indices** (values may repeat)
• Use only sorting, nested loops, while loops, and `.append()`

## 💡 Example Time

**Example 1:**
```
Input: nums = [1, 0, -1, 0, -2, 2], target = 0
Output: [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
```
Why? There are 3 combinations summing to 0:
• -2 + -1 + 1 + 2 = 0 ✅
• -2 + 0 + 0 + 2 = 0 ✅ (works because there are two 0s!)
• -1 + 0 + 0 + 1 = 0 ✅

**Example 2:**
```
Input: nums = [2, 2, 2, 2, 2], target = 8
Output: [[2, 2, 2, 2]]
```
Why? Five 2s, but only one value-wise combination of four (all 2s).

**Example 3:**
```
Input: nums = [1, 2, 3, 4], target = 100
Output: []
```
Why? No combination sums to 100, so return an empty list.

## 🎓 What You Should Know

Before you start coding, make sure you understand:
• How to sort a list with `list.sort()`
• How to write nested `for` loops
• `while` loops and updating conditions
• How to add values to a list with `list.append()`
• How to access list elements by index

## ✅ Your Task

Write a function with this signature:
```python
def four_sum(nums: list[int], target: int) -> list[list[int]]:
    # Your code here
    pass
```

**🧠 Core Idea (follow this blueprint!):**

1. **Sort the list first.** This is the KEY to everything!
2. Outer `for` loop picks the **first number** `nums[i]`
3. Inner `for` loop picks the **second number** `nums[j]` (with `j > i`)
4. Now use **two pointers**: `left = j + 1`, `right = n - 1`
5. Find the remaining two numbers with `while left < right`:
   • sum = `nums[i] + nums[j] + nums[left] + nums[right]`
   • sum == target → append to result, move both pointers
   • sum < target → increment `left` (need bigger numbers)
   • sum > target → decrement `right` (need smaller numbers)

**🚨 Duplicate-Skipping Trick (VERY IMPORTANT!):**

How to avoid duplicate combinations in a sorted list:
• **Don't pick the same value twice in a row.** Example: in `nums = [1, 1, 2, 2]`, if you already used `i=0` (value 1), skip `i=1` (value 1 again)
• Pattern: `if i > 0 and nums[i] == nums[i-1]: continue`
• Apply the same trick for `j`, `left`, and `right`!

## 🎪 Test Your Code

Try running these test cases:

```python
# Test 1: basic case
nums1 = [1, 0, -1, 0, -2, 2]
print(four_sum(nums1, 0))
# Expected: [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]

# Test 2: all same value
nums2 = [2, 2, 2, 2, 2]
print(four_sum(nums2, 8))
# Expected: [[2, 2, 2, 2]]

# Test 3: no solution
nums3 = [1, 2, 3, 4]
print(four_sum(nums3, 100))
# Expected: []

# Test 4: all zeros
nums4 = [0, 0, 0, 0]
print(four_sum(nums4, 0))
# Expected: [[0, 0, 0, 0]]

# Test 5: fewer than 4 elements
nums5 = [1, 2, 3]
print(four_sum(nums5, 6))
# Expected: []

# Test 6: empty list
nums6 = []
print(four_sum(nums6, 0))
# Expected: []
```

## 🤔 Think About It

Before coding, sketch your approach:
1. Why do we need to **sort** the list first?
2. Why do two pointers work? (If the sum is too small, why increment `left`?)
3. Without the `continue` statements, which combinations would appear duplicated?

## 🌶️ Bonus Challenges (Optional)

**🟢 Easy:** Write `count_four_sum(nums, target)` that returns just the **count** of combinations found.

**🟡 Medium:** Write `closest_four_sum(nums, target)` that returns the sum of 4 numbers **closest** to `target`.

**🔴 Hard:** Write `k_sum(nums, target, k)` — generalize to `k` numbers! (Hint: no recursion yet, so you can write separate `k=3`, `k=5` versions)

Drop your questions in the thread if you get stuck! The goal is understanding **why** it works, not just finishing.

Good luck! 🚀
