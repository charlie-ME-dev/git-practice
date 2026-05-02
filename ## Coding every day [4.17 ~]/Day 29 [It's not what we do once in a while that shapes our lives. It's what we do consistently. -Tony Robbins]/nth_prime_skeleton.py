"""
🐍 Python 연습: 10,001번째 소수를 찾아라!
🐍 Python Practice: Find the 10,001st Prime!

과제 / Task:
  1. is_prime(num) 함수를 완성하세요
     Complete the is_prime(num) function
  2. nth_prime(n) 함수를 완성하세요
     Complete the nth_prime(n) function

규칙 / Rules:
  - import 사용 금지 / No import statements
  - 변수명은 snake_case / Use snake_case for variable names
"""


def is_prime(num: int) -> bool:
    """
    숫자가 소수인지 판별합니다.
    Check whether a number is prime.

    소수: 1과 자기 자신으로만 나누어지는 2 이상의 자연수
    Prime: an integer >= 2 that is only divisible by 1 and itself.
    """
    # TODO: 2보다 작은 수는 소수가 아닙니다. False를 반환하세요.
    # TODO: Numbers less than 2 are not prime. Return False.

    # TODO: 2부터 num - 1까지 반복하면서 나누어떨어지는지 확인
    # TODO: Loop from 2 to num - 1 and check if any divides evenly

    # TODO: 나누어떨어지는 숫자가 있으면 소수가 아님 → False
    # TODO: If any number divides evenly, not prime → return False

    # TODO: 아무것도 나누어떨어지지 않았다면 소수 → True
    # TODO: If nothing divides evenly, it's prime → return True

    pass


def nth_prime(n: int) -> int:
    """
    n번째 소수를 반환합니다.
    Return the n-th prime number.

    예 / Example: nth_prime(6) == 13
    """
    # TODO: 지금까지 찾은 소수의 개수를 저장할 변수
    # TODO: A variable to count how many primes have been found so far
    prime_count = 0

    # TODO: 현재 확인 중인 숫자
    # TODO: The number currently being checked
    candidate = 1

    # TODO: prime_count가 n이 될 때까지 반복
    # TODO: Loop until prime_count reaches n
    # 힌트 / Hint: while 반복문 사용 / Use a while loop

    # TODO: candidate를 1씩 증가시키며 소수인지 확인
    # TODO: Increase candidate by 1 and check if it's prime

    # TODO: 소수라면 prime_count를 1 증가
    # TODO: If it is prime, increase prime_count by 1

    # TODO: prime_count == n이 되면 candidate를 반환
    # TODO: When prime_count == n, return candidate

    pass


# ============================================================
# ⚠️ 아래 코드는 수정하지 마세요! / DO NOT MODIFY BELOW! ⚠️
# ============================================================
if __name__ == "__main__":
    print("=== is_prime 테스트 / Tests ===")
    print(f"is_prime(2)  = {is_prime(2)}   (기대값/Expected: True)")
    print(f"is_prime(4)  = {is_prime(4)}   (기대값/Expected: False)")
    print(f"is_prime(17) = {is_prime(17)}  (기대값/Expected: True)")
    print(f"is_prime(1)  = {is_prime(1)}   (기대값/Expected: False)")
    print(f"is_prime(0)  = {is_prime(0)}   (기대값/Expected: False)")
    print(f"is_prime(25) = {is_prime(25)}  (기대값/Expected: False)")

    print("\n=== nth_prime 테스트 / Tests ===")
    print(f"nth_prime(1)  = {nth_prime(1)}   (기대값/Expected: 2)")
    print(f"nth_prime(6)  = {nth_prime(6)}   (기대값/Expected: 13)")
    print(f"nth_prime(10) = {nth_prime(10)}  (기대값/Expected: 29)")
    print(f"nth_prime(25) = {nth_prime(25)}  (기대값/Expected: 97)")

    print("\n=== 최종 목표 / Final Goal ===")
    print(f"nth_prime(10001) = {nth_prime(10001)}")
