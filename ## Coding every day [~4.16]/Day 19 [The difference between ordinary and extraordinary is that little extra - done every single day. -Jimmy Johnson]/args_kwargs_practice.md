# 🎮 Python 연습: 유연한 함수 만들기 - *args와 **kwargs 마스터하기!

여러분, 안녕하세요! 오늘은 Python의 강력한 기능 중 하나인 **유연한 매개변수**를 배워볼 거예요. 게임 개발자처럼 생각하면서 코딩해봅시다!

## 🎯 미션

여러분은 인기 있는 게임 스튜디오의 주니어 개발자입니다! 🎮 팀에서 캐릭터 커스터마이징 시스템을 만들고 있는데, 문제가 생겼어요. 플레이어마다 원하는 옵션의 개수가 다르고, 옵션 종류도 매번 달라요!

예를 들어:
- 어떤 플레이어는 무기 3개만 선택
- 다른 플레이어는 무기 5개 + 방어구 3개 + 특수 스킬
- 또 다른 플레이어는 완전히 다른 조합!

**매번 새로운 함수를 만들 수는 없잖아요?** 😱 바로 이럴 때 `*args`와 `**kwargs`가 필요합니다!

## 📚 개념 설명

### 🌟 *args (별표 하나)
"arguments"의 줄임말로, **개수를 모르는 위치 인자**들을 받을 때 사용해요.

```python
def collect_weapons(*args):
    print(f"수집한 무기 개수: {len(args)}")
    for weapon in args:
        print(f"  - {weapon}")

collect_weapons("검", "활")  # 2개도 OK!
collect_weapons("검", "활", "지팡이", "도끼")  # 4개도 OK!
```

**핵심 포인트:**
- `args`는 튜플(tuple)로 받아집니다
- 원하는 만큼 인자를 전달할 수 있어요
- 순서가 중요합니다

### 🌟 **kwargs (별표 두 개)
"keyword arguments"의 줄임말로, **개수를 모르는 키워드 인자**들을 받을 때 사용해요.

```python
def create_character(**kwargs):
    print("캐릭터 정보:")
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

create_character(name="전사", level=5, hp=100)
create_character(name="마법사", level=3, mp=150, special_skill="파이어볼")
```

**핵심 포인트:**
- `kwargs`는 딕셔너리(dictionary)로 받아집니다
- 키=값 형태로 전달합니다
- 순서는 상관없어요

### 🔥 둘 다 사용하기!
```python
def super_function(required_arg, *args, **kwargs):
    # required_arg: 필수 매개변수
    # args: 추가 위치 인자들
    # kwargs: 추가 키워드 인자들
    pass
```

**순서 규칙 (꼭 기억!):**
1. 일반 매개변수
2. *args
3. **kwargs

## 💡 예제로 이해하기

### 예제 1: 점수 계산기
```python
def calculate_total_score(*scores):
    """여러 개의 점수를 받아서 총합 계산"""
    total = sum(scores)
    print(f"총 {len(scores)}개 점수의 합: {total}")
    return total

# 테스트
calculate_total_score(100, 95, 88)  # 3개
calculate_total_score(100, 95, 88, 92, 87)  # 5개
```

### 예제 2: 게임 캐릭터 생성
```python
def create_game_character(name, *skills, **attributes):
    """
    name: 캐릭터 이름 (필수)
    skills: 스킬 목록 (가변)
    attributes: 캐릭터 속성들 (가변)
    """
    print(f"\n캐릭터 '{name}' 생성 완료!")
    
    if skills:
        print(f"스킬: {', '.join(skills)}")
    
    if attributes:
        print("속성:")
        for attr, value in attributes.items():
            print(f"  - {attr}: {value}")

# 테스트
create_game_character(
    "용사 김철수",
    "검술", "방패막기",
    level=10,
    hp=500,
    mp=100,
    attack=85
)
```

## 🎓 알아야 할 것

시작하기 전에 이것들을 이해하고 있어야 해요:
- 함수 정의와 호출 방법
- 튜플(tuple)과 딕셔너리(dictionary) 기본 사용법
- 반복문 (for loop) 사용법
- `.items()`, `.values()`, `.keys()` 메서드

## ✅ 과제 세트

