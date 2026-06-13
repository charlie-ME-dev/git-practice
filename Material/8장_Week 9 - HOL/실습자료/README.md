# Python Module 실습 자료

## 주제
중간고사 피자 문제를 확장해가면서 module화의 필요성을 이해하고,
자신만의 module을 만들어보고, 표준 라이브러리로 넘어가는 실습.

## 진행 순서

각 폴더를 순서대로 따라가세요.

### step0_시험문제
중간고사 피자 문제 풀이. 5줄짜리 깔끔한 코드.

### step1_조각수확장
1인당 여러 조각 입력받기 추가. 함수 도입.

### step2_메뉴추가
4가지 피자 메뉴와 가격 데이터 추가. 함수가 3개로 늘어남.

### step3_여러종류주문
한 번에 여러 종류 주문하기. 주문 목록(list of dict) 등장.

### step4_영수증
영수증 출력 추가. 한 파일에 함수 6개 → "이거 좀 정리하고 싶다"는 감각.

### step5_모듈분리
하나의 파일을 5개의 module로 분리.
- pizza_menu.py     (메뉴 데이터)
- pizza_calc.py     (계산 함수)
- pizza_order.py    (주문 받기)
- pizza_receipt.py  (영수증 출력)
- main.py           (전체 흐름 조립)

각 모듈에 `if __name__ == "__main__":` 블록으로 자체 테스트 포함.

### step6_표준라이브러리
직접 만든 module과 같은 방식으로 표준 라이브러리(math, datetime, random)를 사용.
- math.ceil로 올림 나눗셈을 더 명확하게
- datetime으로 주문 시각 표시
- random으로 영수증 번호 생성

## 실행 방법

각 step 폴더로 이동해서:

```bash
# step0~4
python party_pizza.py

# step5~6
python main.py

# 또는 개별 모듈의 자체 테스트 실행
python pizza_menu.py
python pizza_calc.py
python pizza_receipt.py
```

## 주의

- 메뉴 가격은 예시이며 실제와 다를 수 있습니다.

## 한글 입력이 안 되는 경우

피자 이름("노모어피자" 등)을 입력했는데 `'\xeb\x85...'` 같은 깨진 문자가
보이거나 `UnicodeDecodeError`가 나면, 터미널 인코딩이 UTF-8이 아닌 것입니다.

### Windows + VS Code 통합 터미널
가장 간단한 해결책은 **PowerShell에서 `chcp 65001`** 한 줄 입력 후 다시 실행:

```powershell
chcp 65001
python main.py
```

`65001`이 UTF-8 코드 페이지입니다. 매번 치기 귀찮으면 VS Code의
`settings.json`에 다음을 추가하세요:

```json
"terminal.integrated.profiles.windows": {
    "PowerShell (UTF-8)": {
        "source": "PowerShell",
        "args": ["-NoExit", "-Command", "chcp 65001"]
    }
},
"terminal.integrated.defaultProfile.windows": "PowerShell (UTF-8)"
```

### Windows + IDLE
IDLE은 기본적으로 UTF-8을 잘 처리합니다. 그래도 문제가 있다면
`Options → Configure IDLE → General` 에서 default source encoding을 UTF-8로.

### macOS / Linux
대부분 기본이 UTF-8이라 별도 설정 불필요. 만약 문제가 있다면:

```bash
export LANG=ko_KR.UTF-8
python main.py
```

### 그래도 안 되면
한글 입력 대신 **영어 메뉴 이름**으로 임시 변경할 수 있습니다.
`pizza_menu.py`의 `MENU` dict를 다음처럼 바꾸세요:

```python
MENU = {
    "nomore":   12000,
    "jackson":  15000,
    "domino":   25000,
    "papajohns": 28000,
}
```

## PowerShell에서 소스 파일을 볼 때 한글이 깨지는 경우

PowerShell에서 `type party_pizza.py` 또는 `Get-Content party_pizza.py`로
파일 내용을 봤을 때 한글이 `??寃쎄퀬` 같이 깨져 보일 수 있습니다.

**이는 PowerShell 5.x의 `Get-Content`가 코드 페이지(`chcp 65001`)와 무관하게
시스템 ANSI(CP949)로 파일을 읽기 때문입니다. 코드와 실행에는 문제가 없습니다.**

해결 방법:

```powershell
# 인코딩을 명시해서 보기
Get-Content party_pizza.py -Encoding UTF8
```

또는 VS Code, IDLE 등의 에디터로 파일을 여세요. 이 도구들은 BOM 없는 UTF-8을
정상적으로 처리합니다.
