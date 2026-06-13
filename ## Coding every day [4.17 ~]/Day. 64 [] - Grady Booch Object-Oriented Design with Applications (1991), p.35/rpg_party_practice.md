# 🎮 Python 연습: RPG 파티 만들기 — 상속 마스터하기!

여러분, 안녕하세요! 오늘은 객체 지향 프로그래밍의 핵심 개념인 **상속(Inheritance)**을 배웁니다. 그리고 무엇으로 배울까요? 바로 우리만의 RPG 게임 캐릭터 시스템입니다! ⚔️🔮🏹

## 🎯 미션

여러분은 게임 회사의 신입 개발자입니다. 디자이너가 새로운 RPG의 캐릭터 시스템을 설계해달라고 요청했어요. 모든 캐릭터(전사, 마법사, 궁수)는 공통점이 있습니다 — 이름, HP, 레벨 — 하지만 각자의 특수 능력도 있죠.

**똑같은 코드를 세 번 작성하시겠어요?** 절대 안 됩니다! 그래서 **상속**이 필요한 거예요.

## 📚 새로운 개념: 상속이란?

**상속**은 한 클래스(자식)가 다른 클래스(부모)의 속성과 메서드를 물려받는 것입니다.

```python
class Parent:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        return f"안녕, 나는 {self.name}이야!"

class Child(Parent):   # ← Parent를 상속받음
    pass

c = Child("Alice")
print(c.greet())   # "안녕, 나는 Alice이야!" — 메서드를 물려받음!
```

> 💡 **핵심 포인트:** `class Child(Parent):`라고 쓰면, `Child`는 `Parent`의 모든 것을 자동으로 가지게 됩니다. 추가로 자신만의 기능을 더할 수도 있어요.

### 자식 클래스에서 새 기능 추가하기

자식 클래스는 부모의 것을 그대로 받으면서, 자기만의 속성과 메서드를 추가할 수 있습니다:

```python
class Child(Parent):
    def __init__(self, name, age):
        Parent.__init__(self, name)   # 부모의 __init__ 호출
        self.age = age                # 자식만의 새 속성
    
    def dance(self):                  # 자식만의 새 메서드
        return f"{self.name}이(가) 춤춰요!"
```

> 📌 **중요:** 자식 클래스에서 `__init__`을 정의할 때, 부모의 `__init__`을 명시적으로 호출해야 부모의 속성이 제대로 설정됩니다. `Parent.__init__(self, ...)` 형태로 호출하세요.

## 📋 규칙

*만들어야 할 것:*

**1) `Character` 클래스 (부모)**
- 속성: `name`, `hp`, `max_hp`, `level`
- 메서드: `introduce()`, `take_damage(amount)`, `level_up()`, `is_alive()`, `__str__()`

**2) `Warrior` 클래스 (`Character`를 상속)**
- 추가 속성: `weapon`, `armor`
- 추가 메서드: `battle_cry()`

**3) `Mage` 클래스 (`Character`를 상속)**
- 추가 속성: `mana`, `spell_book`
- 추가 메서드: `cast_spell(spell_name)`

**4) `Archer` 클래스 (`Character`를 상속)**
- 추가 속성: `arrows`, `range`
- 추가 메서드: `shoot_arrow()`

*반드시 따라야 할 제약사항:*
- 모든 자식 클래스는 `Character`로부터 상속받아야 합니다
- `introduce()`, `take_damage()`, `level_up()`, `is_alive()`, `__str__()` 코드를 자식 클래스에 다시 작성하지 마세요 — 상속의 의미가 없어집니다!
- 변수 및 함수 이름은 모두 `snake_case`로

## 💡 상세 명세

### Character 클래스

