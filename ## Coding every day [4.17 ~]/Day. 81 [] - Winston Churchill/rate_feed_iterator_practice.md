# 🐍 Python 연습: 환율 피드를 한 걸음씩 — 이터레이터(Iterator) 만들기

> "천 리 길도 한 걸음부터." — 노자(老子), 『도덕경』 64장 (千里之行，始於足下)
>
> *"A journey of a thousand miles begins with a single step."* — Laozi, *Tao Te Ching*, ch. 64
>
> 📌 이 명언은 흔히 공자(Confucius)의 말로 잘못 인용되지만, 실제 출처는 노자의 『도덕경』입니다.
> (Often misattributed to Confucius — the real source is Laozi's *Tao Te Ching*.)

이터레이터는 바로 이 명언처럼 동작합니다. 전체를 한꺼번에 보는 것이 아니라, **한 번에 한 걸음씩** 다음 값을 꺼내고, 더 이상 걸음이 없으면 멈춥니다.

---

## 🏦 시나리오 (Scenario): Wonder Exchange 일일 환율 피드

여러분은 핀테크 회사 **Wonder Exchange**의 백엔드 팀에 합류했습니다. 매일 USD/KRW 환율이 한 건씩 발표됩니다. 팀은 이 환율들을 `for` 루프로 하루씩 순회할 수 있는 **재사용 가능한 피드 객체**를 원합니다.

You've joined the backend team at **Wonder Exchange**, a FinTech company. Each day a USD/KRW rate is published. The team wants a **reusable feed object** that can be walked through one day at a time with a `for` loop.

핵심 요구사항: 같은 피드 객체를 **여러 번** 순회할 수 있어야 합니다 (한 번은 출력용, 한 번은 최고가 계산용). 즉 **재반복(re-iterable)** 가능해야 합니다.

The key requirement: the **same** feed object must support being looped over **more than once** (once to print, once to find the high). It must be **re-iterable**.

---

## 🎯 미션 (Your Mission)

두 개의 클래스를 만듭니다 — 이것이 이번 과제의 핵심입니다:

You will build **two** classes — this separation is the heart of the lesson:

1. **`RateFeed`** — *이터러블(iterable)*. 환율 데이터를 보관하고, 호출될 때마다 **새 이터레이터**를 만들어 돌려줍니다.
   *(The iterable: stores the data, hands out a **fresh iterator** each time.)*
2. **`RateFeedIterator`** — *이터레이터(iterator)*. 실제로 위치를 추적하며 한 번에 하나씩 값을 꺼냅니다.
   *(The iterator: tracks position, produces one value at a time.)*

---

## 🧭 먼저 이해하기: 이터러블 vs 이터레이터 (Iterable vs Iterator)

코드를 짜기 전에, 이미 익숙한 객체로 둘의 차이를 느껴봅시다.

Before coding, feel the difference using objects you already know:

```python
numbers = [10, 20, 30]          # 리스트는 '이터러블'입니다 (a list is ITERABLE)

box = iter(numbers)             # iter()는 '이터레이터'를 꺼냅니다 (iter() gives an ITERATOR)
print(next(box))                # 10  ← next()가 한 걸음 (one step)
print(next(box))                # 20
print(next(box))                # 30
print(next(box))                # ❗ StopIteration 예외 발생 (raised when steps run out)
```

> 💡 **핵심 (Key idea)**
> - **이터러블(iterable)**: `for`에 넣을 수 있는 것. `__iter__`를 가집니다.
> - **이터레이터(iterator)**: 실제로 걸음을 세는 것. `__next__`를 가지고, 다 떨어지면 `StopIteration`을 던집니다.
> - `for x in something:` 은 내부적으로 `iter(something)`을 한 번 호출해 이터레이터를 얻고, 값이 떨어질 때까지 `next()`를 반복합니다.
> - **iterable = "can be looped"; iterator = "the thing doing the stepping."** `for` calls `iter()` once, then `next()` until `StopIteration`.

---

## 🔁 왜 두 클래스로 나누나요? (Why two classes?)

> ⚠️ **가장 흔한 함정 (The most common trap)**
> 하나의 클래스에 `__iter__`(자기 자신 반환)와 `__next__`를 모두 넣고 위치를 인스턴스에 저장하면, **한 번 순회한 뒤에는 위치가 끝에 머물러** 두 번째 `for` 루프가 **빈 결과**를 냅니다. 즉 재반복이 불가능합니다.
>
> If one class holds both `__iter__` (returning self) and `__next__` with the position stored on the instance, then after one loop the position sits at the end — a second `for` loop yields **nothing**. Not re-iterable.

**해결책 (Solution):** 데이터를 보관하는 **이터러블**과, 걸음을 세는 **이터레이터**를 분리합니다. `RateFeed.__iter__`가 매번 위치가 0인 **새 `RateFeedIterator`**를 만들어 주면, 루프마다 깨끗하게 다시 시작합니다.

Separate the **iterable** (holds data) from the **iterator** (counts steps). Have `RateFeed.__iter__` build a **brand-new `RateFeedIterator`** (position 0) every time, so each loop starts clean.

---

## 💡 예제 (Example)

```python
feed = RateFeed([1320.5, 1325.0, 1318.75])

for rate in feed:
    print(rate)
# 1320.5
# 1325.0
# 1318.75

# 같은 feed를 다시 순회 — 재반복 가능! (loop the SAME feed again — re-iterable!)
for rate in feed:
    print(rate)
# 1320.5
# 1325.0
# 1318.75   ← 다시 처음부터 (starts fresh again)
```

---

## ✅ 과제 (Your Task)

아래 두 클래스를 완성하세요. 함수/변수 이름은 **snake_case**, 클래스 이름은 **PascalCase** (파이썬 표준 규칙).

Complete the two classes below. Use **snake_case** for methods/variables, **PascalCase** for class names (standard Python convention).

```python
class RateFeed:
    def __init__(self, daily_rates: list[float]) -> None:
        ...

    def __iter__(self):
        ...                       # 새 RateFeedIterator를 반환 (return a fresh iterator)


class RateFeedIterator:
    def __init__(self, daily_rates: list[float]) -> None:
        ...

    def __iter__(self):
        ...                       # 자기 자신을 반환 (return self)

    def __next__(self):
        ...                       # 다음 환율 반환, 없으면 StopIteration
```

**시작 팁 (Tips to get you started):**
- `RateFeedIterator`는 `position`(현재 위치) 변수를 0부터 시작해 추적합니다.
- `__next__`에서 먼저 *끝에 도달했는지* 확인하세요. 도달했으면 `raise StopIteration`.
- 끝이 아니라면, 현재 위치의 값을 저장 → `position`을 1 증가 → 저장한 값을 반환.
- 이터레이터 자신도 `__iter__`(→ `return self`)가 있어야 `for`에 직접 넣을 수 있습니다.

---

## 🎪 코드 테스트 (Test Your Code)

```python
# 테스트 1 — 기본 순회 (basic walk)
feed = RateFeed([1320.5, 1325.0, 1318.75])
result = []
for rate in feed:
    result.append(rate)
print("테스트 1 (Test 1):", result)
# 예상 (Expected): [1320.5, 1325.0, 1318.75]

# 테스트 2 — 재반복 (re-iterable: same feed, second loop)
second = []
for rate in feed:
    second.append(rate)
print("테스트 2 (Test 2):", second)
# 예상 (Expected): [1320.5, 1325.0, 1318.75]   ← 처음부터 다시 (fresh again)

# 테스트 3 — iter() / next() 직접 사용 (built-ins)
box = iter(feed)
print("테스트 3 (Test 3):", next(box), next(box), next(box))
# 예상 (Expected): 1320.5 1325.0 1318.75

# 테스트 4 — 빈 피드 (empty feed)
empty = RateFeed([])
print("테스트 4 (Test 4):", [r for r in empty])
# 예상 (Expected): []

# 테스트 5 — 내장 함수와 호환 (works with built-ins)
print("테스트 5 (Test 5):", list(RateFeed([10, 20, 30])), sum(RateFeed([10, 20, 30])))
# 예상 (Expected): [10, 20, 30] 60
```

---

## 🏆 보너스 도전 (Bonus Challenges)

### 🥉 Easy — 기준 환율 이상인 날 세기 (Count days at/above a threshold)
피드를 순회하며 환율이 `threshold` 이상인 날이 며칠인지 세는 함수를 작성하세요. (이미 만든 `RateFeed`를 `for`로 순회하면 됩니다.)

Write a function that loops over a feed and counts how many days the rate was at or above a given `threshold`.

```python
def count_days_above(feed, threshold):
    ...

# count_days_above(RateFeed([1320.5, 1325.0, 1318.75, 1330.0]), 1320.0) -> 3
```

### 🥈 Medium — 같은 피드를 두 번 순회하기 (Use the same feed twice)
**재반복 가능**이라는 점을 활용해, 같은 `RateFeed`를 (1) 한 번 순회해 평균을 구하고 (2) 다시 순회해 평균보다 높았던 날을 세는 함수를 작성하세요. 새 리스트를 따로 저장하지 말고, 피드를 **두 번 순회**하는 것이 핵심입니다.

Using **re-iterability**, write a function that loops the same `RateFeed` twice: once to compute the average, once to count days above that average. The point is to loop the feed **twice** rather than storing a separate list.

### 🥇 Hard 🔮 — 제너레이터로 다시 쓰기 (Rewrite with a generator) *(미리보기 / preview)*
> 🔮 이 도전은 아직 정식으로 배우지 않은 **`yield`(제너레이터)** 문법을 사용합니다. 다음 주제의 맛보기예요!
> This challenge uses **`yield` (generators)**, which we haven't formally covered yet — a taste of what's next!

두 개의 클래스 대신, `yield`를 사용하는 **하나의 함수**로 똑같은 동작을 만들어 보세요.

```python
def rate_feed_gen(daily_rates):
    for rate in daily_rates:
        yield rate

for rate in rate_feed_gen([1320.5, 1325.0, 1318.75]):
    print(rate)
```

🤔 **생각 거리 (Think about it):** 위 제너레이터를 변수에 담아(`g = rate_feed_gen([...])`) `for`로 두 번 순회하면 어떻게 될까요? 우리가 만든 `RateFeed`와 무엇이 다른가요?
*(What happens if you store the generator and loop it twice? How does that differ from our `RateFeed` class?)*

---

## 🤔 생각해보기 (Reflection)

1. `for x in obj:` 가 내부적으로 호출하는 두 가지는 무엇인가요? (`iter()`와 `next()`)
   *What two things does a `for` loop call under the hood?*
2. `StopIteration`은 누가, 언제 던지나요? `for` 루프는 그것을 어떻게 처리하나요?
   *Who raises `StopIteration`, and when? How does the `for` loop handle it?*
3. `RateFeed`와 `RateFeedIterator`를 하나로 합치면 왜 재반복이 깨지나요?
   *Why does merging the two classes break re-iterability?*
4. 이터레이터의 `__iter__`는 왜 `return self` 인가요?
   *Why does the iterator's `__iter__` just `return self`?*

막히면 스레드에 질문을 남겨주세요! 목표는 끝내는 것이 아니라 **원리를 이해하는 것**입니다. 천천히, 한 걸음씩. 🚶
*Drop questions in the thread! The goal is to understand the mechanism, not just finish. One step at a time.* 🚀