### 🎯 과제 1: 쇼핑 카트
온라인 쇼핑몰의 장바구니 시스템을 만드세요!

```python
def add_to_cart(*items, **item_details):
    """
    items: 상품명들 (위치 인자)
    item_details: 상품별 세부 정보 (키워드 인자)
    
    반환: 총 상품 개수와 상세 정보를 포함한 딕셔너리
    """
    # 여기에 코드 작성
    pass
```

**요구사항:**
- 추가된 모든 상품명을 리스트로 저장
- 각 상품의 세부 정보(가격, 수량 등)를 기록
- 총 상품 개수를 반환
- 상품 정보를 보기 좋게 출력

### 🎯 과제 2: 레스토랑 주문 시스템
다양한 주문을 처리할 수 있는 함수를 만드세요!

```python
def process_order(customer_name, *dishes, **preferences):
    """
    customer_name: 고객 이름 (필수)
    dishes: 주문한 음식들
    preferences: 선호 사항 (매운맛 단계, 알레르기, 특별 요청 등)
    
    반환: 주문 확인 메시지와 예상 조리 시간
    """
    # 여기에 코드 작성
    pass
```

**요구사항:**
- 고객 이름과 주문 음식 목록 출력
- 특별 요청사항이 있으면 강조해서 표시
- 음식 개수에 따라 예상 조리 시간 계산 (음식 1개당 10분)
- 주문 요약 반환

### 🎯 과제 3: 학생 성적 관리
학생의 성적을 유연하게 기록하는 시스템을 만드세요!

```python
def record_grades(student_name, *test_scores, **subject_info):
    """
    student_name: 학생 이름 (필수)
    test_scores: 시험 점수들
    subject_info: 과목별 정보 (과목명, 학점, 선생님 등)
    
    반환: 평균 점수와 성적 정보가 담긴 딕셔너리
    """
    # 여기에 코드 작성
    pass
```

**요구사항:**
- 모든 시험 점수의 평균 계산
- 과목 정보 정리해서 저장
- 평균이 90 이상이면 "우수", 80 이상이면 "양호", 그 외 "보통" 판정
- 결과를 딕셔너리로 반환

## 🎪 코드 테스트

### 과제 1 테스트:
```python
# 테스트 1
result1 = add_to_cart(
    "노트북", "마우스", "키보드",
    laptop_price=1200000,
    mouse_quantity=2,
    keyboard_color="black"
)
print(result1)

# 예상 출력:
# 장바구니에 3개 상품 추가됨
# - 노트북
# - 마우스
# - 키보드
# 상세 정보: laptop_price=1200000, mouse_quantity=2, keyboard_color=black
```

### 과제 2 테스트:
```python
# 테스트 1
order1 = process_order(
    "홍길동",
    "떡볶이", "순대", "튀김",
    spicy_level=3,
    no_onions=True,
    extra_cheese=True
)

# 테스트 2
order2 = process_order(
    "김영희",
    "비빔밥",
    allergies="땅콩",
    extra_vegetables=True
)
```

### 과제 3 테스트:
```python
# 테스트 1
grades1 = record_grades(
    "박민수",
    95, 88, 92, 90,
    subject="Python 프로그래밍",
    semester="2024-2",
    professor="김교수"
)
print(grades1)

# 테스트 2
grades2 = record_grades(
    "이지은",
    78, 82, 85,
    subject="자료구조",
    credits=3
)
print(grades2)
```

## 🔥 보너스 챌린지

### 🌟 레벨 1: 함수 데코레이터 만들기
전달받은 모든 인자를 로깅하는 함수를 만드세요!

```python
def log_function_call(func_name, *args, **kwargs):
    """
    함수 호출 시 모든 인자를 기록
    실제 서비스에서 디버깅할 때 유용해요!
    """
    # 여기에 코드 작성
    pass
```

### 🌟 레벨 2: 다중 언어 인사말
여러 언어로 인사말을 출력하는 함수를 만드세요!

```python
def greet_in_languages(*names, **language_greetings):
    """
    names: 인사할 사람들의 이름
    language_greetings: 언어별 인사말 (예: korean="안녕하세요", english="Hello")
    
    각 이름에 대해 모든 언어로 인사 출력
    """
    # 여기에 코드 작성
    pass

# 테스트
greet_in_languages(
    "철수", "영희",
    korean="안녕하세요",
    english="Hello",
    spanish="Hola"
)
```

