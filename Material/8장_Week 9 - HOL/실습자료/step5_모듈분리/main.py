"""
main.py
전체 흐름을 조립하는 메인 파일.

각 모듈에서 필요한 것만 골라서 import합니다.
이 파일은 "지휘자"이고, 실제 일은 각 모듈이 합니다.
"""

from pizza_menu import show_menu
from pizza_calc import calculate_pizzas, calculate_total, calculate_total_pizzas
from pizza_order import take_order
from pizza_receipt import print_receipt


def main():
    show_menu()

    people = int(input("\n파티 참석 인원: "))
    slices_per_person = int(input("1인당 조각 수: "))
    needed = calculate_pizzas(people, slices_per_person)
    print(f"\n>> 최소 {needed}판이 필요합니다.\n")

    order = take_order()
    ordered = calculate_total_pizzas(order)
    total = calculate_total(order)

    print_receipt(order, total)

    if ordered < needed:
        print(f"\n⚠ 경고: {needed - ordered}판이 부족합니다!")


if __name__ == "__main__":
    main()
