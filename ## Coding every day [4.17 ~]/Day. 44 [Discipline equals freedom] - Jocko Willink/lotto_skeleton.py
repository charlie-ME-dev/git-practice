"""
🎰 Lotto Number Generator / 로또 번호 생성기
============================================
Lotto 6/45: Pick 6 unique numbers from 1~45, plus 1 bonus.
로또 6/45: 1~45 중에서 서로 다른 6개 + 보너스 1개.

Allowed / 허용: random.randint(), while, for, if/else, lists, sets, tuples
NOT allowed / 금지: random.sample(), random.shuffle(), random.choice()
"""

import random


# ============================================================
# Task 1 / 과제 1: generate_lotto_numbers
# ============================================================
def generate_lotto_numbers():
    """
    KO: 1~45 중에서 서로 다른 6개의 숫자를 뽑아 정렬된 리스트로 반환합니다.
    EN: Pick 6 unique numbers from 1~45 and return them as a sorted list.
    """
    # KO: 뽑은 숫자들을 저장할 빈 리스트를 만드세요.
    # EN: Create an empty list to store the drawn numbers.
    numbers = []

    # KO: 6개를 뽑을 때까지 반복하세요. (while 루프 사용)
    # EN: Repeat until you've drawn 6 numbers. (use a while loop)
    # TODO: while 조건을 작성하세요 / write the while condition

    # KO: random.randint(1, 45)로 숫자 하나를 뽑으세요.
    # EN: Draw one number with random.randint(1, 45).
    # TODO

    # KO: 이미 뽑은 숫자가 아니면 리스트에 추가하세요.
    # EN: If the number is not already in the list, append it.
    # TODO

    # KO: 리스트를 오름차순으로 정렬하세요.
    # EN: Sort the list in ascending order.
    # TODO

    # KO: 정렬된 리스트를 반환하세요.
    # EN: Return the sorted list.
    return numbers


# ============================================================
# Task 2 / 과제 2: generate_lotto_with_bonus
# ============================================================
def generate_lotto_with_bonus():
    """
    KO: 본 번호 6개 + 보너스 1개를 생성합니다. 보너스는 본 번호와 겹치면 안 됩니다.
    EN: Generate 6 main numbers + 1 bonus. Bonus must NOT match any main number.
    """
    # KO: 본 번호 6개를 뽑으세요. (과제 1과 같은 방식, 또는 그 함수를 재사용해도 OK)
    # EN: Draw 6 main numbers. (same approach as Task 1, or reuse that function)
    main_numbers = []
    # TODO

    # KO: 보너스 번호를 뽑되, 본 번호와 겹치면 다시 뽑으세요.
    # EN: Draw a bonus number; if it collides with main numbers, draw again.
    bonus = 0
    # TODO

    # KO: 본 번호와 보너스를 함께 반환하세요. (튜플로 두 값 반환)
    # EN: Return main numbers and bonus together. (return two values as a tuple)
    return main_numbers, bonus


# ============================================================
# Task 3 / 과제 3: generate_multiple_games (default parameter!)
# ============================================================
def generate_multiple_games(num_games=5):
    """
    KO: 여러 게임을 한 번에 생성합니다. 기본값은 5게임입니다.
    EN: Generate multiple games at once. Default is 5 games.
    """
    # KO: 게임들을 담을 빈 리스트를 만드세요.
    # EN: Create an empty list to hold the games.
    games = []

    # KO: num_games 만큼 반복하면서 generate_lotto_numbers()를 호출해 추가하세요.
    # EN: Loop num_games times, calling generate_lotto_numbers() and appending each result.
    # TODO

    # KO: 모든 게임이 담긴 리스트를 반환하세요.
    # EN: Return the list of all games.
    return games


# ============================================================
# Test Block / 테스트 블록
# ============================================================
if __name__ == "__main__":
    print("=" * 50)
    print("Test 1 / 테스트 1: generate_lotto_numbers()")
    print("=" * 50)
    nums = generate_lotto_numbers()
    print(f"Main numbers / 본 번호: {nums}")
    print(f"  Length is 6 / 길이 6: {len(nums) == 6}")
    print(f"  All unique / 모두 다름: {len(set(nums)) == len(nums)}")
    print(f"  All in 1~45 / 범위 OK: {all(1 <= n <= 45 for n in nums)}")
    print(f"  Sorted / 정렬됨: {nums == sorted(nums)}")

    print("\n" + "=" * 50)
    print("Test 2 / 테스트 2: generate_lotto_with_bonus()")
    print("=" * 50)
    main, bonus = generate_lotto_with_bonus()
    print(f"Main / 본 번호: {main}")
    print(f"Bonus / 보너스: {bonus}")
    print(f"  Bonus not in main / 보너스 안 겹침: {bonus not in main}")

    print("\n" + "=" * 50)
    print("Test 3 / 테스트 3: generate_multiple_games() — default 5")
    print("=" * 50)
    games = generate_multiple_games()
    print(f"Total games / 총 게임 수: {len(games)}")
    for i, g in enumerate(games, 1):
        print(f"  Game {i}: {g}")

    print("\n" + "=" * 50)
    print("Test 4 / 테스트 4: generate_multiple_games(3)")
    print("=" * 50)
    games = generate_multiple_games(3)
    print(f"Total games / 총 게임 수: {len(games)}")
    for i, g in enumerate(games, 1):
        print(f"  Game {i}: {g}")
