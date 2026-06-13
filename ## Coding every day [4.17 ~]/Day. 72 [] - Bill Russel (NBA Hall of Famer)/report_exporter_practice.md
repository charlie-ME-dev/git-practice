# 📄 Python 연습: 리포트 내보내기 시스템 설계하기 (추상 클래스)!

여러분, 안녕하세요! 오늘은 데이터 분석 회사의 개발자가 되어, 같은 데이터를 여러 형식으로 내보내는 시스템을 설계해봅니다.

## 🎯 미션

여러분의 회사는 학생 성적, 매출 기록 같은 데이터를 고객에게 **여러 파일 형식으로 내보내야** 합니다. 어떤 고객은 엑셀에서 열 CSV를, 어떤 고객은 프로그램이 읽을 JSON을, 어떤 고객은 사람이 읽을 텍스트를 원해요.

**여기서 핵심:** 입력 데이터는 **똑같습니다.** 하지만 형식마다 출력 모양이 완전히 다르죠. 그리고 새로운 형식(예: Markdown)이 추가될 때, 개발자가 **반드시 "확장자"와 "렌더링 방법"을 구현하도록 강제**하고 싶습니다. 깜빡하면 프로그램이 아예 실행되지 않아야 해요. 이것이 바로 **추상 클래스(Abstract Base Class, ABC)**가 필요한 이유입니다!

## 🧠 추상 클래스(ABC)란?

추상 클래스는 **"설계도만 있고, 실제 구현은 자식 클래스가 채워야 하는"** 클래스입니다.

- **추상 메서드(`@abstractmethod`)**: 이름만 선언되고 내용은 비어 있는 메서드. 자식이 반드시 구현해야 함.
- **추상 클래스는 직접 객체를 만들 수 없음**: `ReportExporter("제목")`처럼 직접 인스턴스화하면 `TypeError` 발생.
- **자식이 추상 메서드를 하나라도 빼먹으면**: 그 자식도 인스턴스화 불가능.

> 💡 비유: 추상 클래스는 "계약서"입니다. "리포트 내보내기 도구가 되려면, 확장자를 알려주고 데이터를 렌더링하는 기능을 반드시 제공하겠다"는 약속에 서명하는 것과 같아요.

**실전 적용 분야:**
- 📊 **데이터 분석/리포팅**: 같은 데이터를 CSV·JSON·PDF 등으로 출력
- 🖼️ **이미지 처리**: 하나의 이미지를 PNG·JPG·WebP로 저장
- 🔌 **API 응답**: 동일 데이터를 형식별(XML/JSON)로 직렬화
- 🎮 **게임 저장**: 세이브 데이터를 여러 포맷으로 기록

## 📋 규칙

*주어지는 것:*
- 추상 클래스 `ReportExporter` (여러분이 설계)
- 세 개의 구체 클래스: `CsvExporter`, `JsonExporter`, `TextExporter`
- 데이터는 **딕셔너리들의 리스트** 형태 (각 딕셔너리가 한 행)

*입력 데이터 예시:*
```python
rows = [
    {"name": "Alice", "score": 90},
    {"name": "Bob", "score": 85},
]
```

*형식별 출력 규칙:*

| 형식 | 클래스 | 확장자 | 렌더링 방법 |
|---|---|---|---|
| CSV | `CsvExporter` | `csv` | 첫 줄은 헤더, 이후 각 행을 콤마로 연결 |
| JSON | `JsonExporter` | `json` | `json.dumps`로 직렬화 |
| 텍스트 | `TextExporter` | `txt` | 각 행을 `"1. key: value, ..."` 형식으로 |

*해야 할 일:*
1. `abc` 모듈을 사용하여 추상 클래스 `ReportExporter` 작성
2. `file_extension()`과 `render(rows)`를 추상 메서드로 선언
3. 모든 자식이 공유하는 **구체 메서드** `export(rows)` 작성 (`"제목.확장자\n렌더링결과"` 반환)
4. 세 개의 구체 클래스에서 추상 메서드를 각각 구현

*반드시 따라야 할 제약사항:*
- **`abc` 모듈 사용**: `from abc import ABC, abstractmethod`
- 추상 메서드를 빼먹은 클래스는 인스턴스화되면 안 됩니다
- `export()`는 추상 클래스에 **한 번만** 작성 (중복 금지!)
- 모든 변수/메서드 이름은 **snake_case** (클래스명은 PascalCase)

