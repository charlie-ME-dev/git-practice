# 🎲 Python 연습: 숫자 맞히기 게임 만들기!

여러분, 안녕하세요! 오늘은 `random` 모듈을 사용해서 진짜 게임을 만들어볼 거예요. 코드 한 줄 한 줄이 모여서 친구들과 함께 즐길 수 있는 게임이 됩니다!

## 🎯 미션

게임 회사에 인턴으로 막 입사했다고 상상해보세요. 첫 번째 임무는 **숫자 맞히기 게임**의 핵심 로직을 만드는 것입니다. 컴퓨터가 비밀 숫자를 고르면, 플레이어가 그 숫자를 맞히려고 시도합니다. 매번 추측할 때마다 게임은 "너무 작아요", "너무 커요", 또는 "정답!"이라고 알려줍니다.

여러분은 이 게임을 만들기 위한 작은 함수들을 단계별로 작성하게 됩니다.

## 📋 규칙

*사용할 수 있는 도구:*
- `random.randint(low, high)` — `low`와 `high` 사이의 정수를 무작위로 반환 (양 끝 포함)
- `random.random()` — 0.0 이상 1.0 미만의 실수를 무작위로 반환
- `while` 루프, `if`/`elif`/`else`, 리스트, 딕셔너리, 튜플, 셋

*따라야 할 제약사항:*
- 함수 이름과 변수 이름은 모두 **snake_case**로 작성하세요
- `import random`을 파일 맨 위에 추가하는 것을 잊지 마세요
- 각 함수는 **하나의 명확한 일**만 해야 합니다

## 💡 예제

**함수 1: `generate_secret_number(low, high)`**
```
generate_secret_number(1, 10)  →  7  (또는 1~10 사이의 다른 숫자)
generate_secret_number(1, 100) →  42 (또는 1~100 사이의 다른 숫자)
```

**함수 2: `check_guess(guess, secret)`**
```
check_guess(3, 7)  →  "too low"
check_guess(9, 7)  →  "too high"
check_guess(7, 7)  →  "correct"
```

**함수 3: `flip_coin_until_heads()`**
동전을 앞면이 나올 때까지 계속 던지고, 몇 번 던졌는지 반환합니다.
```
flip_coin_until_heads()  →  1  (운이 좋게 첫 번째에 앞면!)
flip_coin_until_heads()  →  4  (앞앞뒤앞 — 4번째에 앞면)
```
> 💡 힌트: `random.random() < 0.5`이면 앞면이라고 정할 수 있어요.

**함수 4: `play_guessing_game(low, high, max_attempts)`**
전체 게임을 진행합니다. 비밀 숫자를 만들고, 플레이어로부터 추측을 받고, 결과를 알려줍니다. 플레이어가 맞히면 사용한 시도 횟수를 반환하고, 시도 횟수를 모두 사용하면 `-1`을 반환합니다.

## 📦 함수 명세

| 함수 이름 | 입력 | 출력 | 설명 |
|----------|------|------|------|
| `generate_secret_number` | `low: int`, `high: int` | `int` | `low`~`high` 범위의 무작위 정수 |
| `check_guess` | `guess: int`, `secret: int` | `str` | `"too low"`, `"too high"`, `"correct"` 중 하나 |
| `flip_coin_until_heads` | (없음) | `int` | 앞면이 나올 때까지 던진 횟수 |
| `play_guessing_game` | `low: int`, `high: int`, `max_attempts: int` | `int` | 사용한 시도 횟수, 실패 시 `-1` |

## 🎓 알아야 할 것

코딩을 시작하기 전에, 다음을 이해하고 있는지 확인하세요:
- `import random`으로 모듈을 가져오는 방법
- `while` 루프가 언제 멈추는지
- `if`/`elif`/`else`로 여러 조건을 비교하는 방법
- 함수에서 값을 `return`하는 방법

## ✅ 과제

스켈레톤 파일에 있는 네 개의 함수를 완성하세요. 각 함수는 위 명세대로 동작해야 합니다.

## 🎪 코드 테스트

스켈레톤 파일에 테스트 코드가 이미 들어 있습니다. 파일을 실행해서 결과를 확인하세요:

```python
# 테스트 예시
secret = generate_secret_number(1, 10)
print(f"비밀 숫자: {secret}")  # 1~10 사이의 숫자가 나와야 함

print(check_guess(5, 7))   # "too low"
print(check_guess(8, 7))   # "too high"
print(check_guess(7, 7))   # "correct"

flips = flip_coin_until_heads()
print(f"앞면이 나올 때까지 {flips}번 던짐")
```

