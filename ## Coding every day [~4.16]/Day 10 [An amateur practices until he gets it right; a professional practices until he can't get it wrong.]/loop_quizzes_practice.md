# 🐍 Python 연습: 반복문 마스터하기!

안녕하세요, 여러분! 오늘은 `for`와 `while` 반복문을 실전 문제로 연습해볼 시간입니다. 기초부터 고급까지 총 15개 문제가 준비되어 있어요. 천천히, 꼼꼼히 읽으면서 풀어보세요!

---

## 📚 알아야 할 것 / Prerequisites

코딩을 시작하기 전에 다음 개념을 이해하고 있는지 확인하세요:
- `for` 반복문과 `range()` 사용법
- `while` 반복문과 탈출 조건
- `if / elif / else` 조건문
- `input()`, `int()` 를 이용한 사용자 입력
- 누산기 패턴 (`total = total + x`)
- 중첩 반복문 (반복문 안의 반복문)

---
---

## 🌱 기초 단계 (Basic) — Quiz 1–5

---

### 🎯 Quiz 1: 로켓 발사 카운터 / Rocket Launch Counter

#### 🇰🇷 한국어

**시나리오:** 여러분은 우주 발사 통제 센터의 주니어 엔지니어입니다. 발사 전 카운트업과 카운트다운 시스템을 만들어야 합니다!

**미션 A — 카운트업:** 1부터 10까지 숫자를 한 줄씩 출력하세요.

**예상 출력:**
```
1
2
3
...
10
```

**미션 B — 카운트다운:** 10부터 1까지 카운트다운한 후, `"발사!"` 를 출력하세요.

**예상 출력:**
```
10
9
8
...
1
발사!
```

**힌트:**
- `range(시작, 끝)` — 끝 숫자는 포함되지 않아요
- 카운트다운은 `range(시작, 끝, 단계)` 에서 단계를 음수로!

---

#### 🇺🇸 English

**Scenario:** You're a junior engineer at a space launch control center. You need to build a count-up and countdown system before liftoff!

**Mission A — Count Up:** Print numbers from 1 to 10, each on a new line.

**Expected Output:**
```
1
2
3
...
10
```

**Mission B — Countdown:** Count down from 10 to 1, then print `"Blast off!"`.

**Expected Output:**
```
10
9
...
1
Blast off!
```

**Hints:**
- `range(start, stop)` — the stop value is excluded
- For countdown, use `range(start, stop, step)` with a negative step!

---

### 🎯 Quiz 2: 재고 합산기 / Inventory Totals

#### 🇰🇷 한국어

**시나리오:** 여러분은 편의점 아르바이트생입니다. 오늘 하루 팔린 상품 개수를 합산해야 해요.

**미션 A — 1부터 100까지의 합:** 1부터 100까지 모든 숫자를 더한 값을 출력하세요.

**예상 출력:**
```
5050
```

**미션 B — 짝수만 합산:** 1부터 20까지 짝수만 골라서 더한 값을 출력하세요.

**예상 출력:**
```
110
```

**힌트:**
- 누산기 패턴: `total = 0` 으로 시작하고 `total = total + i` 로 더하기
- 짝수 판별: `i % 2 == 0`

---

#### 🇺🇸 English

**Scenario:** You work part-time at a convenience store. You need to tally up the total items sold today.

**Mission A — Sum 1 to 100:** Print the sum of all numbers from 1 to 100.

**Expected Output:**
```
5050
```

**Mission B — Sum of Even Numbers:** Print the sum of all even numbers from 1 to 20.

**Expected Output:**
```
110
```

**Hints:**
- Accumulator pattern: start with `total = 0`, then `total = total + i`
- Even number check: `i % 2 == 0`

---

### 🎯 Quiz 3: 구구단 출력기 / Multiplication Table Generator

#### 🇰🇷 한국어

**시나리오:** 여러분은 초등학교 교육 앱을 만드는 스타트업의 인턴입니다. 사용자가 원하는 단의 구구단을 출력하는 기능을 개발해야 합니다!

