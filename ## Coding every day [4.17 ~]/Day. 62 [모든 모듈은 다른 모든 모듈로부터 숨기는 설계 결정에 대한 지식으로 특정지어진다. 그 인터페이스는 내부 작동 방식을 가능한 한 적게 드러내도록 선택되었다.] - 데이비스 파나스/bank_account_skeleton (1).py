"""
🏦 BankAccount 캡슐화 연습 (Skeleton)
🏦 BankAccount Encapsulation Practice (Skeleton)

핵심 개념 / Core Concept: Name Mangling (이름 맹글링)
- `__attr` 형태의 이중 밑줄 속성은 외부에서 직접 접근 불가
- Double-underscore attributes (`__attr`) cannot be accessed from outside

지시사항 / Instructions:
1. 각 TODO를 순서대로 완성하세요
2. Complete each TODO in order
3. 반드시 `__` (이중 밑줄) 형태로 비공개 속성을 만드세요
4. You MUST use `__` (double underscore) for private attributes
"""


class BankAccount:
    """디지털 지갑 계좌 클래스 / Digital wallet account class"""

    def __init__(self, owner_name: str, initial_deposit: int = 0):
        """
        계좌를 생성합니다 / Create an account
        
        매개변수 / Parameters:
            owner_name: 소유자 이름 / Account owner's name
            initial_deposit: 초기 입금액 (기본값 0) / Initial deposit (default 0)
        """
        # TODO 1: 소유자 이름을 비공개 속성으로 저장하세요 (__owner_name 사용)
        # TODO 1: Store owner_name as a private attribute (use __owner_name)
        pass

        # TODO 2: 잔액을 0으로 초기화하세요 (__balance 사용)
        # TODO 2: Initialize balance to 0 (use __balance)
        pass

        # TODO 3: 계좌 활성 상태를 True로 설정하세요 (__is_active 사용)
        # TODO 3: Set account active status to True (use __is_active)
        pass

        # TODO 4: 초기 입금액이 0보다 크면 deposit() 메서드로 입금하세요
        # TODO 4: If initial_deposit > 0, deposit it using the deposit() method
        pass

    def get_owner_name(self) -> str:
        """소유자 이름을 반환합니다 / Return the owner's name"""
        # TODO 5: __owner_name을 반환하세요
        # TODO 5: Return __owner_name
        pass

    def get_balance(self) -> int:
        """현재 잔액을 반환합니다 / Return the current balance"""
        # TODO 6: __balance를 반환하세요
        # TODO 6: Return __balance
        pass

    def is_active(self) -> bool:
        """계좌 활성 상태를 반환합니다 / Return whether account is active"""
        # TODO 7: __is_active를 반환하세요
        # TODO 7: Return __is_active
        pass

    def deposit(self, amount: int) -> bool:
        """
        입금을 처리합니다 / Process a deposit
        
        규칙 / Rules:
        - 계좌가 비활성이면 False 반환 / If inactive, return False
        - 금액이 0 이하면 False 반환 / If amount <= 0, return False
        - 그 외에는 잔액 증가 후 True 반환 / Otherwise, increase balance and return True
        """
        # TODO 8: 계좌가 비활성 상태면 False를 반환하세요
        # TODO 8: Return False if account is inactive
        pass

        # TODO 9: 금액이 0 이하면 False를 반환하세요
        # TODO 9: Return False if amount <= 0
        pass

        # TODO 10: __balance에 amount를 더하세요
        # TODO 10: Add amount to __balance
        pass

        # TODO 11: True를 반환하세요
        # TODO 11: Return True
        pass

    def withdraw(self, amount: int) -> bool:
        """
        출금을 처리합니다 / Process a withdrawal
        
        규칙 / Rules:
        - 계좌가 비활성이면 False / If inactive, False
        - 금액이 0 이하면 False / If amount <= 0, False
        - 잔액보다 많으면 False / If exceeds balance, False
        - 그 외에는 잔액 차감 후 True / Otherwise, deduct and return True
        """
        # TODO 12: 계좌가 비활성 상태면 False를 반환하세요
        # TODO 12: Return False if account is inactive
        pass

        # TODO 13: 금액이 0 이하면 False를 반환하세요
        # TODO 13: Return False if amount <= 0
        pass

        # TODO 14: 출금액이 잔액보다 크면 False를 반환하세요
        # TODO 14: Return False if amount > balance
        pass

        # TODO 15: __balance에서 amount를 빼세요
        # TODO 15: Subtract amount from __balance
        pass

        # TODO 16: True를 반환하세요
        # TODO 16: Return True
        pass

    def close_account(self) -> None:
        """계좌를 폐쇄합니다 / Close the account"""
        # TODO 17: __is_active를 False로 설정하세요
        # TODO 17: Set __is_active to False
        pass


# ============================================================
# 🎁 보너스 챌린지 / Bonus Challenges
# ============================================================

