"""
[1단계 확장]

"Anna의 친구들이 식욕이 좋아서 1인당 2조각, 3조각씩 먹고 싶어 합니다."
1인당 조각 수를 입력받도록 확장합니다.

여기서 처음으로 함수를 도입합니다.
이유: 계산 로직을 한 곳에 묶어두면, 나중에 어디서든 재사용할 수 있습니다.
"""


def calculate_pizzas(people, slices_per_person=1):
    """필요한 피자 판수를 계산한다."""
    total_slices = people * slices_per_person
    return (total_slices + 7) // 8


# 메인 흐름
people = int(input("파티 참석 인원: "))
slices_per_person = int(input("1인당 조각 수: "))
pizzas = calculate_pizzas(people, slices_per_person)
print(f"필요한 피자: {pizzas}판")
