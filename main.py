
from quiz import Quiz

quizzes = [
    Quiz(
        "FIFA 월드컵을 처음 개최한 나라는?",
        ["브라질", "프랑스", "우루과이", "이탈리아"],
        3
    ),
    Quiz(
        "야구에서 타자가 스트라이크 3개를 받으면 어떻게 되는가?",
        ["볼넷", "아웃", "2루 진루", "홈런"],
        2
    ),
    Quiz(
        "농구에서 NBA의 공격 제한 시간은 기본적으로 몇 초인가?",
        ["14초", "20초", "24초", "30초"],
        3
    ),
    Quiz(
        "올림픽 오륜기의 고리는 몇 개인가?",
        ["4개", "5개", "6개", "7개"],
        2
    ),
    Quiz(
        "테니스에서 4대 메이저 대회를 통틀어 부르는 명칭은?",
        ["마스터스", "데이비스컵", "그랜드슬램", "월드투어"],
        3
    )
]

# 퀴즈 진행
score = 0

print("스포츠 퀴즈 게임을 시작합니다!")
print(f"총 {len(quizzes)}문제입니다.")

try:
    for i, quiz in enumerate(quizzes, start=1):
        print()
        print(f"[문제 {i}]")
        quiz.show_question()

        while True:
            user_input = input("정답 입력: ").strip()

            if not user_input:
                print("답을 입력해주세요.")
                continue

            try:
                user_answer = int(user_input)
            except ValueError:
                print("숫자를 입력해주세요.")
                continue

            if 1 <= user_answer <= len(quiz.choices):
                break
            else:
                print(f"1부터 {len(quiz.choices)}까지의 숫자를 입력해주세요.")

        if quiz.check_answer(user_answer):
            print("정답입니다!")
            score += 1
        else:
            print("오답입니다!")

    print()
    print(f"최종 결과: {len(quizzes)}문제 중 {score}문제 정답!")
    print(f"점수: {score / len(quizzes) * 100:.0f}점")

except KeyboardInterrupt:
    print("\n사용자가 게임을 중단했습니다.")

except EOFError:
    print("\n입력이 종료되어 게임을 마칩니다.") 