# 🐍 Python 연습: 성적 기록 처리하기 (파일 입출력)

여러분, 안녕하세요! 이번에는 컴퓨터의 메모리 너머로 나가봅시다 — **파일**로요!

## 🎯 미션 (시나리오)

여러분은 한 고등학교의 **새로운 데이터 분석 인턴**입니다. 선생님이 학생들의 시험 성적이 담긴 텍스트 파일을 건네주며 이렇게 말씀하셨어요:

> "이 파일을 읽어서, 평균 점수, 최고점/최저점 학생 정보가 담긴 요약 보고서를 만들어 주세요. 파일로 저장해서 교무회의 때 쓸 거예요."

자, 이제 여러분이 인턴으로서 멋지게 일을 처리할 차례입니다! 💼

## 📋 규칙

*주어지는 것:*
- `grades.txt` 파일 (한 줄에 한 학생, 형식: `이름,점수`)

`grades.txt` 예시:
```
Alice,85
Bob,72
Charlie,90
Diana,68
Eve,95
```

*해야 할 일:*
1. 파일에서 성적 데이터를 읽어들이기
2. 평균, 최고점 학생, 최저점 학생 계산하기
3. 결과를 `summary.txt` 파일에 저장하기

*반드시 따라야 할 제약사항:*
- **반드시 `with` 문을 사용해야 합니다** (파일을 안전하게 닫기 위해)
- 파일을 읽을 때는 `"r"` 모드, 쓸 때는 `"w"` 모드 사용
- 모든 파일 작업에 `encoding="utf-8"` 명시
- 함수 두 개로 나누어 작성 (역할 분리!)

## 💡 새로 배우는 개념

### 1. `with` 문으로 파일 열기

```python
with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()
# 여기서 파일은 자동으로 닫힙니다!
```

> **왜 `with`를 쓰나요?** 파일을 열면 운영체제 자원을 사용하게 되는데, 까먹고 안 닫으면 문제가 생길 수 있어요. `with` 문은 블록이 끝나면 **자동으로** 파일을 닫아줍니다.

### 2. 파일 모드

| 모드 | 의미 | 비고 |
|------|------|------|
| `"r"` | 읽기 (read) | 파일이 없으면 에러 |
| `"w"` | 쓰기 (write) | 기존 내용을 모두 **덮어씀** ⚠️ |
| `"a"` | 추가 (append) | 기존 내용 끝에 덧붙임 |

### 3. 파일에서 한 줄씩 읽기

```python
with open("data.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())  # strip()으로 줄바꿈 문자 제거!
```

### 4. 파일에 쓰기

```python
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("첫 번째 줄\n")  # \n을 직접 넣어야 줄바꿈됨
    f.write("두 번째 줄\n")
```

## 🎓 알아야 할 것

- `open()`, `read()`, `write()` 함수
- `with` 문 (context manager)
- `"r"`, `"w"`, `"a"` 모드의 차이
- 문자열 메서드 `strip()`, `split()`
- 문자열을 정수로 변환: `int("85")`
- 튜플과 리스트의 기본 사용
- `f"{x:.2f}"` 같은 f-string 포맷팅

## ✅ 과제

다음 두 함수를 작성하세요:

```python
def read_grades(file_path: str) -> list:
    """파일에서 성적을 읽어 (이름, 점수) 튜플의 리스트로 반환합니다."""
    pass

def write_summary(file_path: str, grades: list) -> None:
    """성적 리스트를 받아 요약 보고서를 파일로 저장합니다."""
    pass
```

**`read_grades`가 해야 할 일:**
- 파일을 한 줄씩 읽기
- 각 줄을 `,`로 분리
- 점수는 정수로 변환
- `[("Alice", 85), ("Bob", 72), ...]` 형태로 반환

**`write_summary`가 해야 할 일:**
- 학생 수, 평균 점수, 최고점 학생, 최저점 학생 계산
- 다음 형식으로 파일에 저장:

```
=== Grade Summary ===
Total students: 5
Average score: 82.00
Highest: Eve (95)
Lowest: Diana (68)
```

**시작하는 데 도움이 될 팁:**
- 평균은 `합계 / 개수`로 계산하세요 (`sum()` 함수 없이!)
- 최고점/최저점은 변수 두 개를 만들어 반복문에서 갱신하세요
- 평균 점수는 소수점 둘째 자리까지: `f"{average:.2f}"`

