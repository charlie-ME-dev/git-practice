# 🐍 Python 연습: 최고 평균 구간 찾기!

여러분, 안녕하세요! 오늘은 데이터 분석에서 자주 쓰이는 **슬라이딩 윈도우(sliding window)** 패턴을 만나볼 거예요.

## 🎯 미션

여러분은 한 스타트업의 데이터 분석 인턴입니다. 회사가 최근 30일간의 일일 매출 데이터를 가지고 있고, 마케팅 팀이 이렇게 물어봅니다:

> "연속된 7일 동안 평균 매출이 가장 높았던 기간은 언제인가요? 그 평균값을 알려주세요!"

이런 질문에 답하는 함수를 작성하는 것이 오늘의 미션입니다. 정수 리스트 `nums`와 정수 `k`가 주어졌을 때, **길이가 정확히 `k`인 연속된 부분 리스트** 중 **평균값이 가장 큰** 것을 찾아 그 평균을 반환하세요.

## 📋 규칙

*주어지는 것:*
- 정수 리스트 `nums` (음수 포함 가능)
- 정수 `k` (윈도우의 크기, `1 <= k <= len(nums)`)

*해야 할 일:*
1. 길이가 `k`인 모든 연속된 부분 리스트를 살펴봅니다
2. 그중 평균이 가장 큰 부분 리스트를 찾습니다
3. 그 **평균값**(부분 리스트가 아니라!)을 반환합니다

*제약사항:*
- 반환값은 `float` 타입이어야 합니다
- 부분 리스트는 반드시 **연속**되어야 합니다 (건너뛰기 금지!)
- `nums`에는 음수가 포함될 수 있으니 조심하세요

## 💡 예제

**예제 1:**
```
입력: nums = [1, 12, -5, -6, 50, 3], k = 4
출력: 12.75
```
왜? 길이 4인 부분 리스트는 다음 세 가지가 있어요:
- `[1, 12, -5, -6]` → 평균 = 2 / 4 = 0.5
- `[12, -5, -6, 50]` → 평균 = 51 / 4 = **12.75** ✨
- `[-5, -6, 50, 3]` → 평균 = 42 / 4 = 10.5

**예제 2:**
```
입력: nums = [5], k = 1
출력: 5.0
```
왜? 부분 리스트가 `[5]` 하나뿐이고, 평균은 5.0입니다.

**예제 3 (음수 주의!):**
```
입력: nums = [-1, -2, -3, -4, -5], k = 2
출력: -1.5
```
왜? 가장 "덜 음수"인 평균이 답입니다. `[-1, -2]`의 평균이 -1.5로 가장 큽니다.

## 🎓 알아야 할 것

코딩을 시작하기 전에, 다음을 이해하고 있는지 확인하세요:
- 리스트 슬라이싱 (`nums[i:j]`)
- 내장 함수 `sum()`, `max()`, `len()`
- `for` 반복문과 `range()`
- 정수 나눗셈 vs 실수 나눗셈 (`/`는 항상 `float` 반환)
- 음수 비교 (예: `-1 > -10`이 `True`)

## ✅ 과제

다음 시그니처로 함수를 작성하세요:

```python
def find_max_average(nums: list[int], k: int) -> float:
    # 여기에 코드 작성
    pass
```

**시작하는 데 도움이 될 팁:**
- 가장 단순한 방법: 모든 길이 `k` 부분 리스트의 합을 따로따로 구해서 비교
- 더 똑똑한 방법: **슬라이딩 윈도우**! 윈도우를 한 칸씩 옮길 때, 들어오는 값을 더하고 나가는 값을 빼면 합을 다시 계산할 필요가 없어요
- 윈도우의 첫 합은 `sum(nums[:k])`로 시작
- "현재 최댓값"을 추적할 변수를 하나 두세요

## 🎪 코드 테스트

다음 테스트 케이스로 확인해보세요:

| 테스트 | 입력 | 예상 출력 |
|--------|------|-----------|
| 기본 | `nums=[1, 12, -5, -6, 50, 3], k=4` | `12.75` |
| 단일 원소 | `nums=[5], k=1` | `5.0` |
| 모두 음수 | `nums=[-1, -2, -3, -4, -5], k=2` | `-1.5` |
| `k`가 전체 길이 | `nums=[1, 2, 3, 4, 5], k=5` | `3.0` |
| 모두 같은 값 | `nums=[1, 1, 1, 1, 1], k=3` | `1.0` |
| `k=1` (개별 원소) | `nums=[10, -10, 10, -10, 10], k=1` | `10.0` |

