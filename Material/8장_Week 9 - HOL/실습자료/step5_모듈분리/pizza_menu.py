"""
pizza_menu.py
메뉴 데이터와 메뉴 출력 함수를 담당하는 모듈.
"""


MENU = {
    "노모어피자": 12000,
    "잭슨피자": 15000,
    "도미노피자": 25000,
    "파파존스": 28000,
}


def show_menu():
    """메뉴를 출력한다."""
    print("=== 메뉴 ===")
    for name, price in MENU.items():
        print(f"  {name}: {price:,}원")


# 이 모듈을 직접 실행했을 때만 동작 (다른 파일에서 import할 땐 무시됨)
if __name__ == "__main__":
    print("== pizza_menu 자체 테스트 ==")
    show_menu()
    print(f"\n메뉴 항목 수: {len(MENU)}")
