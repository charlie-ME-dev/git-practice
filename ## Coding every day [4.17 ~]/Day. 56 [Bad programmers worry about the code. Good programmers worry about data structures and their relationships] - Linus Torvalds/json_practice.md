# 🐍 Python 연습: JSON으로 성적 관리하기!

여러분, 안녕하세요! 오늘은 실제 프로그래머들이 매일 사용하는 도구인 **JSON**을 다뤄볼 시간입니다.

## 🎯 미션

여러분은 한 학기 동안 수업을 듣는 학생들의 성적을 관리하는 시스템을 만들고 있습니다. 데이터는 **JSON 파일**로 저장되어 있고, 여러분의 임무는 이 데이터를 읽고, 분석하고, 수정하고, 다시 저장하는 것입니다.

**왜 JSON인가요?** 웹 API, 설정 파일, 게임 세이브, 모바일 앱 데이터 — 거의 모든 현대 소프트웨어가 JSON으로 데이터를 주고받습니다. JSON을 다룰 줄 알면 여러분은 진짜 개발자처럼 일할 수 있습니다!

## 📚 알아둬야 할 개념

### JSON이란?

**JSON**(JavaScript Object Notation)은 데이터를 텍스트로 표현하는 형식입니다. 다행히 Python의 딕셔너리/리스트와 거의 똑같이 생겼습니다!

| JSON 타입 | Python 타입 |
|-----------|-------------|
| `object` `{...}` | `dict` |
| `array` `[...]` | `list` |
| `string` `"..."` | `str` |
| `number` `42` 또는 `3.14` | `int` 또는 `float` |
| `true` / `false` | `True` / `False` |
| `null` | `None` |

### 4가지 핵심 함수

Python의 `json` 모듈에는 기억해야 할 4개의 함수가 있습니다:

| 함수 | 하는 일 | 방향 |
|------|---------|------|
| `json.loads(s)` | 문자열 → Python 객체 | **load s**tring |
| `json.dumps(obj)` | Python 객체 → 문자열 | **dump s**tring |
| `json.load(f)` | 파일 → Python 객체 | **load** from file |
| `json.dump(obj, f)` | Python 객체 → 파일 | **dump** to file |

> 💡 **외우는 팁:** 끝에 `s`가 붙으면 **s**tring(문자열)을 다룹니다. `s`가 없으면 파일을 다룹니다!

### 사용 예시

```python
import json

# 문자열 → 딕셔너리
text = '{"name": "Alice", "age": 20}'
data = json.loads(text)
print(data["name"])  # Alice

# 딕셔너리 → 문자열
person = {"name": "Bob", "age": 22}
text = json.dumps(person)
print(text)  # {"name": "Bob", "age": 22}

# 파일 읽기/쓰기
with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)
```

## 📋 데이터 구조

여러분이 다룰 성적 데이터는 다음과 같이 생겼습니다:

```json
{
  "class_name": "Python 101",
  "semester": "Spring 2026",
  "students": [
    {
      "id": "S001",
      "name": "Alice Kim",
      "grades": {"math": 92, "english": 85, "science": 78}
    },
    {
      "id": "S002",
      "name": "Bob Park",
      "grades": {"math": 67, "english": 72, "science": 80}
    }
  ]
}
```

중첩이 보이나요? **딕셔너리 안에 리스트가 있고, 그 리스트 안에 또 딕셔너리가 있고, 그 딕셔너리 안에 또 딕셔너리가 있습니다.** 이런 중첩 구조를 자유자재로 다루는 것이 오늘의 핵심입니다.

## ✅ 과제

다음 6개의 함수를 작성하세요:

### 1. `parse_class_data(json_text)`
JSON 문자열을 받아서 Python 딕셔너리로 변환합니다.

### 2. `calculate_student_average(student)`
학생 한 명의 딕셔너리를 받아서, 모든 과목의 평균 점수를 반환합니다.

### 3. `find_top_student(class_data)`
전체 클래스 데이터를 받아서, 평균 점수가 가장 높은 학생의 **이름**을 반환합니다.

### 4. `add_student(class_data, student_id, name, math, english, science)`
새로운 학생을 클래스에 추가합니다. **원본 데이터를 직접 수정**합니다 (반환값 없음).

### 5. `save_class_data(class_data, file_path)`
클래스 데이터를 JSON 파일로 저장합니다. 사람이 읽기 좋게 들여쓰기를 적용하세요.

### 6. `load_class_data(file_path)`
JSON 파일에서 클래스 데이터를 읽어와 반환합니다.

## 🎪 코드 테스트

