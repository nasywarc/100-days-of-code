from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for index in range(len(question_data)-1):
    question_bank.append(
        Question(question_data[index]['text'], question_data[index]['answer']))

quiz = QuizBrain(question_bank)

print(len(question_bank))

for question in range(len(question_bank)+1):
    quiz.next_question()