## 🤔 생각해보기

코딩을 시작하기 전에, 다음 질문에 답해보세요:
1. `random.randint(1, 10)`은 `10`을 포함할까요, 포함하지 않을까요? (힌트: 직접 실험해보세요!)
2. `flip_coin_until_heads`에서 어떤 종류의 루프가 적합할까요? `for`일까요, `while`일까요? 왜요?
3. `play_guessing_game`은 다른 세 함수 중 어떤 것들을 안에서 호출하면 좋을까요?

막히면 언제든지 질문하세요. 목표는 빨리 끝내는 것이 아니라 게임이 어떻게 작동하는지 이해하는 것입니다.

행운을 빕니다! 🎲

---
---

# 🎲 Python Practice: Build a Number Guessing Game!

Hey team! Today we're using the `random` module to build a real game. Line by line, you'll create something you can actually play with friends!

## 🎯 Your Mission

Imagine you've just started as an intern at a game company. Your first assignment is to build the core logic of a **Number Guessing Game**. The computer picks a secret number, and the player tries to guess it. After each guess, the game says "too low", "too high", or "correct!".

You'll write small functions step by step that come together to make this game work.

## 📋 The Rules

*Tools you can use:*
- `random.randint(low, high)` — returns a random integer between `low` and `high` (both inclusive)
- `random.random()` — returns a random float between 0.0 and 1.0 (1.0 not included)
- `while` loops, `if`/`elif`/`else`, lists, dictionaries, tuples, sets

*Constraints to follow:*
- All function and variable names must use **snake_case**
- Don't forget to add `import random` at the top of your file
- Each function should do **one clear job**

## 💡 Examples

**Function 1: `generate_secret_number(low, high)`**
```
generate_secret_number(1, 10)  →  7  (or any other number between 1 and 10)
generate_secret_number(1, 100) →  42 (or any other number between 1 and 100)
```

**Function 2: `check_guess(guess, secret)`**
```
check_guess(3, 7)  →  "too low"
check_guess(9, 7)  →  "too high"
check_guess(7, 7)  →  "correct"
```

**Function 3: `flip_coin_until_heads()`**
Keep flipping a coin until you get heads, and return how many flips it took.
```
flip_coin_until_heads()  →  1  (lucky! heads on the first flip)
flip_coin_until_heads()  →  4  (tails-tails-tails-heads — 4 flips)
```
> 💡 Hint: You can decide that `random.random() < 0.5` counts as heads.

**Function 4: `play_guessing_game(low, high, max_attempts)`**
Runs the whole game. Generates a secret number, takes guesses from the player, and reports results. Returns the number of attempts used if the player wins, or `-1` if they run out of attempts.

## 📦 Function Specs

| Function name | Input | Output | Description |
|---------------|-------|--------|-------------|
| `generate_secret_number` | `low: int`, `high: int` | `int` | Random integer in range `[low, high]` |
| `check_guess` | `guess: int`, `secret: int` | `str` | One of `"too low"`, `"too high"`, `"correct"` |
| `flip_coin_until_heads` | (none) | `int` | Number of flips until heads appears |
| `play_guessing_game` | `low: int`, `high: int`, `max_attempts: int` | `int` | Attempts used, or `-1` if failed |

## 🎓 What You Should Know

Before you start coding, make sure you understand:
- How to import a module with `import random`
- When a `while` loop stops
- How to compare multiple conditions with `if`/`elif`/`else`
- How to `return` a value from a function

## ✅ Your Task

Complete the four functions in the skeleton file. Each function should behave according to the spec above.

## 🎪 Test Your Code

The skeleton file already has test code in it. Run the file to see results:

```python
# Test examples
secret = generate_secret_number(1, 10)
print(f"Secret number: {secret}")  # Should print a number between 1 and 10

print(check_guess(5, 7))   # "too low"
print(check_guess(8, 7))   # "too high"
print(check_guess(7, 7))   # "correct"

flips = flip_coin_until_heads()
print(f"It took {flips} flips to get heads")
```

## 🤔 Think About It

Before coding, answer these questions:
1. Does `random.randint(1, 10)` include `10`, or not? (Hint: try it yourself!)
2. For `flip_coin_until_heads`, what kind of loop fits better — `for` or `while`? Why?
3. Which of the other three functions might `play_guessing_game` call inside itself?

Ask questions whenever you're stuck. The goal isn't to finish fast — it's to understand how the game works.

Good luck! 🎲
