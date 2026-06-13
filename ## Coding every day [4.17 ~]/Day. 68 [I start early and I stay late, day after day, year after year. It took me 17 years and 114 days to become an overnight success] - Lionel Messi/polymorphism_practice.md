# 🌳 Python 연습: 다형성으로 정원 설계하기!

여러분, 안녕하세요! 오늘은 **다형성(polymorphism)**을 활용한 실전 챌린지입니다. 상속을 배웠으니, 이제 그 진짜 위력을 경험할 시간이에요!

## 🎯 미션

여러분은 **조경 회사의 신입 개발자**입니다. 고객들이 다양한 모양의 정원 화단을 주문하는데, 각 화단의 **면적(흙이 얼마나 필요한지)**과 **둘레(울타리가 얼마나 필요한지)**를 계산해야 합니다.

문제는? 화단 모양이 제각각이라는 것! 원형 장미 화단, 직사각형 채소밭, 삼각형 허브 정원 등 다양합니다. 각 모양마다 따로 함수를 만들면 코드가 엉망이 되겠죠.

**해결책:** 다형성을 사용해서 **하나의 인터페이스로 모든 모양을 다루는** 클래스 계층을 설계합시다!

## 📋 규칙

*주어지는 것:*
- 부모 클래스 `Shape` (이름, 색상 등 공통 속성 보유)
- 세 가지 자식 클래스 만들기: `Circle`, `Rectangle`, `Triangle`

*해야 할 일:*
1. `Shape` 부모 클래스 작성 — 공통 속성(`_name`, `_color`)과 메서드(`area()`, `perimeter()`)
2. 세 개의 자식 클래스 작성 — 각각 `area()`와 `perimeter()`를 **오버라이드(override)**
3. 다형성 함수 `total_garden_area()`와 `total_fence_length()` 작성 — 서로 다른 모양들의 리스트를 받아 합계 계산

*반드시 따라야 할 제약사항:*
- **캡슐화 유지**: 속성 이름은 `_`로 시작 (예: `_radius`), 접근은 getter 메서드로
- **`super().__init__()` 사용**: 자식 클래스에서 부모의 초기화 호출
- **메서드 시그니처 동일하게 유지**: 모든 도형의 `area()`와 `perimeter()`는 인자 없이 호출 가능해야 함
- **함수/메서드 이름**: snake_case (예: `get_name`, 절대 `getName` 아님)
- **금지 사항**: 이번 핵심 과제에서는 `__str__` 등 dunder 메서드 사용 금지, `abc` 모듈 사용 금지

## 💡 예제

**예제 1: 원형 장미 화단**
```python
rose_bed = Circle("Rose Bed", "red", radius=5)
print(rose_bed.area())       # 78.5398... (π × 5²)
print(rose_bed.perimeter())  # 31.4159... (2π × 5)
```

**예제 2: 직사각형 채소밭**
```python
veggie_patch = Rectangle("Vegetable Patch", "green", width=4, height=6)
print(veggie_patch.area())       # 24 (4 × 6)
print(veggie_patch.perimeter())  # 20 (2 × (4+6))
```

**예제 3: 다형성의 마법 ✨**
```python
garden = [
    Circle("Rose Bed", "red", 5),
    Rectangle("Vegetable Patch", "green", 4, 6),
    Triangle("Herb Garden", "yellow", 3, 4, 5),
]

print(total_garden_area(garden))    # 약 108.54
print(total_fence_length(garden))   # 약 63.42
```

> 💡 **여기가 핵심!** `total_garden_area()` 함수는 **각 도형이 무엇인지 신경 쓸 필요가 없습니다.** 그냥 `.area()`를 호출하면 Python이 알아서 올바른 버전을 실행해요. 이것이 다형성입니다!

## 🎓 알아야 할 것

코딩을 시작하기 전에, 다음을 이해하고 있는지 확인하세요:
- 클래스 정의와 `__init__` 메서드
- 상속 (`class Child(Parent):`)
- `super().__init__()`의 역할
- 메서드 오버라이딩 — 자식이 부모의 메서드를 다시 정의하는 것
- 캡슐화 — `_attribute` 관례와 getter 메서드

## ✅ 과제

다음 구조로 코드를 작성하세요:

```python
import math

class Shape:
    def __init__(self, name: str, color: str):
        # 여기에 코드
        pass

    def get_name(self) -> str:
        pass

    def get_color(self) -> str:
        pass

    def area(self) -> float:
        # 부모 버전 — 자식이 오버라이드할 것
        return 0.0

    def perimeter(self) -> float:
        return 0.0


class Circle(Shape):
    # 여기에 코드

class Rectangle(Shape):
    # 여기에 코드

class Triangle(Shape):
    # 여기에 코드 — 힌트: Heron의 공식 사용!


def total_garden_area(shapes: list) -> float:
    # 여기에 코드

def total_fence_length(shapes: list) -> float:
    # 여기에 코드
```

