"""
[4단계 확장]

영수증을 깔끔하게 출력하는 기능을 추가합니다.
이제 한 파일에 함수가 6개, 데이터가 1개, 메인 흐름까지 모두 들어있습니다.

[잠깐, 이 코드를 한번 둘러보세요]
- 화면에 한눈에 들어오나요?
- print_receipt() 함수만 다른 프로젝트에서 쓰고 싶다면?
- MENU 데이터만 따로 관리하고 싶다면?
- 누군가 calculate_pizzas()의 버그를 고치려면 어디부터 봐야 하나요?

이런 질문들이 module 분리의 출발점입니다.
다음 단계(step5)에서 정리해봅시다.
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


def calculate_pizzas(people, slices_per_person=1):
    """사람 수로부터 필요한 피자 판수를 계산한다."""
    total_slices = people * slices_per_person
    return (total_slices + 7) // 8


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


def calculate_total(order):
    """주문 목록의 총 금액을 계산한다."""
    total = 0
    for item in order:
        total += MENU[item["name"]] * item["count"]
    return total


def calculate_total_pizzas(order):
    """주문 목록의 총 판수를 합한다."""
    return sum(item["count"] for item in order)


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


# 메인 흐름
show_menu()
people = int(input("\n파티 참석 인원: "))
slices_per_person = int(input("1인당 조각 수: "))
needed = calculate_pizzas(people, slices_per_person)
print(f"\n>> 최소 {needed}판이 필요합니다.\n")

order = take_order()
total = calculate_total(order)
print_receipt(order, total)
