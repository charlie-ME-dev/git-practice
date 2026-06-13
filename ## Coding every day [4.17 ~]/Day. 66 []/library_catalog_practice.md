# 📚 Python 연습 (Day 3 - 상속): 도서관 카탈로그 시스템

여러분, 안녕하세요! 상속 연습 셋째 날입니다. 오늘은 **객체의 타입을 확인하고** 클래스 계층 구조를 똑똑하게 활용하는 방법을 배워봅시다!

---

## 🎯 미션

여러분은 시립 도서관의 새 디지털 카탈로그 시스템을 개발하는 백엔드 엔지니어입니다. 도서관에는 **책(Book)**, **DVD**, **잡지(Magazine)** 세 종류의 자료가 있습니다. 모두 도서관 자료라는 공통점은 있지만, 각각의 고유한 정보(저자, 감독, 발행호)도 있어야 해요.

여러분의 임무는:

1. 공통 동작을 담은 **부모 클래스 `LibraryItem`** 만들기
2. 각각의 특성을 가진 **세 자식 클래스** 만들기
3. 카탈로그를 처리하는 **헬퍼 함수**를 작성하며 `isinstance()`와 `issubclass()` 마스터하기

> *"All well-structured object-oriented architectures are filled with patterns. Indeed, one of the qualities of an object-oriented system of measure is the degree to which its developers have paid attention to the harmonious relationships of its objects."*
>
> — **Grady Booch**, *Object-Oriented Analysis and Design with Applications*

---

## 📋 오늘의 핵심 개념

### 1. `isinstance(객체, 클래스)` — 객체의 타입 확인

```python
book = Book("...", ...)
isinstance(book, Book)         # True
isinstance(book, LibraryItem)  # True (부모 클래스도 True!)
isinstance(book, DVD)          # False
```

**중요한 포인트:** `isinstance()`는 **상속 관계를 따라갑니다**. 즉, `Book`이 `LibraryItem`을 상속받았다면, `Book` 인스턴스는 `LibraryItem`의 인스턴스이기도 합니다. 이게 바로 다형성이 작동하는 핵심 원리예요!

### 2. `issubclass(클래스, 클래스)` — 클래스 관계 확인

```python
issubclass(Book, LibraryItem)   # True
issubclass(DVD, Book)           # False
issubclass(LibraryItem, Book)   # False (반대 방향)
```

**`isinstance` vs `issubclass` 비교:**

| 함수 | 첫 번째 인자 | 무엇을 확인? |
|------|-------------|-------------|
| `isinstance` | **객체 (instance)** | 그 객체가 특정 클래스의 인스턴스인가? |
| `issubclass` | **클래스 (class)** | 그 클래스가 특정 클래스의 자식인가? |

### 3. 보호된 속성 (`_attribute` 관습)

Python에서는 변수명 앞에 **밑줄 하나(`_`)** 를 붙여서 "이건 내부용이니까 직접 건드리지 마세요"라고 표시합니다.

```python
class LibraryItem:
    def __init__(self, title):
        self._title = title   # 보호된 속성 (관습)

# 외부에서:
book._title           # 가능은 하지만 권장하지 않음
book.get_title()      # 이게 올바른 방법!
```

> 💡 Python은 진짜 private을 강제하지 않아요 — **약속(convention)** 입니다. 하지만 팀 코딩에서는 이 약속을 지키는 것이 매우 중요해요!

---

## 🏗️ 클래스 설계도

### 부모 클래스: `LibraryItem`

**속성 (모두 `_`로 시작):**
- `_title`: 자료의 제목
- `_item_id`: 고유 ID (예: "B001", "D001")
- `_year`: 발행/제작 연도
- `_is_checked_out`: 대출 중인지 여부 (`True`/`False`, 처음엔 `False`)
- `_borrower`: 현재 대출자 이름 (대출 안 됐으면 `None`)

**메서드:**
- `__init__(self, title, item_id, year)`: 초기화
- `check_out(self, borrower_name)`: 대출 처리
- `return_item(self)`: 반납 처리
- `get_info(self)`: 자료 정보 문자열 반환
- `get_title(self)`: 제목 반환
- `get_item_id(self)`: ID 반환
- `is_available(self)`: 대출 가능 여부 반환

### 자식 클래스 1: `Book(LibraryItem)`

**추가 속성:**
- `_author`: 저자명
- `_pages`: 페이지 수

**오버라이드:** `get_info()` — 저자와 페이지 수 정보를 추가

