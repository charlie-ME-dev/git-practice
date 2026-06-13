# 🎬 Python 연습: 표준 라이브러리 `csv`로 갈아타기!

여러분, 안녕하세요! 지난 두 번의 미션에서 우리는 영화 데이터를 **직접 손으로** 읽고 썼습니다. `.split(",")`로 파싱하고, `f.write()`에 `\n`을 일일이 붙이고... 잘 동작했지만, 코드가 길었죠.

**오늘의 진실:** Python에는 이 모든 걸 해주는 표준 라이브러리 `csv`가 처음부터 들어 있습니다!

## 🎯 미션

CEO가 미팅에서 이렇게 말합니다:
> *"잠깐, 우리 회사 코드 리뷰 봤는데 — 다들 `csv` 라이브러리 쓰던데 왜 우리만 `.split(",")` 쓰고 있죠?"*

여러분의 임무: 지난 시간의 파이프라인을 표준 `csv` 라이브러리로 **리팩토링**하고, 그 과정에서:

1. ✨ **무엇이 더 쉬워지는지** (헤더 건너뛰기, 줄바꿈, 인용부호)
2. ⚠️ **무엇은 여전히 직접 해야 하는지** (타입 변환!)
3. 🐛 **새로운 함정** (`newline=""` — 안 쓰면 빈 줄이 생깁니다!)
4. 🏆 **`csv`만이 처리할 수 있는 진짜 어려운 케이스** (제목에 콤마가 있을 때)

이걸 모두 직접 체험합니다.

## 📚 빠른 입문: `csv` 라이브러리

### 읽기

```python
import csv

with open("data.csv", "r", encoding="utf-8", newline="") as f:
    reader = csv.reader(f)
    next(reader)  # 헤더 건너뛰기 — 한 줄로 끝!
    for row in reader:
        # row는 문자열 리스트: ['title', 'genre', '1994', '9.3']
        print(row)
```

> 💡 **핵심:** `csv.reader`는 콤마를 똑똑하게 처리합니다 — 따옴표 안의 콤마도 알아챕니다!
>
> ⚠️ **하지만:** 모든 값이 여전히 **문자열**입니다. `int()`와 `float()` 변환은 직접 해야 합니다.

### 쓰기

```python
import csv

with open("out.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["title", "genre", "year", "rating"])  # 헤더
    writer.writerow(["Parasite", "Thriller", 2019, 8.6])    # 한 줄
    writer.writerows(many_rows)                              # 여러 줄을 한 번에!
```

> 💡 **핵심:** `writerow`는 자동으로 콤마와 줄바꿈을 처리합니다. `\n`을 직접 안 붙여도 됩니다!

## ⚠️ 새로운 함정: `newline=""`를 잊지 마세요!

```python
# ❌ 잘못된 코드 (Windows에서 빈 줄이 생김)
with open("out.csv", "w", encoding="utf-8") as f:
    writer = csv.writer(f)
    ...

# ✅ 올바른 코드
with open("out.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    ...
```

`csv` 모듈은 이미 자체적으로 줄바꿈을 처리하기 때문에, OS가 또 줄바꿈을 추가하지 못하도록 `newline=""`로 막아야 합니다. **읽을 때도** 안전을 위해 권장됩니다.

## 📐 규칙

*해야 할 일:*
1. `csv.reader`와 `csv.writer`를 사용해서 모든 함수 다시 작성
2. 따옴표가 있는 콤마 처리 능력 확인
3. `newline=""` 사용

*반드시 따라야 할 제약사항:*
- ✅ `import csv` 가능 (드디어!)
- ❌ `import pandas` 금지
- ❌ `dict` 사용 금지 (이번에도 평행 리스트로)
- ❌ `sorted()` 금지 (정렬이 필요한 경우 — 이번 패키지엔 없음)
- ✅ 모든 파일 작업에 `with` + `encoding="utf-8"` + `newline=""`

## ✅ 과제

다음 6개 함수를 작성하세요:

