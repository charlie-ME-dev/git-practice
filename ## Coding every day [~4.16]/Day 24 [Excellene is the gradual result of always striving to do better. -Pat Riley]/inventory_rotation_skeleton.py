# 📦 Inventory Rotation - Skeleton Code
# 재고 순환 관리 - 뼈대 코드

# ============================================================
# 함수를 완성하세요! Complete each function below.
# 각 TODO 주석을 읽고 코드를 채워 넣으세요.
# Read each TODO comment and fill in the code.
# ============================================================


def restock(inventory: list, item: str) -> None:
    """
    새 물건을 재고 리스트 맨 앞에 추가합니다.
    Adds a new item to the front of the inventory list.
    """
    # TODO 1: item을 리스트의 맨 앞(인덱스 0)에 삽입하세요.
    #         Insert item at the front of the list (index 0).
    #         힌트 / Hint: insert(0, item)

    # TODO 2: 입고 완료 메시지와 현재 재고를 출력하세요.
    #         Print a restock confirmation message with the current inventory.
    #         예시 / Example: "사과 입고 완료! 현재 재고: ['사과']"
    #                         "Apples restocked! Current inventory: ['Apples']"
    pass


def ship(inventory: list) -> str:
    """
    재고 맨 뒤의 물건을 꺼내서 반환합니다.
    Removes and returns the last item in the inventory.
    """
    # TODO 1: 재고가 비어 있는지 확인하세요.
    #         Check if the inventory is empty.
    #         힌트 / Hint: len(inventory) == 0

    # TODO 2: 비어 있으면 실패 메시지를 출력하고 None을 반환하세요.
    #         If empty, print a failure message and return None.

    # TODO 3: 비어 있지 않으면 맨 뒤 항목을 꺼내세요.
    #         If not empty, remove and get the last item.
    #         힌트 / Hint: pop() — 꺼내면서 리스트에서도 제거됩니다!
    #                              removes the item AND returns it!

    # TODO 4: 출고 완료 메시지를 출력하고, 꺼낸 항목을 반환하세요.
    #         Print a shipment confirmation message and return the item.
    pass


def check_stock(inventory: list, threshold: int = 3) -> None:
    """
    재고 수량을 확인하고 부족하면 경고를 출력합니다.
    Checks stock level and prints a warning if below threshold.
    """
    # TODO 1: 현재 재고 수량을 구하세요.
    #         Get the current stock count.
    #         힌트 / Hint: len(inventory)

    # TODO 2: 재고가 threshold보다 적으면 경고 메시지를 출력하세요.
    #         If stock count is less than threshold, print a warning.
    #         예시 / Example: "⚠️ 재고 부족 경고! 현재 2개 남음 (기준: 3개)"
    #                         "⚠️ Low stock warning! 2 item(s) left (threshold: 3)"

    # TODO 3: 재고가 충분하면 양호 메시지를 출력하세요.
    #         Otherwise, print an OK message.
    #         예시 / Example: "✅ 재고 양호. 현재 5개 보유 중"
    #                         "✅ Stock OK. Currently holding 5 item(s)"
    pass


def get_oldest(inventory: list) -> str:
    """
    가장 오래된 물건(맨 뒤 항목)의 이름을 반환합니다.
    Returns the name of the oldest item (last item in the list).
    """
    # TODO 1: 재고가 비어 있는지 확인하세요.
    #         Check if the inventory is empty.

    # TODO 2: 비어 있으면 메시지를 출력하고 None을 반환하세요.
    #         If empty, print a message and return None.

    # TODO 3: 비어 있지 않으면 마지막 항목을 반환하세요.
    #         If not empty, return the last item.
    #         힌트 / Hint: inventory[-1] 또는 inventory[len(inventory) - 1]
    #                      inventory[-1] or inventory[len(inventory) - 1]
    #         ⚠️  pop()을 쓰면 안 돼요! 꺼내는 게 아니라 확인만 해야 합니다.
    #             Don't use pop() here! You're just looking, not removing.
    pass


# ============================================================
# 🌟 보너스 챌린지 / Bonus Challenges
# 기본 과제를 모두 마친 후 시도해보세요!
# Try these only after finishing the main tasks!
# ============================================================


