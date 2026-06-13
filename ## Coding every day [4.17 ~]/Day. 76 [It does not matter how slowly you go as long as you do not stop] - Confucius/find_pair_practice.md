# 🐍 파이썬 연습: 짝꿍 찾기 — 딕셔너리 활용!

> *"혼자서는 작은 일밖에 할 수 없지만, 함께라면 큰 일을 해낼 수 있다."*
> — 헬렌 켈러 (Helen Keller)

여러분, 안녕하세요! 이번에는 *딕셔너리(dictionary)* 를 활용한 실전 문제로 실력을 키워봅시다.

## 🎯 미션

여러분은 동아리 스터디 모임을 운영하고 있어요. 각 멤버마다 일주일에 비어 있는 *자유 시간(시간 단위)* 이 정해져 있습니다. 스터디 한 세션을 진행하려면 정확히 `목표 시간`만큼의 시간이 필요해요.

여러분의 임무: 두 멤버의 자유 시간을 합쳐서 정확히 `목표 시간`이 되는 **딱 한 쌍**을 찾아, 그 두 멤버의 **인덱스(순번)** 를 반환하세요.

## 📋 규칙

*주어지는 것:*
- `free_hours`라는 정수 리스트 (각 멤버의 자유 시간)
- `target_hours`라는 정수 (필요한 세션 시간)

*해야 할 일:*
1. 합이 정확히 `target_hours`가 되는 두 멤버를 찾기
2. 그 두 멤버의 인덱스를 리스트로 반환 (예: `[0, 1]`)
3. 같은 멤버를 두 번 사용할 수 없음
4. 정답은 항상 정확히 **하나만** 존재한다고 가정

*제약사항:*
- 같은 사람을 두 번 쓰지 마세요
- 정답 순서는 상관없어요 (`[0, 1]`이나 `[1, 0]`이나 OK)
- **딕셔너리를 사용해서 빠르게 푸세요!**

## 💡 예제

**예제 1:**
```
입력: free_hours = [2, 7, 11, 15], target_hours = 9
출력: [0, 1]
```
왜? `free_hours[0] + free_hours[1] = 2 + 7 = 9` 이기 때문이에요.

**예제 2:**
```
입력: free_hours = [3, 2, 4], target_hours = 6
출력: [1, 2]
```
왜? `free_hours[1] + free_hours[2] = 2 + 4 = 6` 이기 때문이에요.

**예제 3:**
```
입력: free_hours = [3, 3], target_hours = 6
출력: [0, 1]
```
왜? 두 멤버 모두 3시간이고, `3 + 3 = 6` 이기 때문이에요.

## 🎓 알아야 할 것

코딩을 시작하기 전에, 다음을 이해하고 있는지 확인하세요:
- 딕셔너리를 만들고 값을 추가하는 방법 (`my_dict[key] = value`)
- 어떤 키가 딕셔너리에 있는지 확인하는 방법 (`key in my_dict`)
- 딕셔너리에서 값을 꺼내는 방법 (`my_dict[key]`)
- 리스트를 인덱스로 반복하는 방법 (`range(len(...))`)

## ✅ 과제

다음 시그니처로 함수를 작성하세요:
```python
def find_pair(free_hours: list[int], target_hours: int) -> list[int]:
    # 여기에 코드 작성
    pass
```

**시작하는 데 도움이 될 핵심 아이디어 (보수 개념):**
- 어떤 멤버의 시간이 `hours`라면, 우리가 찾는 짝은 `target_hours - hours` 입니다. 이걸 **보수(complement)** 라고 불러요.
- 리스트를 한 번 훑으면서, 지금까지 본 시간을 딕셔너리에 `{시간: 인덱스}`로 저장하세요.
- 새 멤버를 볼 때마다, "이 멤버의 보수가 이미 딕셔너리에 있나?" 확인하세요. 있다면 짝을 찾은 거예요!

## 🎪 코드 테스트

```python
# 테스트 1
result1 = find_pair([2, 7, 11, 15], 9)
print(f"테스트 1: {result1}")
# 예상: [0, 1]

# 테스트 2
result2 = find_pair([3, 2, 4], 6)
print(f"테스트 2: {result2}")
# 예상: [1, 2]

# 테스트 3
result3 = find_pair([3, 3], 6)
print(f"테스트 3: {result3}")
# 예상: [0, 1]
```

## 🌟 보너스 도전 과제

기본 과제를 끝냈다면, 도전해보세요!

