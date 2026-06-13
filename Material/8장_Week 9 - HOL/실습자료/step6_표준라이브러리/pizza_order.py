"""
pizza_order.py
"""

from pizza_menu import MENU


def take_order():
    order = []
    while True:
        name = input("피자 이름 (종료하려면 Enter): ").strip()
        if not name:
            break
        if name not in MENU:
            print(f"  '{name}'은(는) 메뉴에 없습니다.")
            continue
        count = int(input(f"{name} 몇 판? "))
        order.append({"name": name, "count": count})
    return order
