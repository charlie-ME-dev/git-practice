# 🎬 Python 연습: 영화 평점 데이터 분석하기!

여러분, 안녕하세요! 오늘은 진짜 데이터 과학자처럼 일해봅시다.

## 🎯 미션

여러분은 한 영화 스트리밍 스타트업의 신입 데이터 분석가입니다. CEO가 회의에서 "우리 카탈로그 영화들 평점 좀 빠르게 분석해줄 수 있어요?"라고 물어봤어요. 데이터는 `movie_ratings.csv`라는 CSV 파일로 주어졌습니다.

여러분의 임무는 이 파일을 읽고, 데이터를 정리하고, 몇 가지 핵심 질문에 답하는 함수들을 작성하는 것입니다 — **`csv` 모듈 같은 외부 라이브러리 없이**, 여러분이 배운 문자열 메서드만 사용해서요!

## 📋 데이터 형식

`movie_ratings.csv` 파일은 다음과 같이 생겼습니다:

```
title,genre,year,rating
The Shawshank Redemption,Drama,1994,9.3
The Dark Knight,Action,2008,9.0
Parasite,Thriller,2019,8.6
...
```

각 줄(첫 번째 줄 제외)은 한 영화를 나타내며, 콤마로 구분된 4개의 필드를 가집니다:
- **title**: 영화 제목 (문자열)
- **genre**: 장르 (문자열)
- **year**: 개봉 연도 (정수)
- **rating**: 평점 (실수, 0.0 ~ 10.0)

## 📐 규칙

*주어지는 것:*
- `movie_ratings.csv` 파일

*해야 할 일:*
1. 파일을 열고 한 줄씩 읽기
2. 첫 번째 줄(헤더)은 건너뛰기
3. 각 줄을 `.split(",")`로 나누기
4. `year`는 정수로, `rating`은 실수로 변환
5. 각 영화를 `[title, genre, year, rating]` 형태의 리스트로 저장

*반드시 따라야 할 제약사항:*
- ❌ `import csv` 금지 — 직접 파싱해야 합니다
- ❌ `import pandas` 금지
- ❌ `sum()`, `max()`, `min()` 등의 내장 단축 함수를 평점 계산에 사용 금지
- ✅ `open()`, `with`, `.split()`, `.strip()`, `int()`, `float()`, `len()` 사용 가능
- ✅ `for` 반복문, `if`문, 리스트 메서드 사용 가능

## 💡 예제

**예제 1: 파일 로딩**
```python
ratings = load_ratings("movie_ratings.csv")
print(ratings[0])
# 예상: ['The Shawshank Redemption', 'Drama', 1994, 9.3]
print(type(ratings[0][2]))  # year는 정수여야 함
# 예상: <class 'int'>
print(type(ratings[0][3]))  # rating은 실수여야 함
# 예상: <class 'float'>
```

**예제 2: 평균 평점**
```python
ratings = load_ratings("movie_ratings.csv")
avg = average_rating(ratings)
print(f"{avg:.2f}")
# 예상: 8.65
```

**예제 3: 장르 필터링**
```python
drama_movies = filter_by_genre(ratings, "Drama")
print(len(drama_movies))
# 예상: 3
```

## 🎓 알아야 할 것

시작하기 전에, 다음 개념들을 확인하세요:
- `open()`과 `with` 구문으로 파일 열기
- `.readlines()` 또는 `for line in file`로 줄 읽기
- `.strip()`으로 개행 문자 제거하기
- `.split(",")`로 문자열을 리스트로 나누기
- `int()`와 `float()`로 타입 변환하기
- 리스트의 리스트(2차원 리스트) 다루기

## ✅ 과제

다음 6개의 함수를 작성하세요:

```python
def load_ratings(file_path: str) -> list:
    """CSV 파일을 읽어서 [title, genre, year, rating] 리스트의 리스트를 반환합니다."""
    pass

def count_movies(ratings: list) -> int:
    """영화의 총 개수를 반환합니다. (len() 사용 가능)"""
    pass

def average_rating(ratings: list) -> float:
    """전체 영화의 평균 평점을 반환합니다. 리스트가 비어 있으면 0.0을 반환합니다."""
    pass

def highest_rated(ratings: list) -> str:
    """가장 높은 평점을 가진 영화의 제목을 반환합니다. 리스트가 비어 있으면 None을 반환합니다."""
    pass

def filter_by_genre(ratings: list, genre: str) -> list:
    """주어진 장르와 일치하는 영화들의 리스트를 반환합니다."""
    pass

def count_above_threshold(ratings: list, threshold: float) -> int:
    """평점이 threshold 이상인 영화의 개수를 반환합니다."""
    pass
```

**시작하는 데 도움이 될 팁:**
- 헤더 줄은 `lines[1:]`로 건너뛰거나, 카운터를 사용해서 첫 줄을 무시하세요
- 각 줄 끝에는 `\n`이 붙어 있을 수 있으니 `.strip()`을 잊지 마세요
- 빈 줄(`""`)이 있을 수 있으니 처리해주세요
- `highest_rated`는 첫 번째 영화를 "현재 최고"로 초기화한 뒤 비교해 나가세요