**시작하는 데 도움이 될 팁:**
- 원의 면적: π × r²  /  둘레: 2π × r  →  `math.pi` 사용
- 삼각형 면적은 **Heron의 공식** 사용:
  - s = (a + b + c) / 2
  - area = √(s × (s−a) × (s−b) × (s−c))
  - `math.sqrt()` 사용
- `total_garden_area()`는 단순한 `for` 반복문 — 각 도형의 `.area()`를 더하면 됩니다

## 🎪 코드 테스트

다음 테스트 케이스를 실행해보세요:

```python
# 테스트 1: 개별 도형
rose = Circle("Rose Bed", "red", 5)
veggie = Rectangle("Vegetable Patch", "green", 4, 6)
herb = Triangle("Herb Garden", "yellow", 3, 4, 5)

print(f"{rose.get_name()}: 면적 = {rose.area():.2f}")
# 예상: Rose Bed: 면적 = 78.54

print(f"{veggie.get_name()}: 면적 = {veggie.area():.2f}")
# 예상: Vegetable Patch: 면적 = 24.00

print(f"{herb.get_name()}: 면적 = {herb.area():.2f}")
# 예상: Herb Garden: 면적 = 6.00

# 테스트 2: 다형성
garden = [rose, veggie, herb]
print(f"전체 면적: {total_garden_area(garden):.2f}")
# 예상: 전체 면적: 108.54

print(f"전체 둘레: {total_fence_length(garden):.2f}")
# 예상: 전체 둘레: 63.42

# 테스트 3: 빈 정원
print(f"빈 정원 면적: {total_garden_area([])}")
# 예상: 빈 정원 면적: 0.0
```

## 🤔 생각해보기

코딩을 시작하기 전에, 다음 질문에 답해보세요:
1. 왜 `Shape` 클래스의 `area()`가 `0.0`을 반환할까요? 이게 의미 있는 동작일까요?
2. `total_garden_area()` 함수는 어떻게 `Circle`, `Rectangle`, `Triangle`을 모두 처리할 수 있을까요?
3. 새로운 도형(예: `Hexagon`)을 추가하려면 어떤 코드를 수정해야 할까요? `total_garden_area()`를 바꿔야 할까요?

## 🏆 보너스 챌린지

핵심 과제를 완료했다면, 다음 도전들을 시도해보세요:

### 🥉 Easy: `Square` 클래스 추가
`Rectangle`을 상속받아 `Square` 클래스를 만드세요. 한 변의 길이만 받아서 정사각형으로 동작해야 합니다.

```python
sq = Square("Tile", "blue", side=4)
print(sq.area())       # 16
print(sq.perimeter())  # 16
```

### 🥈 Medium: `find_largest_shape()` 함수
도형 리스트에서 면적이 가장 큰 도형의 **이름**을 반환하는 함수를 작성하세요. 다형성을 활용해야 합니다!

```python
print(find_largest_shape(garden))  # "Rose Bed"
```

### 🥇 Hard: `__str__` 미리보기 🔮 *(다음 주에 배울 내용!)*
각 도형 클래스에 `__str__` 메서드를 추가하면 `print(shape)`를 직접 호출했을 때 예쁘게 출력할 수 있습니다.

```python
def __str__(self):
    return f"{self._name} ({self._color}): 면적={self.area():.2f}"

print(rose)  # "Rose Bed (red): 면적=78.54"
```

> 🔮 이건 **다음 주에 배울 dunder 메서드**의 맛보기입니다. 시도해보고 어떻게 동작하는지 느껴보세요!

막히면 스레드에 질문 남겨주세요! 목표는 단순히 끝내는 것이 아니라 **다형성이 왜 강력한지** 이해하는 것입니다. 🚀

---
---

# 🌳 Python Practice: Design a Garden with Polymorphism!

Hey team! Time for a hands-on challenge with **polymorphism**. You've learned inheritance — now let's see its real power!

## 🎯 Your Mission

You're a **junior developer at a landscaping company**. Clients order garden beds of all different shapes, and you need to calculate the **area** (how much soil they need) and **perimeter** (how much fencing) for each one.

The problem? The bed shapes are all different! Circular rose beds, rectangular vegetable patches, triangular herb gardens. If you write separate functions for every shape, your code will be a mess.

**The solution:** Use polymorphism to design a class hierarchy where **one interface handles every shape**!

## 📋 The Rules

*What you're given:*
- A parent class `Shape` (holds shared attributes like name, color)
- Three child classes to build: `Circle`, `Rectangle`, `Triangle`

*What you need to do:*
1. Write the `Shape` parent class — with shared attributes (`_name`, `_color`) and methods (`area()`, `perimeter()`)
2. Write three child classes — each **overriding** `area()` and `perimeter()`
3. Write polymorphism functions `total_garden_area()` and `total_fence_length()` — they take a list of mixed shapes and return the sum

*Constraints you must follow:*
- **Maintain encapsulation**: attributes start with `_` (e.g., `_radius`), access them via getter methods
- **Use `super().__init__()`**: child classes must call the parent initializer
- **Keep method signatures identical**: every shape's `area()` and `perimeter()` must be callable with no arguments
- **Function/method naming**: snake_case (e.g., `get_name`, never `getName`)
- **Forbidden in core task**: no dunder methods like `__str__`, no `abc` module

