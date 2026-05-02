import random

def alphabet_number_quiz():
    print("=====================================================")
    print("🔠 알파벳 숫자로 바꾸기 연습을 시작합니다! 🔢")
    print("   (A=1, B=2, ..., Z=26)")
    print("   ※ 그만하려면 언제든지 'q'를 입력하세요.")
    print("=====================================================\n")

    while True:
        # 1부터 26 사이의 무작위 숫자 생성
        correct_number = random.randint(1, 26)
        
        # 숫자를 대문자 알파벳으로 변환 (A의 아스키 코드는 65이므로, 숫자 + 64)
        question_alphabet = chr(correct_number + 64)
        
        # 문제 출제 및 사용자 입력 받기
        user_input = input(f"알파벳 '{question_alphabet}' 은(는) 숫자 몇 일까요? : ").strip()
        
        # 종료 조건 확인
        if user_input.lower() == 'q':
            print("\n연습을 종료합니다. 수고하셨습니다!")
            break
            
        # 입력값 검증 및 정답 확인
        try:
            user_answer = int(user_input)
            
            if user_answer == correct_number:
                print("✅ 정답입니다!\n")
            else:
                print(f"❌ 오답입니다. 답은 {correct_number} 입니다.\n")
                
        except ValueError:
            # 사용자가 숫자가 아닌 다른 문자(예: 공백, 특수문자 등)를 입력했을 때의 처리
            print("⚠️ 숫자만 입력해주세요! (종료하려면 'q' 입력)\n")

# 프로그램 실행
if __name__ == "__main__":
    alphabet_number_quiz()