## 🎪 코드 테스트

```python
ratings = load_ratings("movie_ratings.csv")

# 테스트 1: 로딩
print(f"총 영화 수: {count_movies(ratings)}")
# 예상: 12

# 테스트 2: 평균
print(f"평균 평점: {average_rating(ratings):.2f}")
# 예상: 8.65

# 테스트 3: 최고 평점 영화
print(f"최고 평점 영화: {highest_rated(ratings)}")
# 예상: The Shawshank Redemption

# 테스트 4: 장르별 필터링
action = filter_by_genre(ratings, "Action")
print(f"액션 영화 수: {len(action)}")
# 예상: 3

# 테스트 5: 임계값 이상 카운트
print(f"평점 8.5 이상: {count_above_threshold(ratings, 8.5)}편")
# 예상: 9편
print(f"평점 9.0 이상: {count_above_threshold(ratings, 9.0)}편")
# 예상: 2편

# 테스트 6: 빈 리스트 처리
print(f"빈 리스트 평균: {average_rating([])}")
# 예상: 0.0
print(f"빈 리스트 최고: {highest_rated([])}")
# 예상: None
```

## 🤔 생각해보기

코딩을 시작하기 전에, 다음 질문들을 생각해보세요:
1. 만약 영화 제목에 콤마가 포함되어 있다면 어떻게 될까요? (예: `"Crazy, Stupid, Love"`) — `.split(",")`는 잘 동작할까요?
2. 평점이 문자열로 저장되어 있다면, 왜 `float()`로 변환해야 할까요? 변환하지 않으면 어떤 문제가 생길까요?
3. `with open()`과 그냥 `open()`의 차이점은 무엇일까요?
4. 만약 데이터가 100만 줄이라면, `readlines()` 방식과 `for line in file` 방식 중 어느 쪽이 더 효율적일까요?

## 🎁 보너스 도전

핵심 함수를 모두 완성한 후 시도해보세요:

### 🥉 Easy: 연도별 카운트
특정 연도에 개봉한 영화의 개수를 반환하는 함수를 작성하세요.
```python
def count_by_year(ratings: list, year: int) -> int:
    pass
```

### 🥈 Medium: 최저 평점
가장 낮은 평점을 가진 영화의 제목을 반환하는 함수를 작성하세요. (`min()` 사용 금지!)
```python
def lowest_rated(ratings: list) -> str:
    pass
```

### 🥇 Hard: `csv` 모듈 미리보기
Python에는 `csv`라는 표준 라이브러리가 있어서 콤마가 포함된 제목도 안전하게 처리할 수 있습니다. 다음 코드를 연구해보고, 위에서 만든 `load_ratings`와 결과를 비교해보세요:

```python
import csv

def load_ratings_with_csv(file_path):
    ratings = []
    with open(file_path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)  # 헤더 건너뛰기
        for row in reader:
            ratings.append([row[0], row[1], int(row[2]), float(row[3])])
    return ratings
```

> 💭 **질문:** 만약 제목이 `"Crazy, Stupid, Love"`처럼 콤마를 포함하고 CSV에서 따옴표로 감싸져 있다면 (`"Crazy, Stupid, Love",Comedy,2011,7.4`), `csv.reader`는 어떻게 처리할까요? 직접 만든 `.split(",")` 방식과 비교해보세요.

행운을 빕니다! 🚀

---
---

# 🎬 Python Practice: Analyze Movie Ratings Like a Data Analyst!

Hey team! Today we're going to work like real data analysts.

## 🎯 Your Mission

You're a junior data analyst at a movie streaming startup. The CEO just asked in a meeting: "Can you do a quick analysis of the ratings in our catalog?" You've been handed a CSV file called `movie_ratings.csv`.

Your job is to read this file, clean the data, and write functions that answer key questions — **without using any external libraries like the `csv` module**, using only the string methods you've already learned!

## 📋 The Data Format

The `movie_ratings.csv` file looks like this:

```
title,genre,year,rating
The Shawshank Redemption,Drama,1994,9.3
The Dark Knight,Action,2008,9.0
Parasite,Thriller,2019,8.6
...
```

Each line (except the first) represents one movie, with 4 comma-separated fields:
- **title**: Movie title (string)
- **genre**: Genre (string)
- **year**: Release year (integer)
- **rating**: Rating (float, 0.0–10.0)

## 📐 The Rules

*What you're given:*
- A file called `movie_ratings.csv`

*What you need to do:*
1. Open the file and read it line by line
2. Skip the first line (header)
3. Split each line with `.split(",")`
4. Convert `year` to an integer, `rating` to a float
5. Store each movie as a list: `[title, genre, year, rating]`

