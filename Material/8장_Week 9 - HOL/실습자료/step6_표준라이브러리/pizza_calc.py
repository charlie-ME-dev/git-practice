"""
pizza_calc.py

[변경점]
이전엔 (total_slices + 7) // 8 로 직접 올림 나눗셈을 구현했지만,
표준 라이브러리 math 모듈을 쓰면 의도가 더 명확해집니다.

import math 를 추가하고 math.ceil 을 사용해봅시다.
"""

import math
from pizza_menu import MENU


def calculate_pizzas(people, slices_per_person=1):
    """사람 수로부터 필요한 피자 판수를 계산한다."""
    total_slices = people * slices_per_person
    return math.ceil(total_slices / 8)  # 이전: (total_slices + 7) // 8


def calculate_total(order):
    total = 0
    for item in order:
        total += MENU[item["name"]] * item["count"]
    return total


def calculate_total_pizzas(order):
    return sum(item["count"] for item in order)


if __name__ == "__main__":
    print(f"5명: {calculate_pizzas(5)}판")
    print(f"9명: {calculate_pizzas(9)}판")
    print(f"17명, 1인 2조각: {calculate_pizzas(17, 2)}판")