```python
def load_ratings_with_csv(file_path: str) -> list:
    """csv.reader로 영화 평점 로딩.
       각 영화는 [title, genre, year(int), rating(float)] 리스트로."""
    pass

def save_ratings_with_csv(ratings: list, file_path: str) -> None:
    """csv.writer로 영화 리스트를 CSV에 저장 (헤더 포함)."""
    pass

def save_filtered_by_genre(ratings: list, genre: str, file_path: str) -> int:
    """장르 필터링 후 저장. 저장된 개수 반환."""
    pass

def save_summary_report(ratings: list, file_path: str) -> int:
    """장르별 개수/평균 보고서를 csv.writer로 저장.
       평행 리스트 사용 (dict 금지)."""
    pass

def count_rows_in_file(file_path: str) -> int:
    """CSV 파일의 데이터 행 개수 반환 (헤더 제외)."""
    pass

def compare_with_manual(file_path: str) -> bool:
    """csv.reader로 로딩한 결과와 .split(',')로 로딩한 결과가
       일치하는지 비교. (지난 시간의 load_ratings도 함께 import해서 사용)
       만약 둘 중 하나라도 크래시하면 False를 반환."""
    pass
```

**시작하는 데 도움이 될 팁:**
- `csv.reader` 객체는 한 번만 순회할 수 있습니다 (재사용 불가)
- `next(reader)`로 헤더를 건너뛸 때, 빈 파일이면 `StopIteration` 발생 — `next(reader, None)`로 안전하게
- `writer.writerow([1994, 9.3])`처럼 숫자를 전달해도 자동으로 문자열로 변환됩니다
- `compare_with_manual`에서는 `try`/`except`로 양쪽을 감싸세요

## 🎪 코드 테스트

```python
ratings = load_ratings_with_csv("movie_ratings.csv")
print(f"로딩 완료: {len(ratings)}편")
# 예상: 로딩 완료: 12편

print(f"첫 영화: {ratings[0]}")
# 예상: ['The Shawshank Redemption', 'Drama', 1994, 9.3]

print(f"year 타입: {type(ratings[0][2]).__name__}")
print(f"rating 타입: {type(ratings[0][3]).__name__}")
# 예상: year 타입: int / rating 타입: float

# 왕복 테스트
save_ratings_with_csv(ratings, "output/round_trip.csv")
reloaded = load_ratings_with_csv("output/round_trip.csv")
print(f"왕복 성공: {reloaded == ratings}")
# 예상: 왕복 성공: True

# 빈 줄이 생기지 않았는지 확인
with open("output/round_trip.csv", "rb") as f:
    content = f.read()
print(f"빈 줄 없음: {b'\\n\\n' not in content}")
# 예상: 빈 줄 없음: True

# 장르 필터링
n = save_filtered_by_genre(ratings, "Drama", "output/drama.csv")
print(f"Drama: {n}편 저장")
# 예상: Drama: 3편 저장

# 행 개수 (헤더 제외)
print(f"전체 파일 행 수: {count_rows_in_file('output/round_trip.csv')}")
# 예상: 전체 파일 행 수: 12

# 수동 파싱과 비교 (깨끗한 데이터)
print(f"깨끗한 데이터 일치: {compare_with_manual('movie_ratings.csv')}")
# 예상: 깨끗한 데이터 일치: True
```

## 🎓 진실의 순간: 따옴표 콤마 테스트

지난 시간에 우리는 *"제목에 콤마가 있으면 어떻게 될까?"*라는 질문을 남겨두었습니다. 지금이 답을 확인할 시간입니다!

```python
# 콤마가 포함된 영화 제목들 (실제 존재하는 영화들!)
tricky = [
    ["Crazy, Stupid, Love", "Comedy", 2011, 7.4],
    ["Eat, Pray, Love", "Drama", 2010, 5.7],
]

save_ratings_with_csv(tricky, "output/tricky.csv")
```

**먼저 raw 파일을 직접 열어보세요!** `csv.writer`가 무엇을 했는지 확인하세요:

```
title,genre,year,rating
"Crazy, Stupid, Love",Comedy,2011,7.4
"Eat, Pray, Love",Drama,2010,5.7
```

→ 자동으로 따옴표(`"`)로 감싸졌습니다! 콤마가 있는 필드만요. 똑똑하죠?

이제 두 가지 방식으로 다시 읽어보세요:

```python
# csv.reader는 따옴표를 이해함
reloaded = load_ratings_with_csv("output/tricky.csv")
print(reloaded[0])
# 예상: ['Crazy, Stupid, Love', 'Comedy', 2011, 7.4]  ✅

# 수동 .split(",")은 깨짐 — 실제로 크래시할 수 있음!
result = compare_with_manual("output/tricky.csv")
print(f"일치 여부: {result}")
# 예상: 일치 여부: False  (수동 방식은 크래시하거나 잘못 파싱)
```

> 🎉 **이게 바로 우리가 라이브러리를 쓰는 이유입니다!** 직접 만든 코드로는 처리하기 정말 어려운 케이스를, 라이브러리는 한 줄로 해결합니다.

## 🤔 생각해보기

코딩 후에 다음 질문들을 생각해보세요:
1. `csv.reader`가 자동으로 처리해주는 일과 **여전히 직접 해야 하는 일**은 무엇인가요?
2. 만약 영화 평점이 `"9.3"`이라는 문자열이면 그대로 비교나 계산이 가능할까요? `csv.reader`가 타입 변환까지 해주지 않는 이유는 무엇일까요?
3. `newline=""`를 빼고 저장해보세요. 어떤 일이 생기나요? (힌트: 메모장이나 다른 에디터로 열어보세요)
4. `writerow`와 `writerows`(s가 붙음)의 차이는 무엇인가요? 어느 쪽이 더 효율적일까요?

## 🎁 보너스 도전

핵심 함수를 모두 완성한 후 시도해보세요:

### 🥉 Easy: 따옴표 콤마 왕복 검증
콤마가 포함된 제목의 영화 3편을 저장하고 다시 로딩해서, 정확히 같은 데이터가 돌아오는지 확인하는 테스트 함수를 작성하세요.
```python
def test_quoted_comma_round_trip() -> bool:
    """콤마를 포함한 제목으로 저장 → 로딩 → 일치 여부 반환."""
    pass
```

### 🥈 Medium: `newline` 함정 진단
`newline=""`를 **빼고** 같은 데이터를 저장한 뒤, 결과 파일에 몇 개의 빈 줄이 들어있는지 카운트하는 함수를 작성하세요. (이걸로 학생들 사이에서 "왜 내 CSV가 이상하지?" 디버깅 무용담을 나눌 수 있습니다 😄)
```python
def count_blank_lines_bug(ratings: list, file_path: str) -> int:
    """일부러 newline=""을 빼고 저장 후, 빈 줄 개수 반환."""
    pass
```
> 💭 **힌트:** 파일을 텍스트 모드로 열어서 `len(f.readlines())`와 데이터 행 수를 비교해보세요.

### 🥇 Hard: 다중 구분자 (Dialects)
"CSV"라는 이름은 사실 거짓말입니다 — 실제로는 `\t`(탭), `|`(파이프), `;`(세미콜론)도 자주 쓰입니다. 같은 데이터를 세 가지 다른 구분자로 저장하는 함수를 작성하세요.
```python
def save_in_multiple_dialects(ratings: list, base_path: str) -> list:
    """다음 3개 파일을 저장하고 경로 리스트를 반환:
       - base_path + '.csv'  (콤마)
       - base_path + '.tsv'  (탭, delimiter='\\t')
       - base_path + '.psv'  (파이프, delimiter='|')"""
    pass
```
> 💭 **힌트:** `csv.writer(f, delimiter="\t")`처럼 구분자를 지정할 수 있습니다. 읽을 때도 `csv.reader(f, delimiter="\t")`로 지정해야 합니다.

행운을 빕니다! 🚀

> *"바보도 컴퓨터가 이해할 수 있는 코드는 쓸 수 있다. 훌륭한 프로그래머는 사람이 이해할 수 있는 코드를 쓴다."*
> — Martin Fowler

---
---

# 🎬 Python Practice: Switch to the Standard `csv` Library!

Hey team! For the last two sessions, we've been reading and writing movie data **by hand**. We parsed with `.split(",")`, manually added `\n` to every `f.write()`, and it worked — but the code was long.

**Today's revelation:** Python has had a built-in `csv` library this whole time!

## 🎯 Your Mission