## 💡 예제

**예제 1: CSV 내보내기**
```
csv_exporter = CsvExporter("grades")
csv_exporter.file_extension()  →  "csv"
csv_exporter.render(rows)      →  "name,score\nAlice,90\nBob,85"
csv_exporter.export(rows)      →  "grades.csv\nname,score\nAlice,90\nBob,85"
```

**예제 2: 추상 클래스는 직접 만들 수 없음**
```
ReportExporter("test")   →  TypeError 발생! ❌
```
왜? `ReportExporter`는 추상 메서드를 가진 추상 클래스라서 직접 객체를 만들 수 없어요.

**예제 3: 다형성 — 같은 데이터, 다른 출력**
```python
exporters = [CsvExporter("g"), JsonExporter("g"), TextExporter("g")]
for exporter in exporters:
    print(exporter.export(rows))
```
서로 다른 클래스지만, 모두 `ReportExporter`의 자식이므로 **똑같은 방식으로 호출**할 수 있습니다. 하지만 결과는 형식마다 완전히 다르죠!

## 🎓 알아야 할 것

코딩을 시작하기 전에, 다음을 이해하고 있는지 확인하세요:
- 클래스와 상속 (`class Child(Parent):`)
- `__init__`과 `super().__init__()` 사용법
- `self`의 의미와 인스턴스 속성
- 딕셔너리 다루기 (`.keys()`, `row[key]`)
- 리스트 순회와 `"\n".join(...)` 으로 줄 합치기
- f-string 포매팅

## ✅ 과제

다음 구조로 클래스들을 작성하세요:
```python
from abc import ABC, abstractmethod

class ReportExporter(ABC):
    def __init__(self, title: str):
        # 여기에 코드 작성
        pass

    @abstractmethod
    def file_extension(self) -> str:
        ...

    @abstractmethod
    def render(self, rows: list[dict]) -> str:
        ...

    def export(self, rows: list[dict]) -> str:
        # 추상 메서드 두 개를 모두 활용하는 구체 메서드
        pass

class CsvExporter(ReportExporter):
    # 여기에 코드 작성
    pass
```

**시작하는 데 도움이 될 팁:**
- 추상 메서드의 본문은 `...` 또는 `pass`로 비워둡니다
- `export()`는 `self.file_extension()`과 `self.render()`를 **둘 다** 호출합니다 — 자식마다 다르게 동작!
- CSV 헤더는 첫 번째 행의 `.keys()`로 얻을 수 있어요
- JSON은 `import json` 후 `json.dumps(rows, ensure_ascii=False)`를 사용하세요 (한글이 깨지지 않도록)

## 🎪 코드 테스트

다음 테스트 케이스를 실행해보세요:

```python
rows = [
    {"name": "Alice", "score": 90},
    {"name": "Bob", "score": 85},
]

# 테스트 1: 확장자
print(CsvExporter("g").file_extension())   # 예상: csv
print(JsonExporter("g").file_extension())  # 예상: json
print(TextExporter("g").file_extension())  # 예상: txt

# 테스트 2: CSV 렌더링
print(CsvExporter("g").render(rows))
# 예상:
# name,score
# Alice,90
# Bob,85

# 테스트 3: export (제목 + 확장자 포함)
print(CsvExporter("grades").export(rows))
# 예상 첫 줄: grades.csv

# 테스트 4: 추상 클래스 직접 생성 시도 (에러가 나야 정상!)
try:
    ReportExporter("test")
except TypeError:
    print("정상: 추상 클래스는 인스턴스화 불가 ✅")
```

## 🌟 보너스 챌린지

기본 과제를 끝냈다면 도전해보세요! (추가 점수 — 기본 점수에 더해집니다)

### 🥉 Easy: 행 개수 알려주기
모든 내보내기 도구가 공통으로 쓰는 `row_count(rows)` 구체 메서드를 추상 클래스에 추가하세요. 행의 개수를 정수로 반환합니다.

### 🥈 Medium: Markdown 표 내보내기
`MarkdownExporter` 클래스를 추가하세요. 확장자는 `md`이고, 데이터를 Markdown 표로 렌더링합니다:
```
| name | score |
| --- | --- |
| Alice | 90 |
| Bob | 85 |
```