*Constraints you must follow:*
- ❌ No `import csv` — you must parse manually
- ❌ No `import pandas`
- ❌ No built-in shortcut functions (`sum()`, `max()`, `min()`) for rating calculations
- ✅ You CAN use `open()`, `with`, `.split()`, `.strip()`, `int()`, `float()`, `len()`
- ✅ You CAN use `for` loops, `if` statements, list methods

## 💡 Examples

**Example 1: Loading the file**
```python
ratings = load_ratings("movie_ratings.csv")
print(ratings[0])
# Expected: ['The Shawshank Redemption', 'Drama', 1994, 9.3]
print(type(ratings[0][2]))  # year should be int
# Expected: <class 'int'>
print(type(ratings[0][3]))  # rating should be float
# Expected: <class 'float'>
```

**Example 2: Average rating**
```python
ratings = load_ratings("movie_ratings.csv")
avg = average_rating(ratings)
print(f"{avg:.2f}")
# Expected: 8.65
```

**Example 3: Genre filtering**
```python
drama_movies = filter_by_genre(ratings, "Drama")
print(len(drama_movies))
# Expected: 3
```

## 🎓 What You Should Know

Before you start, make sure you're comfortable with:
- Opening files with `open()` and the `with` statement
- Reading lines using `.readlines()` or `for line in file`
- Removing newline characters with `.strip()`
- Splitting strings into lists with `.split(",")`
- Type conversion with `int()` and `float()`
- Working with lists of lists (2D lists)

## ✅ Your Task

Write the following 6 functions:

```python
def load_ratings(file_path: str) -> list:
    """Read CSV file and return a list of [title, genre, year, rating] lists."""
    pass

def count_movies(ratings: list) -> int:
    """Return the total number of movies. (len() allowed)"""
    pass

def average_rating(ratings: list) -> float:
    """Return the average rating across all movies. Return 0.0 if the list is empty."""
    pass

def highest_rated(ratings: list) -> str:
    """Return the title of the highest-rated movie. Return None if the list is empty."""
    pass

def filter_by_genre(ratings: list, genre: str) -> list:
    """Return a list of movies matching the given genre."""
    pass

def count_above_threshold(ratings: list, threshold: float) -> int:
    """Return the count of movies with rating >= threshold."""
    pass
```

**Tips to get you started:**
- Skip the header line with `lines[1:]` or use a counter to ignore the first line
- Each line may end with `\n`, so don't forget `.strip()`
- There might be empty lines (`""`) — handle them too
- For `highest_rated`, initialize "current best" with the first movie, then compare

## 🎪 Test Your Code

```python
ratings = load_ratings("movie_ratings.csv")

# Test 1: Loading
print(f"Total movies: {count_movies(ratings)}")
# Expected: 12

# Test 2: Average
print(f"Average rating: {average_rating(ratings):.2f}")
# Expected: 8.65

# Test 3: Highest-rated movie
print(f"Top movie: {highest_rated(ratings)}")
# Expected: The Shawshank Redemption

# Test 4: Genre filter
action = filter_by_genre(ratings, "Action")
print(f"Action movies: {len(action)}")
# Expected: 3

# Test 5: Threshold count
print(f"Rated 8.5+: {count_above_threshold(ratings, 8.5)} movies")
# Expected: 9 movies
print(f"Rated 9.0+: {count_above_threshold(ratings, 9.0)} movies")
# Expected: 2 movies

# Test 6: Empty list handling
print(f"Empty avg: {average_rating([])}")
# Expected: 0.0
print(f"Empty top: {highest_rated([])}")
# Expected: None
```

## 🤔 Think About It

Before you start coding, consider these questions:
1. What if a movie title contains a comma (e.g., `"Crazy, Stupid, Love"`)? Will `.split(",")` work?
2. If a rating is stored as a string, why must you convert it with `float()`? What breaks if you don't?
3. What's the difference between `with open()` and just `open()`?
4. If the dataset had 1 million rows, would `readlines()` or `for line in file` be more efficient?

## 🎁 Bonus Challenges

Try these after completing the core functions:

### 🥉 Easy: Count by year
Write a function that returns the number of movies released in a specific year.
```python
def count_by_year(ratings: list, year: int) -> int:
    pass
```

### 🥈 Medium: Lowest-rated
Write a function that returns the title of the lowest-rated movie. (No `min()` allowed!)
```python
def lowest_rated(ratings: list) -> str:
    pass
```

### 🥇 Hard: Preview of the `csv` module
Python has a standard library called `csv` that handles commas inside titles safely. Study the code below and compare its results with your manual `load_ratings`:

```python
import csv

def load_ratings_with_csv(file_path):
    ratings = []
    with open(file_path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)  # skip header
        for row in reader:
            ratings.append([row[0], row[1], int(row[2]), float(row[3])])
    return ratings
```

> 💭 **Question:** If a title contains a comma like `"Crazy, Stupid, Love"` and is wrapped in quotes in the CSV (`"Crazy, Stupid, Love",Comedy,2011,7.4`), how does `csv.reader` handle it? Compare with your manual `.split(",")` approach.

Good luck! 🚀
