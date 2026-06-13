# 🐍 Python 연습: 반응 속도 게임 만들기!

여러분, 안녕하세요! `time` 모듈을 활용해서 진짜 게임을 만들어볼 시간입니다.

## 🎯 미션

여러분은 모바일 앱 개발 스타트업에 인턴으로 막 합류했습니다. 팀 리더가 "사용자들이 로딩 화면에서 지루해하지 않도록 미니 게임을 넣고 싶어!"라고 말합니다. 여러분의 첫 임무는 **반응 속도 측정 게임**을 Python으로 프로토타입 만들기입니다.

게임의 흐름은 이렇습니다:
1. "준비..."라는 메시지가 나타남
2. **랜덤한 시간** (1~3초) 동안 기다림
3. "GO!" 메시지가 나타나면, 사용자는 최대한 빨리 Enter 키를 누름
4. 반응 속도(초)를 측정하고 등급을 매겨서 보여줌

## 📋 규칙

*주어지는 것:*
- `time` 모듈 (이미 배웠죠!)
- `random` 모듈 (이미 배웠죠!)
- `input()` 함수로 사용자 입력 받기

*해야 할 일:*
1. 사용자가 Enter를 누르기 전후의 시간을 측정
2. 반응 속도(초)를 계산
3. 속도에 따라 등급 부여
4. 결과를 보기 좋게 출력

*반드시 따라야 할 제약사항:*
- `time.time()`과 `time.sleep()`만 사용
- 함수를 3개로 분리해서 각자 역할 명확히
- 반응 속도는 소수점 셋째 자리까지 표시 (예: `0.342초`)

## 💡 예제

**실행 예시 1 (빠른 반응):**
```
준비...
GO! (Enter를 누르세요)
(사용자가 0.250초 후 Enter)
반응 속도: 0.250초
등급: ⚡ 번개처럼 빠름!
```

**실행 예시 2 (평균 반응):**
```
준비...
GO! (Enter를 누르세요)
(사용자가 0.500초 후 Enter)
반응 속도: 0.500초
등급: 👍 평균
```

## 🎓 알아야 할 것

코딩을 시작하기 전에, 다음을 이해하고 있는지 확인하세요:
- `import` 문으로 모듈 가져오기
- `time.time()`은 현재 시각을 초 단위 숫자로 반환한다는 점
- `time.sleep(seconds)`는 지정한 시간만큼 프로그램을 멈춘다는 점
- `random.uniform(a, b)`는 a와 b 사이의 실수를 반환한다는 점
- `input()`은 사용자가 Enter를 누를 때까지 기다린다는 점
- f-string으로 숫자 형식 지정하기 (예: `f"{x:.3f}"`)

## ✅ 과제

세 개의 함수를 작성하세요:

```python
def measure_reaction_time() -> float:
    """사용자가 Enter를 누를 때까지 걸린 시간을 측정해서 반환"""
    pass

def rate_reaction(elapsed: float) -> str:
    """반응 속도(초)를 받아서 등급 문자열을 반환"""
    pass

def play_reaction_game() -> None:
    """게임 전체를 실행 (위 두 함수를 활용)"""
    pass
```

**등급 기준:**

| 반응 속도 | 등급 |
|---|---|
| 0.25초 미만 | ⚡ 번개처럼 빠름! |
| 0.25초 이상 ~ 0.40초 미만 | 🚀 빠름! |
| 0.40초 이상 ~ 0.60초 미만 | 👍 평균 |
| 0.60초 이상 | 🐢 다시 도전! |

**시작하는 데 도움이 될 팁:**
- "스냅샷 패턴"을 기억하세요: 시작 시간 저장 → 무언가 발생 → 끝 시간 저장 → 차이 계산
- `random.uniform(1.0, 3.0)`으로 1~3초 사이 랜덤 대기 시간 만들기
- 등급은 `if`/`elif`/`else`로 분기 처리

## 🎪 코드 테스트

함수들을 다음과 같이 테스트해보세요:

```python
# 테스트 1: rate_reaction 함수만 단독 테스트
print(rate_reaction(0.15))  # 예상: ⚡ 번개처럼 빠름!
print(rate_reaction(0.30))  # 예상: 🚀 빠름!
print(rate_reaction(0.50))  # 예상: 👍 평균
print(rate_reaction(1.00))  # 예상: 🐢 다시 도전!

# 테스트 2: 경계값 테스트
print(rate_reaction(0.25))  # 예상: 🚀 빠름! (0.25는 "미만"이 아님)
print(rate_reaction(0.40))  # 예상: 👍 평균
print(rate_reaction(0.60))  # 예상: 🐢 다시 도전!

# 테스트 3: 게임 실행
play_reaction_game()
```

## 🤔 생각해보기

