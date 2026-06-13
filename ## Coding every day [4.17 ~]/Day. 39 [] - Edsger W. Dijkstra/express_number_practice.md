# 🐍 Python 연습: 숫자를 연속된 수의 합으로 표현하기!

여러분, 안녕하세요! 오늘은 수학과 코딩이 만나는 재미있는 챌린지입니다.

## 🎯 미션

여러분은 사내 회계팀의 인턴입니다. 팀장님이 흥미로운 부탁을 하셨어요: "**N원짜리 청구서를 연속된 날짜에 걸쳐 매일 1원, 2원, 3원... 식으로 분할 납부할 수 있는 방법이 몇 가지인지** 알려줄래?"

예를 들어 15원짜리 청구서라면:

- 1+2+3+4+5 = 15 (5일에 걸쳐)
- 4+5+6 = 15 (3일에 걸쳐)
- 7+8 = 15 (2일에 걸쳐)
- 15 = 15 (하루에)

→ **총 4가지 방법!**

자연수 `n`을 연속된 자연수들의 합으로 표현하는 방법의 수를 반환하세요.

## 📋 규칙

**주어지는 것:**

- 자연수 `n` (1 ≤ n ≤ 10,000)

**해야 할 일:**

1. `n`을 연속된 자연수들의 합으로 표현하는 모든 방법을 찾기
2. **단 하나의 숫자도 방법에 포함됨** (예: `15 = 15`)
3. 방법의 개수를 반환

**반드시 따라야 할 제약사항:**

- 함수 이름은 `count_consecutive_sums` 사용
- snake_case로 변수 이름 작성
- 자연수만 사용 (1, 2, 3, ... — 0이나 음수 제외)

## 💡 예제

### 예제 1

```
입력: n = 15
출력: 4
```

설명: `1+2+3+4+5`, `4+5+6`, `7+8`, `15` — 총 4가지 방법

### 예제 2

```
입력: n = 9
출력: 3
```

설명: `2+3+4`, `4+5`, `9` — 총 3가지 방법

### 예제 3

```
입력: n = 1
출력: 1
```

설명: `1` 그 자체 한 가지 방법밖에 없어요

## 🎓 알아야 할 것

코딩을 시작하기 전에, 다음을 이해하고 있는지 확인하세요:

- `for` 반복문과 `range()` 사용법
- `while` 반복문 사용법
- 누적 합계를 변수에 저장하는 방법
- 조건문 (`if`, `elif`, `else`)으로 분기하기

## ✅ 과제

다음 시그니처로 함수를 작성하세요:

```python
def count_consecutive_sums(n: int) -> int:
    # 여기에 코드 작성
    pass
```

**시작하는 데 도움이 될 팁:**

- 시작 숫자를 1부터 n까지 바꿔가며 시도해보세요
- 각 시작 숫자에서, 합이 `n`이 될 때까지 다음 수를 더해보세요
- 합이 `n`을 넘어가면 그 시작 숫자는 실패 — 다음으로 넘어가세요

## 🎪 코드 테스트

다음 테스트 케이스를 실행해보세요:

```python
print(count_consecutive_sums(15))  # 예상: 4
print(count_consecutive_sums(9))   # 예상: 3
print(count_consecutive_sums(1))   # 예상: 1
print(count_consecutive_sums(10))  # 예상: 2  (1+2+3+4, 10)
print(count_consecutive_sums(100)) # 예상: 3
```

## 🤔 생각해보기

코딩을 시작하기 전에, 접근 방법을 스케치해보세요:

1. "연속된 자연수의 합"이라는 말은 정확히 무엇을 의미하나요?
2. 시작 숫자가 정해지면, 언제까지 더해야 할까요?
3. 합이 `n`보다 커지면 어떻게 해야 할까요?
4. 어떤 `n`에 대해서라도 항상 최소 한 가지 방법은 존재합니다. 왜 그럴까요?

## 🌶️ 보너스 챌린지

기본 문제를 다 풀었다면 도전해보세요.

### 🟢 Easy — 모든 방법 출력하기

방법의 개수만 반환하지 말고, 각 방법을 실제로 출력해보세요:

```
n = 15
1 + 2 + 3 + 4 + 5 = 15
4 + 5 + 6 = 15
7 + 8 = 15
15 = 15
총 4가지 방법
```

### 🟡 Medium — 슬라이딩 윈도우 (투 포인터)

