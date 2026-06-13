# 🎰 Python 연습: 로또 번호 생성기 만들기!

여러분, 안녕하세요! 오늘은 한국에서 가장 유명한 게임 중 하나, **로또 6/45**를 직접 코드로 만들어 봅니다.

## 🎯 미션

여러분은 신생 로또 분석 스타트업에 인턴으로 합류했습니다. 첫 번째 임무는 **로또 번호 자동 생성기**를 만드는 것! 매주 일요일 새벽, 친구들이 "이번 주 번호 좀 뽑아줘~"라고 톡을 보내는데 이제는 직접 만든 프로그램으로 답할 수 있겠죠?

## 📋 로또 6/45 규칙

> 한국 로또는 **1부터 45까지의 숫자 중에서 서로 다른 6개의 숫자**를 뽑습니다. 추가로 **보너스 번호 1개**도 뽑는데, 이는 본 번호 6개와 절대 겹치지 않아야 합니다.

*제약사항:*
- `random.randint(a, b)`만 사용 가능 (`random.sample()` 같은 편한 함수는 ❌)
- 같은 숫자가 두 번 나오면 안 됨
- 번호는 **오름차순 정렬**되어 출력
- 함수 3개를 작성합니다 (난이도 점진 상승)

---

## ✅ 과제 1: `generate_lotto_numbers()`

**시나리오:** 가장 기본적인 로또 번호 생성기. 1~45 중에서 서로 다른 6개의 숫자를 뽑아 정렬된 리스트로 반환합니다.

| 항목 | 내용 |
|------|------|
| 입력 | 없음 |
| 출력 | 6개의 정수가 담긴 정렬된 리스트 |
| 제약 | 1~45 범위, 중복 없음, 오름차순 정렬 |

**예시 출력:**
```
[3, 11, 17, 22, 38, 42]
```

> 💡 **힌트:** `while` 루프와 `in` 연산자를 활용해보세요. "이미 뽑은 숫자인지" 확인하는 로직이 핵심입니다.

---

## ✅ 과제 2: `generate_lotto_with_bonus()`

**시나리오:** 이제 보너스 번호까지! 본 번호 6개와 보너스 번호 1개를 모두 생성합니다. 보너스는 본 번호와 겹치면 안 됩니다.

| 항목 | 내용 |
|------|------|
| 입력 | 없음 |
| 출력 | (본 번호 리스트, 보너스 번호) — 튜플로 두 값 반환 |
| 제약 | 보너스는 본 번호 6개와 달라야 함 |

**예시 출력:**
```
본 번호: [5, 12, 19, 23, 31, 40], 보너스: 7
```

> 💡 **힌트:** 함수에서 두 개의 값을 동시에 반환할 수 있다는 것 기억하시죠? `return a, b`

---

## ✅ 과제 3: `generate_multiple_games(num_games=5)`

**시나리오:** 친구가 "한 게임만 뽑지 말고 5게임 자동으로 뽑아줘!"라고 합니다. 게임 수를 인자로 받되, 기본값은 5게임으로 설정하세요.

| 항목 | 내용 |
|------|------|
| 입력 | `num_games` (정수, 기본값 5) |
| 출력 | 게임들이 담긴 리스트 (각 게임은 6개 숫자의 리스트) |
| 제약 | 기본값 동작 필수 |

**예시 출력 (`num_games=3`):**
```
[[2, 8, 15, 22, 33, 41],
 [4, 11, 19, 27, 35, 44],
 [1, 9, 18, 26, 30, 38]]
```

> 💡 **힌트:** 과제 1의 함수를 재사용하세요! 함수 안에서 다른 함수를 호출할 수 있습니다.

---

## 🎪 테스트 케이스

```python
# 테스트 1: 기본 생성기
nums = generate_lotto_numbers()
print(f"본 번호: {nums}")
# 검증: 길이 6, 모두 1~45, 중복 없음, 정렬됨

# 테스트 2: 보너스 포함
main, bonus = generate_lotto_with_bonus()
print(f"본 번호: {main}, 보너스: {bonus}")
# 검증: 보너스가 본 번호에 없음

# 테스트 3: 기본값으로 5게임
games = generate_multiple_games()
print(f"총 {len(games)}게임 생성")  # 5

# 테스트 4: 인자 전달
games = generate_multiple_games(3)
print(f"총 {len(games)}게임 생성")  # 3
```

