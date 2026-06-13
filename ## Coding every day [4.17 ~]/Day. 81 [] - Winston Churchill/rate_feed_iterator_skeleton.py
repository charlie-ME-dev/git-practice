# =====================================================================
# 🐍 Wonder Exchange — 일일 환율 피드 이터레이터 (Daily Rate Feed Iterator)
# =====================================================================
# 이터러블(RateFeed)과 이터레이터(RateFeedIterator)를 분리해 만듭니다.
# Build an ITERABLE (RateFeed) separated from its ITERATOR (RateFeedIterator).
#
# 작성 규칙 (Rules):
#   - 메서드/변수: snake_case   |  클래스: PascalCase
#   - `___` 부분을 채우세요. (Fill in each `___` blank.)
#   - 아래 "테스트 영역(TEST HARNESS)"은 수정하지 마세요!
#     Do NOT modify the TEST HARNESS section below!
# =====================================================================


class RateFeed:
    """이터러블: 환율을 보관하고, 매번 새 이터레이터를 만들어 준다.
    Iterable: stores the rates, hands out a fresh iterator each time."""

    def __init__(self, daily_rates: list[float]) -> None:
        # TODO 1: 전달받은 환율 리스트를 인스턴스에 저장하세요.
        #         Store the given list of rates on the instance.
        self.daily_rates = ___

    def __iter__(self):
        # TODO 2: 위치가 0부터 시작하는 '새' RateFeedIterator를 만들어 반환하세요.
        #         이렇게 해야 같은 피드를 여러 번 순회할 수 있습니다 (재반복).
        #         Return a BRAND-NEW RateFeedIterator (position 0) so the same
        #         feed can be looped more than once (re-iterable).
        return ___


class RateFeedIterator:
    """이터레이터: 위치를 추적하며 한 번에 하나씩 환율을 꺼낸다.
    Iterator: tracks position, yields one rate at a time."""

    def __init__(self, daily_rates: list[float]) -> None:
        # TODO 3: 순회할 환율 리스트를 저장하세요.
        #         Store the list of rates to walk through.
        self.daily_rates = ___
        # TODO 4: 현재 위치를 0으로 초기화하세요.
        #         Initialize the current position to 0.
        self.position = ___

    def __iter__(self):
        # TODO 5: 이터레이터는 자기 자신이 이터레이터이므로 자신을 반환합니다.
        #         An iterator IS its own iterator — return itself.
        return ___

    def __next__(self):
        # TODO 6: 이미 끝에 도달했다면(위치 >= 길이) StopIteration을 발생시키세요.
        #         If we've reached the end (position >= length), raise StopIteration.
        if self.position >= ___:
            raise ___

        # TODO 7: 현재 위치의 환율을 변수에 저장하세요.
        #         Grab the rate at the current position into a variable.
        current_rate = self.daily_rates[___]

        # TODO 8: 위치를 한 칸 앞으로 옮기세요 (1 증가).
        #         Advance the position by one step.
        self.position += ___

        # TODO 9: 저장해 둔 현재 환율을 반환하세요.
        #         Return the rate you grabbed.
        return ___


# =====================================================================
# 🔒 테스트 영역 (TEST HARNESS) — 수정하지 마세요! / Do NOT modify!
# =====================================================================

# 테스트 1 — 기본 순회 (basic walk)
feed = RateFeed([1320.5, 1325.0, 1318.75])
result = []
for rate in feed:
    result.append(rate)
print("테스트 1 (Test 1):", result)
print("예상 (Expected): [1320.5, 1325.0, 1318.75]")
print()

# 테스트 2 — 재반복: 같은 feed를 다시 순회 (re-iterable: loop same feed again)
second = []
for rate in feed:
    second.append(rate)
print("테스트 2 (Test 2):", second)
print("예상 (Expected): [1320.5, 1325.0, 1318.75]")
print()

# 테스트 3 — iter() / next() 직접 사용 (built-ins)
box = iter(feed)
print("테스트 3 (Test 3):", next(box), next(box), next(box))
print("예상 (Expected): 1320.5 1325.0 1318.75")
print()

# 테스트 4 — 빈 피드 (empty feed)
empty = RateFeed([])
print("테스트 4 (Test 4):", [r for r in empty])
print("예상 (Expected): []")
print()

# 테스트 5 — 내장 함수와 호환 (works with built-ins)
print("테스트 5 (Test 5):", list(RateFeed([10, 20, 30])), sum(RateFeed([10, 20, 30])))
print("예상 (Expected): [10, 20, 30] 60")
