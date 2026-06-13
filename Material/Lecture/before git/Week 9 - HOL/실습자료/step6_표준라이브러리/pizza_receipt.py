"""
pizza_receipt.py

[변경점]
영수증에 주문 시각과 영수증 번호를 추가합니다.
- datetime: 현재 시각
- random: 영수증 번호 생성

이 둘 모두 표준 라이브러리입니다.
우리가 pizza_menu.py를 만든 것과 똑같이, 누군가 만들어둔 .py 파일들이죠.
차이는 단지 Python을 설치할 때 함께 들어있다는 것뿐.
"""

import datetime
import random

from pizza_menu import MENU


def print_receipt(order, total):
    receipt_no = random.randint(1000, 9999)
    now = datetime.datetime.now()

    print("=" * 35)
    print("           주문 영수증")
    print(f"  영수증 번호: #{receipt_no}")
    print(f"  주문 시각:   {now:%Y-%m-%d %H:%M}")
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
    sample_order = [
        {"name": "노모어피자", "count": 2},
        {"name": "도미노피자", "count": 1},
    ]
    sample_total = 12000 * 2 + 25000 * 1
    print_receipt(sample_order, sample_total)