**미션:** 사용자에게 숫자를 입력받아, 해당 단의 구구단을 출력하세요.

**예상 출력 (입력값: 5):**
```
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
...
5 x 9 = 45
```

**힌트:**
- `n = int(input("단을 입력하세요: "))` 로 입력받기
- f-string: `f"{n} x {i} = {n * i}"`

---

#### 🇺🇸 English

**Scenario:** You're an intern at an ed-tech startup building a math learning app for elementary kids. Your task: build a multiplication table generator!

**Mission:** Ask the user for a number and print that number's multiplication table.

**Expected Output (input: 5):**
```
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
...
5 x 9 = 45
```

**Hints:**
- Get input: `n = int(input("Enter a number: "))`
- f-string: `f"{n} x {i} = {n * i}"`

---

### 🎯 Quiz 4: 짝수 필터 / Even Number Filter

#### 🇰🇷 한국어

**시나리오:** 데이터 분석팀에서 숫자 목록 중 짝수만 추려내는 필터 프로그램을 요청했습니다.

**미션:** 1부터 20까지의 숫자 중 짝수만 출력하세요. 두 가지 방법으로 풀어보세요!

**방법 1:** `if` 문으로 짝수 판별
**방법 2:** `range()` 의 세 번째 인자(step) 활용

**예상 출력:**
```
2
4
6
8
10
12
14
16
18
20
```

**힌트:**
- 방법 1: `if i % 2 == 0:`
- 방법 2: `range(2, 21, 2)`

---

#### 🇺🇸 English

**Scenario:** The data analytics team needs a filter program that picks out only the even numbers from a list.

**Mission:** Print only the even numbers from 1 to 20. Try solving it two different ways!

**Method 1:** Use an `if` statement to check for even numbers
**Method 2:** Use the step parameter in `range()`

**Expected Output:**
```
2
4
6
...
20
```

**Hints:**
- Method 1: `if i % 2 == 0:`
- Method 2: `range(2, 21, 2)`

---

### 🎯 Quiz 5: 사용자 입력 합산 / User Input Accumulator

#### 🇰🇷 한국어

**시나리오:** 카페 포스 시스템을 만들고 있습니다. 손님이 주문할 때마다 가격을 입력하고, 0을 입력하면 계산이 끝나고 총합을 보여주는 기능이 필요합니다.

**미션:** 사용자가 숫자를 계속 입력하고, `0`을 입력하면 멈추고 합계를 출력하세요.

**예상 실행 예시:**
```
숫자를 입력하세요 (0이면 종료): 4500
숫자를 입력하세요 (0이면 종료): 3000
숫자를 입력하세요 (0이면 종료): 2500
숫자를 입력하세요 (0이면 종료): 0
합계: 10000
```

**힌트:**
- `while True:` 와 `break` 조합
- `if num == 0: break`

---

#### 🇺🇸 English

**Scenario:** You're building a POS (point-of-sale) system for a café. Each time a customer orders, the cashier enters the price. When they enter 0, the system shows the total.

**Mission:** Keep reading numbers from the user until they enter `0`, then print the total.

**Sample Run:**
```
Enter a number (0 to stop): 4500
Enter a number (0 to stop): 3000
Enter a number (0 to stop): 2500
Enter a number (0 to stop): 0
Total: 10000
```

**Hints:**
- Use `while True:` with `break`
- `if num == 0: break`

---
---

## 🌿 중급 단계 (Intermediate) — Quiz 6–10

---

### 🎯 Quiz 6: 팩토리얼 계산기 / Factorial Calculator

#### 🇰🇷 한국어

**시나리오:** 확률 계산 앱을 만드는 팀에 합류했습니다. 팩토리얼은 확률 계산의 핵심입니다!

**미션:** 사용자가 입력한 숫자 `n`의 팩토리얼을 계산하세요.
- `5! = 5 × 4 × 3 × 2 × 1 = 120`

**예상 출력 (입력값: 5):**
```
120
```

