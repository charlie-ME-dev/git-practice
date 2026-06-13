# 📚 Python 연습: 도서관 카탈로그를 JSON으로 관리하기!

여러분, 안녕하세요! 오늘은 Python 딕셔너리와 JSON을 자유자재로 변환하는 방법을 배워봅시다.

## 🌍 시나리오

여러분은 대학교 도서관의 인턴으로 일하고 있습니다. 도서관은 모든 책 정보를 컴퓨터로 관리하려고 하는데, 문제가 하나 있어요!

각 분관(branch)마다 다른 시스템을 쓰고 있어서, 책 정보를 주고받을 수 있는 **공통 형식**이 필요합니다. 사서 선생님이 말합니다:

> *"JSON으로 변환하면 어떤 시스템에서도 읽을 수 있어요. 학생, JSON 변환 함수들 좀 만들어 줄래요?"*

여러분의 임무: 책 정보를 Python 딕셔너리 ↔ JSON 문자열로 변환하는 도구를 만들어 보세요!

## 🤔 JSON이 뭔가요?

**JSON** (JavaScript Object Notation)은 데이터를 텍스트로 저장하는 형식입니다.

| Python | JSON |
|--------|------|
| `dict` | object `{...}` |
| `list` | array `[...]` |
| `str` | string `"..."` |
| `int`, `float` | number |
| `True` | `true` |
| `False` | `false` |
| `None` | `null` |

> 💡 **핵심**: JSON은 **문자열(string)** 입니다! 딕셔너리처럼 보이지만, 사실은 그냥 텍스트예요.

### 🔧 우리가 사용할 두 가지 함수

```python
import json

# 딕셔너리 → JSON 문자열
json_text = json.dumps(my_dict)

# JSON 문자열 → 딕셔너리
my_dict = json.loads(json_text)
```

> 💡 **외우는 팁**: `dump**s**` 와 `load**s**` 의 마지막 's'는 **string**의 's'입니다!

## 📋 책 정보의 구조

도서관의 모든 책은 다음과 같은 딕셔너리로 표현됩니다:

```python
{
    "title": "1984",
    "author": "George Orwell",
    "year": 1949,
    "available": True
}
```

여러 권의 책은 **딕셔너리의 리스트**로 표현됩니다:

```python
[
    {"title": "1984", "author": "George Orwell", "year": 1949, "available": True},
    {"title": "Dune", "author": "Frank Herbert", "year": 1965, "available": False}
]
```

## ✅ 여러분의 과제

다음 5개의 함수를 작성하세요:

### 과제 1: `dict_to_json_string(book)`

책 딕셔너리 한 권을 JSON 문자열로 변환합니다.

```python
book = {"title": "1984", "author": "George Orwell", "year": 1949, "available": True}
result = dict_to_json_string(book)
# result는 다음과 같은 문자열:
# '{"title": "1984", "author": "George Orwell", "year": 1949, "available": true}'
```

### 과제 2: `json_string_to_dict(json_text)`

JSON 문자열을 다시 Python 딕셔너리로 변환합니다.

```python
json_text = '{"title": "Dune", "author": "Frank Herbert", "year": 1965, "available": false}'
result = json_string_to_dict(json_text)
# result는 Python 딕셔너리:
# {"title": "Dune", "author": "Frank Herbert", "year": 1965, "available": False}
```

### 과제 3: `count_available_books(catalog_json)`

여러 책이 들어있는 JSON 문자열을 받아, **대출 가능한** 책의 수를 반환합니다.

```python
catalog_json = '[{"title": "1984", "available": true}, {"title": "Dune", "available": false}, ...]'
count = count_available_books(catalog_json)
# count는 정수 (대출 가능한 책의 수)
```

### 과제 4: `add_new_book(catalog_json, new_book)`

기존 카탈로그(JSON 문자열)에 새 책(딕셔너리)을 추가하고, 업데이트된 카탈로그를 JSON 문자열로 반환합니다.

```python
catalog_json = '[{"title": "1984", ...}]'
new_book = {"title": "Animal Farm", "author": "George Orwell", "year": 1945, "available": True}
updated = add_new_book(catalog_json, new_book)
# updated는 두 권이 들어있는 JSON 문자열
```

### 과제 5: `find_books_by_author(catalog_json, author_name)`

카탈로그에서 특정 저자의 모든 책 **제목**을 리스트로 반환합니다.

```python
titles = find_books_by_author(catalog_json, "George Orwell")
# titles는 ["1984", "Animal Farm"] 같은 리스트
```

## 💡 시작 힌트

- 모든 함수에서 **가장 먼저 `import json`** 이 필요합니다 (스켈레톤에 이미 작성되어 있음)
- 과제 3, 4, 5 는 **JSON 문자열을 먼저 딕셔너리/리스트로 변환** 한 다음 작업하세요
- 과제 4 는 변환 → 추가 → 다시 변환의 3단계입니다

## 🎁 보너스 챌린지

기본 5문제를 다 끝냈다면 도전해보세요!

### 🥉 Easy: `pretty_print_book(book)`

책 딕셔너리를 받아 **들여쓰기(indent)** 가 적용된 JSON 문자열을 반환하세요.

> 💡 힌트: `json.dumps()`의 `indent` 매개변수를 검색해보세요.

### 🥈 Medium: `get_oldest_book(catalog_json)`