**추가 메서드:** `get_author()`

### 자식 클래스 2: `DVD(LibraryItem)`

**추가 속성:**
- `_director`: 감독명
- `_runtime_minutes`: 상영 시간(분)

**오버라이드:** `get_info()` — 감독과 상영 시간 정보를 추가

**추가 메서드:** `get_director()`

### 자식 클래스 3: `Magazine(LibraryItem)`

**추가 속성:**
- `_issue_number`: 발행 호수
- `_month`: 발행 월

**오버라이드:** `get_info()` — 발행 호수와 월 정보를 추가

**추가 메서드:** `get_issue_number()`

### 헬퍼 함수 (클래스 외부, 일반 함수로 작성)

- `count_books(items)`: 리스트에서 `Book` 인스턴스의 개수 반환
- `filter_by_type(items, item_type)`: 주어진 타입의 인스턴스만 리스트로 반환
- `is_library_item_subclass(some_class)`: 어떤 클래스가 `LibraryItem`의 자식인지 확인 (단, `LibraryItem` 자기 자신은 제외)
- `get_available_items(items)`: 대출 가능한 자료들만 리스트로 반환

---

## 💡 예제

```python
# 객체 생성
book = Book("The Great Gatsby", "B001", 1925, "F. Scott Fitzgerald", 180)
dvd = DVD("Inception", "D001", 2010, "Christopher Nolan", 148)
mag = Magazine("National Geographic", "M001", 2024, 245, "March")

# 부모로부터 상속받은 메서드 사용
print(book.check_out("Alice"))
# 출력: 'The Great Gatsby' has been checked out by Alice

# 오버라이드된 메서드 — 각 클래스마다 다르게 동작!
print(book.get_info())
# 출력: [B001] The Great Gatsby (1925) - Checked out | Author: F. Scott Fitzgerald, 180 pages

print(dvd.get_info())
# 출력: [D001] Inception (2010) - Available | Director: Christopher Nolan, 148 min

# isinstance() 사용
isinstance(book, Book)         # True
isinstance(book, LibraryItem)  # True (상속 관계!)
isinstance(book, DVD)          # False

# issubclass() 사용
issubclass(Book, LibraryItem)  # True
issubclass(DVD, Book)          # False
```

---

## ⚠️ 제약사항

- ❌ **데코레이터 사용 금지**: `@property`, `@classmethod`, `@staticmethod` 사용하지 마세요 (아직 안 배웠어요!)
- ✅ 모든 속성은 `_` 접두사를 붙여 보호된 속성으로 선언
- ✅ 외부에서 속성에 접근할 때는 반드시 getter 메서드 사용
- ✅ 모든 이름은 snake_case (PEP 8)
- ✅ `isinstance()`와 `issubclass()`를 적극 활용

---

## 🧪 테스트 케이스

```python
# 테스트 1: 객체 생성과 기본 동작
book1 = Book("1984", "B001", 1949, "George Orwell", 328)
print(book1.get_info())
# 예상: [B001] 1984 (1949) - Available | Author: George Orwell, 328 pages

# 테스트 2: 대출과 반납
print(book1.check_out("Alice"))
# 예상: 'Alice'가 대출했다는 메시지
print(book1.check_out("Bob"))
# 예상: 이미 대출 중이라는 메시지
print(book1.return_item())
# 예상: 'Alice'가 반납했다는 메시지

# 테스트 3: 오버라이드된 get_info() — 각 클래스마다 다름
dvd1 = DVD("The Matrix", "D001", 1999, "Wachowskis", 136)
mag1 = Magazine("Time", "M001", 2024, 12, "January")
print(book1.get_info())  # Book 형식
print(dvd1.get_info())   # DVD 형식
print(mag1.get_info())   # Magazine 형식

# 테스트 4: isinstance()로 카운트
catalog = [book1, dvd1, mag1, Book("Dune", "B002", 1965, "Herbert", 412)]
assert count_books(catalog) == 2

# 테스트 5: filter_by_type()
dvds = filter_by_type(catalog, DVD)
assert len(dvds) == 1

# 부모 클래스로 필터링하면? → 모든 자료!
all_items = filter_by_type(catalog, LibraryItem)
assert len(all_items) == 4

# 테스트 6: issubclass()
assert is_library_item_subclass(Book) == True
assert is_library_item_subclass(DVD) == True
assert is_library_item_subclass(str) == False
assert is_library_item_subclass(LibraryItem) == False  # 자기 자신은 제외!

# 테스트 7: get_available_items()
dvd1.check_out("Charlie")
available = get_available_items(catalog)
assert dvd1 not in available
```

