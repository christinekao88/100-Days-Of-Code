# import Question class
from question_model import Question

# import data bank
from data import question_data

# form quiz_brain (file) import QuizBrain (class)
from quiz_brain import QuizBrain

question_bank=[]
for data in question_data:    
    question_bank.append(Question(data['question'],data['correct_answer']))

# print(question_bank)
# print(question_bank[0].answer)

# quiz(object) = class QuizBrain (pass a list here)
quiz = QuizBrain(question_bank)

# if quiz still has questions remaining
while quiz.still_has_questions():
    quiz.next_question()
    
print("You've completed the quiz")
print(f"Your final score was {quiz.score}/{quiz.question_number}")

