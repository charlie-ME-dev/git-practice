# ☕ Python 클래스 연습: 카페 음료 주문 시스템

여러분, 안녕하세요! 오늘은 직접 배운 **클래스**를 가지고 진짜 같은 시스템을 만들어볼 거예요.

## 🎯 미션

여러분은 학교 앞 카페의 사장님입니다. 손님이 음료를 주문하면, 이름·사이즈·우유 추가 여부·샷 추가 개수에 따라 가격이 달라져야 해요. 매번 if문으로 계산하는 건 너무 번거롭죠. 그래서 **`Drink` 클래스**를 만들어서 음료 하나하나를 객체로 관리할 거예요.

## 📋 규칙

*주어지는 것:*
- 음료 이름 (예: `"Americano"`, `"Latte"`)
- 사이즈 (`"Small"`, `"Medium"`, `"Large"` 중 하나)
- 기본 가격 (Small 사이즈 기준의 가격)
- 우유 추가 여부 (기본값은 추가 안 함)

*해야 할 일:*
1. `Drink` 클래스를 정의하기
2. `__init__`에서 속성(attribute)을 초기화하기
3. 가격을 계산해서 돌려주는 메서드 만들기
4. 음료 설명을 문자열로 돌려주는 메서드 만들기
5. 샷을 한 번에 하나씩 추가할 수 있는 메서드 만들기

*반드시 따라야 할 제약사항:*
- **`self`를 꼭 사용해야 합니다.** 객체마다 따로 값을 저장해야 하니까요
- **`__init__`은 매개변수를 받고**, 그것들을 속성으로 저장해야 합니다
- **메서드는 클래스 안에 정의**하고, 첫 번째 매개변수는 항상 `self`
- 가격 계산은 메서드 안에서만 — 외부에서 직접 계산하지 마세요
- 함수/변수 이름은 `snake_case`로

## 💰 가격 규칙

| 항목 | 추가 요금 |
|------|----------|
| Small 사이즈 | +0원 (기본) |
| Medium 사이즈 | +500원 |
| Large 사이즈 | +1000원 |
| 우유 추가 | +500원 |
| 샷 추가 (1회당) | +500원 |

**최종 가격 = 기본 가격 + 사이즈 요금 + 우유 요금 + (샷 추가 × 500)**

## 💡 예제

**예제 1: 기본 아메리카노**
```python
drink = Drink("Americano", "Small", 3000)
print(drink.get_price())   # 3000
print(drink.describe())    # "Small Americano (no milk, +0 shot)"
```

**예제 2: 우유 추가한 미디엄 라떼**
```python
drink = Drink("Latte", "Medium", 4000, add_milk=True)
print(drink.get_price())   # 5000  (4000 + 500 + 500)
print(drink.describe())    # "Medium Latte (with milk, +0 shot)"
```

**예제 3: 샷 두 번 추가한 라지 라떼**
```python
drink = Drink("Latte", "Large", 4000, add_milk=True)
drink.add_shot()
drink.add_shot()
print(drink.get_price())   # 6500  (4000 + 1000 + 500 + 500*2)
print(drink.describe())    # "Large Latte (with milk, +2 shot)"
```

## 🎓 알아야 할 것

코딩을 시작하기 전에 다음을 떠올려보세요:
- `class` 키워드로 클래스를 정의하는 방법
- `__init__` 메서드의 역할
- `self`가 무엇을 의미하는지
- 속성(attribute)과 메서드(method)의 차이
- default parameter (`add_milk=False`처럼)

## ✅ 과제

다음 시그니처로 클래스를 작성하세요:

```python
class Drink:
    def __init__(self, name, size, base_price, add_milk=False):
        # 속성 초기화
        pass

    def add_shot(self):
        # 샷 1회 추가
        pass

    def get_price(self):
        # 최종 가격 계산해서 반환
        pass

    def describe(self):
        # 음료 설명 문자열 반환
        pass
```

