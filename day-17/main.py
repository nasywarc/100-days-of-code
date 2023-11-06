from data import question_data
from question_model import Question

question_bank = []

for index in range(len(question_data)-1):
    question_bank.append(
        Question(question_data[index]['text'], question_data[index]['answer']))
