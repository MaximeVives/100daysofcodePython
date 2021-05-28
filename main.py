from question_model import Question
from data import question_data
from quizz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_bank.append(Question(question["question"], question["answer"]))


qb = QuizBrain(question_bank)

while qb.still_has_questions():
    answer = qb.next_question()
    if qb.check_answer(answer=answer):
        pass
    else:
        break
if qb.score == len(question_bank):
    print(f"You win, you reached {qb.score} points")
else:
    print(f"You lose, you had {qb.score} points")