```python
import json

# 테스트 1: 문자열 파싱
json_text = '{"class_name": "Python 101", "students": []}'
data = parse_class_data(json_text)
print(data["class_name"])  # 예상: Python 101

# 테스트 2: 학생 평균
alice = {"id": "S001", "name": "Alice Kim",
         "grades": {"math": 92, "english": 85, "science": 78}}
print(calculate_student_average(alice))  # 예상: 85.0

# 테스트 3: 최고 성적 학생
class_data = {
    "class_name": "Python 101",
    "semester": "Spring 2026",
    "students": [
        {"id": "S001", "name": "Alice Kim",
         "grades": {"math": 92, "english": 85, "science": 78}},
        {"id": "S002", "name": "Bob Park",
         "grades": {"math": 67, "english": 72, "science": 80}},
        {"id": "S003", "name": "Carol Lee",
         "grades": {"math": 88, "english": 95, "science": 91}}
    ]
}
print(find_top_student(class_data))  # 예상: Carol Lee

# 테스트 4: 학생 추가
add_student(class_data, "S004", "David Choi", 75, 80, 85)
print(len(class_data["students"]))  # 예상: 4

# 테스트 5 & 6: 저장 후 다시 불러오기 (round-trip)
save_class_data(class_data, "class.json")
loaded = load_class_data("class.json")
print(loaded == class_data)  # 예상: True
```

## 🤔 시작하기 전 생각해보기

1. `json.load()`와 `json.loads()`의 차이가 뭔가요? 어떤 상황에서 어떤 것을 써야 할까요?
2. 중첩된 딕셔너리에서 특정 값을 꺼내려면 어떻게 해야 하나요? (예: `class_data`에서 첫 번째 학생의 수학 점수)
3. 파일을 열 때 `with open(...)`을 쓰는 이유는 무엇인가요?

## 🎁 보너스 도전 과제

### 🥉 Easy: 과목별 클래스 평균

```python
def class_averages_by_subject(class_data):
    """각 과목별로 클래스 전체의 평균을 딕셔너리로 반환.
    
    예: {"math": 82.3, "english": 84.0, "science": 83.0}
    """
```

### 🥈 Medium: 기준점 이상 학생 찾기

```python
def students_above_threshold(class_data, threshold):
    """평균이 threshold 이상인 학생들의 이름 리스트를 반환."""
```

### 🥇 Hard: `pathlib` 미리보기 (다음 학기 예고편!)

지금까지 우리는 파일 경로를 문자열로 다뤘습니다 (`"class.json"`). 하지만 Python에는 더 우아한 방법이 있습니다 — `pathlib` 모듈입니다!

```python
from pathlib import Path

def save_with_pathlib(class_data, folder_name, file_name):
    """folder_name 폴더를 만들고(없으면), 그 안에 file_name으로 저장.
    
    힌트:
    - Path(folder_name).mkdir(exist_ok=True)로 폴더 생성
    - Path 객체끼리는 / 연산자로 합칠 수 있음: folder / file_name
    - open()은 Path 객체를 그대로 받음
    """
```

> 🌟 **왜 `pathlib`이 좋은가요?** 운영체제(Windows/Mac/Linux)와 상관없이 동작하고, 경로 조작이 훨씬 직관적입니다. 다음 학기에 본격적으로 배우게 될 것입니다!

## 💭 마무리 질문

- JSON과 Python 딕셔너리는 무엇이 다른가요? 무엇이 같은가요?
- 만약 JSON 파일에 한글이 들어있다면, 어떤 옵션을 추가해야 할까요? (힌트: `ensure_ascii`)
- 실제 회사에서는 JSON을 어디에 쓸까요? 3가지만 생각해보세요.

막히면 스레드에 질문 남겨주세요. 목표는 끝내는 것이 아니라 **이해하는 것**입니다! 🚀

---
---

# 🐍 Python Practice: Manage Grades with JSON!

Hey team! Today we're tackling **JSON** — a tool real programmers use every single day.

## 🎯 Your Mission

You're building a system to manage student grades for a semester. The data is stored as a **JSON file**, and your job is to read it, analyze it, modify it, and save it back.

**Why JSON?** Web APIs, config files, game saves, mobile app data — almost all modern software exchanges data using JSON. Master JSON and you can work like a real developer!

## 📚 Concepts to Know

### What is JSON?

**JSON** (JavaScript Object Notation) is a text format for representing data. Lucky for us, it looks almost exactly like Python dictionaries and lists!

| JSON Type | Python Type |
|-----------|-------------|
| `object` `{...}` | `dict` |
| `array` `[...]` | `list` |
| `string` `"..."` | `str` |
| `number` `42` or `3.14` | `int` or `float` |
| `true` / `false` | `True` / `False` |
| `null` | `None` |

### The 4 Key Functions

Python's `json` module has 4 functions you must remember:

| Function | What it does | Direction |
|----------|--------------|-----------|
| `json.loads(s)` | string → Python object | **load s**tring |
| `json.dumps(obj)` | Python object → string | **dump s**tring |
| `json.load(f)` | file → Python object | **load** from file |
| `json.dump(obj, f)` | Python object → file | **dump** to file |

