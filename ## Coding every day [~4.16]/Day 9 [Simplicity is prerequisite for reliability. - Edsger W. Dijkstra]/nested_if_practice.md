# 🐍 Python 연습: 캐릭터 상태에 따라 스탯이 달라져요!

여러분, 안녕하세요! 이번에는 조건문 안에 조건문이 들어가는 **중첩 if(nested if)**를 연습합니다. 현실의 많은 문제는 이렇게 "조건 안의 조건"으로 이루어져 있어요! 🎮

## 🎯 미션

RPG 게임의 전투 시스템을 만들고 있어요. 캐릭터의 **HP**와 **레벨**에 따라 전투 스탯(공격력, 방어력)이 결정됩니다.

먼저 HP 상태를 확인하고, 그 안에서 다시 레벨을 확인하여 알맞은 스탯을 출력하세요.

## 📋 스탯 규칙

| HP 상태 | 레벨 | 공격력 (ATK) | 방어력 (DEF) |
|---------|------|------------|------------|
| HP ≥ 50 (건강) | 레벨 ≥ 50 | 200 | 100 |
| HP ≥ 50 (건강) | 레벨 < 50  | 100 | 50  |
| HP < 50 (부상) | 레벨 ≥ 50 | 100 | 50  |
| HP < 50 (부상) | 레벨 < 50  | 50  | 25  |

## 📋 규칙

*주어지는 것:*  
• 정수 `hp` — 캐릭터의 현재 체력   
• 정수 `level` — 캐릭터의 현재 레벨

*해야 할 일:*
1. HP가 50 이상인지 확인 (건강 / 부상)
2. 그 안에서 다시 레벨이 50 이상인지 확인 (고레벨 / 저레벨)
3. 해당하는 공격력과 방어력을 출력

*반드시 따라야 할 제약사항:*
• **중첩 if**를 사용해야 합니다 — 바깥 `if`/`else` 안에 또 다른 `if`/`else`가 있어야 해요
• 입력은 코드 스켈레톤에 이미 제공되어 있습니다 — `input()` 부분은 건드리지 마세요!

## 💡 예제

**예제 1:**
```
입력: hp = 80, level = 60
출력:
ATK: 200
DEF: 100
```
왜? HP 80 ≥ 50 (건강) ✅, 레벨 60 ≥ 50 (고레벨) ✅ → 풀 스탯!

**예제 2:**
```
입력: hp = 80, level = 30
출력:
ATK: 100
DEF: 50
```
왜? HP 80 ≥ 50 (건강) ✅, 레벨 30 < 50 (저레벨) ❌ → 중간 스탯

**예제 3:**
```
입력: hp = 20, level = 70
출력:
ATK: 100
DEF: 50
```
왜? HP 20 < 50 (부상) ❌, 레벨 70 ≥ 50 (고레벨) ✅ → 부상으로 스탯 감소

**예제 4:**
```
입력: hp = 20, level = 30
출력:
ATK: 50
DEF: 25
```
왜? HP 20 < 50 (부상) ❌, 레벨 30 < 50 (저레벨) ❌ → 최저 스탯

## 🎓 알아야 할 것

코딩을 시작하기 전에, 다음을 이해하고 있는지 확인하세요:
• `if` / `else` 조건문이 어떻게 작동하는지
• 들여쓰기(indentation)가 Python에서 어떤 의미인지
• 중첩 if가 무엇인지 (아래 섹션 참고!)

## 🆕 새로운 개념: 중첩 if (Nested if)

`if` 블록 **안에** 또 다른 `if`를 넣을 수 있습니다. 이것을 **중첩 if**라고 해요.

```python
if 바깥_조건:
    # 바깥 조건이 True일 때만 여기 진입
    if 안쪽_조건:
        # 바깥도 True, 안쪽도 True
    else:
        # 바깥은 True, 안쪽은 False
else:
    # 바깥 조건이 False일 때 여기 진입
    if 안쪽_조건:
        # 바깥은 False, 안쪽은 True
    else:
        # 바깥도 False, 안쪽도 False
```

**핵심:** 안쪽 `if`는 바깥 조건을 통과한 경우에만 실행됩니다. 마치 건물에 들어가야(바깥 조건) 엘리베이터를 탈 수 있는(안쪽 조건) 것처럼요!