## 💡 Examples

**Example 1: Circular rose bed**
```python
rose_bed = Circle("Rose Bed", "red", radius=5)
print(rose_bed.area())       # 78.5398... (π × 5²)
print(rose_bed.perimeter())  # 31.4159... (2π × 5)
```

**Example 2: Rectangular veggie patch**
```python
veggie_patch = Rectangle("Vegetable Patch", "green", width=4, height=6)
print(veggie_patch.area())       # 24 (4 × 6)
print(veggie_patch.perimeter())  # 20 (2 × (4+6))
```

**Example 3: The magic of polymorphism ✨**
```python
garden = [
    Circle("Rose Bed", "red", 5),
    Rectangle("Vegetable Patch", "green", 4, 6),
    Triangle("Herb Garden", "yellow", 3, 4, 5),
]

print(total_garden_area(garden))    # ~108.54
print(total_fence_length(garden))   # ~63.42
```

> 💡 **Here's the key!** The `total_garden_area()` function **doesn't care what each shape actually is.** It just calls `.area()` and Python figures out which version to run. That's polymorphism!

## 🎓 What You Should Know

Before you start coding, make sure you understand:
- Class definitions and the `__init__` method
- Inheritance (`class Child(Parent):`)
- The role of `super().__init__()`
- Method overriding — child redefines a parent's method
- Encapsulation — the `_attribute` convention and getter methods

## ✅ Your Task

Write your code with this structure:

```python
import math

class Shape:
    def __init__(self, name: str, color: str):
        # Your code
        pass

    def get_name(self) -> str:
        pass

    def get_color(self) -> str:
        pass

    def area(self) -> float:
        # Parent version — children will override
        return 0.0

    def perimeter(self) -> float:
        return 0.0


class Circle(Shape):
    # Your code

class Rectangle(Shape):
    # Your code

class Triangle(Shape):
    # Your code — hint: use Heron's formula!


def total_garden_area(shapes: list) -> float:
    # Your code

def total_fence_length(shapes: list) -> float:
    # Your code
```

**Tips to get you started:**
- Circle area: π × r²  /  perimeter: 2π × r  →  use `math.pi`
- For the triangle area, use **Heron's formula**:
  - s = (a + b + c) / 2
  - area = √(s × (s−a) × (s−b) × (s−c))
  - use `math.sqrt()`
- `total_garden_area()` is just a simple `for` loop — sum each shape's `.area()`

## 🎪 Test Your Code

Try running these test cases:

```python
# Test 1: Individual shapes
rose = Circle("Rose Bed", "red", 5)
veggie = Rectangle("Vegetable Patch", "green", 4, 6)
herb = Triangle("Herb Garden", "yellow", 3, 4, 5)

print(f"{rose.get_name()}: area = {rose.area():.2f}")
# Expected: Rose Bed: area = 78.54

print(f"{veggie.get_name()}: area = {veggie.area():.2f}")
# Expected: Vegetable Patch: area = 24.00

print(f"{herb.get_name()}: area = {herb.area():.2f}")
# Expected: Herb Garden: area = 6.00

# Test 2: Polymorphism
garden = [rose, veggie, herb]
print(f"Total area: {total_garden_area(garden):.2f}")
# Expected: Total area: 108.54

print(f"Total perimeter: {total_fence_length(garden):.2f}")
# Expected: Total perimeter: 63.42

# Test 3: Empty garden
print(f"Empty garden area: {total_garden_area([])}")
# Expected: Empty garden area: 0.0
```

## 🤔 Think About It

Before you start coding, answer these questions:
1. Why does the `Shape` class's `area()` return `0.0`? Is that meaningful behavior?
2. How is `total_garden_area()` able to handle `Circle`, `Rectangle`, AND `Triangle`?
3. If you wanted to add a new shape (like `Hexagon`), what code would you need to change? Would you need to modify `total_garden_area()`?

## 🏆 Bonus Challenges

Finished the core task? Try these:

### 🥉 Easy: Add a `Square` class
Inherit from `Rectangle` and build a `Square` class. It should take just one side length.

```python
sq = Square("Tile", "blue", side=4)
print(sq.area())       # 16
print(sq.perimeter())  # 16
```

### 🥈 Medium: `find_largest_shape()` function
Write a function that takes a list of shapes and returns the **name** of the shape with the largest area. You must use polymorphism!

```python
print(find_largest_shape(garden))  # "Rose Bed"
```

### 🥇 Hard: `__str__` preview 🔮 *(coming next week!)*
Add a `__str__` method to each shape class — then `print(shape)` will work directly with nice formatting:

```python
def __str__(self):
    return f"{self._name} ({self._color}): area={self.area():.2f}"

print(rose)  # "Rose Bed (red): area=78.54"
```

> 🔮 This is a sneak peek at **dunder methods** coming next week. Try it out and feel how it works!

Drop your questions in the thread if you get stuck! Remember — the goal isn't just to finish, but to understand **why polymorphism is powerful**. 🚀
