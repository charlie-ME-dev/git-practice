# 🐍 Python 연습: 피보나치 수열의 짝수 합 구하기!

여러분, 안녕하세요! 오늘은 반복문(loop)을 활용한 실전 챌린지입니다. 수학과 코딩이 만나는 순간을 경험해봐요!

## 🎯 미션

피보나치 수열을 들어보셨나요? 앞의 두 숫자를 더해서 다음 숫자를 만드는 특별한 수열이에요.

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

여러분의 임무는: **100만(1,000,000) 이하의 피보나치 수 중에서 짝수만 골라 전부 더하세요!**

## 📋 규칙

*피보나치 수열 규칙:*
• 첫 번째 항: `1`
• 두 번째 항: `2`
• 그 다음부터: 바로 앞 두 항의 합

예) 1 → 2 → 1+2=3 → 2+3=5 → 3+5=8 → ...

*해야 할 일:*
1. 피보나치 수열을 while 루프로 생성
2. 각 항이 100만 이하인 동안 계속 진행
3. 짝수인 항만 찾아서 합산
4. 최종 합계를 출력

*힌트:*
• 짝수 판별: `숫자 % 2 == 0`
• 변수 두 개로 현재 항과 다음 항을 추적하세요
• `while` 루프를 사용하는 것이 자연스럽습니다

## 💡 예제 (작은 버전으로 먼저 이해해봐요)

10 이하의 피보나치 수 중 짝수의 합을 구한다면?

```
수열: 1, 2, 3, 5, 8  (다음은 13으로 10 초과)
짝수: 2, 8
합계: 2 + 8 = 10
```

## 🎓 알아야 할 것

코딩을 시작하기 전에, 다음을 이해하고 있는지 확인하세요:
• `while` 루프 작성 방법
• 변수를 업데이트하는 방법 (`a, b = b, a + b` 패턴)
• 나머지 연산자 `%`로 짝수 판별하는 방법
• 누적 합계를 변수에 쌓는 방법 (`total = total + 값`)

## 🌍 실제로 어디에 쓰일까요?

피보나치 수열은 생각보다 우리 주변 곳곳에 있어요!  
• 🌻 해바라기 씨앗 배열, 솔방울 나선형 — 자연의 패턴  
• 📈 주식 시장 기술적 분석 — 트레이더들이 피보나치 비율을 사용  
• 🎨 황금 비율 디자인 — UI/UX 디자이너들이 레이아웃에 활용  
• 💻 알고리즘 효율성 분석 — CS 연구의 핵심 수열

오늘 여러분은 금융 데이터 분석가처럼 수열에서 특정 조건을 만족하는 값만 골라 집계하는 연습을 하는 거예요!

## ✅ 과제

다음 시그니처로 함수를 작성하세요:

```python
def sum_even_fibonacci(limit: int) -> int:
    # 여기에 코드 작성
    pass
```

그리고 메인 실행 블록에서 함수를 호출하세요:

```python
result = sum_even_fibonacci(1_000_000)
print(f"100만 이하 피보나치 짝수의 합: {result}")
```

## 🎪 코드 테스트

다음 테스트 케이스를 실행해보세요:

```python
# 테스트 1: 소규모 (손으로 검산 가능!)
print(sum_even_fibonacci(10))
# 예상: 10  (2 + 8)

# 테스트 2: 중간 규모
print(sum_even_fibonacci(100))
# 예상: 44  (2 + 8 + 34)

# 테스트 3: 실제 미션
print(sum_even_fibonacci(1_000_000))
# 예상: 1089154
```

## 🤔 생각해보기

코딩을 시작하기 전에, 접근 방법을 스케치해보세요:
1. 피보나치 수열을 어떻게 계속 생성할까요? (변수가 몇 개 필요할까요?)
2. 언제 루프를 멈춰야 할까요?
3. 짝수인지 아닌지 어떻게 판별할까요?
4. 합계를 어떻게 누적할까요?

막히면 스레드에 질문을 남겨주세요! 목표는 끝내는 것이 아니라 배우는 것입니다. 천천히 논리를 이해하면서 진행하세요.

행운을 빕니다! 🚀

---
---

# 🐍 Python Practice: Sum of Even Fibonacci Numbers!

Hey team! Today's challenge combines loops with a classic math sequence. Get ready to see how code and patterns connect!

## 🎯 Your Mission

Have you heard of the Fibonacci sequence? It's a special sequence where each number is the sum of the two before it:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

Your mission: **Find the sum of all even-valued Fibonacci terms that don't exceed one million (1,000,000)!**

## 📋 The Rules

*How Fibonacci works:*
• First term: `1`
• Second term: `2`
• Every term after: sum of the two terms before it

Example: 1 → 2 → 1+2=3 → 2+3=5 → 3+5=8 → ...

*What you need to do:*
1. Generate the Fibonacci sequence using a while loop
2. Keep going as long as the current term is under one million
3. Pick out only the even terms and add them up
4. Print the final total

*Hints:*
• Check for even: `number % 2 == 0`
• Use two variables to track the current and next term
• A `while` loop fits naturally here

## 💡 Example (Try a smaller version first!)

Find the sum of even Fibonacci terms up to 10:

```
Sequence: 1, 2, 3, 5, 8  (next is 13, which exceeds 10)
Even terms: 2, 8
Sum: 2 + 8 = 10
```

## 🎓 What You Should Know

Before you start coding, make sure you understand:
• How to write a `while` loop
• How to update variables (`a, b = b, a + b` pattern)
• How to check for even numbers using `%`
• How to accumulate a running total (`total = total + value`)

## 🌍 Real-World Connection

Fibonacci numbers show up more than you'd think!
• 🌻 Sunflower seeds and pinecone spirals — nature's own pattern
• 📈 Stock market technical analysis — traders use Fibonacci ratios
• 🎨 Golden ratio in design — UI/UX designers use it for layouts
• 💻 Algorithm analysis — a key sequence in CS research

Today you're practicing exactly what a financial data analyst does: generate a series, filter by a condition, and aggregate the results!

## ✅ Your Task

Write a function with this signature:

```python
def sum_even_fibonacci(limit: int) -> int:
    # Your code here
    pass
```

Then call it in your main block:

```python
result = sum_even_fibonacci(1_000_000)
print(f"Sum of even Fibonacci numbers up to 1 million: {result}")
```

## 🎪 Test Your Code

Try these test cases — start small so you can check by hand!

```python
# Test 1: Small scale (you can verify manually!)
print(sum_even_fibonacci(10))
# Expected: 10  (2 + 8)

# Test 2: Medium scale
print(sum_even_fibonacci(100))
# Expected: 44  (2 + 8 + 34)

# Test 3: The real mission
print(sum_even_fibonacci(1_000_000))
# Expected: 1089154
```

## 🤔 Think About It

Before you start coding, sketch out your approach:
1. How will you keep generating new Fibonacci numbers? (How many variables do you need?)
2. When should the loop stop?
3. How do you check whether a number is even?
4. How do you keep a running total?

Drop your questions in the thread if you get stuck! Remember, the goal is to learn, not just to finish. Take your time and understand the logic.

Good luck! 🚀
