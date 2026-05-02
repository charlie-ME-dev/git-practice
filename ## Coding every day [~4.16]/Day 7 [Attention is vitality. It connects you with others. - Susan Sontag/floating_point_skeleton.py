# 🐍 부동소수점 연습 | Floating Point Practice
# -------------------------------------------------------
# 미션: 원의 둘레 출력 결과를 62.8로 깔끔하게 만드세요
# Mission: Fix the circumference output to print cleanly as 62.8
# -------------------------------------------------------

radius = 10.0

# -------------------------------------------------------
# ⚠️  아래 코드를 실행하면 62.800000000000004 가 출력됩니다
# ⚠️  Running the code below prints 62.800000000000004
#
# print('원의 반지름', radius)
# print('원의 면적', 3.14 * radius**2)
# print('원의 둘레', 2.0 * 3.14 * radius)   ← 여기가 문제! | This is the problem!
# -------------------------------------------------------


# 방법 1: round() 함수 사용 | Method 1: Using round()
# -------------------------------------------------------
# TODO 1-1: 반지름을 출력하세요 (수정 불필요)
#           Print the radius (no fix needed)
print('원의 반지름', radius)

# TODO 1-2: 면적을 출력하세요 (수정 불필요)
#           Print the area (no fix needed)
print('원의 면적', 3.14 * radius**2)

# TODO 1-3: round()를 사용하여 둘레를 소수점 1자리로 출력하세요
#           Use round() to print the circumference to 1 decimal place
#           힌트(Hint): print('원의 둘레', round(___, ___))
print('원의 둘레', )   # ← 이 줄을 수정하세요 | Fix this line


print()   # 빈 줄 구분 | blank line separator


# 방법 2: f-string 포맷 사용 | Method 2: Using f-string formatting
# -------------------------------------------------------
# TODO 2-1: 반지름을 출력하세요 (수정 불필요)
#           Print the radius (no fix needed)
print('원의 반지름', radius)

# TODO 2-2: 면적을 출력하세요 (수정 불필요)
#           Print the area (no fix needed)
print('원의 면적', 3.14 * radius**2)

# TODO 2-3: f-string :.1f 를 사용하여 둘레를 소수점 1자리로 출력하세요
#           Use f-string :.1f to print the circumference to 1 decimal place
#           힌트(Hint): print(f'원의 둘레 {___:.1f}')
print()   # ← 이 줄을 수정하세요 | Fix this line
