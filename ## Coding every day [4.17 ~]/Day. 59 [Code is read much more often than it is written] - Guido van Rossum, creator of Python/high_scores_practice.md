# 🎮 Python 클래스 연습 Day 3: 게임 최고 점수판 만들기!

여러분, 안녕하세요! 클래스 설계 셋째 날이에요. 오늘은 **객체를 예쁘게 출력하는 법**을 배워봅시다. 80년대 오락실의 전설, **Frogger** 게임의 최고 점수판을 직접 만들어볼 거예요! 🐸

## 🎯 미션

게임에는 항상 점수판이 있죠. 점수 리스트를 받아서 최고 점수, 최근 점수, 상위 3개 점수를 알려주는 `HighScores` 클래스를 만드세요. 그리고 — 여기가 오늘의 핵심입니다 — 이 객체를 `print()` 했을 때 **사람이 읽기 좋게** 보이도록 만들어 봅시다.

## 📚 새로운 개념: `__str__`과 `__repr__`

`print(my_object)` 하면 뭐가 나오는지 본 적 있나요?

```python
class Dog:
    def __init__(self, name):
        self.name = name

buddy = Dog("Buddy")
print(buddy)
# <__main__.Dog object at 0x7f8c1a2b3d40>  😱
```

이상하죠? Python은 객체를 어떻게 출력해야 할지 모르니까 메모리 주소를 보여줍니다. 이 문제를 해결하는 두 개의 매직 메서드(dunder method)가 있어요:

### `__str__`: "사용자용" 표현
- `print(obj)` 또는 `str(obj)`을 호출할 때 실행됨
- **사람이 보기 좋게**, 예쁘고 친근하게
- 게임 화면에 보여줄 텍스트라고 생각하세요

### `__repr__`: "개발자용" 표현
- `repr(obj)`을 호출하거나, 리스트 안에 객체가 있을 때 실행됨
- **명확하고 디버깅에 유용하게**
- 이상적으로는 `eval(repr(obj))`로 같은 객체를 재현할 수 있어야 함
- 로그나 에러 메시지에서 객체의 정체를 파악할 때 유용

### 비교 예시

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"🐶 {self.name} ({self.age}살)"

    def __repr__(self):
        return f"Dog(name={self.name!r}, age={self.age!r})"

buddy = Dog("Buddy", 3)

print(buddy)           # 🐶 Buddy (3살)         ← __str__ 사용
print(repr(buddy))     # Dog(name='Buddy', age=3)  ← __repr__ 사용
print([buddy, buddy])  # [Dog(name='Buddy', age=3), Dog(name='Buddy', age=3)]
                       # 리스트 안에서는 __repr__ 사용!
```

> 💡 **핵심 규칙**: `__str__`은 사람을 위해, `__repr__`은 개발자(미래의 너 자신!)를 위해.
>
> 💡 **`!r` 포맷팅 팁**: f-string에서 `{value!r}`을 쓰면 그 값의 `repr()`을 호출합니다. 문자열을 따옴표로 감싸주기 때문에 `__repr__` 안에서 쓰기 딱 좋아요.

## 📋 규칙

*주어지는 것:*
- 정수 점수들의 리스트 (예: `[30, 50, 20, 70]`)
- 게임이 진행되는 순서대로 저장되어 있음 (마지막이 가장 최근 점수)

*만들어야 할 것 — `HighScores` 클래스에 다음 메서드들:*
1. `__init__(self, scores)`: 점수 리스트를 받아서 인스턴스 속성으로 저장
2. `latest(self)`: 가장 최근 점수 반환
3. `personal_best(self)`: 최고 점수 반환
4. `personal_top_three(self)`: 상위 3개 점수를 **내림차순 리스트**로 반환 (점수가 3개 미만이면 있는 만큼만)
5. `__str__(self)`: 사용자에게 보여줄 예쁜 문자열
6. `__repr__(self)`: 개발자용 명확한 문자열

*반드시 따라야 할 제약사항:*
- 모든 함수와 변수 이름은 **snake_case**
- 원본 점수 리스트의 순서는 절대 바꾸지 말 것 (`sort()` ❌, `sorted()` ⭕)
- `__repr__`은 가능하면 `eval()`로 복원 가능하게

## 💡 예제

**예제 1: 기본 동작**
```python
hs = HighScores([30, 50, 20, 70])
hs.latest()              # 70
hs.personal_best()       # 70
hs.personal_top_three()  # [70, 50, 30]
```

**예제 2: 동점 처리**
```python
hs = HighScores([40, 20, 40, 30])
hs.personal_top_three()  # [40, 40, 30]  ← 동점도 그대로 포함
```

**예제 3: 출력**
```python
hs = HighScores([100, 0, 90, 30])
print(hs)
# 🎮 High Scores — Top: [100, 90, 30] | Latest: 30
print(repr(hs))
# HighScores(scores=[100, 0, 90, 30])
```

## 🎓 알아야 할 것

코딩을 시작하기 전에, 다음을 이해하고 있는지 확인하세요:
- `class`와 `__init__`으로 클래스를 정의하는 법
- `self`를 사용해 인스턴스 속성에 접근하는 법
- `max()`, `sorted()` 같은 내장 함수
- 리스트 슬라이싱 (`[:3]`)
- f-string 포맷팅

## ✅ 과제

스켈레톤 파일을 열고 다음 시그니처를 완성하세요:

```python
class HighScores:
    def __init__(self, scores: list[int]) -> None:
        # TODO
        pass

    def latest(self) -> int:
        # TODO
        pass

    def personal_best(self) -> int:
        # TODO
        pass

    def personal_top_three(self) -> list[int]:
        # TODO
        pass

    def __str__(self) -> str:
        # TODO
        pass

    def __repr__(self) -> str:
        # TODO
        pass
