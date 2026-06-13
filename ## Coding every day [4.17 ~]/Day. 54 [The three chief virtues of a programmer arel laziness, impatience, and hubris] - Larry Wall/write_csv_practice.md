# 🎬 Python 연습: 영화 데이터 보고서 만들기!

여러분, 안녕하세요! 지난번 미션 기억나시나요? CEO를 위해 영화 평점을 분석했죠. 이번에는 그 분석을 **파일로 저장**해서 다른 팀과 공유해야 합니다!

## 🎯 미션

지난 시간에는 데이터를 **읽기만** 했지만, 진짜 데이터 엔지니어는 **읽고 → 변환하고 → 저장**합니다. 이 사이클이 바로 모든 데이터 파이프라인의 기본입니다.

이번 미션은 CEO에게 다음 4개의 보고서를 CSV 파일로 만들어 제출하는 것입니다:

1. 📂 **전체 영화 카탈로그** (백업용)
2. 🎭 **장르별 영화 목록** (마케팅 팀이 요청)
3. 🏆 **TOP N 영화** (메인 페이지 추천용)
4. 📊 **장르별 요약 통계** (경영진 보고용)

> 💡 **핵심 개념:** 파이썬에서 파일에 **쓰기**는 `open(path, "w")`로 열고 `f.write(...)`로 한 줄씩 작성합니다. 줄바꿈은 자동으로 추가되지 않으니 직접 `"\n"`을 붙여야 합니다!

## 📋 데이터 형식 (지난 시간과 동일)

```
title,genre,year,rating
The Shawshank Redemption,Drama,1994,9.3
The Dark Knight,Action,2008,9.0
...
```

각 영화는 `[title, genre, year, rating]` 형태의 리스트로 메모리에 저장됩니다.

## 📐 규칙

*주어지는 것:*
- `movie_ratings.csv` 파일 (지난 시간과 동일)

*해야 할 일:*
1. 파일에서 영화 데이터를 로딩
2. 데이터를 변환 (필터링, 정렬, 집계)
3. 결과를 **새로운 CSV 파일에 저장**
4. 저장된 파일이 다시 로딩 가능해야 함 (왕복 검증!)

*반드시 따라야 할 제약사항:*
- ❌ `import csv` 금지 — 직접 작성해야 합니다
- ❌ `import pandas` 금지
- ❌ `sorted()` 함수 사용 금지 (`save_top_n`에서) — 직접 정렬하세요
- ❌ 딕셔너리(dict) 사용 금지 — 리스트만으로 해결합니다
- ✅ `open("w")`, `f.write()`, f-string 사용
- ✅ `try`/`except` 사용 가능 (한 군데서 필요함)
- ✅ 지난 시간의 `load_ratings`를 재사용 가능

## 💡 파일 쓰기 빠른 예제

```python
with open("hello.csv", "w", encoding="utf-8") as f:
    f.write("name,age\n")           # 헤더 — 줄바꿈 직접!
    f.write("Alice,30\n")
    f.write("Bob,25\n")
```

f-string으로 변수를 끼워 넣을 수 있습니다:
```python
name = "Charlie"
age = 28
f.write(f"{name},{age}\n")
```

> ⚠️ **자주 잊는 것:** `f.write()`는 `print()`처럼 자동으로 줄바꿈을 추가하지 않습니다. 줄 끝에 `\n`을 꼭 넣으세요!

## ✅ 과제

다음 6개의 함수를 작성하세요:

```python
def load_ratings(file_path: str) -> list:
    """지난 시간의 함수를 재사용합니다."""
    pass

def save_ratings(ratings: list, file_path: str) -> None:
    """영화 리스트를 CSV 파일로 저장합니다 (헤더 포함)."""
    pass

def save_filtered_by_genre(ratings: list, genre: str, file_path: str) -> int:
    """특정 장르만 필터링해서 저장하고, 저장된 개수를 반환합니다."""
    pass

def save_top_n(ratings: list, n: int, file_path: str) -> int:
    """평점이 높은 순서대로 상위 N개를 저장합니다. sorted() 사용 금지!"""
    pass

def save_summary_report(ratings: list, file_path: str) -> int:
    """장르별 영화 개수와 평균 평점을 요약해서 저장합니다.
       반환값: 요약된 장르의 개수."""
    pass

def load_ratings_safe(file_path: str) -> list:
    """파일이 없으면 빈 리스트를 반환합니다 (크래시 금지!).
       try/except를 사용하세요."""
    pass
```