## 🎪 코드 테스트

다음 테스트 케이스를 실행해보세요:

```python
# 테스트용 입력 파일 만들기
with open("grades.txt", "w", encoding="utf-8") as f:
    f.write("Alice,85\n")
    f.write("Bob,72\n")
    f.write("Charlie,90\n")
    f.write("Diana,68\n")
    f.write("Eve,95\n")

# 테스트 1: 읽기
grades = read_grades("grades.txt")
print(grades)
# 예상: [('Alice', 85), ('Bob', 72), ('Charlie', 90), ('Diana', 68), ('Eve', 95)]

# 테스트 2: 쓰기
write_summary("summary.txt", grades)
with open("summary.txt", "r", encoding="utf-8") as f:
    print(f.read())
# 예상 출력:
# === Grade Summary ===
# Total students: 5
# Average score: 82.00
# Highest: Eve (95)
# Lowest: Diana (68)
```

## 🤔 생각해보기

코딩을 시작하기 전에, 접근 방법을 스케치해보세요:
1. `for line in f:`로 읽으면 각 `line`에는 무엇이 들어있을까요? (`\n`은요?)
2. `"Alice,85"`라는 문자열을 어떻게 `("Alice", 85)`로 만들까요?
3. 최고점을 찾을 때, 첫 번째 학생의 점수로 시작 변수를 어떻게 설정하면 좋을까요?
4. 만약 `"w"` 모드로 같은 파일에 두 번 쓰면 어떻게 될까요?

## 🌟 보너스 챌린지

### 🥉 Easy: 일기장 (Append 모드)
오늘의 학습 일기를 `diary.txt`에 한 줄씩 추가하는 함수를 작성하세요. 여러 번 실행해도 이전 기록이 사라지면 안 됩니다!

```python
def add_diary_entry(file_path: str, entry: str) -> None:
    # "a" 모드를 사용하세요!
    pass
```

### 🥈 Medium: CSV 형식 처리하기
실제 데이터는 보통 헤더(제목 줄)가 있어요! 다음 형식의 파일을 처리하는 함수를 작성하세요:

```
name,score
Alice,85
Bob,72
```

그리고 결과를 `pass_fail.csv`로 저장하세요 (70점 이상이면 PASS):

```
name,score,status
Alice,85,PASS
Bob,72,PASS
Diana,68,FAIL
```

### 🥇 Hard: 파일이 없을 때는? (예외 처리 미리보기)
존재하지 않는 파일을 열려고 하면 프로그램이 멈춰버려요. 다음 코드를 시도해보세요:

```python
def safe_read_grades(file_path: str) -> list:
    try:
        # read_grades 호출
        pass
    except FileNotFoundError:
        print(f"⚠️  '{file_path}' 파일을 찾을 수 없습니다.")
        return []
```

> 💡 `try`/`except`는 다음에 배울 내용이에요. 미리 맛보기로 도전해보세요!

---

막히면 슬랙 스레드에 질문을 남겨주세요! 목표는 끝내는 것이 아니라 배우는 것입니다. 천천히 논리를 이해하면서 진행하세요.

행운을 빕니다! 🚀

---
---

# 🐍 Python Practice: Process Grade Records (File I/O)

Hey team! This time we're going beyond computer memory — into **files**!

## 🎯 Your Mission (Scenario)

You're the **new data analytics intern** at a high school. The teacher hands you a text file containing student exam scores and says:

> "Read this file and create a summary report with the average score and the top/bottom students. Save it as a file — we'll use it at the faculty meeting."

Now it's your turn to handle this like a pro intern! 💼

## 📋 The Rules

*What you're given:*
- A `grades.txt` file (one student per line, format: `name,score`)

Example `grades.txt`:
```
Alice,85
Bob,72
Charlie,90
Diana,68
Eve,95
```

*What you need to do:*
1. Read the grade data from the file
2. Calculate the average, highest scorer, and lowest scorer
3. Save the result to a `summary.txt` file

*Constraints you must follow:*
- **You must use the `with` statement** (to safely close files)
- Use `"r"` mode for reading, `"w"` mode for writing
- Always specify `encoding="utf-8"` in file operations
- Split your code into two functions (separation of concerns!)

## 💡 New Concepts

### 1. Opening Files with `with`

```python
with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()
# The file is automatically closed here!
```