### 🌟 레벨 3: API 요청 시뮬레이터
실제 API처럼 작동하는 함수를 만드세요!

```python
def api_request(endpoint, method="GET", *params, **headers):
    """
    endpoint: API 엔드포인트 (필수)
    method: HTTP 메서드 (기본값: GET)
    params: URL 파라미터들
    headers: HTTP 헤더들
    
    요청 정보를 정리해서 딕셔너리로 반환
    """
    # 여기에 코드 작성
    pass
```

## 🤔 생각해보기

코드를 작성하면서 다음 질문들을 생각해보세요:

1. **언제 *args를 사용하는 게 좋을까요?**
   - 힌트: 인자의 개수를 미리 알 수 없을 때!

2. **언제 **kwargs를 사용하는 게 좋을까요?**
   - 힌트: 선택적인 옵션이 많을 때!

3. ***args와 리스트를 매개변수로 받는 것의 차이는?**
   - `def func(*args)` vs `def func(items)`

4. **실제로 어디에 사용될까요?**
   - 예: 프린트 함수 `print()`도 *args를 사용해요!
   - `print("안녕", "하세요", "여러분")` ← 여러 개를 한 번에!

5. **디버깅할 때 어떻게 확인하나요?**
   ```python
   def debug_function(*args, **kwargs):
       print(f"args의 타입: {type(args)}")  # tuple
       print(f"kwargs의 타입: {type(kwargs)}")  # dict
   ```

## 💪 실전 활용 예시

### 실제 활용 1: 로깅 시스템
```python
def log_message(level, *messages, **context):
    """실제 프로그램에서 사용하는 로깅"""
    timestamp = "2024-11-16 10:30:00"
    print(f"[{timestamp}] [{level}]")
    for msg in messages:
        print(f"  {msg}")
    if context:
        print(f"  Context: {context}")
```

### 실제 활용 2: 데이터베이스 쿼리 빌더
```python
def build_query(table_name, *columns, **conditions):
    """SQL 쿼리를 동적으로 생성"""
    cols = ", ".join(columns) if columns else "*"
    query = f"SELECT {cols} FROM {table_name}"
    
    if conditions:
        where_clause = " AND ".join([f"{k}={v}" for k, v in conditions.items()])
        query += f" WHERE {where_clause}"
    
    return query
```

## 📝 제출 전 체크리스트

- [ ] 모든 함수가 snake_case로 작성되었나요?
- [ ] *args와 **kwargs의 순서가 올바른가요?
- [ ] 각 함수에 docstring이 있나요?
- [ ] 테스트 케이스를 모두 통과하나요?
- [ ] 에러 처리를 고려했나요?
- [ ] 코드가 읽기 쉽게 작성되었나요?

## 🎉 마무리

*args와 **kwargs는 처음에는 어려워 보이지만, 익숙해지면 정말 강력한 도구예요! 유연한 함수를 만들 수 있고, 실제 프로젝트에서도 자주 사용됩니다.

**핵심 정리:**
- `*args` → 튜플로 받음, 위치 인자
- `**kwargs` → 딕셔너리로 받음, 키워드 인자
- 순서: 일반 매개변수 → *args → **kwargs

질문이 있으면 언제든지 스레드에 남겨주세요! 함께 배워가요! 🚀

---
---

# 🎮 Python Practice: Building Flexible Functions - Master *args and **kwargs!

Hey team! Today we're diving into one of Python's most powerful features: **flexible parameters**. Let's think like game developers while we code!

## 🎯 Your Mission

You're a junior developer at a popular game studio! 🎮 Your team is building a character customization system, but there's a problem. Different players want different numbers of options, and the option types vary every time!

For example:
- Some players want only 3 weapons
- Others want 5 weapons + 3 armor pieces + special skills
- Yet others want completely different combinations!

**You can't create a new function every time, right?** 😱 This is exactly when you need `*args` and `**kwargs`!

## 📚 Concept Explanation

### 🌟 *args (one star)
Short for "arguments," used to accept **an unknown number of positional arguments**.