---

## 🤔 생각해보기

코딩하기 전에 잠깐 생각해봅시다:

1. `isinstance(book, LibraryItem)`이 `True`인 이유는 무엇일까요?
2. `filter_by_type(catalog, LibraryItem)`을 호출하면 왜 모든 자료가 반환될까요?
3. 왜 `_title`처럼 밑줄을 붙여서 작성하나요? Python이 진짜로 막아주나요?
4. `issubclass(Book, LibraryItem)`과 `isinstance(some_book, LibraryItem)`의 차이는 무엇인가요?

---

## 🎁 보너스 챌린지

### 🥉 Easy: `sort_by_type_and_title(items)`

자료들을 다음 순서로 정렬하세요:
- 먼저 **타입별로 그룹화**: Books → DVDs → Magazines
- 각 그룹 안에서는 **제목 알파벳순**

```python
items = [
    Magazine("Time", ...),
    Book("Zelda", ...),
    DVD("Avatar", ...),
    Book("Atomic Habits", ...),
]
result = sort_by_type_and_title(items)
# 결과 순서: Atomic Habits → Zelda → Avatar → Time
```

**힌트:** `isinstance()`로 각 그룹을 분리하고, 각 그룹을 정렬한 후 합쳐보세요.

### 🥈 Medium: `AudioBook(Book)` — 다단계 상속

`Book`을 상속받는 `AudioBook` 클래스를 만드세요:
- 추가 속성: `_narrator` (성우), `_duration_hours` (재생 시간)
- `get_info()` 오버라이드 (성우와 시간 정보 추가)

테스트:
```python
ab = AudioBook("Becoming", "A001", 2018, "Michelle Obama", 448, "Michelle Obama", 19)
isinstance(ab, AudioBook)   # True
isinstance(ab, Book)        # True (다단계 상속!)
isinstance(ab, LibraryItem) # True
isinstance(ab, DVD)         # False
```

**질문:** 왜 `AudioBook` 인스턴스가 `Book`과 `LibraryItem` 모두의 인스턴스인가요?

### 🥇 Hard: 안전한 카탈로그 처리

두 함수를 작성하세요:

**(1) `safe_check_out(item, borrower_name)`**
- `item`이 `LibraryItem`의 인스턴스가 아니면 에러 메시지 반환
- 맞다면 정상적으로 대출 처리

```python
safe_check_out("not a book", "Alice")
# 출력: "Error: str is not a library item and cannot be checked out"

safe_check_out(book1, "Alice")
# 출력: 정상 대출 메시지
```

**(2) `count_by_each_type(items)`**
- 각 정확한 타입(exact type)별로 개수를 세서 딕셔너리로 반환

```python
catalog = [book1, book2, dvd1, mag1, audiobook1]
count_by_each_type(catalog)
# 출력: {'Book': 2, 'DVD': 1, 'Magazine': 1, 'AudioBook': 1}
```

**힌트:** `type(item).__name__`을 사용하면 객체의 정확한 타입 이름(문자열)을 얻을 수 있어요.

> 💡 `type(item)`과 `isinstance(item, ...)`의 차이: `type()`은 **정확한 타입만** 확인하고, `isinstance()`는 **상속 관계를 포함**해서 확인합니다.

막히면 언제든 스레드에 질문 주세요! 목표는 끝내는 것이 아니라 **이해하는 것**입니다. 🎯

행운을 빕니다! 🚀

---
---

# 📚 Python Practice (Day 3 - Inheritance): Library Catalog System

Hey team! Welcome to day three of inheritance practice. Today we're learning how to **check object types** and use class hierarchies intelligently!

---

## 🎯 Your Mission

You're a backend engineer building the new digital catalog system for the city library. The library has three types of items: **Books**, **DVDs**, and **Magazines**. They share common behavior (they're all library items), but each has unique data (author, director, issue number).

Your tasks:

1. Build a **parent class `LibraryItem`** with shared behavior
2. Build **three child classes** with their unique attributes
3. Write **helper functions** that process catalogs — mastering `isinstance()` and `issubclass()` along the way

> *"All well-structured object-oriented architectures are filled with patterns. Indeed, one of the qualities of an object-oriented system of measure is the degree to which its developers have paid attention to the harmonious relationships of its objects."*
>
> — **Grady Booch**, *Object-Oriented Analysis and Design with Applications*

---

## 📋 Today's Core Concepts

