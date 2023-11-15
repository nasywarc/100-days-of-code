from data import question_data2
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for index in range(len(question_data2['results'])):
    question_bank.append(
        Question(question_data2['results'][index]['question'], question_data2['results'][index]['correct_answer']))

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print('You\'ve completed the quiz.')
print(f'Your final score was : {quiz.score}/{quiz.question_number}')