The CEO drops this in a meeting:
> *"Wait — I was reviewing our company code, and everyone else is using the `csv` library. Why are we still using `.split(",")`?"*

Your job: **refactor** last session's pipeline to use the standard `csv` library, and in the process discover:

1. ✨ **What gets easier** (skipping headers, line breaks, quotes)
2. ⚠️ **What you still have to do yourself** (type conversion!)
3. 🐛 **A new gotcha** (`newline=""` — skip it and you get blank lines!)
4. 🏆 **The genuinely hard cases only `csv` can handle** (titles containing commas)

You'll experience all of this firsthand.

## 📚 Quick Primer: The `csv` Library

### Reading

```python
import csv

with open("data.csv", "r", encoding="utf-8", newline="") as f:
    reader = csv.reader(f)
    next(reader)  # skip header — one line!
    for row in reader:
        # row is a list of strings: ['title', 'genre', '1994', '9.3']
        print(row)
```

> 💡 **Key:** `csv.reader` handles commas intelligently — even commas inside quoted fields!
>
> ⚠️ **But:** All values are still **strings**. You still convert with `int()` and `float()` yourself.

### Writing

```python
import csv

with open("out.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["title", "genre", "year", "rating"])  # header
    writer.writerow(["Parasite", "Thriller", 2019, 8.6])    # one row
    writer.writerows(many_rows)                              # many rows at once!
```

> 💡 **Key:** `writerow` handles commas AND newlines for you. No more `\n` by hand!

## ⚠️ The New Gotcha: Don't Forget `newline=""`

```python
# ❌ Wrong (causes blank lines between rows on Windows)
with open("out.csv", "w", encoding="utf-8") as f:
    writer = csv.writer(f)
    ...

# ✅ Right
with open("out.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    ...
```

The `csv` module already handles newlines itself, so we tell Python *not* to add OS-specific ones on top. **Recommended for reading too** for safety.

## 📐 The Rules

*What you need to do:*
1. Rewrite every function using `csv.reader` and `csv.writer`
2. Verify quoted-comma handling works
3. Use `newline=""` everywhere

*Constraints you must follow:*
- ✅ `import csv` is now allowed (finally!)
- ❌ No `import pandas`
- ❌ No `dict` (use parallel lists again)
- ❌ No `sorted()` (not needed in this package)
- ✅ All file ops use `with` + `encoding="utf-8"` + `newline=""`

## ✅ Your Task

Write these 6 functions:

```python
def load_ratings_with_csv(file_path: str) -> list:
    """Load ratings using csv.reader.
       Each movie: [title, genre, year(int), rating(float)]."""
    pass

def save_ratings_with_csv(ratings: list, file_path: str) -> None:
    """Save the movie list to CSV using csv.writer (include header)."""
    pass

def save_filtered_by_genre(ratings: list, genre: str, file_path: str) -> int:
    """Filter by genre, save, return saved count."""
    pass

def save_summary_report(ratings: list, file_path: str) -> int:
    """Save a per-genre summary using csv.writer.
       Use parallel lists (no dict)."""
    pass

def count_rows_in_file(file_path: str) -> int:
    """Return the number of DATA rows (excluding header)."""
    pass

def compare_with_manual(file_path: str) -> bool:
    """Compare csv.reader's result with .split(',') manual parsing.
       (Import your previous load_ratings to do this.)
       If either crashes, return False."""
    pass
```

**Tips to get you started:**
- A `csv.reader` object can only be iterated once (not reusable)
- `next(reader)` raises `StopIteration` on an empty file — use `next(reader, None)` to be safe
- `writer.writerow([1994, 9.3])` auto-converts numbers to strings for you
- In `compare_with_manual`, wrap both calls in `try`/`except`

## 🎪 Test Your Code