**힌트:**
- 누산기 시작값은 `1` (곱셈이니까요!)
- `factorial = factorial * i`

---

#### 🇺🇸 English

**Scenario:** You've joined a team building a probability calculator app. Factorials are at the heart of probability math!

**Mission:** Calculate the factorial of a number `n` entered by the user.
- `5! = 5 × 4 × 3 × 2 × 1 = 120`

**Expected Output (input: 5):**
```
120
```

**Hints:**
- Start your accumulator at `1` (it's multiplication!)
- `factorial = factorial * i`

---

### 🎯 Quiz 7: 자릿수 세기 / Digit Counter

#### 🇰🇷 한국어

**시나리오:** 금융 앱에서 사용자가 입력한 숫자가 몇 자리인지 확인해야 합니다 (예: 계좌번호 자릿수 검증).

**미션:** 사용자가 입력한 양의 정수의 자릿수를 세서 출력하세요.

**예상 출력 (입력값: 12345):**
```
5
```

**힌트:**
- `n // 10` 을 반복하면 마지막 자리가 잘려나가요
- `n > 0` 인 동안 반복!

---

#### 🇺🇸 English

**Scenario:** A banking app needs to verify how many digits a number has (e.g., validating account number length).

**Mission:** Count and print the number of digits in a positive integer entered by the user.

**Expected Output (input: 12345):**
```
5
```

**Hints:**
- `n // 10` chops off the last digit each time
- Loop `while n > 0`!

---

### 🎯 Quiz 8: 자릿수 합산 / Digit Sum Calculator

#### 🇰🇷 한국어

**시나리오:** 주민등록번호 검증 알고리즘처럼, 숫자의 각 자릿수를 더하는 계산이 필요할 때가 많습니다.

**미션:** 사용자가 입력한 양의 정수의 각 자릿수를 모두 더한 값을 출력하세요.

**예상 출력 (입력값: 123):**
```
6
```
(1 + 2 + 3 = 6)

**힌트:**
- `n % 10` 으로 마지막 자리 추출
- `n // 10` 으로 마지막 자리 제거

---

#### 🇺🇸 English

**Scenario:** Many verification algorithms (like ID number checks) require summing the individual digits of a number.

**Mission:** Print the sum of all digits in a positive integer entered by the user.

**Expected Output (input: 123):**
```
6
```
(1 + 2 + 3 = 6)

**Hints:**
- `n % 10` extracts the last digit
- `n // 10` removes the last digit

---

### 🎯 Quiz 9: 숫자 뒤집기 / Number Reverser

#### 🇰🇷 한국어

**시나리오:** 회문(palindrome) 검사 알고리즘의 첫 단계는 숫자를 뒤집는 것입니다. 보안 시스템이나 데이터 검증에서 자주 쓰이는 기술이에요.

**미션:** 사용자가 입력한 양의 정수를 뒤집어서 출력하세요.

**예상 출력 (입력값: 12345):**
```
54321
```

**힌트:**
- `digit = n % 10` 으로 마지막 자리 추출
- `reversed_num = reversed_num * 10 + digit` 로 앞에 붙이기

---

#### 🇺🇸 English

**Scenario:** The first step of a palindrome checker is reversing a number — a technique used in security systems and data validation.

**Mission:** Reverse a positive integer entered by the user and print the result.

**Expected Output (input: 12345):**
```
54321
```

**Hints:**
- `digit = n % 10` extracts the last digit
- `reversed_num = reversed_num * 10 + digit` builds the reversed number

---

### 🎯 Quiz 10: 최댓값 찾기 / Maximum Finder

#### 🇰🇷 한국어

**시나리오:** 스포츠 점수 추적 앱을 만들고 있습니다. 선수들의 점수를 입력받아 최고 점수를 찾아야 합니다.

**미션:** 사용자에게 계속 숫자를 입력받다가 `-1`을 입력하면 멈추고, 그 중 가장 큰 숫자를 출력하세요.

**예상 실행 예시:**
```
숫자 입력 (-1이면 종료): 85
숫자 입력 (-1이면 종료): 92
숫자 입력 (-1이면 종료): 78
숫자 입력 (-1이면 종료): -1
최댓값: 92
```

**힌트:**
- 첫 번째로 입력된 숫자가 자동으로 현재 최댓값이 됩니다
- `if num > max_num:` 으로 비교

---

#### 🇺🇸 English

**Scenario:** You're building a sports score tracker. The app reads scores from users and finds the highest one.

**Mission:** Keep reading numbers until the user enters `-1`, then print the maximum value.

**Sample Run:**
```
Enter a number (-1 to stop): 85
Enter a number (-1 to stop): 92
Enter a number (-1 to stop): 78
Enter a number (-1 to stop): -1
Maximum: 92
```

**Hints:**
- The first number entered naturally becomes the current maximum
- Compare with `if num > max_num:`

---
---

## 🔥 고급 단계 (Advanced) — Quiz 11–15

---

### 🎯 Quiz 11: 별표 정사각형 / Star Square

#### 🇰🇷 한국어

**시나리오:** 터미널 기반 게임을 만드는 인디 개발자입니다. 게임 맵의 경계선을 별표(*)로 그려야 합니다.

**미션:** 5×5 정사각형을 별표로 출력하세요.

**예상 출력:**
```
*****
*****
*****
*****
*****
```

**힌트:**
- 중첩 반복문: 바깥 반복문(행) + 안쪽 반복문(열)
- `print("*", end="")` 로 같은 줄에 출력
- `print()` 로 줄바꿈

---

#### 🇺🇸 English

**Scenario:** You're an indie game developer drawing map borders in a terminal-based game using asterisks.

**Mission:** Print a 5×5 square using asterisks.

**Expected Output:**
```
*****
*****
*****
*****
*****
```

**Hints:**
- Nested loops: outer loop (rows) + inner loop (columns)
- `print("*", end="")` prints on the same line
- `print()` creates a new line

---

### 🎯 Quiz 12: 직각삼각형 패턴 / Right Triangle Pattern

#### 🇰🇷 한국어

**시나리오:** 같은 게임에서 이번엔 삼각형 모양의 장애물을 그려야 합니다.

**미션:** 5행의 직각삼각형 패턴을 출력하세요.

**예상 출력:**
```
*
**
***
****
*****
```

**힌트:**
- 1행에는 별 1개, 2행에는 별 2개... 규칙이 보이나요?
- 안쪽 반복문의 범위를 바깥 반복문 변수 `i` 와 연결해보세요

---

#### 🇺🇸 English

**Scenario:** Still in game dev mode — now you need to draw a triangular obstacle.

**Mission:** Print a right triangle pattern with 5 rows.

**Expected Output:**
```
*
**
***
****
*****
```

**Hints:**
- Row 1 has 1 star, row 2 has 2 stars... see the pattern?
- Link the inner loop's range to the outer loop variable `i`

---

### 🎯 Quiz 13: 소수 판별기 / Prime Number Checker

#### 🇰🇷 한국어

**시나리오:** 암호화 시스템 개발팀에서 인턴을 하고 있습니다. 소수(prime number)는 암호화 알고리즘의 핵심입니다!

**미션:** 사용자가 입력한 숫자가 소수인지 판별하세요.
- 소수: 1과 자기 자신으로만 나누어떨어지는 수 (2, 3, 5, 7, 11...)

**예상 출력 (입력값: 29):**
```
29 는 소수입니다
```

**예상 출력 (입력값: 12):**
```
12 는 소수가 아닙니다
```

**힌트:**
- 2부터 `n-1` 까지 나누어 떨어지는 수가 있는지 확인
- 하나라도 나누어 떨어지면 → 소수 아님
- `break` 로 일찍 탈출 가능!

---

#### 🇺🇸 English

**Scenario:** You're interning at a cryptography team. Prime numbers are the backbone of encryption algorithms!

**Mission:** Check whether a number entered by the user is prime.
- Prime: only divisible by 1 and itself (2, 3, 5, 7, 11...)

**Expected Output (input: 29):**
```
29 is prime
```

**Expected Output (input: 12):**
```
12 is not prime
```

**Hints:**
- Check if anything from 2 to `n-1` divides `n` evenly
- If any divisor is found → not prime
- Use `break` to exit early!

---

### 🎯 Quiz 14: 피보나치 수열 / Fibonacci Sequence

#### 🇰🇷 한국어

**시나리오:** 자연 다큐멘터리 앱을 만들고 있습니다. 꽃잎 수, 나선형 패턴 등 자연에서 자주 나타나는 피보나치 수열을 시각화하는 기능이 필요합니다!

**미션:** 피보나치 수열의 첫 10개 숫자를 출력하세요.
- 규칙: 앞 두 숫자의 합이 다음 숫자
- `0, 1, 1, 2, 3, 5, 8, 13, 21, 34`

**예상 출력:**
```
0
1
1
2
3
5
8
13
21
34
```

**힌트:**
- 두 변수 `a = 0`, `b = 1` 로 시작
- 매 반복마다: `a` 를 출력하고, `a`와 `b` 를 업데이트
- `temp` 변수를 이용해 값을 교환!

---

#### 🇺🇸 English

**Scenario:** You're building a nature documentary app. You need to generate the Fibonacci sequence — a pattern found everywhere in nature, from flower petals to spiral shells!

**Mission:** Print the first 10 numbers of the Fibonacci sequence.
- Rule: each number is the sum of the two before it
- `0, 1, 1, 2, 3, 5, 8, 13, 21, 34`

**Expected Output:**
```
0
1
1
2
3
5
8
13
21
34
```

**Hints:**
- Start with two variables: `a = 0`, `b = 1`
- Each iteration: print `a`, then update `a` and `b`
- Use a `temp` variable to swap values!

---

### 🎯 Quiz 15: 최대공약수 (GCD) / Greatest Common Divisor

#### 🇰🇷 한국어

**시나리오:** 분수 계산 앱에서 분수를 약분하려면 두 수의 최대공약수(GCD)가 필요합니다!

**미션:** 사용자에게 두 수를 입력받아 최대공약수를 출력하세요. 유클리드 알고리즘을 사용하세요.

**유클리드 알고리즘이란?**
- `a`와 `b` 가 있을 때, `b`가 0이 될 때까지 `a = b`, `b = a % b` 를 반복
- `b`가 0이 되었을 때의 `a`가 바로 GCD!

**예상 출력 (입력값: 48, 18):**
```
최대공약수: 6
```

**힌트:**
- `temp = b` → `b = a % b` → `a = temp` 순서로!
- `while b != 0:` 조건으로 반복

---

#### 🇺🇸 English

**Scenario:** A fraction calculator app needs to simplify fractions — and that requires finding the GCD of two numbers!

**Mission:** Ask the user for two numbers and print their GCD using the Euclidean algorithm.

**What is the Euclidean Algorithm?**
- Given `a` and `b`, keep doing `a = b`, `b = a % b` until `b` becomes 0
- The value of `a` when `b` reaches 0 is the GCD!

**Expected Output (input: 48 and 18):**
```
GCD: 6
```

**Hints:**
- Order matters: `temp = b` → `b = a % b` → `a = temp`
- Loop condition: `while b != 0:`

---
---

## 🤔 생각해보기 / Think About It

각 문제를 풀기 전에 스스로에게 물어보세요:

1. `for` 반복문과 `while` 반복문 중 어떤 것이 더 적합한가요? 왜?
2. 누산기 변수의 초기값은 얼마가 되어야 할까요? (합산이면 0, 곱셈이면 1)
3. 반복이 언제 끝나야 하는지 명확한가요?
4. 반복문 안에서 매 단계마다 어떤 일이 일어나는지 손으로 추적해봤나요?

막히면 스레드에 질문 남겨주세요! 목표는 빠르게 끝내는 것이 아니라 **논리를 이해하는 것**입니다. 🎯

행운을 빕니다! 🚀