## 🤔 생각해보기

코딩을 시작하기 전에, 접근 방법을 스케치해보세요:
1. 평균을 비교하는 것과 합을 비교하는 것은 같은 결과를 줄까요? (왜?)
2. 윈도우를 오른쪽으로 한 칸 옮길 때, 새 합과 이전 합의 차이는 무엇인가요?
3. 첫 번째 윈도우의 합을 어떻게 초기화할까요?
4. 음수가 있을 때 `max_sum`을 `0`으로 초기화하면 어떤 문제가 생길까요?

막히면 스레드에 질문을 남겨주세요! 목표는 끝내는 것이 아니라 패턴을 익히는 것입니다.

행운을 빕니다! 🚀

---
---

# 🐍 Python Practice: Find the Highest-Average Window!

Hey team! Today we're meeting one of the most useful patterns in data analysis: the **sliding window**.

## 🎯 Your Mission

You're a data analyst intern at a startup. The company has the last 30 days of daily revenue data, and the marketing team asks:

> "Which 7-day stretch had the highest average revenue? Give us that average!"

Your mission is to write a function that answers this kind of question. Given a list of integers `nums` and an integer `k`, find the **contiguous subarray of length exactly `k`** with the **largest average value**, and return that average.

## 📋 The Rules

*What you're given:*
- An integer list `nums` (may contain negatives)
- An integer `k` (the window size, `1 <= k <= len(nums)`)

*What you need to do:*
1. Look at every contiguous subarray of length `k`
2. Find the one with the largest average
3. Return that **average** (not the subarray itself!)

*Constraints:*
- The return value must be a `float`
- The subarray must be **contiguous** (no skipping elements!)
- `nums` may contain negatives, so be careful

## 💡 Example Time

**Example 1:**
```
Input: nums = [1, 12, -5, -6, 50, 3], k = 4
Output: 12.75
```
Why? There are three subarrays of length 4:
- `[1, 12, -5, -6]` → average = 2 / 4 = 0.5
- `[12, -5, -6, 50]` → average = 51 / 4 = **12.75** ✨
- `[-5, -6, 50, 3]` → average = 42 / 4 = 10.5

**Example 2:**
```
Input: nums = [5], k = 1
Output: 5.0
```
Why? There's only one subarray, `[5]`, and its average is 5.0.

**Example 3 (watch out for negatives!):**
```
Input: nums = [-1, -2, -3, -4, -5], k = 2
Output: -1.5
```
Why? The "least negative" average wins. `[-1, -2]` has the largest average at -1.5.

## 🎓 What You Should Know

Before you start coding, make sure you understand:
- List slicing (`nums[i:j]`)
- Built-in functions `sum()`, `max()`, `len()`
- `for` loops with `range()`
- Integer vs float division (`/` always returns a `float`)
- Comparing negative numbers (e.g., `-1 > -10` is `True`)

## ✅ Your Task

Write a function with this signature:

```python
def find_max_average(nums: list[int], k: int) -> float:
    # Your code here
    pass
```

**Tips to get you started:**
- Simplest approach: compute the sum of every length-`k` subarray separately, then compare
- Smarter approach: **sliding window**! When the window moves one step right, just add the new element and subtract the one that left — no need to recompute the whole sum
- Initialize the first window's sum with `sum(nums[:k])`
- Keep one variable to track the "best so far"

## 🎪 Test Your Code

Try these test cases:

| Test | Input | Expected Output |
|------|-------|-----------------|
| Basic | `nums=[1, 12, -5, -6, 50, 3], k=4` | `12.75` |
| Single element | `nums=[5], k=1` | `5.0` |
| All negative | `nums=[-1, -2, -3, -4, -5], k=2` | `-1.5` |
| `k` equals full length | `nums=[1, 2, 3, 4, 5], k=5` | `3.0` |
| All same values | `nums=[1, 1, 1, 1, 1], k=3` | `1.0` |
| `k=1` (each element) | `nums=[10, -10, 10, -10, 10], k=1` | `10.0` |

## 🤔 Think About It

Before you start coding, sketch out your approach:
1. Does comparing averages give the same result as comparing sums? (Why?)
2. When you slide the window one step right, what's the difference between the new sum and the previous sum?
3. How do you initialize the first window's sum?
4. If `nums` has negatives, what could go wrong if you initialize `max_sum` to `0`?

Drop questions in the thread if you get stuck! The goal isn't to finish — it's to internalize the pattern.

Good luck! 🚀
