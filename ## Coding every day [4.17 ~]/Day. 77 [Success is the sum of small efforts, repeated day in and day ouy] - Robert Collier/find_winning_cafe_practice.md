# 🐍 파이썬 연습: 오늘의 카페 투표 집계 — 딕셔너리로 개수 세기!

> *"우리는 반복적으로 행하는 것의 결과다. 그러므로 탁월함은 행위가 아니라 습관이다."*
> — 윌 듀런트 (Will Durant), *철학 이야기*
> *(아리스토텔레스의 생각을 정리한 문장으로, 흔히 아리스토텔레스의 말로 잘못 알려져 있어요!)*

여러분, 안녕하세요! 기말고사가 다가오고 있어요. 마지막까지 꾸준히 연습하는 습관이 실력을 만듭니다. 오늘은 *딕셔너리로 개수를 세는(frequency counting)* 핵심 기법을 익혀봅시다. 💪

## 🎯 미션

우리 스터디 동아리는 매일 아침 어느 카페에서 모일지 **투표**로 정해요. 각 멤버가 카페 이름을 하나씩 투표하면, 여러분은 그 표를 집계해서 **과반수(절반 초과)** 의 표를 받은 카페를 찾아야 합니다.

여러분의 임무: 투표 리스트를 받아, 전체의 절반을 **넘는** 표를 받은 카페 이름을 반환하세요.

## 📋 규칙

*주어지는 것:*
- `votes`라는 리스트 (각 원소는 멤버가 투표한 카페 이름 문자열)

*해야 할 일:*
1. 각 카페가 몇 표를 받았는지 딕셔너리로 집계
2. 전체 투표 수의 절반을 **초과**하는 표를 받은 카페를 찾기
3. 그 카페 이름을 반환
4. 과반 카페가 항상 하나 존재한다고 가정 (기본 과제)

*제약사항:*
- **딕셔너리로 개수를 세세요!** `list.count()`를 반복 호출하지 마세요
- "절반 초과"는 `> 전체/2` 입니다 (정확히 절반은 과반이 아니에요!)

## 💡 예제

**예제 1:**
```
입력: votes = ["블루보틀", "블루보틀", "그린빈"]
출력: "블루보틀"
```
왜? 블루보틀이 2표, 전체 3표의 절반(1.5)을 넘으니까요.

**예제 2:**
```
입력: votes = ["A", "B", "A", "C", "A", "A"]
출력: "A"
```
왜? A가 4표, 전체 6표의 절반(3)을 넘으니까요.

**예제 3:**
```
입력: votes = ["더블유"]
출력: "더블유"
```
왜? 한 표뿐이고, 그것이 전체의 절반(0.5)을 넘으니까요.

## 🎓 알아야 할 것

코딩을 시작하기 전에, 다음을 이해하고 있는지 확인하세요:
- 딕셔너리에 값을 추가/갱신하는 방법 (`my_dict[key] = value`)
- 키가 딕셔너리에 있는지 확인하는 방법 (`key in my_dict`)
- 딕셔너리의 키들을 반복하는 방법 (`for key in my_dict:`)
- 리스트의 길이를 구하는 방법 (`len(...)`)

## ✅ 과제

다음 시그니처로 함수를 작성하세요:
```python
def find_winning_cafe(votes: list[str]) -> str:
    # 여기에 코드 작성
    pass
```

**핵심 아이디어 (개수 세기 패턴):**
- 빈 딕셔너리 `counts`를 만드세요. `{카페이름: 표수}` 형태입니다.
- 투표를 하나씩 보면서: 이미 딕셔너리에 있으면 표수에 1을 더하고, 없으면 1로 시작하세요.
- 다 세었으면, 딕셔너리를 훑으며 표수가 `len(votes) / 2`를 넘는 카페를 찾으세요.

## 🎪 코드 테스트

```python
# 테스트 1
print(find_winning_cafe(["블루보틀", "블루보틀", "그린빈"]))
# 예상: 블루보틀

# 테스트 2
print(find_winning_cafe(["A", "B", "A", "C", "A", "A"]))
# 예상: A

# 테스트 3
print(find_winning_cafe(["더블유"]))
# 예상: 더블유
```

## 🌟 보너스 도전 과제

기본 과제를 끝냈다면, 도전해보세요!

- 🥉 **(쉬움)** 과반 카페가 없으면 `None`을 반환하도록 수정해보세요.
- 🥈 **(중간)** 과반이 아니라, 가장 많은 표를 받은 카페(최다 득표)를 반환해보세요. (동점이면 아무거나 OK)
- 🥇 **(어려움)** 🔮 *개념 미리보기:* 표가 많은 순서대로 정렬된 `(카페, 표수)` 리스트를 반환해보세요. (힌트: `sorted()`와 정렬 키)