> **Why use `with`?** Opening a file uses operating system resources. If you forget to close it, problems can occur. The `with` statement **automatically** closes the file when the block ends.

### 2. File Modes

| Mode | Meaning | Notes |
|------|---------|-------|
| `"r"` | Read | Error if file doesn't exist |
| `"w"` | Write | **Overwrites** existing content ⚠️ |
| `"a"` | Append | Adds to the end of existing content |

### 3. Reading a File Line by Line

```python
with open("data.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())  # Use strip() to remove the newline!
```

### 4. Writing to a File

```python
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("First line\n")  # You must add \n yourself for line breaks
    f.write("Second line\n")
```

## 🎓 What You Should Know

- `open()`, `read()`, `write()` functions
- The `with` statement (context manager)
- The difference between `"r"`, `"w"`, `"a"` modes
- String methods `strip()`, `split()`
- Converting strings to integers: `int("85")`
- Basic tuple and list usage
- f-string formatting like `f"{x:.2f}"`

## ✅ Your Task

Write the following two functions:

```python
def read_grades(file_path: str) -> list:
    """Read grades from file and return a list of (name, score) tuples."""
    pass

def write_summary(file_path: str, grades: list) -> None:
    """Take a list of grades and save a summary report to file."""
    pass
```

**What `read_grades` should do:**
- Read the file line by line
- Split each line by `,`
- Convert score to integer
- Return in the form `[("Alice", 85), ("Bob", 72), ...]`

**What `write_summary` should do:**
- Calculate student count, average, highest scorer, lowest scorer
- Save to file in the following format:

```
=== Grade Summary ===
Total students: 5
Average score: 82.00
Highest: Eve (95)
Lowest: Diana (68)
```

**Tips to get you started:**
- Calculate average as `total / count` (without `sum()`!)
- Track highest/lowest with two variables, updated inside the loop
- Format average to 2 decimal places: `f"{average:.2f}"`

## 🎪 Test Your Code

Try running these test cases:

```python
# Create a test input file
with open("grades.txt", "w", encoding="utf-8") as f:
    f.write("Alice,85\n")
    f.write("Bob,72\n")
    f.write("Charlie,90\n")
    f.write("Diana,68\n")
    f.write("Eve,95\n")

# Test 1: Reading
grades = read_grades("grades.txt")
print(grades)
# Expected: [('Alice', 85), ('Bob', 72), ('Charlie', 90), ('Diana', 68), ('Eve', 95)]

# Test 2: Writing
write_summary("summary.txt", grades)
with open("summary.txt", "r", encoding="utf-8") as f:
    print(f.read())
# Expected output:
# === Grade Summary ===
# Total students: 5
# Average score: 82.00
# Highest: Eve (95)
# Lowest: Diana (68)
```

## 🤔 Think About It

Before you start coding, sketch out your approach:
1. When you read with `for line in f:`, what's actually in each `line`? (What about `\n`?)
2. How do you turn `"Alice,85"` (a string) into `("Alice", 85)` (a tuple)?
3. When finding the highest score, how should you initialize your tracking variables using the first student?
4. What happens if you write to the same file twice in `"w"` mode?

## 🌟 Bonus Challenges

### 🥉 Easy: Diary Log (Append Mode)
Write a function that adds today's study diary entry to `diary.txt`, one line at a time. It should preserve previous entries no matter how many times you run it!

```python
def add_diary_entry(file_path: str, entry: str) -> None:
    # Use "a" mode!
    pass
```

### 🥈 Medium: Handling CSV Format
Real-world data usually has a header (title row)! Write a function that processes files in this format:

```
name,score
Alice,85
Bob,72
```

And save the result to `pass_fail.csv` (PASS if score >= 70):

```
name,score,status
Alice,85,PASS
Bob,72,PASS
Diana,68,FAIL
```

### 🥇 Hard: What If the File Doesn't Exist? (Exception Handling Preview)
If you try to open a file that doesn't exist, your program crashes. Try the following code:

```python
def safe_read_grades(file_path: str) -> list:
    try:
        # call read_grades
        pass
    except FileNotFoundError:
        print(f"⚠️  Could not find file '{file_path}'.")
        return []
```

> 💡 `try`/`except` is something we'll learn next time. Try this as a preview!

---

Drop your questions in the Slack thread if you get stuck! Remember, the goal is to learn, not just to finish. Take your time and understand the logic.

Good luck! 🚀
