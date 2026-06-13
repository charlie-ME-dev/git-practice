# 📅 Python 연습: 마감일 카운트다운 트래커!

> **출처:** LeetCode #1360 *Number of Days Between Two Dates* 변형
> **새로운 개념:** `datetime` 모듈 (날짜 다루기)

여러분, 안녕하세요! 오늘은 새로운 무기를 손에 쥐게 됩니다 — 바로 Python의 `datetime` 모듈입니다.

## 🎯 시나리오

여러분은 대학생을 위한 생산성 앱 **DeadlineHero** 의 신입 개발자가 되었습니다. 사용자들이 가장 많이 요청한 기능은 단순합니다:

> *"중요한 마감일까지 며칠 남았는지 한눈에 보고 싶어요. 그리고 임박했을 때는 경고도 받고 싶어요."*

CTO가 여러분에게 말합니다:
*"세 가지 핵심 함수만 만들어주세요. 나중에 우리는 이걸로 알림 시스템, 캘린더 연동, 통계 대시보드까지 확장할 거예요."*

여러분의 임무는 마감일 트래커의 핵심 로직을 구현하는 것입니다!

## 🆕 이번에 배울 도구: `datetime` 모듈

```python
from datetime import date, timedelta

today = date.today()          # 오늘 날짜
target = date(2026, 12, 25)   # 특정 날짜 만들기
diff = target - today         # 두 날짜의 차이 → timedelta 객체
print(diff.days)              # 며칠 차이인지 정수로 가져오기

target.year     # 2026
target.month    # 12
target.day      # 25
target.weekday() # 0=월요일, 1=화요일, ..., 6=일요일
```

`strftime()` 도 사용합니다 — 날짜를 원하는 형식의 문자열로 만들어주는 함수입니다.

## 📋 작성할 함수

### 함수 1: `days_until(target_date)`
어떤 날짜까지 며칠 남았는지 계산합니다.
- 미래 날짜 → 양수 (예: 7)
- 오늘 → 0
- 과거 날짜 → 음수 (예: -3)

### 함수 2: `format_deadline(target_date)`
날짜를 한국식 문자열로 보기 좋게 포맷합니다.
- 입력: `date(2026, 12, 25)`
- 출력: `"2026년 12월 25일 (금요일)"`

### 함수 3: `deadline_status(target_date)`
남은 일수와 상태 메시지를 **튜플**로 함께 반환합니다.

| 남은 일수 | 상태 메시지 |
|---|---|
| 음수 | `"지남 (N일 전)"` |
| 0 | `"오늘 마감!"` |
| 1 ~ 3 | `"임박"` |
| 4 ~ 7 | `"곧"` |
| 8 이상 | `"여유"` |

## 💡 예제

오늘이 **2026년 5월 5일 (화요일)** 이라고 가정합니다.

**예제 1: `days_until`**
```python
days_until(date(2026, 5, 12))   # → 7
days_until(date(2026, 5, 5))    # → 0
days_until(date(2026, 5, 1))    # → -4
```

**예제 2: `format_deadline`**
```python
format_deadline(date(2026, 12, 25))
# → "2026년 12월 25일 (금요일)"

format_deadline(date(2026, 1, 1))
# → "2026년 1월 1일 (목요일)"
```

**예제 3: `deadline_status`**
```python
deadline_status(date(2026, 5, 8))   # → (3, "임박")
deadline_status(date(2026, 5, 5))   # → (0, "오늘 마감!")
deadline_status(date(2026, 5, 20))  # → (15, "여유")
deadline_status(date(2026, 5, 1))   # → (-4, "지남 (4일 전)")
```

## 🎓 알아야 할 것

- 모듈에서 도구 가져오기: `from datetime import date, timedelta`
- `date(year, month, day)` 로 날짜 객체 만들기
- `date.today()` 로 오늘 날짜 가져오기
- 날짜 빼기: `date1 - date2` → `timedelta` 객체
- `timedelta.days` 로 일수 정수값 꺼내기
- f-string 으로 한국식 문자열 만들기
- 튜플로 여러 값 반환하기 — `return a, b`

## ✅ 과제

`deadline_tracker_skeleton.py` 파일에 세 함수를 모두 구현하세요.

```python
from datetime import date, timedelta

def days_until(target_date: date) -> int:
    pass

def format_deadline(target_date: date) -> str:
    pass

def deadline_status(target_date: date) -> tuple:
    pass
```

