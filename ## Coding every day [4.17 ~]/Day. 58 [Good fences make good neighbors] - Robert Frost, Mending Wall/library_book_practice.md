# 📚 Python 클래스 연습 Day 2: 도서관 시스템 만들기!

안녕하세요 여러분! Day 1에서는 클래스의 기본 — `__init__`, 속성(attributes), 메서드 — 를 배웠어요. 오늘 Day 2에서는 한 단계 더 나아가서, **실제 시스템에서 데이터를 어떻게 보호하는지** 배워봅시다.

## 🎯 미션

대학교 도서관에서 책을 관리하는 `Book` 클래스를 만들어주세요. 단순히 정보만 저장하는 게 아니라, **책의 상태(빌렸는지/반납됐는지)를 안전하게 관리**해야 해요.

**핵심 포인트:** 책의 내부 데이터(제목, 빌린 사람 등)는 외부에서 함부로 바꿀 수 없어야 합니다. 모든 변경은 **메서드를 통해서만** 이루어져야 해요. 이게 바로 오늘의 핵심 개념인 **캡슐화(encapsulation)** 입니다!

## 🆕 오늘 새로 배우는 것

### 1. Private 속성 (밑줄 표시)

Python에서는 속성 이름 앞에 밑줄(`_`)을 붙여서 "이건 내부용이에요, 직접 만지지 마세요"라고 표시합니다.

```python
class Account:
    def __init__(self, balance):
        self._balance = balance  # 밑줄 = "private"이라는 약속
```

> 💡 **참고:** Python은 강제로 막지는 않아요. 이건 **개발자 사이의 약속**입니다. "밑줄이 있으면 직접 건드리지 말고 메서드를 쓰자!"

### 2. Getter와 Setter

Private 속성을 읽거나 바꿀 때는 **전용 메서드**를 만듭니다:

```python
class Account:
    def __init__(self, balance):
        self._balance = balance

    def get_balance(self):           # getter: 읽기
        return self._balance

    def set_balance(self, new_value): # setter: 쓰기 (검증 포함!)
        if new_value < 0:
            raise ValueError("잔액은 음수가 될 수 없습니다")
        self._balance = new_value
```

**Setter의 진짜 힘:** 그냥 값을 바꾸기 전에 **검증(validation)** 을 할 수 있어요. 잘못된 값이 들어오는 걸 막을 수 있죠!

### 3. 행동 메서드 (Behavior Methods)

Getter/Setter는 단순한 읽기/쓰기지만, **행동 메서드**는 객체가 "무언가를 한다"는 의미입니다:

```python
account.deposit(1000)   # 입금하는 행동
account.withdraw(500)   # 출금하는 행동
```

이런 메서드들은 내부적으로 여러 속성을 함께 업데이트하고, 규칙을 지키도록 만듭니다.

## 📋 요구사항

`Book` 클래스를 만들어주세요. 다음을 포함해야 합니다:

### Private 속성 (모두 밑줄 시작!)
- `_title`: 책 제목 (문자열)
- `_author`: 저자 (문자열)
- `_is_borrowed`: 대출 상태 (True/False)
- `_borrower`: 현재 빌린 사람 이름 (대출 중이 아니면 `None`)
- `_borrow_count`: 지금까지 총 대출된 횟수 (정수)

### Getter 메서드
- `get_title()` → 제목 반환
- `get_author()` → 저자 반환
- `get_borrower()` → 현재 빌린 사람 반환 (없으면 `None`)
- `get_borrow_count()` → 총 대출 횟수 반환
- `is_available()` → 빌릴 수 있으면 `True`, 아니면 `False`

### Setter 메서드 (검증 포함!)
- `set_title(new_title)` → 제목 변경. **빈 문자열이면 `ValueError` 발생!**

### 행동 메서드
- `borrow(borrower_name)` → 책 대출
  - 이미 빌려간 상태면 `False` 반환 (실패)
  - 빌려갈 수 있으면 상태 업데이트하고 `True` 반환
  - 대출 횟수(`_borrow_count`) 1 증가
- `return_book()` → 책 반납
  - 빌려간 적이 없으면 `False` 반환
  - 반납 처리하고 `True` 반환

### 생성자 (`__init__`) 검증
- 제목이나 저자가 빈 문자열이면 `ValueError` 발생
- 처음에는 대출 중이 아니고, 대출 횟수는 0

## 💡 예제

```python
book = Book("파이썬 코딩의 기술", "브렛 슬라킨")

print(book.is_available())      # True
print(book.get_borrow_count())  # 0

book.borrow("김철수")
print(book.is_available())      # False
print(book.get_borrower())      # "김철수"
print(book.get_borrow_count())  # 1

book.borrow("이영희")            # 이미 대출 중!
# 반환값: False (대출 실패)

book.return_book()
print(book.is_available())      # True
print(book.get_borrower())      # None

book.borrow("이영희")
print(book.get_borrow_count())  # 2 (누적!)
```