이중 반복문 대신, **두 개의 변수** (`left`, `right`)와 **누적 합** 하나만 사용해서 풀어보세요. 합이 작으면 `right`를 늘리고, 크면 `left`를 늘리는 방식입니다. 효율이 훨씬 좋아집니다!

### 🔴 Hard — 수학적 통찰

사실 이 문제는 반복문 없이도 풀 수 있어요! 힌트: `n`의 **홀수 약수의 개수**가 정답입니다. 왜 그럴까요? 직접 증명해보고, 몇 줄짜리 코드로 만들어보세요.

스레드에 질문을 남겨주세요! 목표는 끝내는 것이 아니라 **왜 그렇게 되는지 이해하는 것**입니다.

행운을 빕니다! 🚀

---

# 🐍 Python Practice: Express a Number as Consecutive Sum!

Hey team! Today's challenge is where math meets coding.

## 🎯 Your Mission

You're an intern on the company's accounting team. Your manager has an interesting request: "**For an N-won invoice, how many ways can we split it into installments paid on consecutive days — like 1 won on day 1, 2 won on day 2, 3 won on day 3...?**"

For example, a 15-won invoice:

- 1+2+3+4+5 = 15 (over 5 days)
- 4+5+6 = 15 (over 3 days)
- 7+8 = 15 (over 2 days)
- 15 = 15 (in one day)

→ **4 ways total!**

Given a natural number `n`, return the number of ways to express it as a sum of consecutive natural numbers.

## 📋 The Rules

**What you're given:**

- A natural number `n` (1 ≤ n ≤ 10,000)

**What you need to do:**

1. Find every way to express `n` as a sum of consecutive natural numbers
2. **A single number counts as a valid way** (e.g., `15 = 15`)
3. Return the count of ways

**Constraints you must follow:**

- Function name must be `count_consecutive_sums`
- Variable names must use snake_case
- Use only natural numbers (1, 2, 3, ... — no zero, no negatives)

## 💡 Example Time

### Example 1

```
Input: n = 15
Output: 4
```

Explanation: `1+2+3+4+5`, `4+5+6`, `7+8`, `15` — 4 ways total

### Example 2

```
Input: n = 9
Output: 3
```

Explanation: `2+3+4`, `4+5`, `9` — 3 ways total

### Example 3

```
Input: n = 1
Output: 1
```

Explanation: Just `1` itself — only one way

## 🎓 What You Should Know

Before you start coding, make sure you understand:

- How to use `for` loops with `range()`
- How to use `while` loops
- How to track a running sum in a variable
- How to branch with `if`, `elif`, `else`

## ✅ Your Task

Write a function with this signature:

```python
def count_consecutive_sums(n: int) -> int:
    # Your code here
    pass
```

**Tips to get you started:**

- Try every possible starting number from 1 up to n
- For each starting number, keep adding the next number until the sum reaches `n`
- If the sum goes past `n`, that starting number doesn't work — move on

## 🎪 Test Your Code

Try running these test cases:

```python
print(count_consecutive_sums(15))  # Expected: 4
print(count_consecutive_sums(9))   # Expected: 3
print(count_consecutive_sums(1))   # Expected: 1
print(count_consecutive_sums(10))  # Expected: 2  (1+2+3+4, 10)
print(count_consecutive_sums(100)) # Expected: 3
```

## 🤔 Think About It

Before you start coding, sketch out your approach:

1. What does "sum of consecutive natural numbers" actually mean?
2. Once you fix a starting number, when should you stop adding?
3. What do you do when the running sum goes over `n`?
4. For any `n`, there's always at least one way. Why?

## 🌶️ Bonus Challenges

If you finished the main task, try these.

### 🟢 Easy — Print Every Way

Instead of just returning the count, print each way explicitly:

```
n = 15
1 + 2 + 3 + 4 + 5 = 15
4 + 5 + 6 = 15
7 + 8 = 15
15 = 15
Total: 4 ways
```

### 🟡 Medium — Sliding Window (Two Pointers)

Instead of a nested loop, use **two variables** (`left`, `right`) and a **single running sum**. When the sum is too small, advance `right`; when too big, advance `left`. Way more efficient!

### 🔴 Hard — Mathematical Insight

This problem can actually be solved without any loop over starting positions! Hint: the answer equals the **number of odd divisors of `n`**. Why is that true? Try to prove it yourself, then write a few-line solution.

Drop your questions in the thread! The goal isn't just to finish — it's to **understand why the logic works**.

Good luck! 🚀