카탈로그에서 **가장 오래된** 책의 제목을 반환하세요. (`year` 값이 가장 작은 책)

### 🥇 Hard: `catalog_summary(catalog_json)`

카탈로그를 받아, **저자별 책 권수**를 담은 딕셔너리를 반환하세요.

```python
# 입력: 5권의 책이 담긴 카탈로그
# 출력: {"George Orwell": 2, "Frank Herbert": 1, "Isaac Asimov": 2}
```

> 💡 힌트: 빈 딕셔너리를 만든 뒤, 카탈로그를 순회하면서 저자가 이미 있으면 +1, 없으면 새 키로 1을 추가하세요.

---
---

# 📚 Python Practice: Manage a Library Catalog with JSON!

Hey team! Today we'll learn how to convert between Python dictionaries and JSON.

## 🌍 The Scenario

You're an intern at the university library. They want to manage all their book information digitally — but there's a problem!

Each branch uses a different system, so they need a **common format** to exchange book data. The librarian tells you:

> *"If we convert everything to JSON, any system can read it. Could you write some JSON conversion functions for us?"*

Your mission: Build tools that convert book data between Python dictionaries ↔ JSON strings!

## 🤔 What Is JSON?

**JSON** (JavaScript Object Notation) is a text-based data format.

| Python | JSON |
|--------|------|
| `dict` | object `{...}` |
| `list` | array `[...]` |
| `str` | string `"..."` |
| `int`, `float` | number |
| `True` | `true` |
| `False` | `false` |
| `None` | `null` |

> 💡 **Key point**: JSON is a **string**! It looks like a dictionary, but it's actually just text.

### 🔧 The Two Functions We'll Use

```python
import json

# Dictionary → JSON string
json_text = json.dumps(my_dict)

# JSON string → Dictionary
my_dict = json.loads(json_text)
```

> 💡 **Memory tip**: The 's' at the end of `dump**s**` and `load**s**` stands for **string**!

## 📋 Book Data Structure

Every book in our library is represented as a dictionary:

```python
{
    "title": "1984",
    "author": "George Orwell",
    "year": 1949,
    "available": True
}
```

Multiple books are represented as a **list of dictionaries**:

```python
[
    {"title": "1984", "author": "George Orwell", "year": 1949, "available": True},
    {"title": "Dune", "author": "Frank Herbert", "year": 1965, "available": False}
]
```

## ✅ Your Tasks

Write the following 5 functions:

### Task 1: `dict_to_json_string(book)`

Convert a single book dictionary into a JSON string.

```python
book = {"title": "1984", "author": "George Orwell", "year": 1949, "available": True}
result = dict_to_json_string(book)
# result is the string:
# '{"title": "1984", "author": "George Orwell", "year": 1949, "available": true}'
```

### Task 2: `json_string_to_dict(json_text)`

Convert a JSON string back into a Python dictionary.

```python
json_text = '{"title": "Dune", "author": "Frank Herbert", "year": 1965, "available": false}'
result = json_string_to_dict(json_text)
# result is a Python dictionary:
# {"title": "Dune", "author": "Frank Herbert", "year": 1965, "available": False}
```

### Task 3: `count_available_books(catalog_json)`

Take a JSON string containing multiple books, and return the number of **available** ones.

```python
catalog_json = '[{"title": "1984", "available": true}, {"title": "Dune", "available": false}, ...]'
count = count_available_books(catalog_json)
# count is an integer (the number of available books)
```

### Task 4: `add_new_book(catalog_json, new_book)`

Add a new book (dictionary) to an existing catalog (JSON string), and return the updated catalog as a JSON string.

```python
catalog_json = '[{"title": "1984", ...}]'
new_book = {"title": "Animal Farm", "author": "George Orwell", "year": 1945, "available": True}
updated = add_new_book(catalog_json, new_book)
# updated is a JSON string containing both books
```

### Task 5: `find_books_by_author(catalog_json, author_name)`

Return a list of all **titles** by a given author from the catalog.

```python
titles = find_books_by_author(catalog_json, "George Orwell")
# titles is a list like ["1984", "Animal Farm"]
```

## 💡 Starting Tips

- Every function needs `import json` **at the top** (already in the skeleton)
- For Tasks 3, 4, 5 — **convert the JSON string to a dict/list first**, then work with it
- Task 4 is a 3-step process: convert → append → convert back

## 🎁 Bonus Challenges

If you finish the 5 main tasks, try these!

### 🥉 Easy: `pretty_print_book(book)`

Take a book dictionary and return a JSON string with **indentation** applied.

> 💡 Hint: Look up the `indent` parameter of `json.dumps()`.

### 🥈 Medium: `get_oldest_book(catalog_json)`

Return the title of the **oldest** book in the catalog (smallest `year` value).

### 🥇 Hard: `catalog_summary(catalog_json)`

Take a catalog and return a dictionary mapping each **author to their book count**.

```python
# Input: a catalog with 5 books
# Output: {"George Orwell": 2, "Frank Herbert": 1, "Isaac Asimov": 2}
```

> 💡 Hint: Start with an empty dictionary. Loop through the catalog — if the author is already a key, add 1; if not, create a new key with value 1.

Drop your questions in the thread if you get stuck! Take your time and understand the logic.

Good luck! 🚀
