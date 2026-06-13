"""
random_guessing_game_skeleton.py
숫자 맞히기 게임 / Number Guessing Game

각 함수를 명세에 맞게 완성하세요.
Complete each function according to the spec.
"""

import random


def generate_secret_number(low, high):
    """
    KO: low ~ high 사이의 무작위 정수를 반환합니다 (양 끝 포함).
    EN: Returns a random integer between low and high (both inclusive).
    """
    # TODO (KO): random.randint()를 사용해서 무작위 정수를 만들고 반환하세요.
    # TODO (EN): Use random.randint() to generate a random integer and return it.
    secret = 0
    return secret


def check_guess(guess, secret):
    """
    KO: 추측한 값과 비밀 숫자를 비교해서 "too low", "too high", "correct" 중 하나를 반환합니다.
    EN: Compares guess and secret, returns one of "too low", "too high", or "correct".
    """
    # TODO (KO): if / elif / else를 사용해서 세 가지 경우를 처리하세요.
    # TODO (EN): Use if / elif / else to handle the three cases.
    result = ""
    return result


def flip_coin_until_heads():
    """
    KO: 앞면이 나올 때까지 동전을 던지고, 던진 횟수를 반환합니다.
        random.random() < 0.5 이면 앞면(heads)으로 정합니다.
    EN: Flips a coin until heads appears and returns the number of flips.
        Treat random.random() < 0.5 as heads.
    """
    # TODO (KO): while 루프를 사용해서 앞면이 나올 때까지 계속 던지세요.
    # TODO (EN): Use a while loop to keep flipping until heads appears.
    flip_count = 0
    return flip_count


def play_guessing_game(low, high, max_attempts):
    """
    KO: 비밀 숫자를 만들고, 플레이어로부터 최대 max_attempts번 추측을 받습니다.
        맞히면 사용한 시도 횟수를 반환하고, 실패하면 -1을 반환합니다.
        플레이어 입력은 input()을 사용해서 받으세요.
    EN: Generates a secret number and takes up to max_attempts guesses from the player.
        Returns the number of attempts used if the player wins, or -1 if they fail.
        Use input() to get the player's guesses.
    """
    # TODO (KO): 1) generate_secret_number()로 비밀 숫자를 만드세요.
    # TODO (KO): 2) while 루프 안에서 input()으로 추측을 받고 int()로 변환하세요.
    # TODO (KO): 3) check_guess()로 결과를 확인하고 플레이어에게 알려주세요.
    # TODO (KO): 4) 맞히면 시도 횟수를 반환하고, 실패하면 -1을 반환하세요.

    # TODO (EN): 1) Generate a secret number using generate_secret_number().
    # TODO (EN): 2) Inside a while loop, get a guess with input() and convert with int().
    # TODO (EN): 3) Use check_guess() to check the result and tell the player.
    # TODO (EN): 4) Return attempts used if correct, otherwise return -1.
    secret = 0
    attempts_used = 0
    return -1


if __name__ == "__main__":
    # ──────────────────────────────────────────
    # KO: 아래 코드로 함수들을 테스트할 수 있습니다.
    # EN: Use the code below to test your functions.
    # ──────────────────────────────────────────

    # Test 1: generate_secret_number
    print("=== Test 1: generate_secret_number ===")
    for i in range(5):
        n = generate_secret_number(1, 10)
        print(f"  생성된 숫자 / generated: {n}")

    # Test 2: check_guess
    print("\n=== Test 2: check_guess ===")
    print(f"  check_guess(3, 7) = {check_guess(3, 7)}  (expect: too low)")
    print(f"  check_guess(9, 7) = {check_guess(9, 7)}  (expect: too high)")
    print(f"  check_guess(7, 7) = {check_guess(7, 7)}  (expect: correct)")

    # Test 3: flip_coin_until_heads
    print("\n=== Test 3: flip_coin_until_heads ===")
    for i in range(5):
        flips = flip_coin_until_heads()
        print(f"  앞면까지 / flips until heads: {flips}")

    # Test 4: play_guessing_game
    # KO: 실제 게임을 플레이하려면 아래 줄의 주석을 해제하세요.
    # EN: Uncomment the line below to play the actual game.
    # print("\n=== Test 4: play_guessing_game ===")
    # result = play_guessing_game(1, 10, 5)
    # print(f"  결과 / result: {result}")
