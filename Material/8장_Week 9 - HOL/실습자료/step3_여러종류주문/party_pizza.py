"""
[3단계 확장]

"한 종류만 시키는 게 아니라, 여러 종류를 섞어서 주문하고 싶다."
주문 목록(list of dict) 자료구조가 필요해집니다.

여기서 새로 등장하는 함수:
- take_order():        사용자에게 여러 종류의 주문을 받는다.
- calculate_total():   주문 목록 전체의 총 금액을 계산한다.
- calculate_total_pizzas(): 주문 목록의 총 판수를 합한다.

[중요한 구분]
- calculate_pizzas(people)       : 사람 수로부터 "필요한" 판수를 구함 (시험 문제)
- calculate_total_pizzas(order)  : 주문 목록의 "주문된" 판수를 합함
이름이 비슷해도 역할이 완전히 다릅니다!
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


# 메인 흐름
show_menu()
people = int(input("\n파티 참석 인원: "))
slices_per_person = int(input("1인당 조각 수: "))
needed = calculate_pizzas(people, slices_per_person)
print(f"\n>> 최소 {needed}판이 필요합니다.\n")

order = take_order()
ordered = calculate_total_pizzas(order)
total = calculate_total(order)

print(f"\n주문하신 피자: 총 {ordered}판")
print(f"총 금액: {total:,}원")

if ordered < needed:
    print(f"⚠ 경고: {needed - ordered}판이 부족합니다!")