### 🥇 Hard: 형식 문자열로 도구 선택하기 (새 개념 미리보기 🔮)
`"csv"`, `"json"`, `"txt"` 같은 문자열을 받아 알맞은 내보내기 객체를 돌려주는 함수 `get_exporter(fmt, title)`를 작성하세요.

```python
def get_exporter(fmt, title):
    # 힌트: 딕셔너리에 {문자열: 클래스}를 담아두면 깔끔합니다
    pass
```

> 🔮 이 문제는 **"클래스 자체를 값처럼 저장하는"** 패턴(팩토리)을 미리 맛보는 challenge입니다. if-elif로 풀어도 괜찮아요!

## 🤔 생각해보기

코딩을 시작하기 전에, 다음을 고민해보세요:
1. 왜 `export()`를 자식 클래스마다 따로 만들지 않고, 부모(추상 클래스)에 한 번만 만들까요?
2. 추상 메서드를 빼먹었을 때 **실행 시점이 아니라 객체 생성 시점에** 에러가 나는 것이 왜 좋을까요?
3. 만약 `abc`를 쓰지 않고 그냥 일반 클래스로 만들면 어떤 문제가 생길까요?

막히면 스레드에 질문을 남겨주세요! 목표는 끝내는 것이 아니라 **"왜 추상 클래스가 필요한가"**를 이해하는 것입니다. 천천히 논리를 따라가 보세요.

행운을 빕니다! 🚀

---
---

# 📄 Python Practice: Design a Report Exporter System (Abstract Classes)!

Hey team! Today you're a developer at a data analytics company, designing a system that exports the same data into multiple formats.

## 🎯 Your Mission

Your company needs to export data — student grades, sales records — to clients in **multiple file formats.** Some clients want CSV to open in Excel, some want JSON for their programs to read, some want plain text a human can read.

**Here's the key:** The input data is **identical.** But each format looks completely different on output. And when a new format (say, Markdown) is added, you want to **force the developer to implement both "the extension" and "how to render."** If they forget, the program shouldn't even run. That's exactly why we need an **Abstract Base Class (ABC)**!

## 🧠 What is an Abstract Class (ABC)?

An abstract class is a class that is **"a blueprint only — the actual implementation must be filled in by child classes."**

- **Abstract method (`@abstractmethod`)**: A method that is declared by name but has an empty body. Children MUST implement it.
- **An abstract class cannot be instantiated directly**: Calling `ReportExporter("title")` raises a `TypeError`.
- **If a child skips even one abstract method**: That child also cannot be instantiated.

> 💡 Analogy: An abstract class is a "contract." It's like signing an agreement that says "to be a report exporter, I promise to always provide an extension and a way to render the data."

**Real-world applications:**
- 📊 **Data Analytics/Reporting**: Output the same data as CSV, JSON, PDF, etc.
- 🖼️ **Image Processing**: Save one image as PNG, JPG, WebP
- 🔌 **API Responses**: Serialize the same data per format (XML/JSON)
- 🎮 **Game Saves**: Write save data in multiple formats

## 📋 The Rules

*What you're given:*
- An abstract class `ReportExporter` (you design it)
- Three concrete classes: `CsvExporter`, `JsonExporter`, `TextExporter`
- Data comes as a **list of dictionaries** (each dict is one row)

*Example input data:*
```python
rows = [
    {"name": "Alice", "score": 90},
    {"name": "Bob", "score": 85},
]
```

*Output rules per format:*

| Format | Class | Extension | How to render |
|---|---|---|---|
| CSV | `CsvExporter` | `csv` | First line is the header, then each row joined by commas |
| JSON | `JsonExporter` | `json` | Serialize with `json.dumps` |
| Text | `TextExporter` | `txt` | Each row as `"1. key: value, ..."` |

*What you need to do:*
1. Use the `abc` module to write the abstract class `ReportExporter`
2. Declare `file_extension()` and `render(rows)` as abstract methods
3. Write a shared **concrete method** `export(rows)` (returns `"title.ext\nrendered"`)
4. Implement the abstract methods in each of the three concrete classes

*Constraints you must follow:*
- **Use the `abc` module**: `from abc import ABC, abstractmethod`
- A class missing an abstract method must NOT be instantiable
- Write `export()` **only once** in the abstract class (no duplication!)
- All variable/method names must be **snake_case** (class names use PascalCase)