def show_inventory(inventory: list) -> None:
    """
    🥉 Easy Bonus
    현재 재고를 번호와 함께 출력합니다 (최신 → 오래된 순).
    Prints the current inventory with numbers (newest → oldest).
    """
    # TODO 1: 재고가 비어 있는지 확인하고, 비어 있으면 안내 메시지를 출력하세요.
    #         Check if empty and print a message if so.

    # TODO 2: 구분선과 헤더를 출력하세요.
    #         Print a separator line and header.
    #         힌트 / Hint: "=" * 29 로 구분선을 만들 수 있어요!

    # TODO 3: 반복문으로 각 항목을 번호와 함께 출력하세요.
    #         Loop through and print each item with its number.
    #         힌트 / Hint: 첫 번째 항목에는 "(최신 / newest)", 마지막에는 "(가장 오래됨 / oldest)" 표시

    # TODO 4: 총 수량을 출력하세요.
    #         Print the total count.
    pass


def bulk_restock(inventory: list, items: list) -> None:
    """
    🥈 Medium Bonus
    물건 리스트를 순서대로 한 번에 입고합니다.
    Restocks a list of items one by one, in order.

    restock()을 재사용해야 합니다!
    You must reuse restock()!
    """
    # TODO 1: items 리스트의 각 항목에 대해 restock()을 호출하세요.
    #         Call restock() for each item in items.

    # TODO 2: 전체 입고가 끝난 후 check_stock()을 자동으로 실행하세요.
    #         After all items are restocked, automatically run check_stock().
    pass


def ship_until_low(inventory: list, threshold: int) -> None:
    """
    🥇 Hard Bonus
    재고가 threshold개가 될 때까지 계속 출고합니다.
    Keeps shipping items until stock reaches threshold.
    """
    # TODO 1: 현재 재고가 이미 threshold 이하인지 확인하세요.
    #         Check if stock is already at or below threshold.
    #         그렇다면 메시지를 출력하고 함수를 끝내세요.
    #         If so, print a message and return early.

    # TODO 2: 출고 횟수를 추적할 카운터 변수를 만드세요.
    #         Create a counter variable to track how many items were shipped.

    # TODO 3: while 반복문으로 재고가 threshold보다 많은 동안 계속 출고하세요.
    #         Use a while loop to keep shipping while stock is above threshold.
    #         힌트 / Hint: while len(inventory) > threshold:
    #         힌트 / Hint: ship()을 재사용하세요! / reuse ship()!

    # TODO 4: 총 출고 수량과 남은 재고를 출력하세요.
    #         Print total shipped count and remaining stock.
    pass


# ============================================================
# 🎪 테스트 코드 / Test Code
# 아래 코드를 실행해서 함수가 잘 작동하는지 확인하세요!
# Run the code below to check if your functions work!
# ============================================================

if __name__ == "__main__":
    print("=" * 45)
    print("테스트 1: 입고 / Test 1: Restocking")
    print("=" * 45)
    inventory = []
    restock(inventory, "사과 / Apples")
    restock(inventory, "바나나 / Bananas")
    restock(inventory, "딸기 / Strawberries")
    restock(inventory, "포도 / Grapes")
    restock(inventory, "수박 / Watermelon")

    print()
    print("=" * 45)
    print("테스트 2: 재고 확인 / Test 2: Stock check")
    print("=" * 45)
    check_stock(inventory, 3)
    # 예상 / Expected: ✅ Stock OK. Currently holding 5 item(s)

    print()
    print("=" * 45)
    print("테스트 3: 가장 오래된 항목 / Test 3: Oldest item")
    print("=" * 45)
    print(get_oldest(inventory))
    # 예상 / Expected: 사과 / Apples

    print()
    print("=" * 45)
    print("테스트 4: 출고 / Test 4: Shipping")
    print("=" * 45)
    print(ship(inventory))
    print(ship(inventory))
    check_stock(inventory, 3)
    # 예상 / Expected: ⚠️ Low stock warning! 3 item(s) left (threshold: 3)?
    # 🤔 3개 남았을 때 경고가 떠야 할까요? / Should 3 items trigger a warning?

    print()
    print("=" * 45)
    print("테스트 5: 빈 창고 / Test 5: Empty inventory")
    print("=" * 45)
    empty = []
    print(ship(empty))
    print(get_oldest(empty))

    print()
    print("=" * 45)
    print("🥉 보너스 Easy / Bonus Easy")
    print("=" * 45)
    show_inventory(inventory)

    print()
    print("=" * 45)
    print("🥈 보너스 Medium / Bonus Medium")
    print("=" * 45)
    bulk_restock(inventory, ["키위 / Kiwi", "망고 / Mango", "파인애플 / Pineapple"])

    print()
    print("=" * 45)
    print("🥇 보너스 Hard / Bonus Hard")
    print("=" * 45)
    ship_until_low(inventory, 2)
    ship_until_low(inventory, 10)   # 이미 threshold 이하 / already below threshold
