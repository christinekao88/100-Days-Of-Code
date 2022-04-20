from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface
question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)

# 為了跟main.py取得一樣的題目，可以將quiz當作參數傳入quiz_ui
quiz_ui = QuizInterface(quiz)

# class QuizInterface() 裡有 mainloop() 不停的檢查是否需要更新ui中的東西，或是user是否與之有交互
# 此時若main.py裡有while loop會使mainloop混淆，不能成功執行
# while quiz.still_has_questions():
#     quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
