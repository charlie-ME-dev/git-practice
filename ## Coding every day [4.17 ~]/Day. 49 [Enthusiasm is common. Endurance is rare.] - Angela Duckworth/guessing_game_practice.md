# 🎰 Python 연습: 숫자 맞추기 미니게임 부스!

여러분, 안녕하세요! 오늘은 **아케이드 게임 개발자**가 되어볼 시간입니다.

## 🎯 미션

여러분은 동네 오락실에서 일하는 신입 게임 개발자입니다. 사장님이 새로운 미니게임 부스를 위한 프로토타입을 만들어 달라고 하셨어요.

게임 규칙은 간단합니다: **컴퓨터가 1~20 사이의 비밀 숫자를 하나 뽑으면, 손님이 그 숫자를 맞추는 게임**입니다. 손님이 숫자를 입력할 때마다 컴퓨터는 "더 큰 숫자입니다!" 또는 "더 작은 숫자입니다!"라고 힌트를 줍니다. 정답을 맞추면 시도 횟수에 따라 다른 칭찬 메시지가 출력되도록 만들어 주세요!

## 📋 규칙

*주어지는 것:*
- `random` 모듈 (이미 배웠죠!)
- `input()` 함수로 손님의 입력을 받을 수 있음
- 1부터 20까지의 정수 범위

*해야 할 일:*
1. `random.randrange()`를 사용해 1~20 사이의 비밀 숫자 `x`를 생성
2. 손님이 숫자를 입력할 때마다 정답과 비교
3. 정답보다 작으면 "더 큰 숫자입니다!", 크면 "더 작은 숫자입니다!" 출력
4. 시도 횟수를 변수 `n`에 저장
5. 정답을 맞추면 시도 횟수에 따라 다른 메시지 출력

*반드시 따라야 할 제약사항:*
- **입력값은 1~20 범위 안이어야 합니다!** (범위 밖이면 다시 입력 받기)
- `n`은 시도할 때마다 1씩 증가
- 정답을 맞추기 전까지 게임은 계속됩니다
- 함수 이름과 변수 이름은 모두 `snake_case`로 작성

## 💡 예제

**예제 1: 천재 시나리오**
```
비밀 숫자: 10 (컴퓨터가 뽑음)

숫자를 입력하세요 (1~20): 10
정답입니다!
1번만에 맞춘 당신은 천재!
```
> *왜?* 시도 횟수가 3번 이하이므로 "천재" 메시지!

**예제 2: 평범한 시나리오**
```
비밀 숫자: 7 (컴퓨터가 뽑음)

숫자를 입력하세요 (1~20): 10
더 작은 숫자입니다!
숫자를 입력하세요 (1~20): 5
더 큰 숫자입니다!
숫자를 입력하세요 (1~20): 7
정답입니다!
3번만에 맞춘 당신은 천재!
```

**예제 3: 분발해야 하는 시나리오**
```
비밀 숫자: 15 (컴퓨터가 뽑음)

숫자를 입력하세요 (1~20): 1
... (여러 번 시도) ...
숫자를 입력하세요 (1~20): 15
정답입니다!
8번만에 맞추다니 분발하세요.
```

### 🏆 시도 횟수에 따른 메시지

| 시도 횟수 `n` | 메시지 |
|---|---|
| 1 ~ 3번 | `n번만에 맞춘 당신은 천재!` |
| 4 ~ 6번 | `n번만에 맞추셨네요. 잘했어요^^` |
| 7번 이상 | `n번만에 맞추다니 분발하세요.` |

## 🎓 알아야 할 것

코딩을 시작하기 전에, 다음을 이해하고 있는지 확인하세요:
- `random.randrange(a, b)` 함수의 사용법 (b는 포함되지 않음을 기억!)
- `while` 루프로 반복 작성하기
- `if` / `elif` / `else`로 조건 분기
- `int(input())`로 사용자 입력을 정수로 변환
- 카운터 변수를 1씩 증가시키기 (`n = n + 1`)

## ✅ 과제

다음 시그니처로 함수를 작성하세요:

```python
def play_guessing_game() -> int:
    """
    숫자 맞추기 게임을 실행하고, 손님이 사용한 시도 횟수를 반환합니다.
    """
    # 여기에 코드 작성
    pass
```