**시작하는 데 도움이 될 팁:**
- `save_ratings`를 먼저 완성하면, 나머지 함수에서 재사용할 수 있어요!
- `save_top_n`의 정렬: "최고값 찾기 → 결과에 추가 → 원본에서 제거"를 N번 반복하는 방식 (선택 정렬)
- `save_summary_report`: 딕셔너리 대신 **평행 리스트**(`genres = []`, `counts = []`, `totals = []`)를 써보세요
- `n`이 영화 개수보다 클 때도 안전하게 처리해야 합니다 (슬라이싱 `[:n]` 사용)

## 🎪 코드 테스트

```python
ratings = load_ratings("movie_ratings.csv")

# 테스트 1: 전체 저장 (왕복 검증)
save_ratings(ratings, "all_movies.csv")
reloaded = load_ratings("all_movies.csv")
print(f"왕복 성공: {reloaded == ratings}")
# 예상: 왕복 성공: True

# 테스트 2: 장르 필터링 저장
count = save_filtered_by_genre(ratings, "Drama", "drama.csv")
print(f"Drama {count}편 저장 완료")
# 예상: Drama 3편 저장 완료

# 테스트 3: TOP 3 저장
n = save_top_n(ratings, 3, "top3.csv")
print(f"TOP {n} 저장 완료")
top = load_ratings("top3.csv")
for movie in top:
    print(f"  - {movie[0]}: {movie[3]}")
# 예상:
#   - The Shawshank Redemption: 9.3
#   - The Dark Knight: 9.0
#   - Forrest Gump: 8.8  (또는 Inception, 둘 다 8.8)

# 테스트 4: 장르별 요약
n_genres = save_summary_report(ratings, "summary.csv")
print(f"{n_genres}개 장르 요약 완료")
with open("summary.csv", "r", encoding="utf-8") as f:
    print(f.read())
# 예상 출력:
# genre,count,average_rating
# Drama,3,8.87
# Action,3,8.83
# ...

# 테스트 5: 안전한 로딩
data = load_ratings_safe("does_not_exist.csv")
print(f"없는 파일 처리: {data}")
# 예상: 없는 파일 처리: []

# 테스트 6: 경계 조건
save_ratings([], "empty.csv")
save_top_n(ratings, 100, "top100.csv")  # n > 영화 개수
print(f"TOP 100 요청: 실제 {len(load_ratings('top100.csv'))}편 저장")
# 예상: TOP 100 요청: 실제 12편 저장
```

## 🤔 생각해보기

코딩을 시작하기 전에, 다음 질문들을 생각해보세요:
1. `open(path, "w")`로 이미 존재하는 파일을 열면 어떻게 될까요? 데이터가 보존될까요?
2. 헤더를 빼먹으면 어떤 일이 생길까요? `load_ratings`로 다시 읽을 때 무슨 일이?
3. 영화 제목에 콤마가 있으면 (예: `"Crazy, Stupid, Love"`) 저장된 CSV는 깨질 수 있을까요?
4. 만약 평점이 `8.876543`처럼 길다면 어떻게 짧게(예: `8.88`) 저장할 수 있을까요? f-string 포맷 지정자를 찾아보세요.

## 🎁 보너스 도전

핵심 함수를 모두 완성한 후 시도해보세요:

### 🥉 Easy: 연도별 저장
특정 연도에 개봉한 영화만 저장하는 함수를 작성하세요.
```python
def save_by_year(ratings: list, year: int, file_path: str) -> int:
    pass
```

