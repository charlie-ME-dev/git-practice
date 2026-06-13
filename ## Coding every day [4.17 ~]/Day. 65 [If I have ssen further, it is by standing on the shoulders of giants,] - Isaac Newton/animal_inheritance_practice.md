# 🐍 Python 연습: 동물 보호소 시스템 만들기!

여러분, 안녕하세요! 오늘은 상속(Inheritance)의 두 번째 날입니다. 어제 배운 `super()`를 더 깊이 활용해볼 거예요.

## 🎯 미션

여러분은 동물 보호소(Animal Shelter)의 신입 개발자입니다! 보호소장님이 말씀하셨어요:

> "우리 보호소에는 강아지, 고양이, 새가 있어요. 각자 특성이 다르지만 공통점도 많죠. 동물마다 울음소리와 설명을 출력하는 시스템이 필요해요. 그런데 코드를 중복해서 쓰지 말고, **공통 부분은 부모 클래스가 처리하고, 자식 클래스는 그 위에 자기만의 정보를 추가**하는 식으로 만들어주세요!"

오늘의 핵심: **메서드 오버라이딩(Method Overriding)** + **`super().메서드명()` 호출**

부모의 일을 *완전히 대체*하는 게 아니라, 부모의 결과를 *받아서 확장*하는 패턴을 연습합니다.

## 📋 규칙

**클래스 구조:**

```
        Animal (부모)
       /    |    \
     Dog   Cat   Bird
```

**`Animal` 클래스 (부모):**

| 속성 | 타입 | 설명 |
|---|---|---|
| `name` | str | 동물 이름 |
| `age` | int | 나이 |
| `sound` | str | 울음소리 |

| 메서드 | 반환값 |
|---|---|
| `speak()` | `"{name} says {sound}!"` |
| `describe()` | `"{name} is {age} years old."` |

**자식 클래스들이 해야 할 일:**

1. `__init__`에서 `super().__init__(...)`로 부모 속성 초기화
2. 자기만의 추가 속성 저장
3. `speak()`와 `describe()`를 **오버라이딩**하되, **반드시 `super().speak()`와 `super().describe()`를 먼저 호출**해서 그 결과를 확장할 것

**`Dog` 클래스:**
- 추가 속성: `breed` (품종, str)
- 부모의 `sound`는 자동으로 `"Woof"`로 설정
- `speak()` 반환값: `"{부모 speak() 결과} (A {breed} barking happily)"`
- `describe()` 반환값: `"{부모 describe() 결과} It is a {breed} dog."`

**`Cat` 클래스:**
- 추가 속성: `indoor` (실내묘 여부, bool)
- 부모의 `sound`는 자동으로 `"Meow"`로 설정
- `speak()` 반환값:
  - `indoor=True`이면: `"{부모 speak() 결과} (purring softly)"`
  - `indoor=False`이면: `"{부모 speak() 결과} (hissing at strangers)"`
- `describe()` 반환값:
  - `indoor=True`이면: `"{부모 describe() 결과} It is an indoor cat."`
  - `indoor=False`이면: `"{부모 describe() 결과} It is an outdoor cat."`

**`Bird` 클래스:**
- 추가 속성: `can_fly` (비행 가능 여부, bool)
- 부모의 `sound`는 자동으로 `"Tweet"`로 설정
- `speak()` 반환값:
  - `can_fly=True`이면: `"{부모 speak() 결과} (while flying around)"`
  - `can_fly=False`이면: `"{부모 speak() 결과} (from its perch)"`
- `describe()` 반환값:
  - `can_fly=True`이면: `"{부모 describe() 결과} This bird can fly."`
  - `can_fly=False`이면: `"{부모 describe() 결과} This bird cannot fly."`

> ⚠️ **중요:** 자식 클래스에서 부모의 메서드 결과를 직접 다시 쓰지 마세요! 반드시 `super().speak()`와 `super().describe()`를 호출해서 받은 결과를 활용해야 합니다. 이것이 오늘의 핵심 학습 목표입니다.

## 💡 예제

