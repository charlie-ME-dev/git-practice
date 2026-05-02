# 🎵 Python 연습: 나만의 플레이리스트 앱 만들기!

여러분, 안녕하세요! 오늘은 실제로 쓸 수 있는 음악 플레이리스트 관리 프로그램을 만들어볼 거예요.

## 🎯 미션

여러분은 신생 음악 스트리밍 스타트업의 주니어 개발자입니다! 팀장이 이런 말을 했어요:

> "우리 앱에 플레이리스트 기능이 필요해요. 노래를 추가하고, 삭제하고, 검색하고, 현재 목록을 보여주는 기능을 만들어주세요!"

리스트(list)를 활용해서 이 기능들을 하나씩 구현해봅시다.

## 📋 만들어야 할 함수들

### 1️⃣ `add_song(playlist, song)`
플레이리스트 맨 끝에 노래를 추가합니다.
• 이미 있는 노래라면: `"[song]은(는) 이미 플레이리스트에 있어요!"` 출력
• 새 노래라면: `"[song]이(가) 추가되었습니다! 🎵"` 출력

### 2️⃣ `remove_song(playlist, song)`
플레이리스트에서 노래를 삭제합니다.
• 노래가 있으면: 삭제 후 `"[song]이(가) 삭제되었습니다."` 출력
• 없으면: `"[song]을(를) 찾을 수 없어요."` 출력

### 3️⃣ `find_song(playlist, song)`
노래가 플레이리스트에 있는지 확인합니다.
• 있으면: `"✅ [song] - 플레이리스트에 있어요! ([index]번째 트랙)"` 출력
• 없으면: `"❌ [song] - 플레이리스트에 없어요."` 출력

### 4️⃣ `show_playlist(playlist)`
현재 플레이리스트를 번호와 함께 출력합니다.
• 노래가 있으면: 번호 매겨서 목록 출력
• 비어 있으면: `"플레이리스트가 비어 있어요. 노래를 추가해보세요! 🎶"` 출력

## 💡 예제

```python
playlist = []

add_song(playlist, "Supernova")
add_song(playlist, "APT.")
add_song(playlist, "Supernova")   # 중복!

show_playlist(playlist)

find_song(playlist, "APT.")
find_song(playlist, "Whiplash")

remove_song(playlist, "Supernova")
remove_song(playlist, "Whiplash")  # 없는 노래

show_playlist(playlist)
```

**예상 출력:**
```
Supernova이(가) 추가되었습니다! 🎵
APT.이(가) 추가되었습니다! 🎵
Supernova은(는) 이미 플레이리스트에 있어요!

1. Supernova
2. APT.

✅ APT. - 플레이리스트에 있어요! (2번째 트랙)
❌ Whiplash - 플레이리스트에 없어요.

Supernova이(가) 삭제되었습니다.
Whiplash을(를) 찾을 수 없어요.

1. APT.
```

## 🎓 알아야 할 것

코딩 시작 전, 다음 개념을 떠올려보세요:
• `append()` — 리스트 끝에 항목 추가
• `remove()` — 리스트에서 항목 삭제
• `in` — 항목이 리스트 안에 있는지 확인
• `len()` — 리스트 길이 확인
• 인덱싱 — `playlist[0]`은 첫 번째 항목

## ✅ 과제

아래 함수 시그니처를 사용해서 코드를 완성하세요:

```python
def add_song(playlist: list, song: str) -> None:
    # TODO: 여기에 코드 작성
    pass

def remove_song(playlist: list, song: str) -> None:
    # TODO: 여기에 코드 작성
    pass

def find_song(playlist: list, song: str) -> None:
    # TODO: 여기에 코드 작성
    pass

def show_playlist(playlist: list) -> None:
    # TODO: 여기에 코드 작성
    pass
```

## 🎪 코드 테스트

```python
# 테스트 1: 기본 추가 및 출력
playlist = []
add_song(playlist, "Supernova")
add_song(playlist, "APT.")
add_song(playlist, "Whiplash")
show_playlist(playlist)
# 예상: 1. Supernova / 2. APT. / 3. Whiplash

# 테스트 2: 중복 추가 방지
add_song(playlist, "APT.")
# 예상: APT.은(는) 이미 플레이리스트에 있어요!

# 테스트 3: 검색
find_song(playlist, "Whiplash")
find_song(playlist, "Dynamite")
# 예상: ✅ Whiplash - 플레이리스트에 있어요! (3번째 트랙)
# 예상: ❌ Dynamite - 플레이리스트에 없어요.

# 테스트 4: 삭제
remove_song(playlist, "Supernova")
remove_song(playlist, "Dynamite")
show_playlist(playlist)
# 예상: Supernova이(가) 삭제되었습니다.
# 예상: Dynamite을(를) 찾을 수 없어요.
# 예상: 1. APT. / 2. Whiplash

# 테스트 5: 빈 플레이리스트
empty = []
show_playlist(empty)
# 예상: 플레이리스트가 비어 있어요. 노래를 추가해보세요! 🎶
```

## 🌟 보너스 챌린지

기본 과제를 다 끝냈나요? 한 단계 더 도전해봅시다!

**🎯 보너스: `move_to_top(playlist, song)`**

좋아하는 노래를 플레이리스트 맨 앞으로 이동시키는 기능을 만들어보세요.

```
move_to_top(playlist, "Whiplash")
# 플레이리스트: ["APT.", "Whiplash"] → ["Whiplash", "APT."]
```

