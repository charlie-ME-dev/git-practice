"""
[2단계 확장]

"파티에 노모어, 잭슨, 도미노, 파파존스 중에서 시키려는데 가격이 다 다릅니다."
메뉴 데이터와 가격 계산을 추가합니다.

* 가격은 예시이며 실제와 다를 수 있습니다.
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


def calculate_pizzas(people, slices_per_person=1):
    """필요한 피자 판수를 계산한다."""
    total_slices = people * slices_per_person
    return (total_slices + 7) // 8


def calculate_total(pizza_name, count):
    """선택한 피자 한 종류의 총 금액을 계산한다."""
    return MENU[pizza_name] * count


# 메인 흐름
show_menu()
people = int(input("파티 참석 인원: "))
slices_per_person = int(input("1인당 조각 수: "))
pizzas_needed = calculate_pizzas(people, slices_per_person)
print(f"필요한 피자: {pizzas_needed}판")

choice = input("주문할 피자 이름: ")
total = calculate_total(choice, pizzas_needed)
print(f"총 금액: {total:,}원")