**예제 1: Dog**

```python
buddy = Dog("Buddy", 3, "Golden Retriever")
print(buddy.speak())
# 출력: Buddy says Woof! (A Golden Retriever barking happily)
print(buddy.describe())
# 출력: Buddy is 3 years old. It is a Golden Retriever dog.
```

**예제 2: Cat (실내묘)**

```python
whiskers = Cat("Whiskers", 5, True)
print(whiskers.speak())
# 출력: Whiskers says Meow! (purring softly)
print(whiskers.describe())
# 출력: Whiskers is 5 years old. It is an indoor cat.
```

**예제 3: Bird (날 수 없는 새)**

```python
pingu = Bird("Pingu", 4, False)
print(pingu.speak())
# 출력: Pingu says Tweet! (from its perch)
print(pingu.describe())
# 출력: Pingu is 4 years old. This bird cannot fly.
```

## 🎓 알아야 할 것

코딩을 시작하기 전에, 다음을 이해하고 있는지 확인하세요:

- 어제 배운 `super().__init__(...)`로 부모 생성자 호출하기
- 클래스 정의 시 `class Child(Parent):` 구문
- 메서드 안에서 `super().메서드명()`을 호출하는 방법 (← 오늘의 새로운 부분!)
- f-string으로 문자열 만들기
- `if/else`로 조건에 따라 다른 값 반환하기

## ✅ 과제

다음 시그니처로 세 개의 자식 클래스를 작성하세요:

```python
class Animal:
    def __init__(self, name: str, age: int, sound: str):
        # 이미 작성되어 있음
        pass

    def speak(self) -> str:
        # 이미 작성되어 있음
        pass

    def describe(self) -> str:
        # 이미 작성되어 있음
        pass


class Dog(Animal):
    def __init__(self, name: str, age: int, breed: str):
        # 여기에 코드 작성
        pass

    def speak(self) -> str:
        # 여기에 코드 작성 (super().speak() 사용!)
        pass

    def describe(self) -> str:
        # 여기에 코드 작성 (super().describe() 사용!)
        pass


class Cat(Animal):
    # 여기에 코드 작성
    pass


class Bird(Animal):
    # 여기에 코드 작성
    pass
```

**시작하는 데 도움이 될 팁:**

- 자식 클래스의 `__init__`은 부모가 요구하는 모든 인자(`name`, `age`, `sound`)를 `super().__init__(...)`로 전달해야 합니다
- `sound`는 자식 클래스마다 고정값이므로, 사용자에게 받지 않고 `super().__init__()` 호출 시 직접 지정합니다
- 메서드 오버라이딩 시: `parent_result = super().speak()` → `return f"{parent_result} (추가 내용)"` 패턴을 사용하세요
- `super().__init__()`은 자식의 `__init__` 안에서 **가장 먼저** 호출하는 것이 안전합니다

## 🎪 코드 테스트

다음 테스트 케이스를 실행해보세요:

```python
# 테스트 1: Dog
buddy = Dog("Buddy", 3, "Golden Retriever")
print(buddy.speak())     # Buddy says Woof! (A Golden Retriever barking happily)
print(buddy.describe())  # Buddy is 3 years old. It is a Golden Retriever dog.

# 테스트 2: Cat (실내묘)
whiskers = Cat("Whiskers", 5, True)
print(whiskers.speak())     # Whiskers says Meow! (purring softly)
print(whiskers.describe())  # Whiskers is 5 years old. It is an indoor cat.

# 테스트 3: Cat (실외묘)
shadow = Cat("Shadow", 2, False)
print(shadow.speak())     # Shadow says Meow! (hissing at strangers)
print(shadow.describe())  # Shadow is 2 years old. It is an outdoor cat.

# 테스트 4: Bird (날 수 있음)
tweety = Bird("Tweety", 1, True)
print(tweety.speak())     # Tweety says Tweet! (while flying around)
print(tweety.describe())  # Tweety is 1 years old. This bird can fly.

# 테스트 5: Bird (날 수 없음)
pingu = Bird("Pingu", 4, False)
print(pingu.speak())     # Pingu says Tweet! (from its perch)
print(pingu.describe())  # Pingu is 4 years old. This bird cannot fly.
```