## 🤔 생각해보기

코딩을 시작하기 전에, 접근 방법을 스케치해보세요:
1. 왜 `list.count()`를 반복해서 쓰는 것보다 딕셔너리 한 번이 더 좋을까요?
2. 새 카페를 처음 볼 때와 이미 본 카페일 때, 처리가 어떻게 달라야 할까요?
3. "절반 초과"와 "절반 이상"은 어떻게 다를까요? 왜 이 차이가 중요할까요?

막히면 스레드에 질문을 남겨주세요. 마지막까지 함께 달려봅시다! 🚀

---
---

# 🐍 Python Practice: Tally the "Café of the Day" Vote — Counting with Dictionaries!

> *"We are what we repeatedly do. Excellence, then, is not an act, but a habit."*
> — Will Durant, *The Story of Philosophy*
> *(A summary of Aristotle's idea — often misattributed directly to Aristotle himself!)*

Hey team! The final exam is approaching. The habit of steady practice right up to the end is what builds real skill. Today we'll master a core technique: *frequency counting* with dictionaries. 💪

## 🎯 Your Mission

Our study club votes every morning on which café to meet at. Each member votes for one café name, and your job is to tally the votes and find the café that received a **majority** (more than half) of the votes.

Your job: take a list of votes and return the name of the café that got **more than half** the votes.

## 📋 The Rules

*What you're given:*
- A list `votes` (each item is a string: the café a member voted for)

*What you need to do:*
1. Count how many votes each café received, using a dictionary
2. Find the café whose count is **more than** half the total votes
3. Return that café's name
4. Assume a majority café always exists (for the core task)

*Constraints:*
- **Count using a dictionary!** Don't repeatedly call `list.count()`
- "More than half" means `> total/2` (exactly half is NOT a majority!)

## 💡 Example Time

**Example 1:**
```
Input: votes = ["Blue Bottle", "Blue Bottle", "Green Bean"]
Output: "Blue Bottle"
```
Why? Blue Bottle has 2 votes, more than half of 3 (which is 1.5).

**Example 2:**
```
Input: votes = ["A", "B", "A", "C", "A", "A"]
Output: "A"
```
Why? A has 4 votes, more than half of 6 (which is 3).

**Example 3:**
```
Input: votes = ["W Collection"]
Output: "W Collection"
```
Why? Just one vote, and it's more than half of 1 (which is 0.5).

## 🎓 What You Should Know

Before you start coding, make sure you understand:
- How to add/update a value in a dictionary (`my_dict[key] = value`)
- How to check if a key is in a dictionary (`key in my_dict`)
- How to loop over a dictionary's keys (`for key in my_dict:`)
- How to get the length of a list (`len(...)`)

## ✅ Your Task

Write a function with this signature:
```python
def find_winning_cafe(votes: list[str]) -> str:
    # Your code here
    pass
```

**The key idea (the counting pattern):**
- Make an empty dictionary `counts`, shaped as `{cafe_name: vote_count}`.
- Walk through the votes one by one: if a café is already in the dictionary, add 1 to its count; if not, start it at 1.
- Once counted, scan the dictionary for the café whose count is greater than `len(votes) / 2`.

## 🎪 Test Your Code

```python
# Test 1
print(find_winning_cafe(["Blue Bottle", "Blue Bottle", "Green Bean"]))
# Expected: Blue Bottle

# Test 2
print(find_winning_cafe(["A", "B", "A", "C", "A", "A"]))
# Expected: A

# Test 3
print(find_winning_cafe(["W Collection"]))
# Expected: W Collection
```

## 🌟 Bonus Challenges

Finished the core task? Push further!

- 🥉 **(Easy)** Modify it to return `None` when no café has a majority.
- 🥈 **(Medium)** Instead of a majority, return the café with the most votes (a plurality). Ties can return any of the top.
- 🥇 **(Hard)** 🔮 *Concept preview:* Return a list of `(cafe, count)` sorted from most to fewest votes. (Hint: `sorted()` with a sort key.)

## 🤔 Think About It

Before you start coding, sketch out your approach:
1. Why is one dictionary pass better than repeatedly calling `list.count()`?
2. How should handling differ between seeing a café for the first time vs. one you've already counted?
3. How is "more than half" different from "at least half"? Why does this difference matter?

Drop your questions in the thread if you get stuck. Let's run all the way to the finish together! 🚀