```

**시작하는 데 도움이 될 팁:**
- `sorted(self.scores, reverse=True)`는 새 리스트를 반환 — 원본 보존! ⭕
- `self.scores.sort()`는 원본을 직접 수정 — 점수 순서가 망가짐! ❌
- `__str__` 안에서 다른 메서드를 호출해도 됩니다 (예: `self.personal_top_three()`)
- `__repr__`에서 `{self.scores!r}`을 활용해보세요

## 🎪 코드 테스트

```python
# 테스트 1: 기본 메서드
hs1 = HighScores([30, 50, 20, 70])
assert hs1.scores == [30, 50, 20, 70]
assert hs1.latest() == 70
assert hs1.personal_best() == 70
assert hs1.personal_top_three() == [70, 50, 30]

# 테스트 2: 동점
assert HighScores([40, 20, 40, 30]).personal_top_three() == [40, 40, 30]

# 테스트 3: 점수가 3개 미만
assert HighScores([30, 70]).personal_top_three() == [70, 30]
assert HighScores([40]).personal_top_three() == [40]

# 테스트 4: 원본 리스트 보존
hs4 = HighScores([30, 50, 20, 70])
_ = hs4.personal_top_three()
assert hs4.scores == [30, 50, 20, 70], "원본 리스트를 수정하면 안 돼요!"

# 테스트 5: __str__과 __repr__
hs5 = HighScores([100, 0, 90, 30])
print(str(hs5))    # 사람이 읽기 좋은 형식이면 OK
print(repr(hs5))   # HighScores(scores=[100, 0, 90, 30])

# 테스트 6: __repr__ 라운드트립
hs6 = HighScores([1, 2, 3])
hs6_copy = eval(repr(hs6))
assert hs6_copy.scores == hs6.scores

print("✅ 모든 테스트 통과!")
```

## 🌟 보너스 챌린지

### 🥉 Bronze: `add_score(score)` 메서드 추가
게임이 끝날 때마다 점수를 추가할 수 있게 만드세요.
```python
hs = HighScores([10, 20, 30])
hs.add_score(50)
assert hs.scores == [10, 20, 30, 50]
```

### 🥈 Silver: 더 파이썬다운 top_three
`heapq.nlargest(3, self.scores)`를 사용해서 `personal_top_three`를 다시 작성해보세요.
정렬 전체를 하지 않고 상위 3개만 뽑기 때문에 점수가 매우 많을 때 더 효율적입니다.
```python
import heapq
# 힌트: heapq.nlargest(3, [10, 30, 90, 30, 100]) → [100, 90, 30]
```

### 🥇 Gold: 플레이어 이름과 메달 점수판
- `__init__`에 `player_name` 매개변수 추가 (기본값 `"Player 1"`)
- `__str__`을 메달 이모지와 함께 여러 줄로 예쁘게:
```
🎮 Alice's Hall of Fame
  🥇 100
  🥈 95
  🥉 80
  (Latest: 60)