**시작하는 데 도움이 될 팁:**
- `random.randrange(1, 21)`을 쓰면 1~20 사이의 숫자가 나옵니다 (21은 포함 안 됨!)
- `while True:` 루프 안에서 정답을 맞추면 `break`로 빠져나오세요
- 시도 횟수 `n`은 루프 시작 전에 0으로 초기화하고, 입력받을 때마다 1씩 증가시키세요
- 범위를 벗어난 입력(예: 25, -3)은 카운트하지 않고 다시 입력받으세요

## 🎪 코드 테스트

직접 실행해서 다양한 시나리오를 시도해보세요:

```python
n = play_guessing_game()
print(f"게임 종료! 총 시도 횟수: {n}")
```

테스트 체크리스트:
- [ ] 첫 시도에 맞추면 "천재!" 메시지가 나오는가?
- [ ] 5번째에 맞추면 "잘했어요^^" 메시지가 나오는가?
- [ ] 10번째에 맞추면 "분발하세요" 메시지가 나오는가?
- [ ] 0이나 21을 입력하면 다시 입력받는가?
- [ ] 매번 다른 비밀 숫자가 나오는가?

## 🤔 생각해보기

코딩을 시작하기 전에, 접근 방법을 스케치해보세요:
1. 비밀 숫자는 게임 시작 시 한 번만 뽑아야 할까요, 매번 뽑아야 할까요?
2. 시도 횟수 `n`은 언제 증가시켜야 할까요?
3. 어떤 종류의 루프(for / while)가 이 게임에 적합할까요? 왜 그럴까요?

---

## 🎁 보너스 챌린지

기본 과제를 끝냈다면, 도전해보세요!

### 🥉 Easy: 입력 타입 검증
손님이 숫자가 아닌 문자(예: "abc")를 입력하면 프로그램이 멈추지 않도록 만들어보세요.
> 힌트: `try` / `except`를 모른다면, `.isdigit()` 메서드를 활용해보세요.

### 🥈 Medium: 난이도 선택 기능
함수에 기본 매개변수를 추가하여 손님이 난이도를 선택할 수 있게 만들어보세요.

```python
def play_guessing_game(low: int = 1, high: int = 20) -> int:
    ...
```

- 쉬움: 1~10 (`play_guessing_game(1, 10)`)
- 보통: 1~20 (기본값)
- 어려움: 1~50 (`play_guessing_game(1, 50)`)

### 🥇 Hard: 멀티 라운드 + 점수 보드
손님이 여러 라운드를 플레이하고, 결과를 **딕셔너리**에 저장하여 통계를 보여주세요.

```python
# 예상 출력
🎰 라운드 1 종료: 4번 시도
🎰 라운드 2 종료: 2번 시도
🎰 라운드 3 종료: 7번 시도

📊 게임 통계:
- 총 라운드: 3
- 평균 시도 횟수: 4.33
- 최고 기록: 2번
- 최저 기록: 7번
```

> 💡 *힌트: 딕셔너리를 활용하여 멀티 라운드 + 점수 보드를 구현해보세요!*

```python
stats = {"rounds": 0, "total_attempts": 0, "best": None, "worst": None}
```

---

막히면 스레드에 질문을 남겨주세요! 목표는 끝내는 것이 아니라 배우는 것입니다. 천천히 논리를 이해하면서 진행하세요.

행운을 빕니다! 🚀

---
---

# 🎰 Python Practice: Number Guessing Game Booth!

Hey team! Today, you're going to be an **arcade game developer**.

## 🎯 Your Mission

You're a junior game developer working at the local arcade. Your boss has asked you to build a prototype for a new mini-game booth.

The rules are simple: **the computer picks a secret number between 1 and 20, and the customer tries to guess it**. Each time the customer enters a number, the computer gives a hint — "Higher!" or "Lower!". When they finally guess correctly, a different congratulatory message appears based on how many tries it took!

## 📋 The Rules