| 메서드 | 동작 |
|---|---|
| `__init__(name, hp, level=1)` | 속성 초기화. `max_hp`는 처음 `hp`와 같은 값으로 |
| `introduce()` | `"I am {name}, a level {level} adventurer with {hp} HP."` 반환 |
| `take_damage(amount)` | `hp`에서 `amount`만큼 감소. 0 미만이 되면 0으로 |
| `level_up()` | `level` 1 증가, `max_hp` 10 증가, `hp`를 새 `max_hp`로 회복 |
| `is_alive()` | `hp > 0`이면 `True`, 아니면 `False` |
| `__str__()` | `"{name} (Lv.{level}, HP: {hp}/{max_hp})"` 반환 |

### Warrior 클래스
- `__init__(name, hp, level=1, weapon="Sword")` — `armor`는 기본값 5
- `battle_cry()` → `"{name} swings the {weapon} and shouts: For glory!"` 반환

### Mage 클래스
- `__init__(name, hp, level=1, mana=50)` — `spell_book`은 기본값 `["Fireball", "Ice Shard"]`
- `cast_spell(spell_name)` → 주문이 `spell_book`에 있고 `mana >= 10`이면, 마나 10 감소시키고 `"{name} casts {spell_name}!"` 반환. 아니면 `"{name} cannot cast {spell_name}."` 반환

### Archer 클래스
- `__init__(name, hp, level=1, arrows=20)` — `range`는 기본값 50
- `shoot_arrow()` → `arrows > 0`이면 1 감소시키고 `"{name} shoots an arrow! Arrows left: {arrows}"` 반환. 아니면 `"{name} is out of arrows!"` 반환

## 🎪 코드 테스트

```python
# 테스트 1: 기본 Character
hero = Character("Hero", 100)
print(hero.introduce())          # "I am Hero, a level 1 adventurer with 100 HP."
hero.take_damage(30)
print(hero.hp)                   # 70
print(hero.is_alive())           # True

# 테스트 2: Warrior
conan = Warrior("Conan", 120)
print(conan.battle_cry())        # "Conan swings the Sword and shouts: For glory!"
conan.take_damage(20)            # 상속받은 메서드 사용!
print(conan.hp)                  # 100

# 테스트 3: Mage
gandalf = Mage("Gandalf", 70)
print(gandalf.cast_spell("Fireball"))   # "Gandalf casts Fireball!"
print(gandalf.mana)                     # 40

# 테스트 4: Archer
legolas = Archer("Legolas", 90)
print(legolas.shoot_arrow())     # "Legolas shoots an arrow! Arrows left: 19"
legolas.level_up()               # 상속받은 메서드!
print(legolas.level)             # 2

# 테스트 5: __str__ 상속 확인
print(str(conan))                # "Conan (Lv.1, HP: 100/120)"
```

## 🤔 시작 전 생각해보기

1. 왜 `Warrior`, `Mage`, `Archer`가 각자 `take_damage()`를 다시 작성하지 않아도 될까요?
2. `Warrior.__init__`에서 `Character.__init__(self, name, hp, level)`을 호출하지 않으면 어떤 일이 일어날까요?
3. `weapon`이나 `mana` 같은 속성을 왜 `Character`에 두지 않고 자식 클래스에 두는 걸까요?

## 🎁 보너스 챌린지

다 끝내셨나요? 더 깊이 들어가 봅시다!

### 🥉 Easy — 파티 만들기
4명의 캐릭터로 구성된 파티(리스트)를 만들고, 반복문으로 모두의 `introduce()`를 출력해보세요. 같은 코드 한 줄로 서로 다른 타입의 캐릭터들이 자기소개를 합니다 — 이것이 **다형성(polymorphism)**의 시작입니다!

### 🥈 Medium — 전투 시뮬레이션
파티의 모든 멤버에게 25 데미지를 입히는 함수 `attack_party(party)`를 만드세요. 그 다음, 살아있는 멤버만 필터링해서 출력하세요. `is_alive()`가 진가를 발휘하는 순간입니다.

### 🥇 Hard — `__eq__`과 `__repr__` 다루기 (미리 보기 ⚠️)

> 🆕 **새로운 개념 미리 보기:** 아래는 아직 수업에서 다루지 않은 dunder 메서드입니다. 호기심 있는 학생을 위한 도전 과제!