```python
ratings = load_ratings_with_csv("movie_ratings.csv")
print(f"Loaded: {len(ratings)} movies")
# Expected: Loaded: 12 movies

print(f"First: {ratings[0]}")
# Expected: ['The Shawshank Redemption', 'Drama', 1994, 9.3]

print(f"year type: {type(ratings[0][2]).__name__}")
print(f"rating type: {type(ratings[0][3]).__name__}")
# Expected: year type: int / rating type: float

# Round trip
save_ratings_with_csv(ratings, "output/round_trip.csv")
reloaded = load_ratings_with_csv("output/round_trip.csv")
print(f"Round trip OK: {reloaded == ratings}")
# Expected: Round trip OK: True

# Check no blank lines were introduced
with open("output/round_trip.csv", "rb") as f:
    content = f.read()
print(f"No blank lines: {b'\\n\\n' not in content}")
# Expected: No blank lines: True

# Genre filter
n = save_filtered_by_genre(ratings, "Drama", "output/drama.csv")
print(f"Drama: {n} saved")
# Expected: Drama: 3 saved

# Row count (excluding header)
print(f"Total rows: {count_rows_in_file('output/round_trip.csv')}")
# Expected: Total rows: 12

# Compare with manual (clean data)
print(f"Clean data agrees: {compare_with_manual('movie_ratings.csv')}")
# Expected: Clean data agrees: True
```

## 🎓 The Moment of Truth: Quoted-Comma Test

Remember the question from last session: *"What if a movie title contains a comma?"* Now we get the answer!

```python
# Real movies with commas in their titles
tricky = [
    ["Crazy, Stupid, Love", "Comedy", 2011, 7.4],
    ["Eat, Pray, Love", "Drama", 2010, 5.7],
]

save_ratings_with_csv(tricky, "output/tricky.csv")
```

**Open the raw file first!** See what `csv.writer` did:

```
title,genre,year,rating
"Crazy, Stupid, Love",Comedy,2011,7.4
"Eat, Pray, Love",Drama,2010,5.7
```

→ It automatically wrapped values containing commas in quotes (`"`). Just the ones that needed it. Clever!

Now read it back two ways:

```python
# csv.reader understands the quotes
reloaded = load_ratings_with_csv("output/tricky.csv")
print(reloaded[0])
# Expected: ['Crazy, Stupid, Love', 'Comedy', 2011, 7.4]  ✅

# Manual .split(",") breaks — may even crash!
result = compare_with_manual("output/tricky.csv")
print(f"Match: {result}")
# Expected: Match: False  (manual crashes or mis-parses)
```

> 🎉 **This is exactly why we use libraries!** Cases that are hard to handle by hand, the library solves in one line.

## 🤔 Think About It

After coding, consider:
1. What does `csv.reader` handle automatically, and what do **you** still have to do?
2. If a rating is the string `"9.3"`, can you compare or do math with it directly? Why doesn't `csv.reader` convert types for you?
3. Try saving without `newline=""`. What happens? (Hint: open the file in Notepad or another editor)
4. What's the difference between `writerow` and `writerows` (with the `s`)? Which is more efficient?

## 🎁 Bonus Challenges

After completing the core:

### 🥉 Easy: Quoted-comma round-trip verification
Write a test function that saves 3 movies with commas in their titles, reloads, and confirms exact match.
```python
def test_quoted_comma_round_trip() -> bool:
    """Save movies with commas in titles → reload → return whether they match."""
    pass
```

### 🥈 Medium: Diagnose the `newline` bug
Save the same data **without** `newline=""` and count how many blank lines end up in the file. (This is a debugging war story you'll share with classmates 😄)
```python
def count_blank_lines_bug(ratings: list, file_path: str) -> int:
    """Deliberately omit newline="" while saving, then return blank-line count."""
    pass
```
> 💭 **Hint:** Open the saved file in text mode and compare `len(f.readlines())` with the expected row count.

### 🥇 Hard: Multiple delimiters (Dialects)
The name "CSV" is actually a lie — TSV (tabs), PSV (pipes), and `;`-separated files are all common. Save the same data in three formats:
```python
def save_in_multiple_dialects(ratings: list, base_path: str) -> list:
    """Save these 3 files and return the list of paths:
       - base_path + '.csv'  (comma)
       - base_path + '.tsv'  (tab, delimiter='\\t')
       - base_path + '.psv'  (pipe, delimiter='|')"""
    pass
```
> 💭 **Hint:** `csv.writer(f, delimiter="\t")` sets the delimiter. Reading also needs `csv.reader(f, delimiter="\t")`.

Good luck! 🚀

> *"Any fool can write code that a computer can understand. Good programmers write code that humans can understand."*
> — Martin Fowler
