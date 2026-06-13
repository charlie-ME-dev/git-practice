"""
pizza_order.py
사용자로부터 주문을 받는 모듈.
"""

from pizza_menu import MENU


def take_order():
    """사용자에게 주문을 받아 리스트로 반환한다."""
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


if __name__ == "__main__":
    print("== pizza_order 자체 테스트 ==")
    print("아무 피자나 입력해보세요. Enter 누르면 종료.")
    result = take_order()
    print(f"\n받은 주문: {result}")
