"""
pizza_calc.py
피자 개수 및 금액 계산을 담당하는 모듈.

여기서 중요한 점:
- calculate_total()은 MENU 데이터가 필요합니다.
- MENU는 pizza_menu.py에 있습니다.
- 따라서 from pizza_menu import MENU 가 필요합니다.

이게 바로 namespace의 의미입니다.
import는 그 파일을 실행하고, 그 결과로 만들어진 이름을 가져옵니다.
MENU도 이름이니까 가져올 수 있는 것입니다.
"""

from pizza_menu import MENU


def calculate_pizzas(people, slices_per_person=1):
    """사람 수로부터 필요한 피자 판수를 계산한다. (시험 문제의 핵심)"""
    total_slices = people * slices_per_person
    return (total_slices + 7) // 8


def calculate_total(order):
    """주문 목록의 총 금액을 계산한다."""
    total = 0
    for item in order:
        total += MENU[item["name"]] * item["count"]
    return total


def calculate_total_pizzas(order):
    """주문 목록의 총 판수를 합한다."""
    return sum(item["count"] for item in order)


if __name__ == "__main__":
    print("== pizza_calc 자체 테스트 ==")
    print(f"5명, 1인 1조각: {calculate_pizzas(5)}판")        # 1
    print(f"9명, 1인 1조각: {calculate_pizzas(9)}판")        # 2
    print(f"17명, 1인 2조각: {calculate_pizzas(17, 2)}판")  # 5

    sample_order = [
        {"name": "노모어피자", "count": 2},
        {"name": "도미노피자", "count": 1},
    ]
    print(f"\n샘플 주문 총 판수: {calculate_total_pizzas(sample_order)}판")
    print(f"샘플 주문 총 금액: {calculate_total(sample_order):,}원")