두 캐릭터가 같은 이름과 같은 레벨이면 "같다"고 판단하는 `__eq__` 메서드를 `Character`에 추가하세요:

```python
def __eq__(self, other):
    return self.name == other.name and self.level == other.level
```

그리고 디버깅용 `__repr__`도 추가:

```python
def __repr__(self):
    return f"Character(name={self.name!r}, level={self.level})"
```

테스트:
```python
a = Character("Hero", 100, 5)
b = Character("Hero", 80, 5)    # HP 다름, 이름/레벨 같음
print(a == b)                    # True!
print(repr(a))                   # Character(name='Hero', level=5)
```

자식 클래스도 자동으로 이 동작을 물려받습니다 — 또 한 번 상속의 힘을 느껴보세요!

## 📤 제출 방법

1. `removeDuplicates_practice.py`처럼 `rpg_party_practice.py`라는 파일로 저장
2. 모든 테스트가 통과하는지 확인
3. 스레드에 질문이 있으면 언제든지!

행운을 빕니다, 모험가들이여! 🗡️✨

---
---

# 🎮 Python Practice: Build Your RPG Party — Master Inheritance!

Hey team! Today we're tackling one of the cornerstones of object-oriented programming: **inheritance**. And what better way to learn it than by building our very own RPG character system? ⚔️🔮🏹

## 🎯 Your Mission

You're a new developer at a game studio. The designers want you to build the character system for their new RPG. All characters (Warriors, Mages, Archers) share common traits — name, HP, level — but each has their own special abilities.

**Would you write the same code three times?** No way! That's where **inheritance** comes in.

## 📚 New Concept: What is Inheritance?

**Inheritance** lets one class (the child) take on the attributes and methods of another class (the parent).

```python
class Parent:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        return f"Hi, I'm {self.name}!"

class Child(Parent):   # ← Inherits from Parent
    pass

c = Child("Alice")
print(c.greet())   # "Hi, I'm Alice!" — method inherited!
```

> 💡 **Key insight:** Writing `class Child(Parent):` automatically gives `Child` everything `Parent` has. You can also add new things on top.

### Adding New Features in a Child Class

A child can keep what the parent gives AND add its own attributes and methods:

```python
class Child(Parent):
    def __init__(self, name, age):
        Parent.__init__(self, name)   # call parent's __init__
        self.age = age                # new attribute (child-only)
    
    def dance(self):                  # new method (child-only)
        return f"{self.name} is dancing!"
```

> 📌 **Important:** When you define `__init__` in a child class, you must explicitly call the parent's `__init__` to properly set up inherited attributes. Use `Parent.__init__(self, ...)`.

## 📋 The Rules

*What you'll build:*

**1) `Character` class (parent)**
- Attributes: `name`, `hp`, `max_hp`, `level`
- Methods: `introduce()`, `take_damage(amount)`, `level_up()`, `is_alive()`, `__str__()`

**2) `Warrior` class (inherits from `Character`)**
- New attributes: `weapon`, `armor`
- New method: `battle_cry()`

**3) `Mage` class (inherits from `Character`)**
- New attributes: `mana`, `spell_book`
- New method: `cast_spell(spell_name)`

**4) `Archer` class (inherits from `Character`)**
- New attributes: `arrows`, `range`
- New method: `shoot_arrow()`

*Constraints you must follow:*
- All child classes must inherit from `Character`
- Do **NOT** rewrite `introduce()`, `take_damage()`, `level_up()`, `is_alive()`, or `__str__()` in the child classes — that defeats the purpose of inheritance!
- Use `snake_case` for all variables and methods

## 💡 Detailed Specification

### Character class

| Method | Behavior |
|---|---|
| `__init__(name, hp, level=1)` | Initialize attributes. `max_hp` should equal initial `hp` |
| `introduce()` | Returns `"I am {name}, a level {level} adventurer with {hp} HP."` |
| `take_damage(amount)` | Subtract `amount` from `hp`. Clamp to 0 if it goes below |
| `level_up()` | Increase `level` by 1, `max_hp` by 10, restore `hp` to new `max_hp` |
| `is_alive()` | Returns `True` if `hp > 0`, else `False` |
| `__str__()` | Returns `"{name} (Lv.{level}, HP: {hp}/{max_hp})"` |

