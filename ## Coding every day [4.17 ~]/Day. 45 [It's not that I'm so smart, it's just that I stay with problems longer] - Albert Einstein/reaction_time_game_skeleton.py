"""
반응 속도 게임 / Reaction Time Game

목표 / Goal:
- KO: time 모듈을 사용하여 사용자의 반응 속도를 측정하는 게임을 만든다
- EN: Build a game that measures the user's reaction time using the time module
"""

# TODO 1:
# KO: time 모듈과 random 모듈을 import 하세요
# EN: Import the time module and the random module
# (여기에 import 문 작성 / Write your import statements here)


def measure_reaction_time():
    """
    KO: 사용자가 Enter를 누르기까지 걸린 시간을 측정해서 반환한다
    EN: Measure how long it takes the user to press Enter, then return it
    """
    # TODO 2:
    # KO: 현재 시각을 start_time 변수에 저장 (time.time() 사용)
    # EN: Save the current time in the start_time variable (use time.time())
    start_time = 0.0

    # TODO 3:
    # KO: input() 함수로 사용자가 Enter를 누를 때까지 기다린다
    #     (input의 결과는 사용하지 않으므로 변수에 저장 안 해도 됨)
    # EN: Use input() to wait for the user to press Enter
    #     (We don't need the result, so no variable assignment needed)


    # TODO 4:
    # KO: 현재 시각을 end_time 변수에 저장
    # EN: Save the current time in the end_time variable
    end_time = 0.0

    # TODO 5:
    # KO: 경과 시간(elapsed)을 계산해서 반환
    #     elapsed = end_time - start_time
    # EN: Calculate the elapsed time and return it
    #     elapsed = end_time - start_time
    elapsed = 0.0
    return elapsed


def rate_reaction(elapsed):
    """
    KO: 반응 속도(초)를 받아서 등급 문자열을 반환한다
    EN: Take the reaction time (in seconds), return a rating string

    등급 기준 / Rating thresholds:
    - < 0.25s  →  "⚡ 번개처럼 빠름! / Lightning fast!"
    - < 0.40s  →  "🚀 빠름! / Fast!"
    - < 0.60s  →  "👍 평균 / Average"
    - else     →  "🐢 다시 도전! / Try again!"
    """
    # TODO 6:
    # KO: if / elif / else 문을 사용해서 elapsed 값에 따라 등급 문자열을 반환
    # EN: Use if / elif / else to return the rating string based on elapsed
    rating = ""
    return rating


def play_reaction_game():
    """
    KO: 반응 속도 게임 전체를 실행한다
    EN: Run the full reaction time game
    """
    # TODO 7:
    # KO: "준비... / Get ready..." 메시지 출력
    # EN: Print the "Get ready..." message


    # TODO 8:
    # KO: 1.0초에서 3.0초 사이의 랜덤한 대기 시간을 만든다 (random.uniform 사용)
    # EN: Generate a random delay between 1.0 and 3.0 seconds (use random.uniform)
    delay = 0.0

    # TODO 9:
    # KO: time.sleep()을 사용해서 delay 만큼 프로그램을 멈춘다
    # EN: Use time.sleep() to pause the program for `delay` seconds


    # TODO 10:
    # KO: "GO! (Enter를 누르세요)" 메시지 출력
    # EN: Print "GO! (press Enter)"


    # TODO 11:
    # KO: measure_reaction_time() 함수를 호출해서 elapsed에 저장
    # EN: Call measure_reaction_time() and save the result in elapsed
    elapsed = 0.0

    # TODO 12:
    # KO: rate_reaction() 함수를 호출해서 등급을 받아 rating에 저장
    # EN: Call rate_reaction() and save the rating
    rating = ""

    # TODO 13:
    # KO: 결과 출력 - 반응 속도는 소수점 셋째 자리까지 (f-string의 :.3f 사용)
    #     예: "반응 속도: 0.342초"
    #         "등급: 🚀 빠름!"
    # EN: Print the results - reaction time to 3 decimal places (use f-string :.3f)
    #     e.g., "Reaction time: 0.342 seconds"
    #           "Rating: 🚀 Fast!"



if __name__ == "__main__":
    # KO: rate_reaction 함수를 먼저 단독 테스트 (게임을 실행하지 않고도 확인 가능)
    # EN: Test rate_reaction alone first (you can verify without running the game)
    print("=== rate_reaction 테스트 / Test ===")
    print(f"0.15초 → {rate_reaction(0.15)}")  # ⚡ 번개처럼 빠름!
    print(f"0.30초 → {rate_reaction(0.30)}")  # 🚀 빠름!
    print(f"0.50초 → {rate_reaction(0.50)}")  # 👍 평균
    print(f"1.00초 → {rate_reaction(1.00)}")  # 🐢 다시 도전!

    print()
    print("=== 경계값 테스트 / Boundary Tests ===")
    print(f"0.25초 → {rate_reaction(0.25)}")  # 🚀 빠름!
    print(f"0.40초 → {rate_reaction(0.40)}")  # 👍 평균
    print(f"0.60초 → {rate_reaction(0.60)}")  # 🐢 다시 도전!

    print()
    print("=== 게임 실행 / Run the Game ===")
    play_reaction_game()