## 🤔 생각해보기

코딩하면서, 또는 끝낸 후에 생각해보세요:

1. `super().__init__()`을 사용하지 않고 자식 클래스에서 `self.name = name` 식으로 직접 쓰면 어떻게 될까요? 동작은 할까요? 그래도 문제가 있을까요?
2. `speak()` 메서드 안에서 `super().speak()`를 호출하지 않고, 직접 `f"{self.name} says {self.sound}! ..."`라고 쓰면 무엇이 달라질까요?
3. 만약 부모 `Animal`의 `speak()` 출력 형식이 나중에 바뀐다면 (예: `"{name}이(가) {sound} 소리를 냅니다"`로), 어느 방식이 더 유지보수하기 쉬울까요?
4. `Dog`, `Cat`, `Bird`가 모두 같은 메서드 이름(`speak`, `describe`)을 가지지만 다르게 동작합니다. 이런 성질을 뭐라고 부를까요?

## 🎁 보너스 챌린지

기본 과제를 끝낸 학생들을 위한 추가 도전!

### 🥉 Easy: `__str__` 메서드 추가

`Animal` 클래스에 `__str__` 메서드를 추가해서 `print(buddy)`를 하면 `describe()`의 결과가 출력되도록 만들어보세요. 자식 클래스에서 따로 정의하지 않아도, 자식 인스턴스에 `print()`를 하면 각 자식의 `describe()`가 호출되는지 확인해보세요.

### 🥈 Medium: 새로운 동물 추가하기

`Fish` 클래스를 새로 추가하세요:
- 추가 속성: `water_type` (`"freshwater"` 또는 `"saltwater"`, str)
- `sound`는 `"Blub"`
- `speak()`: `"{부모 결과} (blowing bubbles)"`
- `describe()`: `"{부모 결과} It lives in {water_type}."`

```python
nemo = Fish("Nemo", 2, "saltwater")
print(nemo.speak())     # Nemo says Blub! (blowing bubbles)
print(nemo.describe())  # Nemo is 2 years old. It lives in saltwater.
```

### 🥇 Hard: 다형성(Polymorphism)을 활용한 보호소 시뮬레이션

다양한 동물들이 담긴 리스트를 받아서, 보호소의 "아침 점호"를 시뮬레이션하는 함수를 작성하세요:

```python
def morning_roll_call(animals: list) -> None:
    """
    동물 리스트를 받아서 각자의 speak()와 describe()를 차례로 출력.
    리스트 안에 Dog, Cat, Bird가 섞여 있어도 동작해야 함.
    """
    pass

# 테스트
shelter = [
    Dog("Rex", 5, "Bulldog"),
    Cat("Luna", 3, True),
    Bird("Coco", 2, True),
    Cat("Shadow", 7, False)
]
morning_roll_call(shelter)
```

이 함수가 동작하는 이유를 한 문장으로 설명해보세요. (힌트: "다형성"이라는 단어를 사용해보세요!)

---

막히면 스레드에 질문을 남겨주세요! 목표는 끝내는 것이 아니라 배우는 것입니다. `super()`가 어떻게 동작하는지 천천히 이해하면서 진행하세요.

행운을 빕니다! 🚀

---
---

# 🐍 Python Practice: Build an Animal Shelter System!

Hey team! Welcome to Day 2 of inheritance. Today we'll dig deeper into `super()` — beyond just constructors.

## 🎯 Your Mission

You're a new developer at an Animal Shelter! The shelter manager tells you:

> "We have dogs, cats, and birds. They each have unique traits, but a lot in common too. We need a system that prints each animal's sound and description. But please — don't duplicate code! The **parent class should handle the shared part, and child classes should add their own info on top of the parent's work**!"

Today's core idea: **Method Overriding** + **calling `super().method()` inside methods**

The pattern isn't *replacing* the parent's work — it's *receiving the parent's result and extending it*.