> ⚠️ **힌트:** 요일 변환은 리스트로! `["월요일", "화요일", ..., "일요일"]` 를 만들고 `target_date.weekday()` 를 인덱스로 사용하세요.

## 🎪 코드 테스트

스켈레톤 파일 안의 테스트 블록을 그대로 실행하면 자동으로 검증됩니다.

## 🤔 생각해보기

1. 왜 `date` 객체끼리 빼면 `int` 가 아니라 `timedelta` 가 나올까요?
2. `target_date.weekday()` 가 월요일을 0으로 반환하는 게 한국 달력과는 어떻게 다른가요?
3. 만약 사용자가 입력한 날짜가 유효하지 않으면 (예: `date(2026, 13, 1)`) 어떤 일이 벌어질까요?

---

## 🌟 보너스 도전

### 🥉 Easy — 마감일 목록 정렬
여러 마감일을 받아서 **가까운 순서대로** 출력하는 함수를 만들어보세요.

```python
def show_all_deadlines(deadlines: list) -> None:
    """
    deadlines: date 객체들의 리스트
    각 마감일에 대해 'YYYY년 MM월 DD일 (요일) - N일 남음' 형태로 출력
    가까운 마감일부터 순서대로!
    """
    pass
```

### 🥈 Medium — 영업일 계산기
주말(토, 일)을 제외하고 평일만 세는 함수를 만들어보세요.

```python
def working_days_until(target_date: date) -> int:
    """
    오늘 이후 (내일부터) target_date 까지 평일(월~금)만 카운트
    target_date 가 오늘이거나 과거이면 0 반환
    """
    pass
```

> 💡 **힌트:** `weekday()` 가 0~4면 평일, 5~6이면 주말입니다. `while` 루프와 `timedelta(days=1)` 로 하루씩 이동하세요.

### 🥇 Hard — 문자열을 날짜로 변환 (`strptime` 미리보기)
사용자가 `"2026-12-25"` 같은 문자열을 입력한다면? 다음 수업에서 배울 `strptime()` 을 미리 맛보세요.

```python
from datetime import datetime

def parse_deadline(date_string: str) -> date:
    """
    "YYYY-MM-DD" 형식의 문자열을 date 객체로 변환
    예: "2026-12-25" → date(2026, 12, 25)
    """
    # strptime 은 문자열을 datetime 객체로 만듭니다
    dt = datetime.strptime(date_string, "%Y-%m-%d")
    # .date() 메서드로 시간 부분을 빼고 date 객체만 가져옵니다
    return dt.date()
```

> 📚 `"%Y-%m-%d"` 는 *포맷 코드* 입니다. `%Y`=4자리 연도, `%m`=2자리 월, `%d`=2자리 일. 다음 수업에서 자세히 배웁니다!

---

질문이 있으면 스레드에 남겨주세요. 목표는 끝내는 것이 아니라 **이해하는 것** 입니다. 🚀

---
---

# 📅 Python Practice: Deadline Countdown Tracker!

> **Source:** Adapted from LeetCode #1360 *Number of Days Between Two Dates*
> **New concept:** the `datetime` module (working with dates)

Hey team! Today you get a new tool in your belt — Python's `datetime` module.

## 🎯 The Scenario

You're a new developer at **DeadlineHero**, a productivity app for university students. The most-requested feature from users is simple:

> *"I want to see at a glance how many days are left until my important deadlines. And I want a warning when it's coming up soon."*

The CTO tells you:
*"Just build three core functions. Later, we'll extend this into a notification system, calendar integration, and a stats dashboard."*

Your mission is to implement the core deadline tracker logic!

## 🆕 New Tool: the `datetime` Module

```python
from datetime import date, timedelta

today = date.today()          # today's date
target = date(2026, 12, 25)   # build a specific date
diff = target - today         # subtracting dates → timedelta object
print(diff.days)              # extract the integer day count

target.year     # 2026
target.month    # 12
target.day      # 25
target.weekday() # 0=Monday, 1=Tuesday, ..., 6=Sunday
```

We'll also use `strftime()` — but in this practice we build the formatted string ourselves to keep things explicit.

## 📋 Functions to Write

### Function 1: `days_until(target_date)`
Calculate how many days remain until a given date.
- Future date → positive (e.g., 7)
- Today → 0
- Past date → negative (e.g., -3)