- 🥉 **(쉬움)** 짝을 찾지 못했을 때 빈 리스트 `[]`를 반환하도록 수정해보세요.
- 🥈 **(중간)** 합이 `target_hours`가 되는 **모든** 쌍의 인덱스를 찾아 반환해보세요. (정답이 여러 개일 수 있다고 가정)
- 🥇 **(어려움)** 🔮 *개념 미리보기:* 세 멤버의 시간을 합쳐서 `target_hours`가 되는 경우를 찾아보세요. (힌트: 딕셔너리 + 이중 반복문)

## 🤔 생각해보기

코딩을 시작하기 전에, 접근 방법을 스케치해보세요:
1. 왜 딕셔너리가 리스트를 다시 훑는 것보다 빠를까요?
2. 멤버를 딕셔너리에 저장하는 시점은 *보수를 확인하기 전*일까요, *후*일까요? 왜 그럴까요?
3. 같은 멤버를 두 번 쓰지 않으려면 어떻게 해야 할까요?

막히면 스레드에 질문을 남겨주세요! 목표는 끝내는 것이 아니라 *배우는 것*입니다. 🚀

---
---

# 🐍 Python Practice: Find the Pair — Using Dictionaries!

> *"Alone we can do so little; together we can do so much."*
> — Helen Keller

Hey team! This time we'll sharpen our skills with a hands-on *dictionary* problem.

## 🎯 Your Mission

You're running a club study group. Each member has a set number of *free hours* per week. To run one study session, you need exactly `target_hours` of time.

Your job: find the **one pair** of members whose free hours add up to exactly `target_hours`, and return the **indices** of those two members.

## 📋 The Rules

*What you're given:*
- A list of integers `free_hours` (each member's free hours)
- An integer `target_hours` (the session length needed)

*What you need to do:*
1. Find the two members whose hours sum to exactly `target_hours`
2. Return their indices as a list (e.g., `[0, 1]`)
3. You can't use the same member twice
4. Assume there is always exactly **one** valid answer

*Constraints:*
- Don't use the same person twice
- The order of your answer doesn't matter (`[0, 1]` or `[1, 0]` both fine)
- **Use a dictionary to solve it fast!**

## 💡 Example Time

**Example 1:**
```
Input: free_hours = [2, 7, 11, 15], target_hours = 9
Output: [0, 1]
```
Why? `free_hours[0] + free_hours[1] = 2 + 7 = 9`.

**Example 2:**
```
Input: free_hours = [3, 2, 4], target_hours = 6
Output: [1, 2]
```
Why? `free_hours[1] + free_hours[2] = 2 + 4 = 6`.

**Example 3:**
```
Input: free_hours = [3, 3], target_hours = 6
Output: [0, 1]
```
Why? Both members have 3 hours, and `3 + 3 = 6`.

## 🎓 What You Should Know

Before you start coding, make sure you understand:
- How to create a dictionary and add to it (`my_dict[key] = value`)
- How to check if a key is in a dictionary (`key in my_dict`)
- How to get a value out of a dictionary (`my_dict[key]`)
- How to loop through a list by index (`range(len(...))`)

## ✅ Your Task

Write a function with this signature:
```python
def find_pair(free_hours: list[int], target_hours: int) -> list[int]:
    # Your code here
    pass
```

**The key idea to get you started (the complement trick):**
- If a member has `hours` free, then the partner we're looking for has `target_hours - hours` hours. We call this the **complement**.
- Walk through the list once, storing each member you've seen in a dictionary as `{hours: index}`.
- For each new member, ask: "Is this member's complement already in my dictionary?" If yes — you found the pair!

## 🎪 Test Your Code

```python
# Test 1
result1 = find_pair([2, 7, 11, 15], 9)
print(f"Test 1: {result1}")
# Expected: [0, 1]

# Test 2
result2 = find_pair([3, 2, 4], 6)
print(f"Test 2: {result2}")
# Expected: [1, 2]

# Test 3
result3 = find_pair([3, 3], 6)
print(f"Test 3: {result3}")
# Expected: [0, 1]
```

## 🌟 Bonus Challenges

Finished the core task? Push further!

- 🥉 **(Easy)** Modify it to return an empty list `[]` when no pair is found.
- 🥈 **(Medium)** Find and return the indices of **all** pairs that sum to `target_hours` (assume there may be multiple answers).
- 🥇 **(Hard)** 🔮 *Concept preview:* Find three members whose hours sum to `target_hours`. (Hint: dictionary + a nested loop.)

## 🤔 Think About It

Before you start coding, sketch out your approach:
1. Why is a dictionary faster than scanning the list again?
2. Should you store a member in the dictionary *before* or *after* checking for the complement? Why?
3. How do you make sure you never use the same member twice?

Drop your questions in the thread if you get stuck! Remember, the goal is to *learn*, not just to finish. 🚀