## 📋 The Rules

**Class structure:**

```
        Animal (parent)
       /    |    \
     Dog   Cat   Bird
```

**`Animal` class (parent):**

| Attribute | Type | Description |
|---|---|---|
| `name` | str | Animal's name |
| `age` | int | Age |
| `sound` | str | Sound it makes |

| Method | Return value |
|---|---|
| `speak()` | `"{name} says {sound}!"` |
| `describe()` | `"{name} is {age} years old."` |

**What child classes must do:**

1. In `__init__`, call `super().__init__(...)` to initialize parent's attributes
2. Store any additional attributes of its own
3. **Override** `speak()` and `describe()`, but **always call `super().speak()` and `super().describe()` first** and extend their results

**`Dog` class:**
- Extra attribute: `breed` (str)
- `sound` is automatically set to `"Woof"`
- `speak()` returns: `"{parent's speak() result} (A {breed} barking happily)"`
- `describe()` returns: `"{parent's describe() result} It is a {breed} dog."`

**`Cat` class:**
- Extra attribute: `indoor` (bool)
- `sound` is automatically set to `"Meow"`
- `speak()` returns:
  - If `indoor=True`: `"{parent result} (purring softly)"`
  - If `indoor=False`: `"{parent result} (hissing at strangers)"`
- `describe()` returns:
  - If `indoor=True`: `"{parent result} It is an indoor cat."`
  - If `indoor=False`: `"{parent result} It is an outdoor cat."`

**`Bird` class:**
- Extra attribute: `can_fly` (bool)
- `sound` is automatically set to `"Tweet"`
- `speak()` returns:
  - If `can_fly=True`: `"{parent result} (while flying around)"`
  - If `can_fly=False`: `"{parent result} (from its perch)"`
- `describe()` returns:
  - If `can_fly=True`: `"{parent result} This bird can fly."`
  - If `can_fly=False`: `"{parent result} This bird cannot fly."`

> ⚠️ **Important:** Don't rewrite the parent's logic in the child! You **must** call `super().speak()` and `super().describe()` and use their return values. That's today's main learning goal.

## 💡 Examples

**Example 1: Dog**

```python
buddy = Dog("Buddy", 3, "Golden Retriever")
print(buddy.speak())
# Output: Buddy says Woof! (A Golden Retriever barking happily)
print(buddy.describe())
# Output: Buddy is 3 years old. It is a Golden Retriever dog.
```

**Example 2: Cat (indoor)**

```python
whiskers = Cat("Whiskers", 5, True)
print(whiskers.speak())
# Output: Whiskers says Meow! (purring softly)
print(whiskers.describe())
# Output: Whiskers is 5 years old. It is an indoor cat.
```

**Example 3: Bird (flightless)**

```python
pingu = Bird("Pingu", 4, False)
print(pingu.speak())
# Output: Pingu says Tweet! (from its perch)
print(pingu.describe())
# Output: Pingu is 4 years old. This bird cannot fly.
```

## 🎓 What You Should Know

Before you start coding, make sure you understand:

