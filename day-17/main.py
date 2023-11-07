from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for index in range(len(question_data)-1):
    question_bank.append(
        Question(question_data[index]['text'], question_data[index]['answer']))

question = QuizBrain(question_bank)

question.next_question()
