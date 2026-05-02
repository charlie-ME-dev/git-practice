# 🌡️ Sensor Data Cleaner - Skeleton Code
# 센서 데이터 정리기 - 뼈대 코드

# ============================================================
# 함수를 완성하세요! Complete each function below.
# 각 TODO 주석을 읽고 코드를 채워 넣으세요.
# Read each TODO comment and fill in the code.
# ============================================================


def is_valid(reading: float, min_val: float, max_val: float) -> bool:
    """
    측정값이 유효한 범위 안에 있는지 확인합니다.
    Checks whether a reading falls within the valid range.

    유효 조건: min_val 이상 AND max_val 이하
    Valid condition: reading >= min_val AND reading <= max_val
    """
    # TODO 1: reading이 min_val 이상이고 max_val 이하인지 확인하세요.
    #         Check if reading is >= min_val AND <= max_val.
    #         힌트 / Hint: 두 조건을 and로 연결하세요 / connect two conditions with and

    # TODO 2: 조건을 만족하면 True, 아니면 False를 반환하세요.
    #         Return True if valid, False otherwise.
    #         힌트 / Hint: 조건식 자체가 이미 True/False를 반환해요!
    #                      The condition expression itself returns True/False!
    pass


def clean_readings(readings: list, min_val: float, max_val: float) -> list:
    """
    유효하지 않은 값을 걸러낸 새 리스트를 반환합니다.
    Returns a new list with all invalid readings removed.

    is_valid()를 반드시 재사용하세요!
    You must reuse is_valid()!
    """
    # TODO 1: 결과를 담을 빈 리스트를 만드세요.
    #         Create an empty list to store valid readings.

    # TODO 2: 반복문으로 readings의 모든 값을 확인하세요.
    #         Loop through every reading in readings.

    # TODO 3: is_valid()로 각 값을 확인하고, 유효하면 결과 리스트에 추가하세요.
    #         Use is_valid() to check each value; if valid, append to result.
    #         힌트 / Hint: if is_valid(reading, min_val, max_val):

    # TODO 4: 완성된 결과 리스트를 반환하세요.
    #         Return the completed result list.
    pass


def count_errors(readings: list, min_val: float, max_val: float) -> int:
    """
    오류 값의 개수를 세어 반환합니다.
    Counts and returns the number of invalid readings.

    is_valid()를 반드시 재사용하세요!
    You must reuse is_valid()!
    """
    # TODO 1: 오류 개수를 세는 카운터 변수를 0으로 초기화하세요.
    #         Create a counter variable set to 0.

    # TODO 2: 반복문으로 모든 값을 확인하세요.
    #         Loop through every reading.

    # TODO 3: is_valid()가 False인 값마다 카운터를 1 증가시키세요.
    #         For each reading where is_valid() returns False, add 1 to counter.
    #         힌트 / Hint: if not is_valid(reading, min_val, max_val):

    # TODO 4: 최종 카운터를 반환하세요.
    #         Return the final counter.
    pass


def error_rate(readings: list, min_val: float, max_val: float) -> float:
    """
    전체 측정값 중 오류 비율(%)을 반환합니다.
    Returns the percentage of readings that are errors.

    count_errors()를 재사용하세요!
    Reuse count_errors()!
    """
    # TODO 1: 리스트가 비어 있으면 0.0을 반환하세요.
    #         If the list is empty, return 0.0.
    #         힌트 / Hint: len(readings) == 0
    #         왜? / Why? 빈 리스트를 0으로 나누면 에러가 납니다!
    #                    Dividing by 0 causes an error!

    # TODO 2: count_errors()로 오류 개수를 구하세요.
    #         Get the error count using count_errors().

    # TODO 3: 오류 개수 / 전체 개수 * 100 을 계산해서 반환하세요.
    #         Calculate and return: error_count / total_count * 100
    pass


# ============================================================
# 🌟 보너스 챌린지 / Bonus Challenges
# 기본 과제를 모두 마친 후 시도해보세요!
# Try these only after finishing the main tasks!
# ============================================================


def print_summary(readings: list, min_val: float, max_val: float) -> None:
    """
    🥉 Easy Bonus
    센서 데이터 분석 리포트를 출력합니다.
    Prints a formatted sensor data analysis report.

    네 함수를 모두 활용해야 합니다!
    You must use all four functions above!
    """
    # TODO 1: clean_readings(), count_errors(), error_rate()를 호출하세요.
    #         Call clean_readings(), count_errors(), and error_rate().

    # TODO 2: 구분선과 함께 결과를 보기 좋게 출력하세요.
    #         Print the results in a nicely formatted report with separator lines.
    #         힌트 / Hint: "=" * 41 로 구분선을 만들 수 있어요!
    pass


def get_stats(readings: list, min_val: float, max_val: float) -> dict:
    """
    🥈 Medium Bonus
    정제된 데이터의 최솟값, 최댓값, 평균을 딕셔너리로 반환합니다.
    Returns min, max, and average of cleaned data as a dictionary.

    min(), max(), sum() 사용 금지! 반복문으로 직접 계산하세요.
    No min(), max(), or sum()! Calculate with loops.
    """
    # TODO 1: clean_readings()로 먼저 정제하세요.
    #         Clean the data first using clean_readings().

    # TODO 2: 정제 후 데이터가 없으면 None을 반환하세요.
    #         If no valid data remains, return None.

    # TODO 3: 반복문으로 최솟값, 최댓값, 합계를 계산하세요.
    #         Use a loop to find min, max, and total sum.
    #         힌트 / Hint: cleaned[0]으로 시작값을 설정하세요 / use cleaned[0] as starting value

    # TODO 4: 평균을 계산하고 딕셔너리로 반환하세요.
    #         Calculate average and return as a dictionary.
    #         형식 / Format: {"min": ..., "max": ..., "average": ...}
    pass