### Function 2: `format_deadline(target_date)`
Format a date as a Korean-friendly string.
- Input: `date(2026, 12, 25)`
- Output: `"2026년 12월 25일 (금요일)"`

### Function 3: `deadline_status(target_date)`
Return both the days remaining and a status message as a **tuple**.

| Days left | Status message |
|---|---|
| Negative | `"지남 (N일 전)"` |
| 0 | `"오늘 마감!"` |
| 1 ~ 3 | `"임박"` |
| 4 ~ 7 | `"곧"` |
| 8 or more | `"여유"` |

## 💡 Examples

Assume today is **May 5, 2026 (Tuesday)**.

**Example 1: `days_until`**
```python
days_until(date(2026, 5, 12))   # → 7
days_until(date(2026, 5, 5))    # → 0
days_until(date(2026, 5, 1))    # → -4
```

**Example 2: `format_deadline`**
```python
format_deadline(date(2026, 12, 25))
# → "2026년 12월 25일 (금요일)"

format_deadline(date(2026, 1, 1))
# → "2026년 1월 1일 (목요일)"
```

**Example 3: `deadline_status`**
```python
deadline_status(date(2026, 5, 8))   # → (3, "임박")
deadline_status(date(2026, 5, 5))   # → (0, "오늘 마감!")
deadline_status(date(2026, 5, 20))  # → (15, "여유")
deadline_status(date(2026, 5, 1))   # → (-4, "지남 (4일 전)")
```

## 🎓 What You Should Know

- Importing tools from a module: `from datetime import date, timedelta`
- Constructing a date with `date(year, month, day)`
- Getting today's date with `date.today()`
- Subtracting dates: `date1 - date2` → returns a `timedelta` object
- Extracting the integer day count via `timedelta.days`
- Building a Korean-friendly string with f-strings
- Returning multiple values via tuple — `return a, b`

## ✅ Your Task

Implement all three functions in `deadline_tracker_skeleton.py`.

```python
from datetime import date, timedelta

def days_until(target_date: date) -> int:
    pass

def format_deadline(target_date: date) -> str:
    pass

def deadline_status(target_date: date) -> tuple:
    pass
```

> ⚠️ **Hint:** Use a list to map weekday numbers to Korean names: `["월요일", "화요일", ..., "일요일"]`, indexed by `target_date.weekday()`.

## 🎪 Test Your Code

Run the skeleton file as-is — the test block will validate your work automatically.

## 🤔 Think About It

1. Why does subtracting two `date` objects produce a `timedelta` instead of an `int`?
2. `target_date.weekday()` returns 0 for Monday — how does that compare to typical Korean calendar conventions?
3. What happens if a user passes an invalid date like `date(2026, 13, 1)`?

---

## 🌟 Bonus Challenges

### 🥉 Easy — Sorted Deadline List
Take a list of multiple deadlines and print them **sorted by urgency**.

```python
def show_all_deadlines(deadlines: list) -> None:
    """
    deadlines: list of date objects
    Print each as 'YYYY년 MM월 DD일 (요일) - N일 남음', sorted by closest first.
    """
    pass
```

### 🥈 Medium — Working Days Calculator
Skip weekends (Sat, Sun) and count only weekdays.

```python
def working_days_until(target_date: date) -> int:
    """
    Count weekdays (Mon~Fri) from tomorrow through target_date inclusive.
    Returns 0 if target_date is today or earlier.
    """
    pass
```

> 💡 **Hint:** `weekday()` returns 0–4 for weekdays, 5–6 for weekend. Use a `while` loop with `timedelta(days=1)` to step day by day.

### 🥇 Hard — String to Date (`strptime` preview)
What if users type `"2026-12-25"` as a string? Get an early taste of `strptime()`, which we'll cover next class.

```python
from datetime import datetime

def parse_deadline(date_string: str) -> date:
    """
    Convert a "YYYY-MM-DD" string to a date object.
    Example: "2026-12-25" → date(2026, 12, 25)
    """
    # strptime turns a string into a datetime object
    dt = datetime.strptime(date_string, "%Y-%m-%d")
    # .date() drops the time portion, giving just a date object
    return dt.date()
```

> 📚 `"%Y-%m-%d"` is a *format code*. `%Y`=4-digit year, `%m`=2-digit month, `%d`=2-digit day. We'll cover these in detail next class!

---

Drop your questions in the thread. The goal is not to *finish* but to **understand**. 🚀
