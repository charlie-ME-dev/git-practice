"""
JSON 성적 관리 시스템 — 스켈레톤 파일
JSON Grade Management System — Skeleton File

학습 목표 / Learning Goals:
  - json.loads / json.dumps / json.load / json.dump 사용법 익히기
  - 중첩된 딕셔너리/리스트 구조 다루기
  - 파일 입출력과 함께 JSON 사용하기

  - Learn json.loads / json.dumps / json.load / json.dump
  - Work with nested dict/list structures
  - Combine JSON with file I/O
"""

import json


# ============================================================
# 함수 1 / Function 1: parse_class_data
# ============================================================
def parse_class_data(json_text):
    """
    TODO 1.1: JSON 문자열을 Python 딕셔너리로 변환하여 반환하세요.
              힌트: json.loads() 함수를 사용하세요. (s가 붙어있음에 주의!)

    TODO 1.1: Convert the JSON string into a Python dictionary and return it.
              Hint: Use json.loads(). (Note the trailing 's'!)
    """
    # TODO: 여기에 코드 작성 / Write your code here
    pass


# ============================================================
# 함수 2 / Function 2: calculate_student_average
# ============================================================
def calculate_student_average(student):
    """
    TODO 2.1: 학생 딕셔너리에서 "grades" 키를 꺼내세요.
    TODO 2.1: Extract the "grades" key from the student dictionary.

    TODO 2.2: 모든 점수의 합과 개수를 계산하여 평균을 반환하세요.
              힌트: .values()를 사용하면 점수만 꺼낼 수 있습니다.

    TODO 2.2: Compute the sum and count of all scores, then return the average.
              Hint: .values() gives you just the scores.
    """
    # TODO: 여기에 코드 작성 / Write your code here
    grades = None  # ← grades 딕셔너리를 여기에 / put the grades dict here
    average = None  # ← 평균을 계산하여 여기에 / compute the average here
    return average


# ============================================================
# 함수 3 / Function 3: find_top_student
# ============================================================
def find_top_student(class_data):
    """
    TODO 3.1: class_data에서 학생 리스트("students")를 꺼내세요.
    TODO 3.1: Get the list of students from class_data.

    TODO 3.2: 각 학생의 평균을 비교하여 가장 높은 학생의 "name"을 반환하세요.
              힌트: calculate_student_average() 함수를 재사용할 수 있습니다!

    TODO 3.2: Compare each student's average and return the name of the highest.
              Hint: You can reuse calculate_student_average()!
    """
    # TODO: 여기에 코드 작성 / Write your code here
    students = None
    top_name = ""
    top_average = -1  # 어떤 점수보다도 낮은 시작값 / starts lower than any score
    # TODO: students를 반복하면서 비교하세요
    # TODO: Loop through students and compare
    return top_name


# ============================================================
# 함수 4 / Function 4: add_student
# ============================================================
def add_student(class_data, student_id, name, math, english, science):
    """
    TODO 4.1: 새 학생 딕셔너리를 만드세요. 구조는 기존 학생과 동일합니다:
              {"id": ..., "name": ..., "grades": {"math": ..., ...}}

    TODO 4.1: Build a new student dict with the same shape as existing students:
              {"id": ..., "name": ..., "grades": {"math": ..., ...}}

    TODO 4.2: class_data["students"] 리스트의 끝에 추가하세요.
              주의: 새 리스트를 만들지 말고 원본을 수정하세요!

    TODO 4.2: Append it to the end of class_data["students"].
              Warning: Don't create a new list — modify the original!
    """
    # TODO: 여기에 코드 작성 / Write your code here
    new_student = None
    # TODO: class_data["students"]에 추가 / append to class_data["students"]


# ============================================================
# 함수 5 / Function 5: save_class_data
# ============================================================
def save_class_data(class_data, file_path):
    """
    TODO 5.1: file_path를 쓰기 모드("w")로 열고, 한글이 깨지지 않도록
              encoding="utf-8"을 지정하세요.
              with open(...) as f: 구문을 사용하세요.

    TODO 5.1: Open file_path in write mode ("w") with encoding="utf-8"
              so Korean text isn't broken. Use the with open(...) as f: form.

    TODO 5.2: json.dump()을 사용하여 데이터를 파일에 저장하세요.
              사람이 읽기 좋도록 indent=2를 추가하고,
              한글이 그대로 보이도록 ensure_ascii=False를 추가하세요.

    TODO 5.2: Use json.dump() to write the data. Add indent=2 for readability
              and ensure_ascii=False so Korean characters display as-is.
    """
    # TODO: 여기에 코드 작성 / Write your code here
    pass