```
- `__repr__`도 `player_name`을 포함하도록 업데이트
- `eval(repr(obj))`로 여전히 라운드트립 가능해야 함

## 🤔 생각해보기

코딩을 시작하기 전에 (또는 끝낸 후에) 다음을 생각해보세요:
1. `__str__`만 정의하고 `__repr__`은 정의하지 않으면 어떻게 될까요? 반대는요?
2. 왜 `repr(obj)`의 결과는 `eval()`로 복원 가능해야 좋을까요?
3. 동점인 경우 `personal_top_three`가 `[40, 40, 30]`을 반환하는 게 맞을까요, 아니면 중복을 제거한 `[40, 30]`을 반환하는 게 맞을까요? 게임 디자인 관점에서 토론해보세요.
4. `self.scores.sort()`와 `sorted(self.scores)`의 차이는 무엇이고, 이 문제에서는 왜 후자를 써야 할까요?

막히면 스레드에 질문 남겨주세요! 천천히 논리를 이해하면서 진행하세요.

행운을 빕니다! 🚀

---
---

# 🎮 Python Class Practice Day 3: Build a Game Leaderboard!

Hey team! Day three of class design. Today we'll learn **how to print objects beautifully**. We're building the high-score component of the legendary 80's arcade game **Frogger**! 🐸

## 🎯 Your Mission

Every game has a leaderboard. Build a `HighScores` class that takes a list of scores and tells you the personal best, the latest score, and the top three. And — here's today's focus — make sure that when you `print()` the object, it looks **friendly to humans**.

## 📚 New Concept: `__str__` and `__repr__`

Have you ever seen what happens when you `print(my_object)`?

```python
class Dog:
    def __init__(self, name):
        self.name = name

buddy = Dog("Buddy")
print(buddy)
# <__main__.Dog object at 0x7f8c1a2b3d40>  😱
```

Weird, right? Python doesn't know how to display the object, so it shows a memory address. Two magic (dunder) methods fix this:

### `__str__`: "user-facing" representation
- Called by `print(obj)` or `str(obj)`
- **Friendly and readable** for end users
- Think of it as what you'd show on the game screen

### `__repr__`: "developer-facing" representation
- Called by `repr(obj)`, or when the object appears inside a list/dict
- **Unambiguous, useful for debugging**
- Ideally, `eval(repr(obj))` should recreate an equivalent object
- Great for logs and error messages

### Side-by-side example

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"🐶 {self.name} ({self.age} years old)"

    def __repr__(self):
        return f"Dog(name={self.name!r}, age={self.age!r})"

buddy = Dog("Buddy", 3)

print(buddy)           # 🐶 Buddy (3 years old)     ← uses __str__
print(repr(buddy))     # Dog(name='Buddy', age=3)   ← uses __repr__
print([buddy, buddy])  # [Dog(name='Buddy', age=3), Dog(name='Buddy', age=3)]
                       # Lists use __repr__ on their items!
```

> 💡 **Rule of thumb**: `__str__` is for humans, `__repr__` is for developers (future-you!).
>
> 💡 **`!r` formatting tip**: In an f-string, `{value!r}` calls `repr()` on the value. It wraps strings in quotes, which is exactly what you want inside `__repr__`.

## 📋 The Rules

*What you're given:*
- A list of integer scores (e.g., `[30, 50, 20, 70]`)
- Stored in the order the games were played (last item = most recent score)

*What to build — a `HighScores` class with these methods:*
1. `__init__(self, scores)`: store the score list as an instance attribute
2. `latest(self)`: return the most recent score
3. `personal_best(self)`: return the highest score
4. `personal_top_three(self)`: return the top 3 scores as a **descending list** (fewer than 3 if not enough scores)
5. `__str__(self)`: a friendly string for users
6. `__repr__(self)`: an unambiguous string for developers

*Constraints:*
- All function and variable names in **snake_case**
- Never mutate the original score list (`sort()` ❌, `sorted()` ⭕)
- `__repr__` should ideally be `eval()`-recoverable

## 💡 Examples

**Example 1: Basic behavior**
```python
hs = HighScores([30, 50, 20, 70])
hs.latest()              # 70
hs.personal_best()       # 70
hs.personal_top_three()  # [70, 50, 30]
```

