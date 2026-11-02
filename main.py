
from quiz import Quiz

quiz1 = Quiz(
    "월드컵을 처음 개최한 나라는?",
    ["브라질", "프랑스", "우루과이", "이탈리아"],
    3
)

quiz1.show_question()

user_answer = int(input("정답 입력: "))

if quiz1.check_answer(user_answer):
    print("정답입니다!")
else:
    print("오답입니다!")