```python
def collect_weapons(*args):
    print(f"Weapons collected: {len(args)}")
    for weapon in args:
        print(f"  - {weapon}")

collect_weapons("sword", "bow")  # 2 is OK!
collect_weapons("sword", "bow", "staff", "axe")  # 4 is OK too!
```

**Key Points:**
- `args` is received as a tuple
- You can pass as many arguments as you want
- Order matters

### 🌟 **kwargs (two stars)
Short for "keyword arguments," used to accept **an unknown number of keyword arguments**.

```python
def create_character(**kwargs):
    print("Character Info:")
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

create_character(name="Warrior", level=5, hp=100)
create_character(name="Mage", level=3, mp=150, special_skill="Fireball")
```

**Key Points:**
- `kwargs` is received as a dictionary
- Pass as key=value pairs
- Order doesn't matter

### 🔥 Using Both Together!
```python
def super_function(required_arg, *args, **kwargs):
    # required_arg: mandatory parameter
    # args: additional positional arguments
    # kwargs: additional keyword arguments
    pass
```

**Order Rule (Remember this!):**
1. Regular parameters
2. *args
3. **kwargs

## 💡 Learning Through Examples

### Example 1: Score Calculator
```python
def calculate_total_score(*scores):
    """Accept multiple scores and calculate total"""
    total = sum(scores)
    print(f"Sum of {len(scores)} scores: {total}")
    return total

# Test
calculate_total_score(100, 95, 88)  # 3 scores
calculate_total_score(100, 95, 88, 92, 87)  # 5 scores
```

### Example 2: Game Character Creation
```python
def create_game_character(name, *skills, **attributes):
    """
    name: character name (required)
    skills: skill list (variable)
    attributes: character attributes (variable)
    """
    print(f"\nCharacter '{name}' created!")
    
    if skills:
        print(f"Skills: {', '.join(skills)}")
    
    if attributes:
        print("Attributes:")
        for attr, value in attributes.items():
            print(f"  - {attr}: {value}")

# Test
create_game_character(
    "Hero Kim",
    "Swordsmanship", "Shield Block",
    level=10,
    hp=500,
    mp=100,
    attack=85
)
```

## 🎓 Prerequisites

Before starting, you should understand:
- How to define and call functions
- Basic usage of tuples and dictionaries
- How to use for loops
- Methods like `.items()`, `.values()`, `.keys()`

## ✅ Assignment Set

### 🎯 Assignment 1: Shopping Cart
Create a shopping cart system for an online store!

```python
def add_to_cart(*items, **item_details):
    """
    items: product names (positional arguments)
    item_details: detailed product information (keyword arguments)
    
    Returns: dictionary containing total item count and details
    """
    # Your code here
    pass
```

**Requirements:**
- Store all product names in a list
- Record details for each product (price, quantity, etc.)
- Return total item count
- Display product information in a readable format

### 🎯 Assignment 2: Restaurant Order System
Create a function that can handle various orders!

```python
def process_order(customer_name, *dishes, **preferences):
    """
    customer_name: customer's name (required)
    dishes: ordered dishes
    preferences: preferences (spice level, allergies, special requests, etc.)
    
    Returns: order confirmation message and estimated cooking time
    """
    # Your code here
    pass
```

**Requirements:**
- Display customer name and list of ordered dishes
- Highlight any special requests
- Calculate estimated cooking time based on number of dishes (10 minutes per dish)
- Return order summary

### 🎯 Assignment 3: Student Grade Management
Create a system to flexibly record student grades!

```python
def record_grades(student_name, *test_scores, **subject_info):
    """
    student_name: student's name (required)
    test_scores: test scores
    subject_info: subject information (subject name, credits, teacher, etc.)
    
    Returns: dictionary containing average score and grade information
    """
    # Your code here
    pass
```

**Requirements:**
- Calculate average of all test scores
- Organize and store subject information
- Grade: "Excellent" if average ≥ 90, "Good" if ≥ 80, otherwise "Average"
- Return results as a dictionary

## 🎪 Test Your Code

### Assignment 1 Tests:
```python
# Test 1
result1 = add_to_cart(
    "laptop", "mouse", "keyboard",
    laptop_price=1200000,
    mouse_quantity=2,
    keyboard_color="black"
)
print(result1)

# Expected output:
# 3 items added to cart
# - laptop
# - mouse
# - keyboard
# Details: laptop_price=1200000, mouse_quantity=2, keyboard_color=black
```

