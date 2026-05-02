# ☕ 카페 주문 시스템 | Café Order System
# 이름 | Name: ____________________
# 날짜 | Date: ____________________

# ============================================================
# 전역 변수 — 수정하지 마세요! | Global variables — do not modify!
# ============================================================

MENU = {
    "아메리카노": 4500,
    "카페라떼": 5000,
    "카푸치노": 5500,
    "녹차라떼": 5500,
    "초코라떼": 6000,
}
daily_revenue = 0   # 오늘 하루 총 매출 | today's total revenue (won)
total_orders = 0    # 오늘 하루 총 주문 수량 | today's total drinks ordered


# ────────────────────────────────────────────────────────────
# 함수 1 | Function 1
# ────────────────────────────────────────────────────────────
def get_item_price(item_name: str) -> int:
    """
    메뉴에서 음료 가격을 조회합니다.
    Look up the price of a menu item.

    매개변수 | Parameter:
        item_name (str): 메뉴 음료 이름 | the name of the menu item

    반환값 | Returns:
        int: 해당 음료의 가격 (원) | the price of the item in won
    """
    # TODO 1-1: 전역 변수 MENU에서 item_name의 가격을 가져와 지역 변수에 저장하세요.
    #           (힌트: 딕셔너리에서 값을 꺼낼 때는 MENU[item_name] 형태를 사용해요!)
    # TODO 1-1: Get the price of item_name from the global MENU and store it in a local variable.
    #           (Hint: use MENU[item_name] to access a dictionary value!)
    price = 0  # 이 줄을 수정하세요 | modify this line

    # TODO 1-2: 가격을 반환하세요. | Return the price.
    pass


# ────────────────────────────────────────────────────────────
# 함수 2 | Function 2
# ────────────────────────────────────────────────────────────
def calculate_discounted_price(price: int, discount_rate: float) -> int:
    """
    할인율을 적용한 최종 가격을 계산합니다.
    Calculate the final price after applying a discount.

    매개변수 | Parameters:
        price (int): 원래 가격 | original price
        discount_rate (float): 할인율 (예: 0.1 = 10% 할인) | discount rate (e.g. 0.1 = 10% off)

    반환값 | Returns:
        int: 할인 적용 후 최종 가격 | final price after discount
    """
    # TODO 2-1: 할인 금액을 계산하세요. (price × discount_rate)
    # TODO 2-1: Calculate the discount amount. (price × discount_rate)
    discount_amount = 0  # 이 줄을 수정하세요 | modify this line

    # TODO 2-2: 최종 가격을 계산하세요. (원래 가격 - 할인 금액)
    # TODO 2-2: Calculate the final price. (original price - discount amount)
    final_price = 0  # 이 줄을 수정하세요 | modify this line

    # TODO 2-3: 최종 가격을 int로 변환해서 반환하세요.
    # TODO 2-3: Return the final price converted to int.
    pass


# ────────────────────────────────────────────────────────────
# 함수 3 | Function 3
# ────────────────────────────────────────────────────────────
def place_order(item_name: str, quantity: int) -> str:
    """
    주문을 접수하고 전역 매출 변수를 업데이트합니다.
    Record an order and update the global sales variables.

    매개변수 | Parameters:
        item_name (str): 주문한 음료 이름 | name of the ordered drink
        quantity (int): 주문 수량 | number of drinks ordered

    반환값 | Returns:
        str: 주문 내역 문자열 | order summary string
             예: "아메리카노 x2 = 9000원"
    """
    # TODO 3-1: daily_revenue와 total_orders를 수정할 것임을 Python에 알리세요.
    #           (힌트: global 키워드를 사용하세요! 두 변수를 한 줄에 선언할 수 있어요)
    # TODO 3-1: Tell Python you are going to modify daily_revenue and total_orders.
    #           (Hint: use the global keyword! You can declare both on one line)

    # TODO 3-2: MENU에서 item_name의 가격을 가져오세요.
    # TODO 3-2: Get the price of item_name from MENU.
    item_price = 0  # 이 줄을 수정하세요 | modify this line

    # TODO 3-3: 이번 주문의 총금액을 계산하세요. (item_price × quantity)
    # TODO 3-3: Calculate the total for this order. (item_price × quantity)
    order_total = 0  # 이 줄을 수정하세요 | modify this line

    # TODO 3-4: daily_revenue에 order_total을 더하세요.
    # TODO 3-4: Add order_total to daily_revenue.

    # TODO 3-5: total_orders에 quantity를 더하세요.
    # TODO 3-5: Add quantity to total_orders.

    # TODO 3-6: 주문 내역 문자열을 반환하세요.
    #           형식: "아메리카노 x2 = 9000원"
    # TODO 3-6: Return the order summary string.
    #           Format: "아메리카노 x2 = 9000원"
    pass


# ────────────────────────────────────────────────────────────
# 함수 4 | Function 4
# ────────────────────────────────────────────────────────────
def reset_daily_sales() -> str:
    """
    하루 매출을 초기화합니다 (영업 마감).
    Reset the daily sales totals (end of business day).

    반환값 | Returns:
        str: 초기화 완료 메시지 | completion message
    """
    # TODO 4-1: daily_revenue와 total_orders를 수정할 것임을 Python에 알리세요.
    # TODO 4-1: Declare that you will modify daily_revenue and total_orders.

    # TODO 4-2: daily_revenue를 0으로 초기화하세요.
    # TODO 4-2: Reset daily_revenue to 0.

    # TODO 4-3: total_orders를 0으로 초기화하세요.
    # TODO 4-3: Reset total_orders to 0.

    # TODO 4-4: "하루 매출이 초기화되었습니다."를 반환하세요.
    # TODO 4-4: Return "하루 매출이 초기화되었습니다."
    pass


# ============================================================
# 테스트 코드 — 수정하지 마세요! | Test code — do not modify!
# ============================================================
if __name__ == "__main__":
    print("=" * 50)
    print("테스트 1: 가격 조회 | Test 1: Price Lookup")
    print("=" * 50)
    print(get_item_price("아메리카노"))   # 예상 | Expected: 4500
    print(get_item_price("카페라떼"))     # 예상 | Expected: 5000
    print(get_item_price("초코라떼"))     # 예상 | Expected: 6000

    print("\n" + "=" * 50)
    print("테스트 2: 할인 계산 | Test 2: Discount Calculation")
    print("=" * 50)
    print(calculate_discounted_price(5000, 0.1))  # 예상 | Expected: 4500
    print(calculate_discounted_price(6000, 0.2))  # 예상 | Expected: 4800
    print(calculate_discounted_price(4500, 0.0))  # 예상 | Expected: 4500

    print("\n" + "=" * 50)
    print("테스트 3: 주문 접수 | Test 3: Placing Orders")
    print("=" * 50)
    print(place_order("아메리카노", 2))   # 예상 | Expected: 아메리카노 x2 = 9000원
    print(place_order("카페라떼", 1))     # 예상 | Expected: 카페라떼 x1 = 5000원
    print(f"오늘 매출: {daily_revenue}원, 총 주문: {total_orders}잔")
    # 예상 | Expected: 오늘 매출: 14000원, 총 주문: 3잔

    print("\n" + "=" * 50)
    print("테스트 4: 하루 마감 | Test 4: End of Day Reset")
    print("=" * 50)
    print(reset_daily_sales())            # 예상 | Expected: 하루 매출이 초기화되었습니다.
    print(f"초기화 후 매출: {daily_revenue}원, 주문: {total_orders}잔")
    # 예상 | Expected: 초기화 후 매출: 0원, 주문: 0잔