**시작하는 데 도움이 될 팁:**
- `__init__` 안에서 매개변수를 `self.속성이름`으로 저장하세요
- 샷 추가 개수도 속성으로 저장해야 합니다 — 초기값은 `0`
- 사이즈별 추가 요금은 `if/elif`로 처리하면 깔끔해요
- 객체를 두 개 만들었을 때 서로 영향을 주지 않아야 해요!

## 🎪 코드 테스트

다음 테스트 케이스를 실행해보세요:

```python
# 테스트 1: 기본 아메리카노
d1 = Drink("Americano", "Small", 3000)
print(f"가격: {d1.get_price()}원")
print(f"설명: {d1.describe()}")
# 예상: 가격: 3000원 / 설명: Small Americano (no milk, +0 shot)

# 테스트 2: 미디엄 라떼, 우유 추가
d2 = Drink("Latte", "Medium", 4000, add_milk=True)
print(f"가격: {d2.get_price()}원")
# 예상: 5000원

# 테스트 3: 라지 라떼, 우유 + 샷 2개
d3 = Drink("Latte", "Large", 4000, add_milk=True)
d3.add_shot()
d3.add_shot()
print(f"가격: {d3.get_price()}원")
# 예상: 6500원

# 테스트 4: 객체 두 개가 서로 독립적인지 확인
d4a = Drink("Espresso", "Small", 2500)
d4b = Drink("Espresso", "Small", 2500)
d4a.add_shot()
print(f"d4a 샷 개수: {d4a.extra_shots}, d4b 샷 개수: {d4b.extra_shots}")
# 예상: d4a 샷 개수: 1, d4b 샷 개수: 0
```

## 🤔 생각해보기

코딩하기 전에 다음을 스스로 답해보세요:
1. `self.name`과 그냥 `name`은 어떻게 다른가요?
2. `__init__`은 언제 자동으로 호출되나요?
3. 객체를 두 개 만들면, 각각의 속성은 어떻게 따로 저장될까요?

## 🎁 보너스 챌린지

기본 과제를 다 했다면 도전해보세요!

### 🥉 Easy: 시럽 추가 기능
`add_syrup(flavor)` 메서드를 추가해서, 시럽 종류(예: `"vanilla"`, `"hazelnut"`)를 받고 가격에 +500원을 더하세요. 추가한 시럽들은 리스트로 저장하고, `describe()`에 같이 보여주세요.

### 🥈 Medium: 할인 적용
`apply_discount(percent)` 메서드를 추가하세요. 예: `drink.apply_discount(10)`이면 최종 가격에서 10% 할인. `get_price()`를 호출했을 때 할인이 반영되어야 합니다.

### 🥇 Hard: 문자열 표현 (preview)
`__str__`이라는 특별한 메서드를 정의하면, `print(drink)`만 해도 `describe()`처럼 출력됩니다. 한번 도전해보세요:

```python
def __str__(self):
    return self.describe()
```

`print(drink)`와 `print(drink.describe())`가 같은 결과를 내는지 확인해보세요!

---
---

# ☕ Python Class Practice: Cafe Drink Order System

Hey team! Today we're putting **classes** to work in a real-feeling system.

## 🎯 Your Mission

You're running a cafe near campus. When a customer orders a drink, the price depends on the name, size, whether milk is added, and how many extra shots. Doing this with if statements every time is a hassle. So we'll build a **`Drink` class** that manages each drink as an object.

## 📋 The Rules

*What you're given:*
- A drink name (e.g., `"Americano"`, `"Latte"`)
- A size (`"Small"`, `"Medium"`, or `"Large"`)
- A base price (the Small-size price)
- Whether to add milk (default is no)

*What you need to do:*
1. Define a `Drink` class
2. Initialize attributes in `__init__`
3. Add a method that returns the total price
4. Add a method that returns a description string
5. Add a method to add one extra shot at a time

*Constraints you must follow:*
- **You must use `self`** — each object stores its own values
- **`__init__` takes the parameters** and stores them as attributes
- **Methods are defined inside the class** and always take `self` as the first parameter
- Price calculation lives inside a method — don't compute it from outside
- Use `snake_case` for variables and function names