### Warrior class
- `__init__(name, hp, level=1, weapon="Sword")` — `armor` defaults to 5
- `battle_cry()` → returns `"{name} swings the {weapon} and shouts: For glory!"`

### Mage class
- `__init__(name, hp, level=1, mana=50)` — `spell_book` defaults to `["Fireball", "Ice Shard"]`
- `cast_spell(spell_name)` → if spell is in `spell_book` AND `mana >= 10`, reduce mana by 10 and return `"{name} casts {spell_name}!"`. Else return `"{name} cannot cast {spell_name}."`

### Archer class
- `__init__(name, hp, level=1, arrows=20)` — `range` defaults to 50
- `shoot_arrow()` → if `arrows > 0`, decrease by 1 and return `"{name} shoots an arrow! Arrows left: {arrows}"`. Else return `"{name} is out of arrows!"`

## 🎪 Test Your Code

```python
# Test 1: Basic Character
hero = Character("Hero", 100)
print(hero.introduce())          # "I am Hero, a level 1 adventurer with 100 HP."
hero.take_damage(30)
print(hero.hp)                   # 70
print(hero.is_alive())           # True

# Test 2: Warrior
conan = Warrior("Conan", 120)
print(conan.battle_cry())        # "Conan swings the Sword and shouts: For glory!"
conan.take_damage(20)            # Inherited method!
print(conan.hp)                  # 100

# Test 3: Mage
gandalf = Mage("Gandalf", 70)
print(gandalf.cast_spell("Fireball"))   # "Gandalf casts Fireball!"
print(gandalf.mana)                     # 40

# Test 4: Archer
legolas = Archer("Legolas", 90)
print(legolas.shoot_arrow())     # "Legolas shoots an arrow! Arrows left: 19"
legolas.level_up()               # Inherited method!
print(legolas.level)             # 2

# Test 5: __str__ inheritance check
print(str(conan))                # "Conan (Lv.1, HP: 100/120)"
```

## 🤔 Think Before You Code

1. Why don't `Warrior`, `Mage`, and `Archer` each need their own `take_damage()`?
2. What would happen if you forgot to call `Character.__init__(self, name, hp, level)` inside `Warrior.__init__`?
3. Why do `weapon` and `mana` belong on the child classes, not on `Character`?

## 🎁 Bonus Challenges

Finished early? Let's go deeper!

### 🥉 Easy — Build a Party
Make a list of 4 mixed characters (one of each type plus one extra) and use a `for` loop to call `introduce()` on each. One loop, different types — this is the start of **polymorphism**!

### 🥈 Medium — Battle Simulation
Write a function `attack_party(party)` that deals 25 damage to every member. Then filter and print only the survivors. This is where `is_alive()` earns its keep.

### 🥇 Hard — `__eq__` and `__repr__` (Preview ⚠️)

> 🆕 **New concept preview:** These dunders haven't been covered in class yet — for the curious!

Add an `__eq__` method to `Character` that treats two characters as equal if they share the same name AND level:

```python
def __eq__(self, other):
    return self.name == other.name and self.level == other.level
```

Also add a debug-friendly `__repr__`:

```python
def __repr__(self):
    return f"Character(name={self.name!r}, level={self.level})"
```

Test it:
```python
a = Character("Hero", 100, 5)
b = Character("Hero", 80, 5)    # different HP, same name/level
print(a == b)                    # True!
print(repr(a))                   # Character(name='Hero', level=5)
```

Child classes automatically inherit this behavior — feel the power of inheritance again!

## 📤 How to Submit

1. Save your file as `rpg_party_practice.py`
2. Make sure all tests pass
3. Drop questions in the thread anytime!

Good luck, adventurers! 🗡️✨
