"""
🏦 가장 부유한 고객 찾기 / Find the Richest Customer
연습 스켈레톤 / Practice skeleton

map(), filter(), lambda 를 연습합니다.
Practice with map(), filter(), and lambda.

빈칸(___)을 채워서 함수를 완성하세요.
Fill in the blanks (___) to complete each function.
"""


# =========================================================
# CORE / 핵심 과제
# =========================================================
def find_richest_wealth(accounts):
    # TODO 1: 각 고객의 자산(계좌 합계)을 모두 구한 뒤, 그중 최댓값을 반환하세요.
    # TODO 1: Get every customer's wealth (sum of their accounts), then return the largest.
    #         힌트 / hint: max(map(sum, ___))
    return max(map(sum, ___))


# =========================================================
# 🥉 BONUS — Easy
# =========================================================
def list_all_wealth(accounts):
    # TODO 2: 모든 고객의 총 자산을 리스트로 반환하세요.
    # TODO 2: Return a list of every customer's total wealth.
    #         힌트 / hint: list(map(___, accounts))
    return list(map(___, accounts))


# =========================================================
# 🥈 BONUS — Medium
# =========================================================
def count_high_value_customers(accounts, threshold):
    # TODO 3: 자산이 threshold 를 초과(>)하는 고객만 남기세요.
    # TODO 3: Keep only customers whose wealth is strictly greater than threshold.
    #         힌트 / hint: filter(lambda customer: sum(customer) > ___, accounts)
    high_value = filter(lambda customer: sum(customer) > ___, accounts)

    # TODO 4: 남은 고객이 몇 명인지 반환하세요.
    # TODO 4: Return how many customers remain.
    #         힌트 / hint: filter 결과는 list() 로 감싼 뒤 len() / wrap in list() then len()
    return len(list(___))


# =========================================================
# 🥇 BONUS — Hard 🔮 (아직 안 배운 도구 / not taught yet)
# =========================================================
from functools import reduce

def total_bank_wealth(accounts):
    # TODO 5: 모든 고객의 자산을 먼저 구하세요.
    # TODO 5: First get every customer's wealth.
    all_totals = map(sum, accounts)

    # TODO 6: reduce 로 전부 더하세요. 시작값은 0 입니다.
    # TODO 6: Use reduce to add them all up. The starting value is 0.
    #         힌트 / hint: reduce(lambda running, current: running + current, all_totals, ___)
    return reduce(lambda running, current: running + current, all_totals, ___)


# =========================================================
# 테스트 / TESTS  (이 블록은 수정하지 마세요 / do not modify this block)
# =========================================================
if __name__ == "__main__":
    # --- CORE ---
    result_1 = find_richest_wealth([[1, 2, 3], [3, 2, 1]])
    if result_1 == 6:
        print("CORE Test 1 통과 / passed")
    else:
        print("CORE Test 1 실패 / failed -> got:", result_1)

    result_2 = find_richest_wealth([[1, 5], [7, 3], [3, 5]])
    if result_2 == 10:
        print("CORE Test 2 통과 / passed")
    else:
        print("CORE Test 2 실패 / failed -> got:", result_2)

    # --- 🥉 Easy ---
    easy = list_all_wealth([[1, 5], [7, 3], [3, 5]])
    if easy == [6, 10, 8]:
        print("EASY 통과 / passed")
    else:
        print("EASY 실패 / failed -> got:", easy)

    # --- 🥈 Medium ---
    medium = count_high_value_customers([[1, 5], [7, 3], [3, 5]], 7)
    if medium == 2:
        print("MEDIUM 통과 / passed")
    else:
        print("MEDIUM 실패 / failed -> got:", medium)

    # --- 🥇 Hard ---
    hard = total_bank_wealth([[1, 2, 3], [3, 2, 1]])
    if hard == 12:
        print("HARD 통과 / passed")
    else:
        print("HARD 실패 / failed -> got:", hard)
