"""
pizza_receipt.py
영수증을 출력하는 모듈.
"""

from pizza_menu import MENU


def print_receipt(order, total):
    """영수증을 출력한다."""
    print("=" * 35)
    print("           주문 영수증")
    print("=" * 35)
    for item in order:
        name = item["name"]
        count = item["count"]
        subtotal = MENU[name] * count
        print(f"  {name:10s} {count}판  {subtotal:>10,}원")
    print("-" * 35)
    print(f"  합계: {total:>22,}원")
    print("=" * 35)


if __name__ == "__main__":
    print("== pizza_receipt 자체 테스트 ==")
    sample_order = [
        {"name": "노모어피자", "count": 2},
        {"name": "도미노피자", "count": 1},
    ]
    sample_total = 12000 * 2 + 25000 * 1
    print_receipt(sample_order, sample_total)
