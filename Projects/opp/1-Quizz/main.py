from data import question_data  
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for question in question_data :
	question_text = question["text"]
	question_answer = question["answer"]
	n_question = Question(question_text,question_answer)
	question_bank.append(n_question)
	
quiz = QuizBrain(question_bank)
while(quiz.stillQuest()):
	quiz.certain()
	