## 🤔 생각해보기

코딩 시작 전에 이 질문들을 스스로에게 던져보세요:
1. `random.sample()`을 쓸 수 없다면, **중복을 어떻게 방지**할 수 있을까요?
2. 보너스 번호가 본 번호와 겹쳤을 때, **어떻게 다시 뽑게** 만들까요?
3. 같은 로직이 반복된다면, **함수를 재사용**할 수 있을까요?

> 🎯 **목표는 빨리 끝내는 게 아니라 논리를 이해하는 것입니다.**

행운을 빕니다! 🍀

---
---

# 🎰 Python Practice: Build a Lotto Number Generator!

Hey team! Today we're coding one of Korea's most popular games: **Lotto 6/45**.

## 🎯 Your Mission

You've just joined a lotto analytics startup as an intern. Your first task: build an **automatic lotto number generator**! Every Sunday morning, your friends text you "draw some numbers for me!" — soon you'll be answering them with your own program.

## 📋 Lotto 6/45 Rules

> Korean Lotto picks **6 different numbers from 1 to 45**. Additionally, **1 bonus number** is drawn, which must NOT overlap with the 6 main numbers.

*Constraints:*
- Only `random.randint(a, b)` is allowed (no shortcut functions like `random.sample()` ❌)
- No duplicates in the same draw
- Numbers must be returned in **ascending order**
- You'll write 3 functions (gradually increasing in difficulty)

---

## ✅ Task 1: `generate_lotto_numbers()`

**Scenario:** The most basic lotto generator. Pick 6 different numbers from 1~45 and return them as a sorted list.

| Item | Description |
|------|-------------|
| Input | None |
| Output | A sorted list of 6 integers |
| Constraint | Range 1~45, no duplicates, ascending order |

**Example output:**
```
[3, 11, 17, 22, 38, 42]
```

> 💡 **Hint:** Use a `while` loop with the `in` operator. The key logic is: "Have I already picked this number?"

---

## ✅ Task 2: `generate_lotto_with_bonus()`

**Scenario:** Now with a bonus number! Generate 6 main numbers AND 1 bonus number. The bonus must NOT match any of the main numbers.

| Item | Description |
|------|-------------|
| Input | None |
| Output | (main numbers list, bonus number) — return two values as a tuple |
| Constraint | Bonus must differ from all 6 main numbers |

**Example output:**
```
Main: [5, 12, 19, 23, 31, 40], Bonus: 7
```

> 💡 **Hint:** Remember that a function can return multiple values? `return a, b`

---

## ✅ Task 3: `generate_multiple_games(num_games=5)`

**Scenario:** Your friend says "Don't just draw one game — give me 5 auto-picks!" Take the number of games as an argument, with a default value of 5.

| Item | Description |
|------|-------------|
| Input | `num_games` (integer, default 5) |
| Output | A list of games (each game is a list of 6 numbers) |
| Constraint | Default parameter must work |

**Example output (`num_games=3`):**
```
[[2, 8, 15, 22, 33, 41],
 [4, 11, 19, 27, 35, 44],
 [1, 9, 18, 26, 30, 38]]
```

> 💡 **Hint:** Reuse the function from Task 1! You can call functions from inside other functions.

---

## 🎪 Test Cases

```python
# Test 1: Basic generator
nums = generate_lotto_numbers()
print(f"Main numbers: {nums}")
# Verify: length 6, all in 1~45, no duplicates, sorted

# Test 2: With bonus
main, bonus = generate_lotto_with_bonus()
print(f"Main: {main}, Bonus: {bonus}")
# Verify: bonus not in main numbers

# Test 3: Default 5 games
games = generate_multiple_games()
print(f"Total {len(games)} games generated")  # 5

# Test 4: With argument
games = generate_multiple_games(3)
print(f"Total {len(games)} games generated")  # 3
```

## 🤔 Think About It

Before you start coding, ask yourself:
1. Without `random.sample()`, **how do you prevent duplicates**?
2. When the bonus number collides with main numbers, **how do you re-draw**?
3. If the same logic repeats, **can you reuse a function**?

> 🎯 **The goal isn't to finish fast — it's to understand the logic.**

Good luck! 🍀
