"""
📅 마감일 카운트다운 트래커 / Deadline Countdown Tracker
스켈레톤 파일 / Skeleton file

DeadlineHero 앱의 핵심 마감일 추적 기능을 구현하세요.
Implement the core deadline tracking logic for the DeadlineHero app.

⚠️ 아래 테스트 블록은 수정하지 마세요!
⚠️ Do not modify the test block below!
"""

from datetime import date, timedelta


# ============================================================
# 함수 1 / Function 1: days_until
# ============================================================
def days_until(target_date: date) -> int:
    """
    오늘부터 target_date 까지 며칠 남았는지 계산합니다.
    Calculate how many days remain from today until target_date.

    미래 → 양수, 오늘 → 0, 과거 → 음수
    Future → positive, today → 0, past → negative
    """
    # TODO 1-1: date.today() 로 오늘 날짜 가져오기
    # TODO 1-1: Get today's date using date.today()


    # TODO 1-2: target_date 에서 today 를 빼서 timedelta 객체 만들기
    # TODO 1-2: Subtract today from target_date to get a timedelta object


    # TODO 1-3: timedelta 의 .days 속성을 정수로 반환
    # TODO 1-3: Return the .days attribute as an integer
    pass


# ============================================================
# 함수 2 / Function 2: format_deadline
# ============================================================
def format_deadline(target_date: date) -> str:
    """
    날짜를 한국식 문자열로 보기 좋게 포맷합니다.
    Format the date as a Korean-friendly string.

    예시 / Example:
        date(2026, 12, 25) → "2026년 12월 25일 (금요일)"
    """
    # TODO 2-1: 요일 이름 리스트 만들기 (월요일=0, 일요일=6 순서)
    # TODO 2-1: Build a weekday-name list (Monday=0, Sunday=6 order)
    # 힌트 / Hint: ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]


    # TODO 2-2: target_date.weekday() 로 요일 인덱스 가져와서 한글 이름 찾기
    # TODO 2-2: Use target_date.weekday() to look up the Korean weekday name


    # TODO 2-3: f-string 으로 "YYYY년 MM월 DD일 (요일)" 형식의 문자열 만들어서 반환
    # TODO 2-3: Build and return the "YYYY년 MM월 DD일 (요일)" formatted string
    pass


# ============================================================
# 함수 3 / Function 3: deadline_status
# ============================================================
def deadline_status(target_date: date) -> tuple:
    """
    남은 일수와 상태 메시지를 튜플로 반환합니다.
    Return a tuple of (days_left, status_message).

    상태 분류 / Status categories:
        음수 / negative  → "지남 (N일 전)"
        0               → "오늘 마감!"
        1 ~ 3           → "임박"
        4 ~ 7           → "곧"
        8 이상 / ≥ 8     → "여유"
    """
    # TODO 3-1: days_until() 함수를 호출해서 남은 일수 계산
    # TODO 3-1: Call days_until() to compute days remaining


    # TODO 3-2: if/elif/else 로 상태 메시지 결정
    # TODO 3-2: Use if/elif/else to decide the status message
    # 주의 / Note: 음수일 때는 "지남 (N일 전)" — 절댓값 사용 (abs())
    # When negative, use "지남 (N일 전)" — apply abs() for the number


    # TODO 3-3: (남은 일수, 상태 메시지) 튜플 반환
    # TODO 3-3: Return the (days_left, status_message) tuple
    pass


# ============================================================
# ⚠️  테스트 블록 — 수정하지 마세요 / Test block — do not modify
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("🧪 자동 테스트 시작 / Running automated tests")
    print("=" * 60)

    today = date.today()
    passed = 0
    failed = 0

    def check(label, actual, expected):
        global passed, failed
        if actual == expected:
            print(f"  ✓ {label}")
            passed += 1
        else:
            print(f"  ✗ {label}")
            print(f"      기대값/expected: {expected!r}")
            print(f"      실제값/actual:   {actual!r}")
            failed += 1

    # --- Test days_until ---
    print("\n[Test 1] days_until()")
    check("today → 0", days_until(today), 0)
    check("tomorrow → 1", days_until(today + timedelta(days=1)), 1)
    check("today + 7 → 7", days_until(today + timedelta(days=7)), 7)
    check("yesterday → -1", days_until(today - timedelta(days=1)), -1)
    check("today - 30 → -30", days_until(today - timedelta(days=30)), -30)

    # --- Test format_deadline ---
    print("\n[Test 2] format_deadline()")
    check(
        "2026-01-01 (목)",
        format_deadline(date(2026, 1, 1)),
        "2026년 1월 1일 (목요일)",
    )
    check(
        "2026-12-25 (금)",
        format_deadline(date(2026, 12, 25)),
        "2026년 12월 25일 (금요일)",
    )
    check(
        "2024-02-29 (목, leap day)",
        format_deadline(date(2024, 2, 29)),
        "2024년 2월 29일 (목요일)",
    )

    # --- Test deadline_status ---
    print("\n[Test 3] deadline_status()")
    check(
        "today → (0, '오늘 마감!')",
        deadline_status(today),
        (0, "오늘 마감!"),
    )
    check(
        "+1 day → (1, '임박')",
        deadline_status(today + timedelta(days=1)),
        (1, "임박"),
    )
    check(
        "+3 days → (3, '임박') [boundary]",
        deadline_status(today + timedelta(days=3)),
        (3, "임박"),
    )
    check(
        "+4 days → (4, '곧') [boundary]",
        deadline_status(today + timedelta(days=4)),
        (4, "곧"),
    )
    check(
        "+7 days → (7, '곧') [boundary]",
        deadline_status(today + timedelta(days=7)),
        (7, "곧"),
    )
    check(
        "+8 days → (8, '여유') [boundary]",
        deadline_status(today + timedelta(days=8)),
        (8, "여유"),
    )
    check(
        "-5 days → (-5, '지남 (5일 전)')",
        deadline_status(today - timedelta(days=5)),
        (-5, "지남 (5일 전)"),
    )

    # --- Summary ---
    print("\n" + "=" * 60)
    total = passed + failed
    print(f"결과 / Result: {passed} / {total} 통과 / passed")
    if failed == 0:
        print("🎉 모든 테스트 통과! / All tests passed!")
    else:
        print(f"❌ {failed} 개 실패 / {failed} test(s) failed")
    print("=" * 60)
