# 🐍 Python 연습: 속도 비교 실험실!

여러분, 안녕하세요! 이번엔 진짜 데이터 분석가처럼 **코드의 속도를 측정하는 실험**을 해봅니다.

## 🎯 미션

여러분은 데이터 분석 회사에 신입으로 입사했습니다. 첫날, 선임 개발자가 이렇게 말합니다:

> "우리는 매일 수백만 개의 숫자를 더해야 해. 그런데 후배가 직접 `for` 루프로 더하고 있더라고. Python에는 `sum()`이라는 내장 함수가 있는데, 어느 게 정말 더 빠른지 **측정해서 증명**해줄래? 추측 말고 데이터로!"

여러분의 임무는 두 가지 방식으로 합계를 구하고, 각각의 실행 시간을 측정해서 **어느 쪽이 얼마나 더 빠른지** 보고하는 것입니다.

## 📋 규칙

*주어지는 것:*
- `time` 모듈 (이미 배웠죠!)
- `sum()` 내장 함수
- `for` 루프와 `range()`
- 5,000,000개의 숫자 리스트 (`list(range(5_000_000))`로 생성)

*해야 할 일:*
1. `for` 루프로 합계를 구하는 함수 작성
2. `sum()` 내장 함수로 합계를 구하는 함수 작성
3. 함수의 실행 시간을 측정하는 도구 함수 작성
4. 두 방식을 실제로 실행하고 결과 비교 보고

*반드시 따라야 할 제약사항:*
- 두 합계 함수는 **반드시 같은 결과**를 반환해야 함 (검증 필수!)
- `time.time()`만 사용 (다른 측정 도구 금지)
- 실행 시간은 소수점 넷째 자리까지 표시 (예: `0.1234초`)
- 두 함수의 속도 비율을 계산 (예: "3.5배 빠름")

## 💡 예제

**실행 예시:**
```
=== 속도 비교 실험 시작 ===
데이터 준비 중... (5,000,000개의 숫자)

[방법 1] for 루프로 합계
  결과: 12499997500000
  실행 시간: 0.1843초

[방법 2] sum() 내장 함수
  결과: 12499997500000
  실행 시간: 0.0421초

✅ 두 결과가 같음을 확인!

🏆 우승: sum() 내장 함수
   sum()이 for 루프보다 약 4.4배 빠름!
```

## 🎓 알아야 할 것

코딩을 시작하기 전에, 다음을 이해하고 있는지 확인하세요:
- `import time`으로 `time` 모듈 가져오기
- `time.time()`이 현재 시각을 초 단위 숫자로 반환한다는 점
- `for` 루프로 리스트의 모든 원소를 순회하는 방법
- `sum(리스트)` 내장 함수로 합계 구하는 방법
- `list(range(n))`으로 큰 숫자 리스트 만드는 방법
- f-string으로 숫자 형식 지정 (예: `f"{x:.4f}"`)

> 💡 **새로운 개념 미리보기**: 이 연습에서는 **"함수를 다른 함수의 인자로 전달"** 하는 패턴이 나옵니다. 어렵지 않아요 — 함수 이름 뒤에 `()`를 안 붙이면, 함수 자체를 변수처럼 넘길 수 있습니다. 예: `measure_function_time(sum, numbers)` ← `sum` 뒤에 `()`가 없는 점 주목!

## ✅ 과제

네 개의 함수를 작성하세요:

```python
def sum_with_loop(numbers: list[int]) -> int:
    """for 루프를 사용해서 합계를 반환"""
    pass

def sum_with_builtin(numbers: list[int]) -> int:
    """sum() 내장 함수를 사용해서 합계를 반환"""
    pass

def measure_function_time(func, numbers: list[int]) -> tuple:
    """함수와 데이터를 받아서 (결과, 실행시간)을 반환"""
    pass

def run_speed_lab() -> None:
    """전체 실험을 실행하고 결과를 보고"""
    pass
```

**시작하는 데 도움이 될 팁:**
- `sum_with_loop`은 `total = 0`으로 시작해서 누적
- `sum_with_builtin`은 한 줄이면 끝! (`return sum(numbers)`)
- `measure_function_time` 안에서 `func(numbers)`를 호출하면 전달받은 함수가 실행됨
- 두 결과가 같은지 `==`로 검증한 후에 시간을 비교하기

## 🎪 코드 테스트

함수들을 다음과 같이 테스트해보세요:

```python
# 테스트 1: 작은 데이터로 정확성 확인
small_numbers = [1, 2, 3, 4, 5]
print(sum_with_loop(small_numbers))     # 예상: 15
print(sum_with_builtin(small_numbers))  # 예상: 15

# 테스트 2: 빈 리스트와 음수
print(sum_with_loop([]))         # 예상: 0
print(sum_with_loop([-5, 5]))    # 예상: 0
print(sum_with_loop([-1, -2, -3]))  # 예상: -6

# 테스트 3: 시간 측정 도구
result, elapsed = measure_function_time(sum_with_builtin, [1, 2, 3])
print(f"결과: {result}, 시간: {elapsed:.6f}초")

# 테스트 4: 전체 실험 실행
run_speed_lab()
```

## 🤔 생각해보기