### 1. `isinstance(object, class)` — Check an object's type

```python
book = Book("...", ...)
isinstance(book, Book)         # True
isinstance(book, LibraryItem)  # True (parent class is True too!)
isinstance(book, DVD)          # False
```

**Key point:** `isinstance()` **follows the inheritance chain**. If `Book` inherits from `LibraryItem`, then a `Book` instance is also a `LibraryItem` instance. This is exactly how polymorphism works under the hood!

### 2. `issubclass(class, class)` — Check class relationships

```python
issubclass(Book, LibraryItem)   # True
issubclass(DVD, Book)           # False
issubclass(LibraryItem, Book)   # False (reverse direction)
```

**`isinstance` vs `issubclass` comparison:**

| Function | First argument | What it checks |
|----------|---------------|----------------|
| `isinstance` | **object (instance)** | Is the object an instance of this class? |
| `issubclass` | **class** | Is this class a child of that class? |

### 3. Protected attributes (`_attribute` convention)

In Python, prefixing a variable with **a single underscore (`_`)** signals "this is internal — please don't touch it directly."

```python
class LibraryItem:
    def __init__(self, title):
        self._title = title   # protected attribute (by convention)

# From outside:
book._title           # Possible, but not recommended
book.get_title()      # This is the right way!
```

> 💡 Python doesn't enforce true private — it's a **convention**. But in team coding, honoring this convention is hugely important!

---

## 🏗️ Class Blueprint

### Parent class: `LibraryItem`

**Attributes (all start with `_`):**
- `_title`: title of the item
- `_item_id`: unique ID (e.g., "B001", "D001")
- `_year`: publication/release year
- `_is_checked_out`: whether it's checked out (`True`/`False`, starts `False`)
- `_borrower`: current borrower's name (`None` when not checked out)

**Methods:**
- `__init__(self, title, item_id, year)`: initialize
- `check_out(self, borrower_name)`: handle checkout
- `return_item(self)`: handle return
- `get_info(self)`: return item info as a string
- `get_title(self)`: return title
- `get_item_id(self)`: return ID
- `is_available(self)`: return availability

### Child class 1: `Book(LibraryItem)`

**Additional attributes:**
- `_author`: author's name
- `_pages`: number of pages

**Override:** `get_info()` — adds author and page info

**Additional method:** `get_author()`

### Child class 2: `DVD(LibraryItem)`

**Additional attributes:**
- `_director`: director's name
- `_runtime_minutes`: runtime in minutes

**Override:** `get_info()` — adds director and runtime info

**Additional method:** `get_director()`

### Child class 3: `Magazine(LibraryItem)`

**Additional attributes:**
- `_issue_number`: issue number
- `_month`: month of publication

**Override:** `get_info()` — adds issue number and month info

**Additional method:** `get_issue_number()`

### Helper functions (outside classes, regular functions)

- `count_books(items)`: return the count of `Book` instances in the list
- `filter_by_type(items, item_type)`: return only instances of the given type
- `is_library_item_subclass(some_class)`: check if a class is a child of `LibraryItem` (excluding `LibraryItem` itself)
- `get_available_items(items)`: return only items that are available

---

## 💡 Examples

```python
# Create objects
book = Book("The Great Gatsby", "B001", 1925, "F. Scott Fitzgerald", 180)
dvd = DVD("Inception", "D001", 2010, "Christopher Nolan", 148)
mag = Magazine("National Geographic", "M001", 2024, 245, "March")

# Use inherited methods from parent
print(book.check_out("Alice"))
# Output: 'The Great Gatsby' has been checked out by Alice

# Overridden methods — different behavior per class!
print(book.get_info())
# Output: [B001] The Great Gatsby (1925) - Checked out | Author: F. Scott Fitzgerald, 180 pages

print(dvd.get_info())
# Output: [D001] Inception (2010) - Available | Director: Christopher Nolan, 148 min

# Using isinstance()
isinstance(book, Book)         # True
isinstance(book, LibraryItem)  # True (inheritance!)
isinstance(book, DVD)          # False

# Using issubclass()
issubclass(Book, LibraryItem)  # True
issubclass(DVD, Book)          # False
```

---

## ⚠️ Constraints

- ❌ **No decorators**: don't use `@property`, `@classmethod`, `@staticmethod` (we haven't learned these yet!)
- ✅ All attributes must use the `_` prefix (protected attribute convention)
- ✅ Always use getter methods when accessing attributes from outside the class
- ✅ All names must be snake_case (PEP 8)
- ✅ Use `isinstance()` and `issubclass()` actively