이 문제에 적용하면:
```python
if hp >= 50:          # 먼저 HP 확인
    if level >= 50:   # HP가 충분할 때만 레벨 확인
        ...           # 건강 + 고레벨
    else:
        ...           # 건강 + 저레벨
else:
    if level >= 50:   # HP가 부족할 때도 레벨 확인
        ...           # 부상 + 고레벨
    else:
        ...           # 부상 + 저레벨
```

## ✅ 과제

다음 시그니처로 함수를 작성하세요:
```python
def calculate_stats(hp: int, level: int) -> None:
    # 여기에 코드 작성
    pass
```

**시작하는 데 도움이 될 팁:**
• 들여쓰기를 주의하세요! 안쪽 `if`는 바깥 `if` 블록보다 한 단계 더 들여써야 합니다
• 예제 2와 예제 3의 출력이 같은데, 두 경우가 같은 조건에 해당할까요? 🤔
• `print(f"ATK: {공격력}")` 형태로 출력하면 깔끔합니다

## 🎪 코드 테스트

다음 테스트 케이스를 실행해보세요:

```python
# 테스트 1: 건강 + 고레벨
calculate_stats(80, 60)
# 예상 출력:
# ATK: 200
# DEF: 100

# 테스트 2: 건강 + 저레벨
calculate_stats(80, 30)
# 예상 출력:
# ATK: 100
# DEF: 50

# 테스트 3: 부상 + 고레벨
calculate_stats(20, 70)
# 예상 출력:
# ATK: 100
# DEF: 50

# 테스트 4: 부상 + 저레벨
calculate_stats(20, 30)
# 예상 출력:
# ATK: 50
# DEF: 25

# 테스트 5: 경계값 — 정확히 HP 50
calculate_stats(50, 60)
# 예상 출력:
# ATK: 200
# DEF: 100

# 테스트 6: 경계값 — 정확히 레벨 50
calculate_stats(80, 50)
# 예상 출력:
# ATK: 200
# DEF: 100

# 테스트 7: 경계값 — HP 49
calculate_stats(49, 60)
# 예상 출력:
# ATK: 100
# DEF: 50
```

## 🤔 생각해보기

1. 예제 2(건강 + 저레벨)와 예제 3(부상 + 고레벨)의 출력이 같습니다. 그렇다면 두 조건을 `or`로 합쳐서 하나의 `if`로 만들 수 있을까요? 코드가 더 좋아질까요, 나빠질까요?
2. 바깥 `if`와 안쪽 `if`의 들여쓰기 단계가 다릅니다. 만약 들여쓰기를 잘못 맞추면 어떤 오류가 날까요? 직접 틀리게 써보고 Python의 오류 메시지를 확인해보세요!
3. 이 문제를 중첩 `if` 없이 `elif`만으로 해결할 수 있을까요? 조건을 어떻게 써야 할까요?

막히면 스레드에 질문을 남겨주세요! 목표는 끝내는 것이 아니라 배우는 것입니다. 천천히 논리를 이해하면서 진행하세요.

행운을 빕니다! 🚀

---
---

# 🐍 Python Practice: Character Stats Change Based on Status!

Hey team! This time we're practicing **nested if** — a conditional statement inside another conditional statement. A lot of real-world problems work exactly like this: "conditions within conditions"! 🎮

## 🎯 Your Mission

You're building the combat system for an RPG game. A character's battle stats (attack and defense) are determined by both **HP** and **level**.

First check the HP status, then check the level within each HP case, and print the appropriate stats.

## 📋 Stat Rules

| HP Status | Level | ATK | DEF |
|-----------|-------|-----|-----|
| HP ≥ 50 (healthy) | level ≥ 50 | 200 | 100 |
| HP ≥ 50 (healthy) | level < 50  | 100 | 50  |
| HP < 50 (injured) | level ≥ 50  | 100 | 50  |
| HP < 50 (injured) | level < 50  | 50  | 25  |

## 📋 The Rules

*What you're given:*
• An integer `hp` — the character's current health points
• An integer `level` — the character's current level