코딩을 시작하기 전에, 다음을 생각해보세요:
1. 왜 두 방식이 같은 결과를 내는지 미리 검증해야 할까요? (만약 결과가 다르다면 속도 비교가 의미 없겠죠?)
2. `sum()`은 왜 더 빠를까요? 힌트: Python으로 작성된 게 아니라 **C 언어**로 작성되어 있어요!
3. 만약 데이터 크기가 100개뿐이라면, 차이가 보일까요? 1억 개라면?
4. 실험을 한 번만 실행하면 결과를 믿을 수 있을까요? 여러 번 실행하면 어떨까요? (보너스 챌린지에서 다룹니다!)

> 📝 **이 실험에서 배우는 교훈**:
> *"추측하지 말고, 측정하라." — 모든 성능 최적화의 첫 번째 규칙*
> *"Don't guess, measure." — The first rule of all performance optimization*

막히면 스레드에 질문을 남겨주세요! 목표는 끝내는 것이 아니라 배우는 것입니다.

행운을 빕니다! 🚀

---
---

# 🐍 Python Practice: Speed Comparison Lab!

Hey team! This time, you'll work like a real data analyst — running **experiments to measure code speed**.

## 🎯 Your Mission

You just joined a data analysis company as a new hire. On day one, a senior developer says:

> "We sum millions of numbers every day. But I noticed a junior is using a `for` loop to do it. Python has a built-in `sum()` function — can you **measure and prove** which one is actually faster? With data, not guesses!"

Your task: implement the sum two different ways, measure each one's execution time, and report **which is faster and by how much**.

## 📋 The Rules

*What you're given:*
- The `time` module (you've learned this!)
- The `sum()` built-in function
- `for` loops and `range()`
- A list of 5,000,000 numbers (created with `list(range(5_000_000))`)

*What you need to do:*
1. Write a function that sums using a `for` loop
2. Write a function that sums using the `sum()` built-in
3. Write a helper function that measures any function's execution time
4. Actually run both and report the comparison

*Constraints you must follow:*
- Both sum functions **must return the same result** (verify it!)
- Use only `time.time()` (no other timing tools)
- Display elapsed time to 4 decimal places (e.g., `0.1234 seconds`)
- Calculate the speed ratio (e.g., "3.5x faster")

## 💡 Example Time

**Sample run:**
```
=== Speed Comparison Lab ===
Preparing data... (5,000,000 numbers)

[Method 1] for-loop sum
  Result: 12499997500000
  Elapsed: 0.1843 seconds

[Method 2] sum() built-in
  Result: 12499997500000
  Elapsed: 0.0421 seconds

✅ Both results match!

🏆 Winner: sum() built-in
   sum() is about 4.4x faster than the for loop!
```

## 🎓 What You Should Know

Before you start coding, make sure you understand:
- How to import the `time` module
- That `time.time()` returns the current time as a number (seconds)
- How to iterate over a list with a `for` loop
- How to use `sum(list)` to get a total
- That `list(range(n))` creates a list of n numbers
- f-string number formatting (e.g., `f"{x:.4f}"`)

> 💡 **New concept preview:** This exercise introduces the pattern of **"passing a function as an argument to another function."** It's not hard — if you write a function name **without** the `()`, you pass the function itself like a variable. Example: `measure_function_time(sum, numbers)` ← notice no `()` after `sum`!

## ✅ Your Task

Write four functions:

```python
def sum_with_loop(numbers: list[int]) -> int:
    """Return the sum using a for loop"""
    pass

def sum_with_builtin(numbers: list[int]) -> int:
    """Return the sum using the sum() built-in"""
    pass

def measure_function_time(func, numbers: list[int]) -> tuple:
    """Take a function and data, return (result, elapsed_time)"""
    pass

def run_speed_lab() -> None:
    """Run the full experiment and report results"""
    pass
```

**Tips to get you started:**
- For `sum_with_loop`, start with `total = 0` and accumulate
- `sum_with_builtin` is a one-liner: `return sum(numbers)`
- Inside `measure_function_time`, calling `func(numbers)` runs whatever function was passed in
- Verify both results match with `==` BEFORE comparing speeds

## 🎪 Test Your Code

Test your functions like this:

```python
# Test 1: Small data for correctness
small_numbers = [1, 2, 3, 4, 5]
print(sum_with_loop(small_numbers))     # Expected: 15
print(sum_with_builtin(small_numbers))  # Expected: 15

# Test 2: Empty list and negatives
print(sum_with_loop([]))         # Expected: 0
print(sum_with_loop([-5, 5]))    # Expected: 0
print(sum_with_loop([-1, -2, -3]))  # Expected: -6

# Test 3: Timer tool
result, elapsed = measure_function_time(sum_with_builtin, [1, 2, 3])
print(f"Result: {result}, Time: {elapsed:.6f}s")

# Test 4: Full experiment
run_speed_lab()
```

## 🤔 Think About It

Before you start coding, think about these:
1. Why must we verify both methods give the same result first? (If results differ, the speed comparison is meaningless, right?)
2. Why is `sum()` faster? Hint: it's not written in Python — it's written in **C**!
3. Would the difference be visible with only 100 numbers? What about 100 million?
4. Can we trust the result from a single run? What if we ran it multiple times? (Bonus challenge!)

> 📝 **The lesson from this experiment:**
> *"Don't guess, measure." — The first rule of all performance optimization*

Drop your questions in the thread if you get stuck! Remember, the goal is to learn, not just to finish.

Good luck! 🚀