# ============================================================
# 함수 6 / Function 6: load_class_data
# ============================================================
def load_class_data(file_path):
    """
    TODO 6.1: file_path를 읽기 모드("r")로 열고 encoding="utf-8"을 지정하세요.
    TODO 6.1: Open file_path in read mode ("r") with encoding="utf-8".

    TODO 6.2: json.load()를 사용하여 파일 내용을 Python 객체로 변환하고 반환하세요.
              주의: json.loads()가 아니라 json.load() 입니다 (s 없음, 파일용)!

    TODO 6.2: Use json.load() to convert the file contents to a Python object.
              Note: It's json.load() — no 's' — for files!
    """
    # TODO: 여기에 코드 작성 / Write your code here
    pass


# ============================================================
# 🎁 보너스 / Bonus Challenges
# ============================================================

# 🥉 Easy
def class_averages_by_subject(class_data):
    """
    각 과목별 클래스 평균을 딕셔너리로 반환.
    Return a dict of class averages per subject.
    예 / Example: {"math": 82.3, "english": 84.0, "science": 83.0}
    """
    # TODO: 보너스 / Bonus
    pass


# 🥈 Medium
def students_above_threshold(class_data, threshold):
    """
    평균이 threshold 이상인 학생들의 이름 리스트를 반환.
    Return a list of names of students whose average >= threshold.
    """
    # TODO: 보너스 / Bonus
    pass


# 🥇 Hard — pathlib 미리보기 / pathlib preview
def save_with_pathlib(class_data, folder_name, file_name):
    """
    folder_name 폴더를 만들고(없으면), 그 안에 file_name으로 저장.
    Create folder_name (if missing) and save file_name inside it.

    힌트 / Hints:
      from pathlib import Path
      Path(folder_name).mkdir(exist_ok=True)
      file_path = Path(folder_name) / file_name
    """
    # TODO: 보너스 / Bonus
    pass


# ============================================================
# 🔒 보호된 테스트 블록 — 수정하지 마세요!
# 🔒 Protected test block — Do not modify!
# ============================================================
if __name__ == "__main__":
    # 샘플 데이터 / Sample data
    sample_json = '''
    {
      "class_name": "Python 101",
      "semester": "Spring 2026",
      "students": [
        {"id": "S001", "name": "Alice Kim",
         "grades": {"math": 92, "english": 85, "science": 78}},
        {"id": "S002", "name": "Bob Park",
         "grades": {"math": 67, "english": 72, "science": 80}},
        {"id": "S003", "name": "Carol Lee",
         "grades": {"math": 88, "english": 95, "science": 91}}
      ]
    }
    '''

    print("=" * 50)
    print("Test 1: parse_class_data")
    print("=" * 50)
    try:
        data = parse_class_data(sample_json)
        if data is not None:
            print(f"class_name: {data.get('class_name')}")
            print(f"학생 수 / # students: {len(data.get('students', []))}")
        else:
            print("(아직 구현되지 않음 / not implemented yet)")
    except Exception as e:
        print(f"오류 / Error: {e}")

    print()
    print("=" * 50)
    print("Test 2: calculate_student_average")
    print("=" * 50)
    alice = {"id": "S001", "name": "Alice Kim",
             "grades": {"math": 92, "english": 85, "science": 78}}
    try:
        avg = calculate_student_average(alice)
        print(f"Alice 평균 / average: {avg}  (예상 / expected: 85.0)")
    except Exception as e:
        print(f"오류 / Error: {e}")

    print()
    print("=" * 50)
    print("Test 3: find_top_student")
    print("=" * 50)
    try:
        data = parse_class_data(sample_json)
        if data is not None:
            top = find_top_student(data)
            print(f"최고 점수 학생 / top student: {top}  (예상 / expected: Carol Lee)")
    except Exception as e:
        print(f"오류 / Error: {e}")

    print()
    print("=" * 50)
    print("Test 4: add_student")
    print("=" * 50)
    try:
        data = parse_class_data(sample_json)
        if data is not None:
            before = len(data["students"])
            add_student(data, "S004", "David Choi", 75, 80, 85)
            after = len(data["students"])
            print(f"추가 전 / before: {before}, 추가 후 / after: {after}")
            print(f"마지막 학생 / last student: {data['students'][-1].get('name')}")
    except Exception as e:
        print(f"오류 / Error: {e}")

    print()
    print("=" * 50)
    print("Test 5 & 6: save_class_data + load_class_data")
    print("=" * 50)
    try:
        data = parse_class_data(sample_json)
        if data is not None:
            save_class_data(data, "test_class.json")
            loaded = load_class_data("test_class.json")
            print(f"라운드트립 일치 / round-trip match: {loaded == data}")
    except Exception as e:
        print(f"오류 / Error: {e}")

    print()
    print("모든 함수를 구현했다면 모든 테스트가 통과해야 합니다!")
    print("If all functions are implemented, every test should pass!")