- Yesterday's `super().__init__(...)` for calling the parent constructor
- `class Child(Parent):` syntax for defining a subclass
- How to call `super().method_name()` inside a method (← today's new piece!)
- f-strings for building strings
- Using `if/else` to return different values based on conditions

## ✅ Your Task

Write three child classes with these signatures:

```python
class Animal:
    def __init__(self, name: str, age: int, sound: str):
        # Already written
        pass

    def speak(self) -> str:
        # Already written
        pass

    def describe(self) -> str:
        # Already written
        pass


class Dog(Animal):
    def __init__(self, name: str, age: int, breed: str):
        # Your code here
        pass

    def speak(self) -> str:
        # Your code here (use super().speak()!)
        pass

    def describe(self) -> str:
        # Your code here (use super().describe()!)
        pass


class Cat(Animal):
    # Your code here
    pass


class Bird(Animal):
    # Your code here
    pass
```

**Tips to get you started:**

- Your child `__init__` must pass all the arguments the parent expects (`name`, `age`, `sound`) via `super().__init__(...)`
- `sound` is fixed per child class, so don't take it from the user — pass it directly inside `super().__init__()`
- Method overriding pattern: `parent_result = super().speak()` → `return f"{parent_result} (extra stuff)"`
- It's safest to call `super().__init__()` as the **first line** of your child's `__init__`

## 🎪 Test Your Code

Try running these test cases:

```python
# Test 1: Dog
buddy = Dog("Buddy", 3, "Golden Retriever")
print(buddy.speak())     # Buddy says Woof! (A Golden Retriever barking happily)
print(buddy.describe())  # Buddy is 3 years old. It is a Golden Retriever dog.

# Test 2: Cat (indoor)
whiskers = Cat("Whiskers", 5, True)
print(whiskers.speak())     # Whiskers says Meow! (purring softly)
print(whiskers.describe())  # Whiskers is 5 years old. It is an indoor cat.

# Test 3: Cat (outdoor)
shadow = Cat("Shadow", 2, False)
print(shadow.speak())     # Shadow says Meow! (hissing at strangers)
print(shadow.describe())  # Shadow is 2 years old. It is an outdoor cat.

# Test 4: Bird (can fly)
tweety = Bird("Tweety", 1, True)
print(tweety.speak())     # Tweety says Tweet! (while flying around)
print(tweety.describe())  # Tweety is 1 years old. This bird can fly.

# Test 5: Bird (cannot fly)
pingu = Bird("Pingu", 4, False)
print(pingu.speak())     # Pingu says Tweet! (from its perch)
print(pingu.describe())  # Pingu is 4 years old. This bird cannot fly.
```

## 🤔 Think About It

While coding (or after you finish), reflect:

1. What if you skipped `super().__init__()` and just wrote `self.name = name` etc. in the child? Would it work? Would there still be a problem?
2. What if you didn't call `super().speak()` inside the child's `speak()` and just wrote out `f"{self.name} says {self.sound}! ..."` directly? What changes?
3. If the parent `Animal`'s `speak()` output format changes later (e.g., to a different greeting style), which approach is easier to maintain?
4. `Dog`, `Cat`, and `Bird` all have methods with the same name (`speak`, `describe`) but behave differently. What is this property called?

## 🎁 Bonus Challenges

Finished the core task? Try these!

### 🥉 Easy: Add a `__str__` method

Add a `__str__` method to the `Animal` class that returns the result of `describe()`. So `print(buddy)` should call `describe()` automatically. Verify that even without defining `__str__` in child classes, calling `print()` on a child instance triggers each child's `describe()`.

### 🥈 Medium: Add a new animal

Create a new `Fish` class:
- Extra attribute: `water_type` (`"freshwater"` or `"saltwater"`, str)
- `sound` is `"Blub"`
- `speak()`: `"{parent result} (blowing bubbles)"`
- `describe()`: `"{parent result} It lives in {water_type}."`

```python
nemo = Fish("Nemo", 2, "saltwater")
print(nemo.speak())     # Nemo says Blub! (blowing bubbles)
print(nemo.describe())  # Nemo is 2 years old. It lives in saltwater.
```

### 🥇 Hard: Shelter simulation using polymorphism

Write a function that takes a list of animals and runs the shelter's "morning roll call":

```python
def morning_roll_call(animals: list) -> None:
    """
    Take a list of animals and print each one's speak() and describe() in order.
    Should work even when the list mixes Dogs, Cats, and Birds.
    """
    pass

# Test
shelter = [
    Dog("Rex", 5, "Bulldog"),
    Cat("Luna", 3, True),
    Bird("Coco", 2, True),
    Cat("Shadow", 7, False)
]
morning_roll_call(shelter)
```

Explain in one sentence *why* this single function works on mixed animal types. (Hint: use the word "polymorphism"!)

---

Drop your questions in the thread if you get stuck! Remember, the goal is to learn, not just to finish. Take your time and understand how `super()` works.

Good luck! 🚀