### 🥈 Medium: 임계값 이상 저장 + 빈 결과 방지
평점이 threshold 이상인 영화만 저장하되, 해당하는 영화가 없으면 파일을 생성하지 않는 함수를 작성하세요.
```python
def save_above_threshold(ratings: list, threshold: float, file_path: str) -> bool:
    """저장하면 True, 해당 영화가 없어서 저장하지 않으면 False를 반환."""
    pass
```

### 🥇 Hard: 다중 파일 분할
장르별로 **각각 다른 파일**에 저장하는 함수를 작성하세요. 예: Drama 영화는 `drama.csv`, Action 영화는 `action.csv` 등. 어떤 장르가 있는지는 미리 알 수 없습니다.
```python
def save_by_genre_split(ratings: list, output_dir: str = ".") -> list:
    """각 장르별로 별도 파일에 저장.
       반환값: 생성된 파일 경로의 리스트."""
    pass
```
> 💭 **힌트:** 먼저 모든 장르를 찾고, 각 장르마다 `save_filtered_by_genre`를 호출하세요. 파일명은 `f"{output_dir}/{genre.lower()}.csv"` 형태로.

행운을 빕니다! 🚀

> *"데이터 과학자는 시간의 80%를 데이터 정리에 쓰고, 나머지 20%는 데이터 정리에 대해 불평하는 데 씁니다."*
> — 데이터 업계 격언

---
---

# 🎬 Python Practice: Build a Movie Data Reporting Pipeline!

Hey team! Remember last time's mission? You analyzed movie ratings for the CEO. This time, you need to **save your analysis as files** to share with other teams!

## 🎯 Your Mission

Last session you only **read** data. But real data engineers **read → transform → write**. That cycle is the foundation of every data pipeline in existence.

This mission: produce these 4 CSV reports for the CEO:

1. 📂 **Full catalog backup**
2. 🎭 **Genre-specific movie lists** (marketing team request)
3. 🏆 **Top N movies** (for the homepage)
4. 📊 **Genre summary statistics** (for executive briefing)

> 💡 **Key concept:** To **write** to a file in Python, open it with `open(path, "w")` and use `f.write(...)` line by line. Line breaks aren't added automatically — you must include `"\n"` yourself!

## 📋 Data Format (same as last time)

```
title,genre,year,rating
The Shawshank Redemption,Drama,1994,9.3
The Dark Knight,Action,2008,9.0
...
```

Each movie is stored in memory as a `[title, genre, year, rating]` list.

## 📐 The Rules

*What you're given:*
- The `movie_ratings.csv` file (same as before)

*What you need to do:*
1. Load movie data from the file
2. Transform it (filter, sort, aggregate)
3. Save the results to **new CSV files**
4. Saved files must be re-loadable (round-trip test!)

