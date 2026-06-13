"""
☕ Drink Class Practice — Skeleton File
   카페 음료 클래스 연습 — 스켈레톤 파일

Fill in each TODO. Run this file to test as you go.
각 TODO를 채우세요. 실행하면서 테스트해보세요.
"""


class Drink:
    def __init__(self, name, size, base_price, add_milk=False):
        # TODO 1: name을 속성으로 저장하세요 / Store name as an attribute
        # 힌트 / Hint: self.name = name
        pass

        # TODO 2: size를 속성으로 저장하세요 / Store size as an attribute

        # TODO 3: base_price를 속성으로 저장하세요 / Store base_price as an attribute

        # TODO 4: add_milk를 속성으로 저장하세요 / Store add_milk as an attribute

        # TODO 5: extra_shots 속성을 0으로 초기화하세요
        #         Initialize extra_shots attribute to 0

    def add_shot(self):
        # TODO 6: self.extra_shots를 1 증가시키세요
        #         Increase self.extra_shots by 1
        pass

    def get_price(self):
        # TODO 7: size_fee를 계산하세요 (Small=0, Medium=500, Large=1000)
        #         Compute size_fee (Small=0, Medium=500, Large=1000)
        size_fee = 0

        # TODO 8: 우유 추가 요금을 계산하세요 (True면 500, 아니면 0)
        #         Compute milk fee (500 if add_milk else 0)
        milk_fee = 0

        # TODO 9: 샷 추가 요금을 계산하세요 (extra_shots × 500)
        #         Compute shot fee (extra_shots × 500)
        shot_fee = 0

        # TODO 10: 최종 가격을 계산해서 반환하세요
        #          Compute and return the total price
        # total = base_price + size_fee + milk_fee + shot_fee
        return 0  # 임시 값 — 수정하세요 / placeholder — fix me

    def describe(self):
        # TODO 11: 우유 여부를 나타내는 문자열을 만드세요
        #          Build a string showing whether milk is added
        # 힌트 / Hint: "with milk" if self.add_milk else "no milk"
        milk_text = ""

        # TODO 12: 다음 형식의 문자열을 반환하세요
        #          Return a string in this format:
        #          "{size} {name} ({milk_text}, +{extra_shots} shot)"
        return ""


# ============================================================
# 테스트 블록 / Test Block — 수정하지 마세요 / Do not modify
# ============================================================
if __name__ == "__main__":
    print("=" * 50)
    print("테스트 시작 / Running tests")
    print("=" * 50)

    try:
        # Test 1
        d1 = Drink("Americano", "Small", 3000)
        print(f"\n[Test 1] Price: {d1.get_price()}원 / Desc: {d1.describe()}")
        print("        Expected: 3000원 / Small Americano (no milk, +0 shot)")

        # Test 2
        d2 = Drink("Latte", "Medium", 4000, add_milk=True)
        print(f"\n[Test 2] Price: {d2.get_price()}원")
        print("        Expected: 5000원")

        # Test 3
        d3 = Drink("Latte", "Large", 4000, add_milk=True)
        d3.add_shot()
        d3.add_shot()
        print(f"\n[Test 3] Price: {d3.get_price()}원 / Desc: {d3.describe()}")
        print("        Expected: 6500원 / Large Latte (with milk, +2 shot)")

        # Test 4: independence
        d4a = Drink("Espresso", "Small", 2500)
        d4b = Drink("Espresso", "Small", 2500)
        d4a.add_shot()
        print(f"\n[Test 4] d4a shots: {d4a.extra_shots} / d4b shots: {d4b.extra_shots}")
        print("        Expected: 1 / 0")

    except AttributeError as e:
        print(f"\n⚠️  AttributeError: {e}")
        print("   __init__에서 속성을 제대로 저장했는지 확인하세요")
        print("   Check that all attributes are stored in __init__")
    except Exception as e:
        print(f"\n⚠️  에러 / Error: {type(e).__name__}: {e}")