## 🎓 알아야 할 것

- 클래스 정의 (`class`, `__init__`, `self`) — Day 1 복습
- 속성에 값 할당하기 — Day 1 복습
- 메서드 정의와 호출 — Day 1 복습
- `if` 문으로 조건 확인 — 기존
- `raise ValueError("메시지")` — **오늘 새로 사용!**
- `None` 값 다루기 — 기존

## ✅ 과제

```python
class Book:
    def __init__(self, title: str, author: str):
        # 여기에 코드 작성
        pass

    # 나머지 메서드들...
```

스켈레톤 파일(`library_book_skeleton.py`)을 받아서 시작하세요!

## 🎪 테스트 케이스

```python
# 테스트 1: 기본 생성
b1 = Book("이상한 나라의 앨리스", "루이스 캐럴")
assert b1.get_title() == "이상한 나라의 앨리스"
assert b1.is_available() == True

# 테스트 2: 대출
assert b1.borrow("김민수") == True
assert b1.is_available() == False
assert b1.get_borrower() == "김민수"

# 테스트 3: 중복 대출 방지
assert b1.borrow("박지영") == False  # 이미 대출 중

# 테스트 4: 반납
assert b1.return_book() == True
assert b1.is_available() == True

# 테스트 5: 빈 제목 거부
try:
    bad = Book("", "저자")
    print("❌ 실패: 에러가 발생해야 함")
except ValueError:
    print("✅ 빈 제목 거부됨")
```

## 🏆 보너스 챌린지

### 🥉 Bronze — `__str__` 메서드 추가
책을 `print()` 했을 때 보기 좋게 출력되도록 만들어보세요:
```
"파이썬 코딩의 기술" by 브렛 슬라킨 [대출 가능]
"파이썬 코딩의 기술" by 브렛 슬라킨 [대출 중: 김철수]
```

### 🥈 Silver — 대출 기록 (Borrow History)
`_borrow_history`라는 private 리스트 속성을 추가하고, 누가 빌렸는지 순서대로 저장하세요. `get_history()` 메서드로 조회할 수 있게 해주세요.

> ⚠️ **힌트:** 리스트를 그대로 반환하면 외부에서 수정할 수 있어요. `list(self._borrow_history)`처럼 **복사본**을 반환해보세요. 왜 그래야 할까요?

### 🥇 Gold — `Library` 클래스 만들기
여러 권의 책을 관리하는 `Library` 클래스를 만들어보세요:
- `add_book(book)`: 책 추가
- `find_by_title(title)`: 제목으로 검색
- `available_books()`: 빌릴 수 있는 책들의 리스트 반환
- `total_borrows()`: 모든 책의 누적 대출 횟수 합계

## 🤔 생각해보기

코딩을 시작하기 전에:
1. 만약 `_title`을 그냥 `title`로 했다면, 외부에서 `book.title = ""`로 빈 문자열을 넣어버릴 수 있어요. 이게 왜 문제일까요?
2. `borrow()`가 왜 `True`/`False`를 반환할까요? 그냥 아무것도 반환하지 않으면 어떤 문제가 생길까요?
3. 만약 같은 사람이 같은 책을 두 번 빌렸다 반납했다면, `_borrow_count`는 1일까요, 2일까요? 어느 쪽이 더 자연스러울까요?

질문은 언제든지 스레드에 남겨주세요! 🚀

---
---

# 📚 Python Class Practice Day 2: Build a Library System!

Hey team! On Day 1, we learned the basics of classes — `__init__`, attributes, methods. Today on Day 2, we level up by learning **how to protect data in real systems**.

## 🎯 Your Mission

Create a `Book` class for managing books at a university library. It's not just about storing information — you need to **safely manage the book's state** (borrowed or available).

**Key point:** A book's internal data (title, who borrowed it, etc.) shouldn't be modifiable from outside directly. All changes must happen **through methods**. This is today's core concept: **encapsulation**!

## 🆕 What You'll Learn Today

### 1. Private Attributes (Underscore Prefix)

In Python, we prefix attribute names with an underscore (`_`) to signal "this is internal — don't touch directly":

```python
class Account:
    def __init__(self, balance):
        self._balance = balance  # underscore = "private" convention
```

> 💡 **Note:** Python doesn't enforce this — it's a **convention among developers**. "If it has an underscore, don't touch it directly; use a method!"

### 2. Getters and Setters

To read or modify private attributes, we create **dedicated methods**:

```python
class Account:
    def __init__(self, balance):
        self._balance = balance

    def get_balance(self):           # getter: read
        return self._balance

    def set_balance(self, new_value): # setter: write (with validation!)
        if new_value < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = new_value
```

**The real power of setters:** They let you **validate** values before assignment. This blocks invalid data from sneaking in!

### 3. Behavior Methods

While getters/setters are simple read/write, **behavior methods** mean the object "does something":

```python
account.deposit(1000)   # the act of depositing
account.withdraw(500)   # the act of withdrawing
```

These methods update multiple attributes together and enforce rules.

## 📋 Requirements

Create a `Book` class with the following:

### Private Attributes (all start with underscore!)
- `_title`: book title (string)
- `_author`: author name (string)
- `_is_borrowed`: borrow status (True/False)
- `_borrower`: current borrower's name (`None` if not borrowed)
- `_borrow_count`: total times this book has been borrowed (integer)

### Getter Methods
- `get_title()` → returns title
- `get_author()` → returns author
- `get_borrower()` → returns current borrower (`None` if available)
- `get_borrow_count()` → returns total borrow count
- `is_available()` → returns `True` if borrowable, else `False`

### Setter Methods (with validation!)
- `set_title(new_title)` → changes title. **Raises `ValueError` if empty!**

### Behavior Methods
- `borrow(borrower_name)` → borrows the book
  - Returns `False` if already borrowed (fail)
  - Updates state and returns `True` if successful
  - Increments `_borrow_count` by 1
- `return_book()` → returns the book
  - Returns `False` if not currently borrowed
  - Processes the return and returns `True`

### Constructor (`__init__`) Validation
- Raises `ValueError` if title or author is empty
- Initial state: not borrowed, borrow count is 0

## 💡 Example

```python
book = Book("Effective Python", "Brett Slatkin")

print(book.is_available())      # True
print(book.get_borrow_count())  # 0

book.borrow("Alice")
print(book.is_available())      # False
print(book.get_borrower())      # "Alice"
print(book.get_borrow_count())  # 1

book.borrow("Bob")              # Already borrowed!
# Returns: False (borrow failed)

book.return_book()
print(book.is_available())      # True
print(book.get_borrower())      # None

book.borrow("Bob")
print(book.get_borrow_count())  # 2 (cumulative!)
```

## 🎓 What You Should Know

- Class definition (`class`, `__init__`, `self`) — Day 1 review
- Assigning values to attributes — Day 1 review
- Defining and calling methods — Day 1 review
- `if` statements for conditions — existing
- `raise ValueError("message")` — **new today!**
- Handling `None` values — existing

## ✅ Your Task

```python
class Book:
    def __init__(self, title: str, author: str):
        # Your code here
        pass

    # Other methods...
```

Grab the skeleton file (`library_book_skeleton.py`) and get started!

## 🎪 Test Cases

```python
# Test 1: Basic creation
b1 = Book("Alice in Wonderland", "Lewis Carroll")
assert b1.get_title() == "Alice in Wonderland"
assert b1.is_available() == True

# Test 2: Borrow
assert b1.borrow("Minsu Kim") == True
assert b1.is_available() == False
assert b1.get_borrower() == "Minsu Kim"

# Test 3: Block double borrow
assert b1.borrow("Jiyoung Park") == False  # already borrowed

# Test 4: Return
assert b1.return_book() == True
assert b1.is_available() == True

# Test 5: Reject empty title
try:
    bad = Book("", "Author")
    print("❌ FAIL: should have raised")
except ValueError:
    print("✅ Empty title rejected")
```

## 🏆 Bonus Challenges

### 🥉 Bronze — Add `__str__` Method
Make the book print nicely with `print()`:
```
"Effective Python" by Brett Slatkin [Available]
"Effective Python" by Brett Slatkin [Borrowed by: Alice]
```

### 🥈 Silver — Borrow History
Add a private list attribute `_borrow_history` and store who borrowed the book, in order. Provide a `get_history()` method to retrieve it.

> ⚠️ **Hint:** If you return the list directly, outside code can modify it. Try returning `list(self._borrow_history)` — a **copy**. Why does this matter?

### 🥇 Gold — Build a `Library` Class
Create a `Library` class that manages multiple books:
- `add_book(book)`: add a book
- `find_by_title(title)`: search by title
- `available_books()`: list of borrowable books
- `total_borrows()`: sum of all books' borrow counts

## 🤔 Think About It

Before you code:
1. If `_title` were just `title`, outside code could do `book.title = ""` and inject an empty string. Why is that a problem?
2. Why does `borrow()` return `True`/`False`? What would go wrong if it returned nothing?
3. If the same person borrowed and returned a book twice, should `_borrow_count` be 1 or 2? Which feels more natural?

Drop your questions in the thread anytime! 🚀