코딩을 시작하기 전에, 다음을 생각해보세요:
1. `time.time()`을 호출하면 어떤 값이 반환될까요? 직접 출력해보세요!
2. 반응 속도를 계산할 때, "끝 시간 - 시작 시간"의 순서가 중요한 이유는?
3. 만약 사용자가 "GO!" 메시지가 나오기 **전에** Enter를 누르면 어떻게 될까요? (보너스 챌린지에서 다룹니다!)
4. `time.sleep(2)`와 `time.sleep(2.0)`의 차이가 있을까요?

막히면 스레드에 질문을 남겨주세요! 목표는 끝내는 것이 아니라 배우는 것입니다. 천천히 논리를 이해하면서 진행하세요.

행운을 빕니다! 🚀

---
---

# 🐍 Python Practice: Build a Reaction Time Game!

Hey team! Time to use the `time` module to build an actual game.

## 🎯 Your Mission

You just joined a mobile app startup as an intern. Your team lead says, "I want a mini-game on the loading screen so users don't get bored!" Your first task: prototype a **reaction time game** in Python.

Here's the game flow:
1. A "Get ready..." message appears
2. Wait a **random amount of time** (1–3 seconds)
3. When "GO!" appears, the user presses Enter as fast as possible
4. Measure the reaction time (in seconds) and give them a rating

## 📋 The Rules

*What you're given:*
- The `time` module (you've learned this!)
- The `random` module (you've learned this!)
- The `input()` function to get user input

*What you need to do:*
1. Measure the time before and after the user presses Enter
2. Calculate the reaction time (in seconds)
3. Give a rating based on the speed
4. Display the results nicely

*Constraints you must follow:*
- Use only `time.time()` and `time.sleep()`
- Split your code into 3 functions, each with a clear role
- Display the reaction time to 3 decimal places (e.g., `0.342 seconds`)

## 💡 Example Time

**Example run 1 (fast reaction):**
```
Get ready...
GO! (press Enter)
(user presses Enter 0.250s later)
Reaction time: 0.250 seconds
Rating: ⚡ Lightning fast!
```

**Example run 2 (average reaction):**
```
Get ready...
GO! (press Enter)
(user presses Enter 0.500s later)
Reaction time: 0.500 seconds
Rating: 👍 Average
```

## 🎓 What You Should Know

Before you start coding, make sure you understand:
- How to import a module with `import`
- That `time.time()` returns the current time as a number (seconds)
- That `time.sleep(seconds)` pauses the program for the given duration
- That `random.uniform(a, b)` returns a float between a and b
- That `input()` waits until the user presses Enter
- f-string formatting for numbers (e.g., `f"{x:.3f}"`)

## ✅ Your Task

Write three functions:

```python
def measure_reaction_time() -> float:
    """Measure how long it takes the user to press Enter, return it"""
    pass

def rate_reaction(elapsed: float) -> str:
    """Take the reaction time (seconds), return a rating string"""
    pass

def play_reaction_game() -> None:
    """Run the full game (using the two functions above)"""
    pass
```

**Rating thresholds:**

| Reaction Time | Rating |
|---|---|
| Less than 0.25s | ⚡ Lightning fast! |
| 0.25s to less than 0.40s | 🚀 Fast! |
| 0.40s to less than 0.60s | 👍 Average |
| 0.60s or more | 🐢 Try again! |

**Tips to get you started:**
- Remember the "snapshot pattern": save start time → something happens → save end time → compute the difference
- Use `random.uniform(1.0, 3.0)` for a random 1–3 second wait
- Use `if`/`elif`/`else` for the rating logic

## 🎪 Test Your Code

Test your functions like this:

```python
# Test 1: Test rate_reaction alone
print(rate_reaction(0.15))  # Expected: ⚡ Lightning fast!
print(rate_reaction(0.30))  # Expected: 🚀 Fast!
print(rate_reaction(0.50))  # Expected: 👍 Average
print(rate_reaction(1.00))  # Expected: 🐢 Try again!

# Test 2: Boundary values
print(rate_reaction(0.25))  # Expected: 🚀 Fast! (0.25 is NOT "less than")
print(rate_reaction(0.40))  # Expected: 👍 Average
print(rate_reaction(0.60))  # Expected: 🐢 Try again!

# Test 3: Run the game
play_reaction_game()
```

## 🤔 Think About It

Before you start coding, think about these:
1. What value does `time.time()` return when you call it? Try printing it!
2. Why does the order matter when calculating "end time - start time"?
3. What happens if the user presses Enter **before** "GO!" appears? (We'll handle this in bonus challenges!)
4. Is there any difference between `time.sleep(2)` and `time.sleep(2.0)`?

Drop your questions in the thread if you get stuck! Remember, the goal is to learn, not just to finish. Take your time and understand the logic.

Good luck! 🚀