> 💡 **Memory trick:** If it ends with `s`, it deals with a **s**tring. No `s`? It deals with a file!

### Usage Examples

```python
import json

# string → dict
text = '{"name": "Alice", "age": 20}'
data = json.loads(text)
print(data["name"])  # Alice

# dict → string
person = {"name": "Bob", "age": 22}
text = json.dumps(person)
print(text)  # {"name": "Bob", "age": 22}

# Reading/writing files
with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)
```

## 📋 The Data Structure

The grade data you'll work with looks like this:

```json
{
  "class_name": "Python 101",
  "semester": "Spring 2026",
  "students": [
    {
      "id": "S001",
      "name": "Alice Kim",
      "grades": {"math": 92, "english": 85, "science": 78}
    },
    {
      "id": "S002",
      "name": "Bob Park",
      "grades": {"math": 67, "english": 72, "science": 80}
    }
  ]
}
```

See the nesting? **A dict contains a list, which contains dicts, which contain more dicts.** Navigating these nested structures fluently is the core skill for today.

## ✅ Your Task

Write the following 6 functions:

### 1. `parse_class_data(json_text)`
Takes a JSON string and returns a Python dictionary.

### 2. `calculate_student_average(student)`
Takes one student's dictionary and returns their average grade across all subjects.

### 3. `find_top_student(class_data)`
Takes the full class data and returns the **name** of the student with the highest average.

### 4. `add_student(class_data, student_id, name, math, english, science)`
Adds a new student to the class. **Modifies the original data in-place** (returns nothing).

### 5. `save_class_data(class_data, file_path)`
Saves the class data to a JSON file. Use indentation so it's human-readable.

### 6. `load_class_data(file_path)`
Reads class data from a JSON file and returns it.

## 🎪 Test Your Code

```python
import json

# Test 1: Parse a string
json_text = '{"class_name": "Python 101", "students": []}'
data = parse_class_data(json_text)
print(data["class_name"])  # Expected: Python 101

# Test 2: Student average
alice = {"id": "S001", "name": "Alice Kim",
         "grades": {"math": 92, "english": 85, "science": 78}}
print(calculate_student_average(alice))  # Expected: 85.0

# Test 3: Top student
class_data = {
    "class_name": "Python 101",
    "semester": "Spring 2026",
    "students": [
        {"id": "S001", "name": "Alice Kim",
         "grades": {"math": 92, "english": 85, "science": 78}},
        {"id": "S002", "name": "Bob Park",
         "grades": {"math": 67, "english": 72, "science": 80}},
        {"id": "S003", "name": "Carol Lee",
         "grades": {"math": 88, "english": 95, "science": 91}}
    ]
}
print(find_top_student(class_data))  # Expected: Carol Lee

# Test 4: Add student
add_student(class_data, "S004", "David Choi", 75, 80, 85)
print(len(class_data["students"]))  # Expected: 4

# Test 5 & 6: Save then reload (round-trip)
save_class_data(class_data, "class.json")
loaded = load_class_data("class.json")
print(loaded == class_data)  # Expected: True
```

## 🤔 Think Before You Code

1. What's the difference between `json.load()` and `json.loads()`? When would you use each?
2. How do you reach into a nested dictionary to get a specific value? (e.g., the math grade of the first student in `class_data`)
3. Why do we use `with open(...)` when working with files?

## 🎁 Bonus Challenges

### 🥉 Easy: Class Average by Subject

```python
def class_averages_by_subject(class_data):
    """Return a dict with the class average for each subject.
    
    Example: {"math": 82.3, "english": 84.0, "science": 83.0}
    """
```

### 🥈 Medium: Students Above a Threshold

```python
def students_above_threshold(class_data, threshold):
    """Return a list of names of students whose average is >= threshold."""
```

### 🥇 Hard: A Preview of `pathlib` (Coming Next Semester!)

So far we've handled file paths as strings (`"class.json"`). But Python has an elegant alternative — the `pathlib` module!

```python
from pathlib import Path

def save_with_pathlib(class_data, folder_name, file_name):
    """Create the folder (if missing) and save the file inside it.
    
    Hints:
    - Path(folder_name).mkdir(exist_ok=True) creates the folder
    - Path objects can be joined with /: folder / file_name
    - open() accepts Path objects directly
    """
```

> 🌟 **Why is `pathlib` great?** It works the same on Windows/Mac/Linux and makes path manipulation much more intuitive. You'll learn this properly next semester!

## 💭 Reflection Questions

- How is JSON different from a Python dictionary? How is it the same?
- If your JSON file contains Korean characters, what option do you need to add? (Hint: `ensure_ascii`)
- Where do real companies use JSON? Think of 3 examples.

Drop questions in the thread if you get stuck. The goal isn't to finish — it's to **understand**! 🚀
