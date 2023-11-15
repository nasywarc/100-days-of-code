from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for index in range(len(question_data)):
    question_bank.append(
        Question(question_data[index]['text'], question_data[index]['answer']))

quiz = QuizBrain(question_bank)

# for question in range(len(question_bank)):
#     quiz.next_question()

while quiz.still_has_question():
    quiz.next_question()