**Example 2: Ties**
```python
hs = HighScores([40, 20, 40, 30])
hs.personal_top_three()  # [40, 40, 30]  ← ties are kept
```

**Example 3: Printing**
```python
hs = HighScores([100, 0, 90, 30])
print(hs)
# 🎮 High Scores — Top: [100, 90, 30] | Latest: 30
print(repr(hs))
# HighScores(scores=[100, 0, 90, 30])
```

## 🎓 What You Should Know

Before you start, make sure you're comfortable with:
- Defining a class with `class` and `__init__`
- Accessing instance attributes via `self`
- Built-ins like `max()` and `sorted()`
- List slicing (`[:3]`)
- f-string formatting

## ✅ Your Task

Open the skeleton file and complete this signature:

```python
class HighScores:
    def __init__(self, scores: list[int]) -> None:
        # TODO
        pass

    def latest(self) -> int:
        # TODO
        pass

    def personal_best(self) -> int:
        # TODO
        pass

    def personal_top_three(self) -> list[int]:
        # TODO
        pass

    def __str__(self) -> str:
        # TODO
        pass

    def __repr__(self) -> str:
        # TODO
        pass
```

**Tips to get you started:**
- `sorted(self.scores, reverse=True)` returns a **new** list — preserves the original! ⭕
- `self.scores.sort()` mutates the original — destroys the game order! ❌
- You can call other methods from `__str__` (e.g., `self.personal_top_three()`)
- Try using `{self.scores!r}` inside `__repr__`

## 🎪 Test Your Code

```python
# Test 1: basic methods
hs1 = HighScores([30, 50, 20, 70])
assert hs1.scores == [30, 50, 20, 70]
assert hs1.latest() == 70
assert hs1.personal_best() == 70
assert hs1.personal_top_three() == [70, 50, 30]

# Test 2: ties
assert HighScores([40, 20, 40, 30]).personal_top_three() == [40, 40, 30]

# Test 3: fewer than 3 scores
assert HighScores([30, 70]).personal_top_three() == [70, 30]
assert HighScores([40]).personal_top_three() == [40]

# Test 4: preserve the original list
hs4 = HighScores([30, 50, 20, 70])
_ = hs4.personal_top_three()
assert hs4.scores == [30, 50, 20, 70], "Don't mutate the original list!"

# Test 5: __str__ and __repr__
hs5 = HighScores([100, 0, 90, 30])
print(str(hs5))    # any human-readable form
print(repr(hs5))   # HighScores(scores=[100, 0, 90, 30])

# Test 6: __repr__ round-trip
hs6 = HighScores([1, 2, 3])
hs6_copy = eval(repr(hs6))
assert hs6_copy.scores == hs6.scores

print("✅ All tests passed!")
```

## 🌟 Bonus Challenges

### 🥉 Bronze: add an `add_score(score)` method
So players can post a new score after each game.
```python
hs = HighScores([10, 20, 30])
hs.add_score(50)
assert hs.scores == [10, 20, 30, 50]
```

### 🥈 Silver: a more Pythonic top_three
Rewrite `personal_top_three` using `heapq.nlargest(3, self.scores)`.
It only finds the top 3 without sorting the entire list, so it's more efficient when there are many scores.
```python
import heapq
# Hint: heapq.nlargest(3, [10, 30, 90, 30, 100]) → [100, 90, 30]
```

### 🥇 Gold: player name + medal-style leaderboard
- Add a `player_name` parameter to `__init__` (default `"Player 1"`)
- Make `__str__` a multi-line, medal-emoji leaderboard:
```
🎮 Alice's Hall of Fame
  🥇 100
  🥈 95
  🥉 80
  (Latest: 60)
```
- Update `__repr__` to include `player_name`
- `eval(repr(obj))` should still round-trip

## 🤔 Think About It

Before (or after) coding, think about:
1. What happens if you only define `__str__` but not `__repr__`? What about the reverse?
2. Why is it good practice for `repr(obj)` to be `eval()`-recoverable?
3. For ties, should `personal_top_three` return `[40, 40, 30]` or the deduplicated `[40, 30]`? Discuss from a game-design perspective.
4. What's the difference between `self.scores.sort()` and `sorted(self.scores)`, and why does this problem require the latter?

Drop your questions in the thread if you get stuck. Take your time — the goal is to learn, not just to finish.

Good luck! 🚀
