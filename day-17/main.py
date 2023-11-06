from data import question_data
from question_model import Question

new_q = []

for index in range(len(question_data)-1):
    new_q.append(
        Question(question_data[index]['text'], question_data[index]['answer']))