*What you're given:*
- The `random` module (you've learned this!)
- The `input()` function for taking customer input
- An integer range from 1 to 20

*What you need to do:*
1. Use `random.randrange()` to generate a secret number `x` between 1 and 20
2. Compare each customer guess to the answer
3. Print "더 큰 숫자입니다!" (higher) or "더 작은 숫자입니다!" (lower)
4. Track the number of attempts in variable `n`
5. When they guess correctly, print a message based on `n`

*Constraints you must follow:*
- **Input must be in the range 1~20!** (re-prompt if out of range)
- `n` increases by 1 with each attempt
- The game continues until the customer guesses correctly
- All function names and variables must be `snake_case`

## 💡 Examples

**Example 1: Genius Scenario**
```
Secret number: 10 (computer picks)

숫자를 입력하세요 (1~20): 10
정답입니다!
2번만에 맞춘 당신은 천재!
```
> *Why?* The attempt count is 3 or fewer, so they get the "genius" message!

**Example 2: Average Scenario**
```
Secret number: 7

숫자를 입력하세요 (1~20): 10
더 작은 숫자입니다!
숫자를 입력하세요 (1~20): 5
더 큰 숫자입니다!
숫자를 입력하세요 (1~20): 7
정답입니다!
3번만에 맞춘 당신은 천재!
```

**Example 3: Need-More-Practice Scenario**
```
Secret number: 15

숫자를 입력하세요 (1~20): 1
... (many attempts) ...
숫자를 입력하세요 (1~20): 15
정답입니다!
8번만에 맞추다니 분발하세요.
```

### 🏆 Messages by Attempt Count

| Attempts `n` | Message |
|---|---|
| 1 ~ 3 | `n번만에 맞춘 당신은 천재!` |
| 4 ~ 6 | `n번만에 맞추셨네요. 잘했어요^^` |
| 7+ | `n번만에 맞추다니 분발하세요.` |

## 🎓 What You Should Know

Before you start coding, make sure you understand:
- How to use `random.randrange(a, b)` (remember: `b` is excluded!)
- Writing loops with `while`
- Branching with `if` / `elif` / `else`
- Converting input with `int(input())`
- Incrementing a counter (`n = n + 1`)

## ✅ Your Task

Write a function with this signature:

```python
def play_guessing_game() -> int:
    """
    Run the guessing game and return the number of attempts the customer used.
    """
    # Your code here
    pass
```

**Tips to get you started:**
- `random.randrange(1, 21)` gives a number from 1 to 20 (21 is excluded!)
- Use `while True:` and `break` out when the answer is correct
- Initialize `n = 0` before the loop, then increment each time you take input
- Out-of-range inputs (like 25 or -3) should NOT count — just re-prompt

## 🎪 Test Your Code

Run it yourself and try different scenarios:

```python
n = play_guessing_game()
print(f"Game over! Total attempts: {n}")
```

Test checklist:
- [ ] First-try guess shows "천재!"?
- [ ] 5th-try guess shows "잘했어요^^"?
- [ ] 10th-try guess shows "분발하세요"?
- [ ] Inputs like 0 or 21 trigger a re-prompt?
- [ ] Each game has a different secret number?

## 🤔 Think About It

Before you start coding, sketch out your approach:
1. Should the secret number be picked once at the start, or each time?
2. When exactly should `n` be incremented?
3. Which loop type (for / while) fits this game best? Why?

---

## 🎁 Bonus Challenges

Finished the main task? Try these!

### 🥉 Easy: Input Type Validation
Make the program survive when the customer types something that isn't a number (like "abc").
> Hint: If you don't know `try`/`except` yet, try the `.isdigit()` method.

### 🥈 Medium: Difficulty Selection
Add default parameters so the customer can pick a difficulty level.

```python
def play_guessing_game(low: int = 1, high: int = 20) -> int:
    ...
```

- Easy: 1~10 (`play_guessing_game(1, 10)`)
- Normal: 1~20 (default)
- Hard: 1~50 (`play_guessing_game(1, 50)`)

### 🥇 Hard: Multi-Round + Scoreboard
Let the customer play multiple rounds, and store stats in a **dictionary**.

```python
# Expected output
🎰 Round 1 done: 4 attempts
🎰 Round 2 done: 2 attempts
🎰 Round 3 done: 7 attempts

📊 Game Stats:
- Total rounds: 3
- Average attempts: 4.33
- Best record: 2
- Worst record: 7
```

> 💡 *Hint: Dictionaries are coming up in our next class. Try this as a sneak peek!*

```python
stats = {"rounds": 0, "total_attempts": 0, "best": None, "worst": None}
```

---

Drop your questions in the thread if you get stuck! Remember, the goal is to learn, not just to finish. Take your time and understand the logic.

Good luck! 🚀