*Constraints you must follow:*
- ❌ No `import csv` — write it manually
- ❌ No `import pandas`
- ❌ No `sorted()` function (in `save_top_n`) — sort manually
- ❌ No dictionaries (`dict`) — use lists only
- ✅ Use `open("w")`, `f.write()`, f-strings
- ✅ `try`/`except` allowed (you'll need it in one function)
- ✅ Reuse your `load_ratings` from last session

## 💡 Quick File-Writing Primer

```python
with open("hello.csv", "w", encoding="utf-8") as f:
    f.write("name,age\n")           # header — newline by hand!
    f.write("Alice,30\n")
    f.write("Bob,25\n")
```

Use f-strings to interpolate variables:
```python
name = "Charlie"
age = 28
f.write(f"{name},{age}\n")
```

> ⚠️ **Easy to forget:** Unlike `print()`, `f.write()` does NOT add a newline automatically. Always put `\n` at the end!

## ✅ Your Task

Write these 6 functions:

```python
def load_ratings(file_path: str) -> list:
    """Reuse from last session."""
    pass

def save_ratings(ratings: list, file_path: str) -> None:
    """Save a movie list to a CSV file (including header)."""
    pass

def save_filtered_by_genre(ratings: list, genre: str, file_path: str) -> int:
    """Filter by genre, save, and return the count saved."""
    pass

def save_top_n(ratings: list, n: int, file_path: str) -> int:
    """Save the top N movies by rating. No sorted() allowed!"""
    pass

def save_summary_report(ratings: list, file_path: str) -> int:
    """Save genre-level counts and average ratings.
       Returns: the number of genres summarized."""
    pass

def load_ratings_safe(file_path: str) -> list:
    """Return [] if file doesn't exist (don't crash!).
       Use try/except."""
    pass
```

**Tips to get you started:**
- Finish `save_ratings` first — you can reuse it inside the other functions!
- For `save_top_n`: "find the max → append to result → remove from source," repeat N times (selection sort)
- For `save_summary_report`: instead of a dict, use **parallel lists** (`genres = []`, `counts = []`, `totals = []`)
- Handle `n` being larger than the movie count safely (slice with `[:n]`)

## 🎪 Test Your Code

```python
ratings = load_ratings("movie_ratings.csv")

# Test 1: Full save (round-trip check)
save_ratings(ratings, "all_movies.csv")
reloaded = load_ratings("all_movies.csv")
print(f"Round-trip OK: {reloaded == ratings}")
# Expected: Round-trip OK: True

# Test 2: Genre filter save
count = save_filtered_by_genre(ratings, "Drama", "drama.csv")
print(f"Saved {count} Drama movies")
# Expected: Saved 3 Drama movies

# Test 3: TOP 3 save
n = save_top_n(ratings, 3, "top3.csv")
print(f"Saved TOP {n}")
top = load_ratings("top3.csv")
for movie in top:
    print(f"  - {movie[0]}: {movie[3]}")
# Expected:
#   - The Shawshank Redemption: 9.3
#   - The Dark Knight: 9.0
#   - Forrest Gump: 8.8  (or Inception, both are 8.8)

# Test 4: Genre summary
n_genres = save_summary_report(ratings, "summary.csv")
print(f"Summarized {n_genres} genres")
with open("summary.csv", "r", encoding="utf-8") as f:
    print(f.read())
# Expected:
# genre,count,average_rating
# Drama,3,8.87
# Action,3,8.83
# ...

# Test 5: Safe loading
data = load_ratings_safe("does_not_exist.csv")
print(f"Missing file handled: {data}")
# Expected: Missing file handled: []

# Test 6: Edge cases
save_ratings([], "empty.csv")
save_top_n(ratings, 100, "top100.csv")  # n > total movies
print(f"TOP 100 requested: actually saved {len(load_ratings('top100.csv'))}")
# Expected: TOP 100 requested: actually saved 12
```

## 🤔 Think About It

Before coding, consider:
1. What happens if you open an existing file with `open(path, "w")`? Is data preserved?
2. What if you forget the header line? What breaks when `load_ratings` reads it back?
3. If a title contains a comma (e.g., `"Crazy, Stupid, Love"`), could your saved CSV become corrupted?
4. If a rating is `8.876543`, how can you save it shortened (e.g., `8.88`)? Look up f-string format specifiers.

## 🎁 Bonus Challenges

After completing the core functions:

### 🥉 Easy: Save by year
Save only movies released in a specific year.
```python
def save_by_year(ratings: list, year: int, file_path: str) -> int:
    pass
```

### 🥈 Medium: Threshold save + empty-result guard
Save movies above a rating threshold, but **don't create a file** if no movies match.
```python
def save_above_threshold(ratings: list, threshold: float, file_path: str) -> bool:
    """Returns True if saved, False if no movies matched (no file created)."""
    pass
```

### 🥇 Hard: Multi-file split
Save **each genre to its own file**. E.g., Drama → `drama.csv`, Action → `action.csv`. You don't know in advance which genres exist.
```python
def save_by_genre_split(ratings: list, output_dir: str = ".") -> list:
    """Save each genre to a separate file.
       Returns: list of file paths created."""
    pass
```
> 💭 **Hint:** First find all unique genres, then call `save_filtered_by_genre` for each. Filename pattern: `f"{output_dir}/{genre.lower()}.csv"`.

Good luck! 🚀

> *"Data scientists spend 80% of their time cleaning data, and the other 20% complaining about cleaning data."*
> — Industry adage