def find_error_streaks(readings: list, min_val: float, max_val: float) -> list:
    """
    🥇 Hard Bonus
    연속 오류 구간의 길이를 리스트로 반환합니다.
    Returns a list of lengths of consecutive error runs.
    """
    # TODO 1: 결과 리스트와 현재 연속 오류 길이를 추적하는 변수를 만드세요.
    #         Create a result list and a variable to track the current streak length.
    #         힌트 / Hint: streaks = [], current_streak = 0

    # TODO 2: 반복문으로 모든 값을 확인하세요.
    #         Loop through every reading.

        # TODO 3: 오류 값이면 current_streak을 1 증가시키세요.
        #         If it's an error, increment current_streak by 1.

        # TODO 4: 유효한 값이면, current_streak이 0보다 크면 streaks에 추가하고
        #         current_streak을 0으로 초기화하세요.
        #         If it's valid AND current_streak > 0, append to streaks and reset to 0.

    # TODO 5: 반복이 끝난 후, 마지막에 오류로 끝난 경우를 처리하세요.
    #         After the loop, handle the case where the list ends on an error streak.
    #         힌트 / Hint: if current_streak > 0: streaks.append(current_streak)

    # TODO 6: 결과 리스트를 반환하세요.
    #         Return the result list.
    pass


# ============================================================
# 🎪 테스트 코드 / Test Code
# 아래 코드를 실행해서 함수가 잘 작동하는지 확인하세요!
# Run the code below to check if your functions work!
# ============================================================

if __name__ == "__main__":
    min_val = -10
    max_val = 120

    print("=" * 45)
    print("테스트 1: is_valid 경계값 / Test 1: Boundary checks")
    print("=" * 45)
    print(is_valid(-10, min_val, max_val))    # 예상 / Expected: True
    print(is_valid(-10.1, min_val, max_val))  # 예상 / Expected: False
    print(is_valid(120, min_val, max_val))    # 예상 / Expected: True
    print(is_valid(120.1, min_val, max_val))  # 예상 / Expected: False

    print()
    print("=" * 45)
    print("테스트 2: 기본 정제 / Test 2: Basic cleaning")
    print("=" * 45)
    readings = [23.5, -999.0, 45.2, 87.1, 999.9, 30.0, -50.0, 101.3]
    print(clean_readings(readings, min_val, max_val))
    # 예상 / Expected: [23.5, 45.2, 87.1, 30.0, 101.3]

    print()
    print("=" * 45)
    print("테스트 3: 오류 통계 / Test 3: Error statistics")
    print("=" * 45)
    print(count_errors(readings, min_val, max_val))  # 예상 / Expected: 3
    print(error_rate(readings, min_val, max_val))    # 예상 / Expected: 37.5

    print()
    print("=" * 45)
    print("테스트 4: 오류 없음 / Test 4: No errors")
    print("=" * 45)
    clean_data = [10.0, 50.0, 90.0]
    print(count_errors(clean_data, min_val, max_val))  # 예상 / Expected: 0
    print(error_rate(clean_data, min_val, max_val))    # 예상 / Expected: 0.0

    print()
    print("=" * 45)
    print("테스트 5: 전부 오류 / Test 5: All errors")
    print("=" * 45)
    all_errors = [-999.0, 999.9, -500.0]
    print(count_errors(all_errors, min_val, max_val))  # 예상 / Expected: 3
    print(error_rate(all_errors, min_val, max_val))    # 예상 / Expected: 100.0

    print()
    print("=" * 45)
    print("테스트 6: 빈 리스트 / Test 6: Empty list")
    print("=" * 45)
    print(error_rate([], min_val, max_val))            # 예상 / Expected: 0.0

    print()
    print("=" * 45)
    print("🥉 보너스 Easy / Bonus Easy")
    print("=" * 45)
    print_summary(readings, min_val, max_val)

    print()
    print("=" * 45)
    print("🥈 보너스 Medium / Bonus Medium")
    print("=" * 45)
    print(get_stats([23.5, -999.0, 45.2, 87.1, 999.9, 30.0], -10, 120))
    # 예상 / Expected: {"min": 23.5, "max": 87.1, "average": 46.5}
    print(get_stats([-999.0, 999.9], -10, 120))
    # 예상 / Expected: None

    print()
    print("=" * 45)
    print("🥇 보너스 Hard / Bonus Hard")
    print("=" * 45)
    print(find_error_streaks([10, -999, -888, 50, 70, -777, -666, -555, 30], -10, 120))
    # 예상 / Expected: [2, 3]
    print(find_error_streaks([10, 20, 30], -10, 120))
    # 예상 / Expected: []
    print(find_error_streaks([-999, 10, -888, -777], -10, 120))
    # 예상 / Expected: [1, 2]  ← 끝이 오류로 끝나는 경우!