*What you need to do:*
1. Check whether HP is 50 or above (healthy / injured)
2. Inside each case, check whether level is 50 or above (high / low)
3. Print the corresponding attack and defense values

*Constraints you must follow:*
• You must use **nested if** — there must be an `if`/`else` inside another `if`/`else`
• The input section is already provided in the skeleton — don't touch the `input()` lines!

## 💡 Example Time

**Example 1:**
```
Input: hp = 80, level = 60
Output:
ATK: 200
DEF: 100
```
Why? HP 80 ≥ 50 (healthy) ✅, level 60 ≥ 50 (high level) ✅ → full stats!

**Example 2:**
```
Input: hp = 80, level = 30
Output:
ATK: 100
DEF: 50
```
Why? HP 80 ≥ 50 (healthy) ✅, level 30 < 50 (low level) ❌ → mid stats

**Example 3:**
```
Input: hp = 20, level = 70
Output:
ATK: 100
DEF: 50
```
Why? HP 20 < 50 (injured) ❌, level 70 ≥ 50 (high level) ✅ → stats drop due to injury

**Example 4:**
```
Input: hp = 20, level = 30
Output:
ATK: 50
DEF: 25
```
Why? HP 20 < 50 (injured) ❌, level 30 < 50 (low level) ❌ → minimum stats

## 🎓 What You Should Know

Before you start coding, make sure you understand:
• How `if` / `else` conditional statements work
• What indentation means in Python
• What nested if is (see the section below!)

## 🆕 New Concept: Nested if

You can put another `if` **inside** an `if` block. This is called a **nested if**.

```python
if outer_condition:
    # only enters here when outer condition is True
    if inner_condition:
        # outer True AND inner True
    else:
        # outer True, inner False
else:
    # only enters here when outer condition is False
    if inner_condition:
        # outer False, inner True
    else:
        # outer False AND inner False
```

**Key point:** The inner `if` only runs if the outer condition was already passed. It's like needing to enter a building (outer condition) before you can take the elevator (inner condition)!

Applied to this problem:
```python
if hp >= 50:          # check HP first
    if level >= 50:   # only check level if HP is sufficient
        ...           # healthy + high level
    else:
        ...           # healthy + low level
else:
    if level >= 50:   # check level even when HP is low
        ...           # injured + high level
    else:
        ...           # injured + low level
```

## ✅ Your Task

Write a function with this signature:
```python
def calculate_stats(hp: int, level: int) -> None:
    # Your code here
    pass
```

**Tips to get you started:**
• Watch your indentation! The inner `if` must be indented one level deeper than the outer `if`
• Examples 2 and 3 have the same output — but do they belong to the same condition? 🤔
• Use `print(f"ATK: {attack}")` style for clean output

## 🎪 Test Your Code

Try running these test cases:

```python
# Test 1: healthy + high level
calculate_stats(80, 60)
# Expected output:
# ATK: 200
# DEF: 100

# Test 2: healthy + low level
calculate_stats(80, 30)
# Expected output:
# ATK: 100
# DEF: 50

# Test 3: injured + high level
calculate_stats(20, 70)
# Expected output:
# ATK: 100
# DEF: 50

# Test 4: injured + low level
calculate_stats(20, 30)
# Expected output:
# ATK: 50
# DEF: 25

# Test 5: boundary — exactly HP 50
calculate_stats(50, 60)
# Expected output:
# ATK: 200
# DEF: 100

# Test 6: boundary — exactly level 50
calculate_stats(80, 50)
# Expected output:
# ATK: 200
# DEF: 100

# Test 7: boundary — HP 49
calculate_stats(49, 60)
# Expected output:
# ATK: 100
# DEF: 50
```

## 🤔 Think About It

1. Examples 2 (healthy + low level) and 3 (injured + high level) have the same output. Could you combine them into one condition using `or`? Would that make the code better or worse?
2. The outer and inner `if` blocks have different indentation levels. What error would Python give if you got the indentation wrong? Try it deliberately and read the error message!
3. Could you solve this problem using only `elif` with no nesting at all? What would the conditions look like?

Drop your questions in the thread if you get stuck! Remember, the goal is to learn, not just to finish. Take your time and understand the logic.

Good luck! 🚀