### Assignment 2 Tests:
```python
# Test 1
order1 = process_order(
    "Hong Gildong",
    "tteokbokki", "sundae", "fried food",
    spicy_level=3,
    no_onions=True,
    extra_cheese=True
)

# Test 2
order2 = process_order(
    "Kim Younghee",
    "bibimbap",
    allergies="peanuts",
    extra_vegetables=True
)
```

### Assignment 3 Tests:
```python
# Test 1
grades1 = record_grades(
    "Park Minsu",
    95, 88, 92, 90,
    subject="Python Programming",
    semester="2024-2",
    professor="Prof. Kim"
)
print(grades1)

# Test 2
grades2 = record_grades(
    "Lee Jieun",
    78, 82, 85,
    subject="Data Structures",
    credits=3
)
print(grades2)
```

## 🔥 Bonus Challenges

### 🌟 Level 1: Function Decorator Creator
Create a function that logs all received arguments!

```python
def log_function_call(func_name, *args, **kwargs):
    """
    Logs all arguments when function is called
    Very useful for debugging in real services!
    """
    # Your code here
    pass
```

### 🌟 Level 2: Multi-language Greetings
Create a function that outputs greetings in multiple languages!

```python
def greet_in_languages(*names, **language_greetings):
    """
    names: names of people to greet
    language_greetings: greetings by language (e.g., korean="안녕하세요", english="Hello")
    
    Output greeting in all languages for each name
    """
    # Your code here
    pass

# Test
greet_in_languages(
    "Chulsoo", "Younghee",
    korean="안녕하세요",
    english="Hello",
    spanish="Hola"
)
```

### 🌟 Level 3: API Request Simulator
Create a function that works like a real API!

```python
def api_request(endpoint, method="GET", *params, **headers):
    """
    endpoint: API endpoint (required)
    method: HTTP method (default: GET)
    params: URL parameters
    headers: HTTP headers
    
    Returns request information organized as a dictionary
    """
    # Your code here
    pass
```

## 🤔 Think About It

While writing your code, think about these questions:

1. **When is it good to use *args?**
   - Hint: When you don't know the number of arguments in advance!

2. **When is it good to use **kwargs?**
   - Hint: When there are many optional options!

3. **What's the difference between *args and receiving a list as a parameter?**
   - `def func(*args)` vs `def func(items)`

4. **Where is this used in real life?**
   - Example: The print function `print()` also uses *args!
   - `print("Hello", "there", "everyone")` ← Multiple at once!

5. **How do you check during debugging?**
   ```python
   def debug_function(*args, **kwargs):
       print(f"Type of args: {type(args)}")  # tuple
       print(f"Type of kwargs: {type(kwargs)}")  # dict
   ```

## 💪 Real-World Applications

### Real Application 1: Logging System
```python
def log_message(level, *messages, **context):
    """Logging used in actual programs"""
    timestamp = "2024-11-16 10:30:00"
    print(f"[{timestamp}] [{level}]")
    for msg in messages:
        print(f"  {msg}")
    if context:
        print(f"  Context: {context}")
```

### Real Application 2: Database Query Builder
```python
def build_query(table_name, *columns, **conditions):
    """Dynamically generate SQL queries"""
    cols = ", ".join(columns) if columns else "*"
    query = f"SELECT {cols} FROM {table_name}"
    
    if conditions:
        where_clause = " AND ".join([f"{k}={v}" for k, v in conditions.items()])
        query += f" WHERE {where_clause}"
    
    return query
```

## 📝 Pre-Submission Checklist

- [ ] Are all functions written in snake_case?
- [ ] Is the order of *args and **kwargs correct?
- [ ] Does each function have a docstring?
- [ ] Do all test cases pass?
- [ ] Did you consider error handling?
- [ ] Is the code written to be readable?

## 🎉 Wrap Up

*args and **kwargs may seem difficult at first, but once you get used to them, they're really powerful tools! You can create flexible functions and they're frequently used in real projects.

**Key Summary:**
- `*args` → Received as tuple, positional arguments
- `**kwargs` → Received as dictionary, keyword arguments
- Order: Regular parameters → *args → **kwargs

If you have questions, drop them in the thread anytime! Let's learn together! 🚀