## 💰 Pricing Rules

| Item | Extra cost |
|------|-----------|
| Small size | +0 KRW (base) |
| Medium size | +500 KRW |
| Large size | +1000 KRW |
| Add milk | +500 KRW |
| Extra shot (each) | +500 KRW |

**Total = base price + size fee + milk fee + (extra shots × 500)**

## 💡 Example Time

**Example 1: Plain Americano**
```python
drink = Drink("Americano", "Small", 3000)
print(drink.get_price())   # 3000
print(drink.describe())    # "Small Americano (no milk, +0 shot)"
```

**Example 2: Medium Latte with milk**
```python
drink = Drink("Latte", "Medium", 4000, add_milk=True)
print(drink.get_price())   # 5000  (4000 + 500 + 500)
```

**Example 3: Large Latte, milk, 2 extra shots**
```python
drink = Drink("Latte", "Large", 4000, add_milk=True)
drink.add_shot()
drink.add_shot()
print(drink.get_price())   # 6500  (4000 + 1000 + 500 + 500*2)
```

## 🎓 What You Should Know

Before you start, make sure you remember:
- How to define a class with the `class` keyword
- What `__init__` does
- What `self` means
- The difference between an attribute and a method
- Default parameters (like `add_milk=False`)

## ✅ Your Task

Write a class with this signature:

```python
class Drink:
    def __init__(self, name, size, base_price, add_milk=False):
        # initialize attributes
        pass

    def add_shot(self):
        # add one shot
        pass

    def get_price(self):
        # compute and return total price
        pass

    def describe(self):
        # return description string
        pass
```

**Tips to get you started:**
- Inside `__init__`, store parameters as `self.attribute_name`
- The shot count also needs to be an attribute — start it at `0`
- Use `if/elif` for size-based fees
- Two different objects must NOT share state!

## 🎪 Test Your Code

Try these test cases:

```python
# Test 1: plain Americano
d1 = Drink("Americano", "Small", 3000)
print(f"Price: {d1.get_price()} KRW")
print(f"Desc: {d1.describe()}")
# Expected: Price: 3000 KRW / Desc: Small Americano (no milk, +0 shot)

# Test 2: Medium Latte with milk
d2 = Drink("Latte", "Medium", 4000, add_milk=True)
print(f"Price: {d2.get_price()} KRW")
# Expected: 5000 KRW

# Test 3: Large Latte, milk + 2 shots
d3 = Drink("Latte", "Large", 4000, add_milk=True)
d3.add_shot()
d3.add_shot()
print(f"Price: {d3.get_price()} KRW")
# Expected: 6500 KRW

# Test 4: two objects stay independent
d4a = Drink("Espresso", "Small", 2500)
d4b = Drink("Espresso", "Small", 2500)
d4a.add_shot()
print(f"d4a shots: {d4a.extra_shots}, d4b shots: {d4b.extra_shots}")
# Expected: d4a shots: 1, d4b shots: 0
```

## 🤔 Think About It

Before coding, answer these for yourself:
1. How is `self.name` different from just `name`?
2. When is `__init__` called automatically?
3. If you make two objects, how does each one keep its own attributes separate?

## 🎁 Bonus Challenges

Finished the main task? Try these!

### 🥉 Easy: Syrup support
Add a method `add_syrup(flavor)` that takes a syrup name (e.g., `"vanilla"`, `"hazelnut"`) and adds +500 KRW. Store added syrups in a list and include them in `describe()`.

### 🥈 Medium: Apply a discount
Add `apply_discount(percent)`. For example, `drink.apply_discount(10)` means 10% off the final price. `get_price()` should reflect the discount.

### 🥇 Hard: String representation (preview)
Define a special method called `__str__` and `print(drink)` will work just like `describe()`:

```python
def __str__(self):
    return self.describe()
```

Try it and see whether `print(drink)` and `print(drink.describe())` give the same output!

Drop questions in the thread if you get stuck. The goal is to learn, not just to finish. Take your time. 🚀