힌트:
• 노래가 없으면: `"[song]을(를) 찾을 수 없어요."` 출력
• 이미 첫 번째라면: `"[song]은(는) 이미 첫 번째 트랙이에요! 🥇"` 출력
• 이동 성공하면: `"[song]이(가) 맨 앞으로 이동되었습니다! 🔝"` 출력
• 힌트: `remove()`와 `insert()`를 함께 사용해보세요

## 🤔 생각해보기

1. `in` 키워드 없이 중복을 확인하려면 어떻게 해야 할까요?
2. `find_song`에서 인덱스 번호를 어떻게 알 수 있을까요? (힌트: 반복문과 카운터!)
3. 플레이리스트가 아주 길다면, 삭제할 때 어떤 문제가 생길 수 있을까요?

막히면 스레드에 질문 남겨주세요! 완성보다 이해가 목표입니다. 천천히, 하나씩! 💪

행운을 빕니다! 🚀

---
---

# 🎵 Python Practice: Build Your Own Playlist App!

Hey team! Today we're building something you might actually use — a music playlist manager.

## 🎯 Your Mission

You're a junior developer at a music streaming startup! Your team lead just said:

> "We need a playlist feature for our app. Build something that can add songs, remove them, search through them, and display the current queue!"

Let's implement these features one by one using Python lists.

## 📋 Functions to Build

### 1️⃣ `add_song(playlist, song)`
Adds a song to the end of the playlist.
• If the song is already there: print `"[song] is already in the playlist!"`
• If it's new: print `"[song] has been added! 🎵"`

### 2️⃣ `remove_song(playlist, song)`
Removes a song from the playlist.
• If found: remove it and print `"[song] has been removed."`
• If not found: print `"[song] was not found in the playlist."`

### 3️⃣ `find_song(playlist, song)`
Checks whether a song is in the playlist.
• If found: print `"✅ [song] - Found! (Track #[index])"`
• If not found: print `"❌ [song] - Not in the playlist."`

### 4️⃣ `show_playlist(playlist)`
Displays the current playlist with track numbers.
• If not empty: print a numbered list
• If empty: print `"Your playlist is empty. Add some songs! 🎶"`

## 💡 Example

```python
playlist = []

add_song(playlist, "Supernova")
add_song(playlist, "APT.")
add_song(playlist, "Supernova")   # duplicate!

show_playlist(playlist)

find_song(playlist, "APT.")
find_song(playlist, "Whiplash")

remove_song(playlist, "Supernova")
remove_song(playlist, "Whiplash")  # not in list

show_playlist(playlist)
```

**Expected output:**
```
Supernova has been added! 🎵
APT. has been added! 🎵
Supernova is already in the playlist!

1. Supernova
2. APT.

✅ APT. - Found! (Track #2)
❌ Whiplash - Not in the playlist.

Supernova has been removed.
Whiplash was not found in the playlist.

1. APT.
```

## 🎓 What You Should Know

Before you start, make sure you're comfortable with:
• `append()` — adds an item to the end of a list
• `remove()` — removes an item from a list
• `in` — checks if an item is in a list
• `len()` — returns the length of a list
• Indexing — `playlist[0]` is the first item

## ✅ Your Task

Complete the functions using these signatures:

```python
def add_song(playlist: list, song: str) -> None:
    # TODO: your code here
    pass

def remove_song(playlist: list, song: str) -> None:
    # TODO: your code here
    pass

def find_song(playlist: list, song: str) -> None:
    # TODO: your code here
    pass

def show_playlist(playlist: list) -> None:
    # TODO: your code here
    pass
```

## 🎪 Test Your Code

```python
# Test 1: Basic add and display
playlist = []
add_song(playlist, "Supernova")
add_song(playlist, "APT.")
add_song(playlist, "Whiplash")
show_playlist(playlist)
# Expected: 1. Supernova / 2. APT. / 3. Whiplash

# Test 2: Duplicate prevention
add_song(playlist, "APT.")
# Expected: APT. is already in the playlist!

# Test 3: Search
find_song(playlist, "Whiplash")
find_song(playlist, "Dynamite")
# Expected: ✅ Whiplash - Found! (Track #3)
# Expected: ❌ Dynamite - Not in the playlist.

# Test 4: Remove
remove_song(playlist, "Supernova")
remove_song(playlist, "Dynamite")
show_playlist(playlist)
# Expected: Supernova has been removed.
# Expected: Dynamite was not found in the playlist.
# Expected: 1. APT. / 2. Whiplash

# Test 5: Empty playlist
empty = []
show_playlist(empty)
# Expected: Your playlist is empty. Add some songs! 🎶
```

## 🌟 Bonus Challenge

Finished the main tasks? Take it one step further!

**🎯 Bonus: `move_to_top(playlist, song)`**

Build a feature that moves a favorite song to the front of the playlist.

```
move_to_top(playlist, "Whiplash")
# playlist: ["APT.", "Whiplash"] → ["Whiplash", "APT."]
```

Hints:
• If the song isn't found: print `"[song] was not found in the playlist."`
• If it's already first: print `"[song] is already the first track! 🥇"`
• If moved: print `"[song] moved to the top! 🔝"`
• Hint: try using `remove()` and `insert()` together

## 🤔 Think About It

1. How would you check for duplicates *without* the `in` keyword?
2. How can you find the index number of a song in `find_song`? (Hint: loop + counter!)
3. If the playlist were very long, what potential problem might come up when deleting?

Drop questions in the thread if you get stuck! The goal is understanding, not just finishing. One step at a time! 💪

Good luck! 🚀
