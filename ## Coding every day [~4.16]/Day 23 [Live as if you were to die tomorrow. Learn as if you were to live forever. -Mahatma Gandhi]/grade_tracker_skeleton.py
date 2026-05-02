# 📊 Grade Tracker - Completed Code
# 성적 분석기 - 완성된 코드

def get_highest(scores: list) -> int:
    """
    리스트에서 가장 높은 점수를 반환합니다.
    Returns the highest score in the list.
    """
    highest = scores[0]  # 초기화 (Initialization)
    for score in scores:
        if score > highest:
            highest = score
    return highest


def get_lowest(scores: list) -> int:
    """
    리스트에서 가장 낮은 점수를 반환합니다.
    Returns the lowest score in the list.
    """
    lowest = scores[0]
    for score in scores:
        if score < lowest:
            lowest = score
    return lowest


def get_average(scores: list) -> float:
    """
    리스트의 평균 점수를 계산하여 반환합니다.
    Calculates and returns the average score.
    """
    total = 0  # 누적합 변수 (Accumulator variable)
    for score in scores:
        total = total + score
    return total / len(scores)


def get_failing(scores: list, passing_score: int = 60) -> list:
    """
    passing_score 미만인 점수들의 리스트를 반환합니다.
    Returns a new list of scores below passing_score.
    """
    failing_scores = []
    for score in scores:
        if score < passing_score:
            failing_scores.append(score)
    return failing_scores


# ============================================================
# 🌟 보너스 챌린지 / Bonus Challenges
# ============================================================

def print_report(scores: list, passing_score: int = 60) -> None:
    """
    🥉 Easy Bonus
    성적 분석 리포트를 출력합니다.
    Prints a formatted grade analysis report.
    """
    highest = get_highest(scores)
    lowest = get_lowest(scores)
    average = get_average(scores)
    failing = get_failing(scores, passing_score)

    print("=" * 34)
    print("📋 Grade Analysis Report")
    print("=" * 34)
    print(f"Highest Score : {highest}")
    print(f"Lowest Score  : {lowest}")
    print(f"Average Score : {average:.2f}")
    print(f"Failing Scores: {failing}")
    print("=" * 34)


def get_grade(score: int) -> str:
    """
    🥈 Medium Bonus
    점수를 학점 문자열로 변환합니다.
    Converts a score to a letter grade string.
    """
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def get_curved_scores(scores: list, target_average: float) -> list:
    """
    🥇 Hard Bonus
    목표 평균이 되도록 커브를 적용한 새 점수 리스트를 반환합니다.
    Returns a new list with curved scores to reach the target average.
    """
    current_average = get_average(scores)
    curve_amount = target_average - current_average
    
    curved_scores = []
    
    # 1. 새 점수 리스트 생성
    for score in scores:
        curved_scores.append(score + curve_amount)
        
    # 2. 100점 초과 검사 (Validation)
    for score in curved_scores:
        if score > 100:
            print("Error: Curve would result in a score over 100!")
            return None
            
    return curved_scores

# ============================================================
# 🎪 테스트 코드 / Test Code
# ============================================================

if __name__ == "__main__":
    print("=" * 40)
    print("테스트 1: 기본 케이스 / Test 1: Basic case")
    print("=" * 40)
    scores = [85, 92, 78, 60, 45, 99, 72, 55]
    print(get_highest(scores))      # 예상 / Expected: 99
    print(get_lowest(scores))       # 예상 / Expected: 45
    print(get_average(scores))      # 예상 / Expected: 73.25
    print(get_failing(scores, 60))  # 예상 / Expected: [45, 55]

    print()
    print("=" * 40)
    print("테스트 2: 점수 하나 / Test 2: Single score")
    print("=" * 40)
    single = [77]
    print(get_highest(single))      # 예상 / Expected: 77
    print(get_lowest(single))       # 예상 / Expected: 77
    print(get_average(single))      # 예상 / Expected: 77.0

    print()
    print("=" * 40)
    print("테스트 3: 모두 합격 / Test 3: All passing")
    print("=" * 40)
    all_pass = [70, 80, 90]
    print(get_failing(all_pass, 60))  # 예상 / Expected: []

    print()
    print("=" * 40)
    print("테스트 4: 모두 같은 점수 / Test 4: All same")
    print("=" * 40)
    same = [75, 75, 75]
    print(get_highest(same))        # 예상 / Expected: 75
    print(get_lowest(same))         # 예상 / Expected: 75
    print(get_average(same))        # 예상 / Expected: 75.0

    print()
    print("=" * 40)
    print("🥉 보너스 Easy / Bonus Easy")
    print("=" * 40)
    print_report([85, 92, 78, 60, 45, 99, 72, 55], 60)

    print()
    print("=" * 40)
    print("🥈 보너스 Medium / Bonus Medium")
    print("=" * 40)
    print(get_grade(95))   # 예상 / Expected: A
    print(get_grade(83))   # 예상 / Expected: B
    print(get_grade(72))   # 예상 / Expected: C
    print(get_grade(60))   # 예상 / Expected: D
    print(get_grade(45))   # 예상 / Expected: F

    print()
    print("=" * 40)
    print("🥇 보너스 Hard / Bonus Hard")
    print("=" * 40)
    print(get_curved_scores([50, 60, 70, 80], 75))        # 예상 / Expected: [60.0, 70.0, 80.0, 90.0]
    print(get_curved_scores([80, 90, 95, 100], 100))      # 예상 / Expected: None