# 🥉 EASY: PIN 추가
# 🥉 EASY: Add PIN
# class BankAccountWithPin(BankAccount):
#     def __init__(self, owner_name, pin, initial_deposit=0):
#         # 부모 클래스 초기화 후 PIN 검증 & 저장
#         # Initialize parent, then validate & store PIN
#         pass


# 🥈 MEDIUM: 거래 내역
# 🥈 MEDIUM: Transaction history
# - __history 리스트 추가 / Add __history list
# - deposit/withdraw 시 기록 / Record on each transaction
# - get_history()는 복사본 반환 / get_history() returns a copy


# 🥇 HARD: @property 데코레이터 미리보기
# 🥇 HARD: @property decorator preview
# class ModernBankAccount:
#     @property
#     def balance(self):
#         return self.__balance
#     
#     @balance.setter
#     def balance(self, value):
#         # 음수 검증 / Validate non-negative
#         pass


# ============================================================
# 🎪 테스트 코드 - 수정하지 마세요!
# 🎪 Test Code - DO NOT MODIFY!
# ============================================================

if __name__ == "__main__":
    print("=" * 50)
    print("🧪 테스트 시작 / Starting tests")
    print("=" * 50)

    try:
        # 테스트 1: 기본 생성
        # Test 1: Basic creation
        acc = BankAccount("김민준", 1000)
        assert acc.get_owner_name() == "김민준", "Test 1a failed"
        assert acc.get_balance() == 1000, "Test 1b failed"
        assert acc.is_active() == True, "Test 1c failed"
        print("✅ 테스트 1 통과 / Test 1 passed: 기본 생성 / Basic creation")

        # 테스트 2: 입금
        # Test 2: Deposit
        assert acc.deposit(500) == True, "Test 2a failed"
        assert acc.get_balance() == 1500, "Test 2b failed"
        print("✅ 테스트 2 통과 / Test 2 passed: 입금 / Deposit")

        # 테스트 3: 출금
        # Test 3: Withdraw
        assert acc.withdraw(300) == True, "Test 3a failed"
        assert acc.get_balance() == 1200, "Test 3b failed"
        print("✅ 테스트 3 통과 / Test 3 passed: 출금 / Withdraw")

        # 테스트 4: 잘못된 거래 거부
        # Test 4: Reject invalid transactions
        assert acc.deposit(-100) == False, "Test 4a failed"
        assert acc.deposit(0) == False, "Test 4b failed"
        assert acc.withdraw(-50) == False, "Test 4c failed"
        assert acc.withdraw(99999) == False, "Test 4d failed"
        assert acc.get_balance() == 1200, "Test 4e failed (balance changed!)"
        print("✅ 테스트 4 통과 / Test 4 passed: 유효성 검사 / Validation")

        # 테스트 5: 계좌 폐쇄
        # Test 5: Close account
        acc.close_account()
        assert acc.is_active() == False, "Test 5a failed"
        assert acc.deposit(100) == False, "Test 5b failed"
        assert acc.withdraw(100) == False, "Test 5c failed"
        print("✅ 테스트 5 통과 / Test 5 passed: 계좌 폐쇄 / Account closure")

        # 테스트 6: 🔒 캡슐화 확인 (핵심!)
        # Test 6: 🔒 Encapsulation check (KEY!)
        acc2 = BankAccount("이서연", 5000)
        
        # 직접 접근 차단 / Direct access blocked
        try:
            _ = acc2.__balance
            print("❌ 테스트 6a 실패: __balance가 외부에서 읽힘!")
            print("❌ Test 6a failed: __balance is externally accessible!")
        except AttributeError:
            print("✅ 테스트 6a 통과 / Test 6a passed: __balance 읽기 차단 / __balance read-blocked")
        
        # 외부 할당이 진짜 잔액에 영향 없는지 확인
        # Verify external assignment doesn't affect real balance
        acc2.__balance = 99999999
        assert acc2.get_balance() == 5000, "Test 6b failed: balance was tampered!"
        print("✅ 테스트 6b 통과 / Test 6b passed: 외부 변경 차단 / External tampering blocked")

        # 테스트 7: 초기 입금 없는 계좌
        # Test 7: Account without initial deposit
        acc3 = BankAccount("박지훈")
        assert acc3.get_balance() == 0, "Test 7 failed"
        print("✅ 테스트 7 통과 / Test 7 passed: 빈 계좌 / Empty account")

        print("=" * 50)
        print("🎉 모든 테스트 통과! / All tests passed!")
        print("=" * 50)

    except AssertionError as e:
        print(f"❌ 테스트 실패 / Test failed: {e}")
    except TypeError as e:
        print(f"⚠️  TypeError - 함수가 None을 반환했을 수 있습니다 / Function may have returned None")
        print(f"   상세: {e}")
    except Exception as e:
        print(f"⚠️  예상치 못한 오류 / Unexpected error: {type(e).__name__}: {e}")
