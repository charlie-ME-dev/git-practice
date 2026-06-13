"""
pizza_menu.py
"""


MENU = {
    "노모어피자": 12000,
    "잭슨피자": 15000,
    "도미노피자": 25000,
    "파파존스": 28000,
}


def show_menu():
    print("=== 메뉴 ===")
    for name, price in MENU.items():
        print(f"  {name}: {price:,}원")


if __name__ == "__main__":
    show_menu()