---

## 🧪 Test Cases

```python
# Test 1: Object creation and basic behavior
book1 = Book("1984", "B001", 1949, "George Orwell", 328)
print(book1.get_info())
# Expected: [B001] 1984 (1949) - Available | Author: George Orwell, 328 pages

# Test 2: Check out and return
print(book1.check_out("Alice"))
# Expected: message saying Alice checked it out
print(book1.check_out("Bob"))
# Expected: message saying it's already checked out
print(book1.return_item())
# Expected: message saying Alice returned it

# Test 3: Overridden get_info() — each class is different
dvd1 = DVD("The Matrix", "D001", 1999, "Wachowskis", 136)
mag1 = Magazine("Time", "M001", 2024, 12, "January")
print(book1.get_info())  # Book format
print(dvd1.get_info())   # DVD format
print(mag1.get_info())   # Magazine format

# Test 4: Count with isinstance()
catalog = [book1, dvd1, mag1, Book("Dune", "B002", 1965, "Herbert", 412)]
assert count_books(catalog) == 2

# Test 5: filter_by_type()
dvds = filter_by_type(catalog, DVD)
assert len(dvds) == 1

# What about filtering by the parent class? → All items!
all_items = filter_by_type(catalog, LibraryItem)
assert len(all_items) == 4

# Test 6: issubclass()
assert is_library_item_subclass(Book) == True
assert is_library_item_subclass(DVD) == True
assert is_library_item_subclass(str) == False
assert is_library_item_subclass(LibraryItem) == False  # exclude itself!

# Test 7: get_available_items()
dvd1.check_out("Charlie")
available = get_available_items(catalog)
assert dvd1 not in available
```

---

## 🤔 Reflection

Before you start coding, take a moment to think:

1. Why is `isinstance(book, LibraryItem)` `True`?
2. Why does `filter_by_type(catalog, LibraryItem)` return all items?
3. Why do we write `_title` with an underscore? Does Python actually block direct access?
4. What's the difference between `issubclass(Book, LibraryItem)` and `isinstance(some_book, LibraryItem)`?

---

## 🎁 Bonus Challenges

### 🥉 Easy: `sort_by_type_and_title(items)`

Sort items in this order:
- First, **group by type**: Books → DVDs → Magazines
- Within each group, **sort alphabetically by title**

```python
items = [
    Magazine("Time", ...),
    Book("Zelda", ...),
    DVD("Avatar", ...),
    Book("Atomic Habits", ...),
]
result = sort_by_type_and_title(items)
# Order: Atomic Habits → Zelda → Avatar → Time
```

**Hint:** Use `isinstance()` to separate each group, sort each group, then combine.

### 🥈 Medium: `AudioBook(Book)` — multi-level inheritance

Create an `AudioBook` class that inherits from `Book`:
- Additional attributes: `_narrator`, `_duration_hours`
- Override `get_info()` to include narrator and duration

Test:
```python
ab = AudioBook("Becoming", "A001", 2018, "Michelle Obama", 448, "Michelle Obama", 19)
isinstance(ab, AudioBook)   # True
isinstance(ab, Book)        # True (multi-level inheritance!)
isinstance(ab, LibraryItem) # True
isinstance(ab, DVD)         # False
```

**Question:** Why is an `AudioBook` instance an instance of both `Book` AND `LibraryItem`?

### 🥇 Hard: Safe catalog processing

Write two functions:

**(1) `safe_check_out(item, borrower_name)`**
- If `item` is NOT a `LibraryItem` instance, return an error message
- Otherwise, check it out normally

```python
safe_check_out("not a book", "Alice")
# Output: "Error: str is not a library item and cannot be checked out"

safe_check_out(book1, "Alice")
# Output: normal checkout message
```

**(2) `count_by_each_type(items)`**
- Count items by their **exact type** (not by inheritance) and return as a dict

```python
catalog = [book1, book2, dvd1, mag1, audiobook1]
count_by_each_type(catalog)
# Output: {'Book': 2, 'DVD': 1, 'Magazine': 1, 'AudioBook': 1}
```

**Hint:** `type(item).__name__` gives you the exact type name as a string.

> 💡 `type(item)` vs `isinstance(item, ...)`: `type()` checks **exact type only**, while `isinstance()` **follows inheritance**.

Drop your questions in the thread anytime! Remember, the goal isn't to finish — it's to **understand**. 🎯

Good luck! 🚀