## 💡 Example Time

**Example 1: CSV export**
```
csv_exporter = CsvExporter("grades")
csv_exporter.file_extension()  →  "csv"
csv_exporter.render(rows)      →  "name,score\nAlice,90\nBob,85"
csv_exporter.export(rows)      →  "grades.csv\nname,score\nAlice,90\nBob,85"
```

**Example 2: The abstract class can't be created directly**
```
ReportExporter("test")   →  TypeError! ❌
```
Why? `ReportExporter` is an abstract class with abstract methods, so you can't make an object from it directly.

**Example 3: Polymorphism — same data, different output**
```python
exporters = [CsvExporter("g"), JsonExporter("g"), TextExporter("g")]
for exporter in exporters:
    print(exporter.export(rows))
```
They're different classes, but since they're all children of `ReportExporter`, you can **call them the exact same way.** Yet the results differ completely per format!

## 🎓 What You Should Know

Before you start coding, make sure you understand:
- Classes and inheritance (`class Child(Parent):`)
- `__init__` and `super().__init__()`
- The meaning of `self` and instance attributes
- Working with dictionaries (`.keys()`, `row[key]`)
- Looping over lists and joining lines with `"\n".join(...)`
- f-string formatting

## ✅ Your Task

Write the classes with this structure:
```python
from abc import ABC, abstractmethod

class ReportExporter(ABC):
    def __init__(self, title: str):
        # Your code here
        pass

    @abstractmethod
    def file_extension(self) -> str:
        ...

    @abstractmethod
    def render(self, rows: list[dict]) -> str:
        ...

    def export(self, rows: list[dict]) -> str:
        # A concrete method that uses BOTH abstract methods
        pass

class CsvExporter(ReportExporter):
    # Your code here
    pass
```

**Tips to get you started:**
- Leave the body of abstract methods as `...` or `pass`
- `export()` calls **both** `self.file_extension()` and `self.render()` — it behaves differently per child!
- Get CSV headers from the first row's `.keys()`
- For JSON, use `import json` then `json.dumps(rows, ensure_ascii=False)` (so Korean text isn't garbled)

## 🎪 Test Your Code

Try running these test cases:

```python
rows = [
    {"name": "Alice", "score": 90},
    {"name": "Bob", "score": 85},
]

# Test 1: Extensions
print(CsvExporter("g").file_extension())   # Expected: csv
print(JsonExporter("g").file_extension())  # Expected: json
print(TextExporter("g").file_extension())  # Expected: txt

# Test 2: CSV render
print(CsvExporter("g").render(rows))
# Expected:
# name,score
# Alice,90
# Bob,85

# Test 3: export (includes title + extension)
print(CsvExporter("grades").export(rows))
# Expected first line: grades.csv

# Test 4: Try to instantiate the abstract class (error is correct!)
try:
    ReportExporter("test")
except TypeError:
    print("Correct: abstract class can't be instantiated ✅")
```

## 🌟 Bonus Challenges

Finished the core task? Give these a shot! (Extra points — added on top of your base score)

### 🥉 Easy: Report the row count
Add a shared concrete method `row_count(rows)` to the abstract class that all exporters inherit. It returns the number of rows as an integer.

### 🥈 Medium: Markdown table exporter
Add a `MarkdownExporter` class. Its extension is `md`, and it renders the data as a Markdown table:
```
| name | score |
| --- | --- |
| Alice | 90 |
| Bob | 85 |
```

### 🥇 Hard: Pick an exporter by format string (concept preview 🔮)
Write a function `get_exporter(fmt, title)` that takes a string like `"csv"`, `"json"`, or `"txt"` and returns the matching exporter object.

```python
def get_exporter(fmt, title):
    # Hint: a dict of {string: class} keeps this clean
    pass
```

> 🔮 This previews the "store a class as a value" pattern (a factory). Solving it with if-elif is fine too!

## 🤔 Think About It

Before you start coding, consider:
1. Why write `export()` only once in the parent (abstract class) instead of in every child?
2. Why is it good that a missing abstract method fails **at object-creation time, not at run time**?
3. What problems would arise if you used a plain class instead of `abc`?

Drop your questions in the thread if you get stuck! The goal isn't just to finish — it's to understand **why abstract classes exist.** Take your time and follow the logic.

Good luck! 🚀
